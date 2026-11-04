# Installation Guide — Xiaomi Pad 7 / POCO Pad X1 (uke)

> [!WARNING]
> - Your warranty is void.
> - If you decide to experiment, mess something up, corrupt your storage, turn your phone into a fancy paperweight, or brick it beyond recovery — **don’t blame us**.
> - You are doing this at **your own risk** and take full responsibility for anything that may happen.

> [!NOTE]
> - All official release builds are tested and safe to use.
> - The device must have an **unlocked bootloader**.
> - Make a **full data backup** before flashing.
> - Make sure to be on [latest](https://developer.android.com/tools/releases/platform-tools) **platform tools** for adb/fastboot commands.
> - Ensure your device has at least **30% battery**.
> - Flash **only** files meant for **Xiaomi Pad 7 / POCO Pad X1 (uke)**.
> - First boot may take 5–10 minutes. Do **not** interrupt or force reboot unless it exceeds 10 minutes.

---

## Clean Installation

1. Download the latest **fastboot ROM** zip (`axion-...-uke-fastboot.zip`) and verify its `.sha256sum`.
2. Reboot to fastboot: `adb reboot fastboot`
3. Flash the ROM:

```
fastboot update <drag-&-drop-rom.zip>
```

4. When it finishes, **format data** from recovery (**Factory reset** -> **Format data/factory reset**), then reboot to **System**.

---

## Update (Dirty Flash)

> [!NOTE]
> Dirty flashing **will not work** for major Android version upgrades
> (example: **1.x → 2.x**).

1. Reboot to fastboot: `adb reboot fastboot`
2. Flash the new ROM zip over the old one:

```
fastboot update <drag-&-drop-rom.zip>
```

3. Reboot to **System**.

---

> [!IMPORTANT]
> For **vanilla builds**, **GApps must be reflashed after every update**.

---

## Support / Bug Reports

📢 **[Telegram Group](https://t.me/axion_uke)**
