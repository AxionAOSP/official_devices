import json
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
INFRA_DIR = REPO_ROOT / "infra"
if str(INFRA_DIR) not in sys.path:
    sys.path.insert(0, str(INFRA_DIR))

import generate
import maintainer_onboarding


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def build_response(filename):
    return {
        "response": [
            {
                "filename": filename,
                "datetime": 1,
                "size": 2,
                "version": "test",
            }
        ]
    }


@pytest.fixture
def temp_repo(tmp_path, monkeypatch):
    registry = {
        "schema": 1,
        "maintainers": [
            {
                "id": "alice",
                "name": "Alice",
                "github_username": "alice-dev",
            },
            {
                "id": "bob",
                "name": "Bob",
                "github_username": "bob-dev",
            },
        ],
        "devices": [
            {
                "codename": "motoedge",
                "name": "Motorola Edge 50",
                "status": "active",
                "official": True,
                "website": True,
                "maintainers": ["bob"],
            },
            {
                "codename": "beta",
                "name": "Google Pixel 10",
                "status": "active",
                "official": True,
                "website": True,
                "maintainers": ["alice", "bob"],
            },
            {
                "codename": "old",
                "name": "OnePlus 6",
                "status": "inactive",
                "official": False,
                "website": True,
                "maintainers": ["bob"],
            },
            {
                "codename": "hidden",
                "name": "Google Pixel 9",
                "status": "active",
                "official": True,
                "website": False,
                "maintainers": ["alice"],
            },
            {
                "codename": "alpha",
                "name": "Google Pixel 9 Pro",
                "status": "active",
                "official": True,
                "website": True,
                "maintainers": ["alice"],
            },
        ],
    }
    write_json(tmp_path / "infra" / "device_registry.json", registry)
    write_json(tmp_path / "OTA" / "GMS" / "alpha.json", build_response("alpha-gms.zip"))
    write_json(tmp_path / "OTA" / "VANILLA" / "beta.json", build_response("beta-vanilla.zip"))
    (tmp_path / "OTA" / "CHANGELOG").mkdir(parents=True)
    (tmp_path / "OTA" / "CHANGELOG" / "alpha.txt").write_text(
        "alpha changelog\n",
        encoding="utf-8",
    )
    (tmp_path / "Wiki").mkdir(parents=True)
    (tmp_path / "Wiki" / "beta.md").write_text("# beta\n", encoding="utf-8")
    (tmp_path / "README.md").write_text(
        "# Old generated list\n\n"
        "## 🛠 Maintainer and device registry\n\n"
        "Keep this documentation.\n",
        encoding="utf-8",
    )
    (tmp_path / "dinfo.json").write_text("{}\n", encoding="utf-8")
    monkeypatch.setattr(generate, "ROOT", tmp_path)
    monkeypatch.setattr(generate, "REGISTRY_FILE", tmp_path / "infra" / "device_registry.json")
    monkeypatch.setattr(generate, "README_FILE", tmp_path / "README.md")
    return tmp_path


def test_generate_all_writes_sorted_outputs_and_api(temp_repo):
    generate.generate_all(generate.load_registry())

    assert (temp_repo / "OTA" / "axion.devices").read_text(encoding="utf-8") == (
        "hidden\nalpha\nbeta\nmotoedge\n"
    )
    assert (temp_repo / "OTA" / "axion.maintainers").read_text(encoding="utf-8") == (
        "alice\nbob\n"
    )
    assert "AXION_OFFICIAL_MAINTAINERS_beta := alice bob" in (
        temp_repo / "infra" / "official_devices.mk"
    ).read_text(encoding="utf-8")

    registry = read_json(temp_repo / "infra" / "device_registry.json")
    alpha = next(device for device in registry["devices"] if device["codename"] == "alpha")
    hidden = next(device for device in registry["devices"] if device["codename"] == "hidden")
    old = next(device for device in registry["devices"] if device["codename"] == "old")
    assert alpha == {
        "codename": "alpha",
        "name": "Google Pixel 9 Pro",
        "maintainers": ["alice"],
    }
    assert hidden["website"] is False
    assert old == {
        "codename": "old",
        "name": "OnePlus 6",
        "maintainers": ["bob"],
        "status": "inactive",
    }
    assert not (temp_repo / "dinfo.json").exists()

    downloads = read_json(temp_repo / "api" / "downloads.json")
    assert downloads["schema"] == 2
    assert [device["codename"] for device in downloads["devices"]] == [
        "alpha",
        "beta",
        "motoedge",
        "old",
    ]
    alpha_api = downloads["devices"][0]
    beta_api = downloads["devices"][1]
    assert alpha_api["maintainer_ids"] == ["alice"]
    assert alpha_api["ota"]["gms"].endswith("/OTA/GMS/alpha.json")
    assert alpha_api["ota"]["vanilla"].endswith("/OTA/VANILLA/alpha.json")
    assert alpha_api["changelog"].endswith("/OTA/CHANGELOG/alpha.txt")
    assert beta_api["guide"].endswith("/Wiki/beta.md")
    assert "alpha-gms.zip" not in (temp_repo / "api" / "downloads.json").read_text(
        encoding="utf-8",
    )

    maintainers = read_json(temp_repo / "api" / "maintainers.json")
    assert maintainers["schema"] == 2
    assert [maintainer["id"] for maintainer in maintainers["maintainers"]] == [
        "alice",
        "bob",
    ]
    assert maintainers["maintainers"][0]["devices"] == [
        "hidden",
        "alpha",
        "beta",
    ]

    readme = (temp_repo / "README.md").read_text(encoding="utf-8")
    assert "| **Google Pixel 9** | `hidden` |" in readme
    assert "| **Google Pixel 9 Pro** | `alpha` |" in readme
    assert "Keep this documentation." in readme
    assert "# Old generated list" not in readme


def test_onboarding_adds_device_and_regenerates_outputs(temp_repo, monkeypatch):
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "maintainer_onboarding.py",
            "--maintainer-id",
            "carol",
            "--maintainer-name",
            "Carol",
            "--github",
            "https://github.com/carol-dev",
            "--device",
            "POCO F5 (marble)",
            "--co-maintainer-id",
            "alice",
            "--support-group",
            "https://t.me/poco",
            "--image-url",
            "https://example.com/poco.png",
        ],
    )

    assert maintainer_onboarding.main() == 0

    registry = read_json(temp_repo / "infra" / "device_registry.json")
    assert registry["maintainers"][-1] == {
        "id": "carol",
        "name": "Carol",
        "github_username": "carol-dev",
    }
    assert [device["codename"] for device in registry["devices"]] == [
        "hidden",
        "alpha",
        "beta",
        "motoedge",
        "old",
        "marble",
    ]
    marble = registry["devices"][-1]
    assert marble["maintainers"] == ["carol", "alice"]
    assert "official" not in marble
    assert "website" not in marble

    assert (temp_repo / "OTA" / "axion.devices").read_text(encoding="utf-8") == (
        "hidden\nalpha\nbeta\nmotoedge\nmarble\n"
    )
    assert "| **POCO F5** | `marble` |" in (temp_repo / "README.md").read_text(
        encoding="utf-8",
    )
    downloads = read_json(temp_repo / "api" / "downloads.json")
    assert [device["codename"] for device in downloads["devices"]] == [
        "alpha",
        "beta",
        "motoedge",
        "old",
        "marble",
    ]
    assert downloads["devices"][-1]["ota"]["gms"].endswith("/OTA/GMS/marble.json")


def test_onboarding_dry_run_does_not_write(temp_repo, monkeypatch, capsys):
    before_registry = (temp_repo / "infra" / "device_registry.json").read_text(
        encoding="utf-8",
    )
    before_readme = (temp_repo / "README.md").read_text(encoding="utf-8")
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "maintainer_onboarding.py",
            "--maintainer-id",
            "carol",
            "--maintainer-name",
            "Carol",
            "--github",
            "carol-dev",
            "--device",
            "POCO F5 (marble)",
            "--dry-run",
        ],
    )

    assert maintainer_onboarding.main() == 0

    output = capsys.readouterr().out
    assert "validated: marble / POCO F5" in output
    assert (temp_repo / "infra" / "device_registry.json").read_text(
        encoding="utf-8",
    ) == before_registry
    assert (temp_repo / "README.md").read_text(encoding="utf-8") == before_readme
    assert not (temp_repo / "api" / "downloads.json").exists()


@pytest.mark.parametrize(
    ("value", "message"),
    [
        ("bad id", "whitespace"),
        ("bad#id", "unsupported"),
    ],
)
def test_normalize_maintainer_id_rejects_bad_values(value, message):
    with pytest.raises(ValueError, match=message):
        maintainer_onboarding.normalize_maintainer_id(value)


def test_onboarding_rejects_duplicate_codename(temp_repo, monkeypatch, capsys):
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "maintainer_onboarding.py",
            "--maintainer-id",
            "carol",
            "--maintainer-name",
            "Carol",
            "--github",
            "carol-dev",
            "--device",
            "Pixel Clone (alpha)",
        ],
    )

    assert maintainer_onboarding.main() == 1
    assert "device alpha already exists" in capsys.readouterr().err


def test_generate_drop_subcommand(temp_repo, monkeypatch):
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "generate.py",
            "drop",
            "alpha",
        ],
    )

    generate.main()

    registry = read_json(temp_repo / "infra" / "device_registry.json")
    alpha = next(device for device in registry["devices"] if device["codename"] == "alpha")
    assert alpha["status"] == "inactive"

    # Verify that it also regenerated outputs (e.g. alpha is removed from active devices list)
    assert "alpha" not in (temp_repo / "OTA" / "axion.devices").read_text(encoding="utf-8")


def test_generate_drop_invalid_codename(temp_repo, monkeypatch):
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "generate.py",
            "drop",
            "nonexistent",
        ],
    )

    with pytest.raises(SystemExit) as excinfo:
        generate.main()
    assert excinfo.value.code == 1


def test_generate_drop_missing_codename(temp_repo, monkeypatch):
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "generate.py",
            "drop",
        ],
    )

    with pytest.raises(SystemExit) as excinfo:
        generate.main()
    assert excinfo.value.code == 1


def test_generate_invalid_subcommand(temp_repo, monkeypatch):
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "generate.py",
            "invalid",
        ],
    )

    with pytest.raises(SystemExit) as excinfo:
        generate.main()
    assert excinfo.value.code == 1
