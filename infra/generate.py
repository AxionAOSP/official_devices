import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW_BASE_URL = "https://raw.githubusercontent.com/AxionAOSP/official_devices/refs/heads/main"
REGISTRY_FILE = ROOT / "infra" / "device_registry.json"
README_FILE = ROOT / "README.md"
README_REGISTRY_HEADING = "## 🛠 Maintainer and device registry"
BRAND_ORDER = (
    "asus",
    "google",
    "motorola",
    "nothing",
    "oneplus",
    "poco",
    "realme",
    "xiaomi",
    "samsung",
    "tecno",
    "itel",
    "other",
)
BRAND_RANK = {brand: index for index, brand in enumerate(BRAND_ORDER)}


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def write_text(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def require(condition, message):
    if not condition:
        raise ValueError(message)


def status_key(status):
    value = str(status or "active").strip().lower()
    require(value in {"active", "inactive"}, f"invalid status {status}")
    return value


def device_status(device):
    return status_key(device.get("status"))


def is_official(device):
    return device.get("official", device_status(device) == "active")


def is_visible(device):
    return device.get("website", True)


def markdown_text(value):
    return str(value).replace("\\", "\\\\").replace("[", "\\[").replace("]", "\\]")


def markdown_table_cell(value):
    return markdown_text(value).replace("|", "\\|").replace("\n", " ")


def read_registry_section():
    if not README_FILE.exists():
        return ""
    text = README_FILE.read_text(encoding="utf-8")
    index = text.find(README_REGISTRY_HEADING)
    if index < 0:
        return ""
    return text[index:].strip()


def brand_for(name):
    brands = [
        ("asus", r"ASUS|Asus|Zenfone|ZenFone"),
        ("google", r"Google Pixel"),
        ("samsung", r"Galaxy|Samsung"),
        ("poco", r"POCO"),
        ("realme", r"Realme"),
        ("xiaomi", r"Xiaomi|Redmi|Mi"),
        ("tecno", r"TECNO"),
        ("motorola", r"Motorola|Moto"),
        ("nothing", r"Nothing|CMF"),
        ("oneplus", r"Oneplus|OnePlus"),
        ("itel", r"Itel|itel"),
    ]
    for brand, pattern in brands:
        if re.search(pattern, name):
            return brand
    return "other"


def natural_key(value):
    normalized = re.sub(r"[/()_-]+", " ", str(value).casefold())
    parts = re.split(r"(\d+)", normalized)
    return [(1, int(part)) if part.isdigit() else (0, part.strip()) for part in parts]


def device_sort_key(device):
    brand = device.get("brand") or brand_for(device["name"])
    return (
        BRAND_RANK.get(brand, BRAND_RANK["other"]),
        natural_key(device["name"]),
        str(device["codename"]).casefold(),
    )


def sorted_devices(devices):
    return sorted(devices, key=device_sort_key)


def compact_device(device):
    status = device_status(device)
    official = is_official(device)
    output = {
        "codename": device["codename"],
        "name": device["name"],
        "maintainers": device["maintainers"],
    }
    brand = device.get("brand")
    if brand and brand != brand_for(device["name"]):
        output["brand"] = brand
    if status != "active":
        output["status"] = status
    if official != (status == "active"):
        output["official"] = official
    if not is_visible(device):
        output["website"] = False
    for key in ("support_group", "image_url"):
        if device.get(key):
            output[key] = device[key]
    return output


def compact_registry(registry):
    return {
        "schema": registry.get("schema", 1),
        "maintainers": [
            {
                "id": maintainer["id"],
                "name": maintainer["name"],
                "github_username": maintainer["github_username"],
            }
            for maintainer in registry["maintainers"]
        ],
        "devices": [compact_device(device) for device in sorted_devices(registry["devices"])],
    }


def validate_registry(registry):
    maintainers = registry.get("maintainers", [])
    devices = registry.get("devices", [])
    require(isinstance(maintainers, list), "maintainers must be a list")
    require(isinstance(devices, list), "devices must be a list")

    maintainer_ids = set()
    for maintainer in maintainers:
        maintainer_id = maintainer.get("id")
        require(maintainer_id, "maintainer id is required")
        require(maintainer_id not in maintainer_ids, f"duplicate maintainer {maintainer_id}")
        require(maintainer.get("name"), f"maintainer {maintainer_id} missing name")
        require(maintainer.get("github_username"), f"maintainer {maintainer_id} missing github_username")
        maintainer_ids.add(maintainer_id)

    codenames = set()
    for device in devices:
        codename = device.get("codename")
        require(codename, "device codename is required")
        require(codename not in codenames, f"duplicate device {codename}")
        require(device.get("name"), f"device {codename} missing name")
        status = device_status(device)
        device_maintainers = device.get("maintainers", [])
        require(device_maintainers, f"device {codename} missing maintainers")
        seen_device_maintainers = set()
        for maintainer_id in device_maintainers:
            require(maintainer_id in maintainer_ids, f"device {codename} references unknown maintainer {maintainer_id}")
            require(maintainer_id not in seen_device_maintainers, f"device {codename} has duplicate maintainer {maintainer_id}")
            seen_device_maintainers.add(maintainer_id)
        if is_official(device):
            require(status == "active", f"official device {codename} must be active")
        codenames.add(codename)

    return registry


def load_registry():
    return validate_registry(read_json(REGISTRY_FILE))


def maintainer_index(registry):
    return {maintainer["id"]: maintainer for maintainer in registry["maintainers"]}


def visible_devices(registry):
    return sorted_devices([device for device in registry["devices"] if is_visible(device)])


def official_devices(registry):
    return sorted_devices([device for device in registry["devices"] if is_official(device)])


def published_devices(registry):
    by_codename = {}
    for device in registry["devices"]:
        if is_visible(device) or is_official(device):
            by_codename[device["codename"]] = device
    return sorted_devices(by_codename.values())


def raw_repo_url(*parts):
    return f"{RAW_BASE_URL}/{'/'.join(parts)}"


def generate_registry(registry):
    write_json(REGISTRY_FILE, registry)


def generate_ota_lists(registry):
    devices = official_devices(registry)
    maintainer_ids = []
    for device in devices:
        for maintainer_id in device["maintainers"]:
            if maintainer_id not in maintainer_ids:
                maintainer_ids.append(maintainer_id)
    write_text(ROOT / "OTA" / "axion.devices", "\n".join(device["codename"] for device in devices) + "\n")
    write_text(ROOT / "OTA" / "axion.maintainers", "\n".join(maintainer_ids) + "\n")


def generate_official_makefile(registry):
    devices = official_devices(registry)
    lines = []
    lines.append("AXION_OFFICIAL_DEVICES := \\")
    for index, device in enumerate(devices):
        suffix = " \\" if index < len(devices) - 1 else ""
        lines.append(f"    {device['codename']}{suffix}")
    lines.append("")
    for device in devices:
        lines.append(f"AXION_OFFICIAL_MAINTAINERS_{device['codename']} := {' '.join(device['maintainers'])}")
    write_text(ROOT / "infra" / "official_devices.mk", "\n".join(lines) + "\n")


def generate_downloads_api(registry):
    devices = []
    for device in visible_devices(registry):
        codename = device["codename"]
        devices.append({
            "codename": codename,
            "name": device["name"],
            "brand": device.get("brand") or brand_for(device["name"]),
            "status": device_status(device),
            "maintainer_ids": device["maintainers"],
            "support_group": device.get("support_group", ""),
            "images": {
                "banner": raw_repo_url("OTA", "Banners", "devices", f"{codename}.webp"),
                "banner_lower": raw_repo_url("OTA", "Banners", "devices", f"{codename.lower()}.webp"),
                "fallback": device.get("image_url", ""),
            },
            "ota": {
                "gms": raw_repo_url("OTA", "GMS", f"{codename}.json"),
                "vanilla": raw_repo_url("OTA", "VANILLA", f"{codename}.json"),
            },
            "changelog": raw_repo_url("OTA", "CHANGELOG", f"{codename}.txt"),
            "guide": raw_repo_url("Wiki", f"{codename}.md"),
        })

    write_json(ROOT / "api" / "downloads.json", {"schema": 2, "devices": devices})


def generate_maintainers_api(registry):
    devices_by_maintainer = {}
    for device in published_devices(registry):
        for maintainer_id in device["maintainers"]:
            devices_by_maintainer.setdefault(maintainer_id, []).append(device["codename"])

    output = []
    for maintainer in registry["maintainers"]:
        maintainer_id = maintainer["id"]
        devices = devices_by_maintainer.get(maintainer_id)
        if not devices:
            continue
        output.append({
            "id": maintainer_id,
            "name": maintainer["name"],
            "github_username": maintainer["github_username"],
            "devices": devices,
        })

    write_json(ROOT / "api" / "maintainers.json", {"schema": 2, "maintainers": output})


def generate_readme(registry):
    maintainers = maintainer_index(registry)
    devices = official_devices(registry)
    devices_by_maintainer = {}
    for device in devices:
        for maintainer_id in device["maintainers"]:
            devices_by_maintainer.setdefault(maintainer_id, []).append(device)

    lines = [
        "# 📱 Supported Devices",
        "",
        "| Device Name | Codename |",
        "|-------------|----------|",
    ]
    for device in devices:
        lines.append(f"| **{markdown_table_cell(device['name'])}** | `{device['codename']}` |")

    lines.extend(["", "## 👤 Maintainers"])
    for maintainer in registry["maintainers"]:
        devices = devices_by_maintainer.get(maintainer["id"])
        if not devices:
            continue
        device_names = ", ".join(f"{markdown_text(device['name'])} (`{device['codename']}`)" for device in devices)
        lines.append(f"- **[{markdown_text(maintainer['name'])}](https://github.com/{maintainer['github_username']})** ({device_names})")

    registry_section = read_registry_section()
    if registry_section:
        lines.extend(["", registry_section])
    write_text(README_FILE, "\n".join(lines) + "\n")


def remove_legacy_dinfo():
    path = ROOT / "dinfo.json"
    if path.exists():
        path.unlink()


def generate_all(registry):
    registry = compact_registry(validate_registry(registry))
    generate_registry(registry)
    remove_legacy_dinfo()
    generate_ota_lists(registry)
    generate_official_makefile(registry)
    generate_downloads_api(registry)
    generate_maintainers_api(registry)
    generate_readme(registry)


def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == "drop":
            if len(sys.argv) < 3:
                print("Error: Specify a codename to drop.", file=sys.stderr)
                sys.exit(1)
            codename = sys.argv[2]
            registry = load_registry()
            
            # Find the device with the given codename
            found = False
            for device in registry["devices"]:
                if device["codename"] == codename:
                    device["status"] = "inactive"
                    device.pop("official", None)
                    found = True
                    break
            
            if not found:
                print(f"Error: Device codename '{codename}' not found in registry.", file=sys.stderr)
                sys.exit(1)
                
            generate_all(registry)
            print(f"Successfully marked '{codename}' as inactive and regenerated all files.")
            return
        else:
            print(f"Error: Unknown argument '{sys.argv[1]}'. Did you mean 'drop'?", file=sys.stderr)
            sys.exit(1)

    generate_all(load_registry())


if __name__ == "__main__":
    main()
