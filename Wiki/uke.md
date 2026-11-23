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

1. Download the latest **axion-*-uke.zip** from the [website](https://cdn.axionos.org/#uke) and verify its SHA-256.
2. Extract the zip's `payload.bin` with a payload dumper (for example [payload-dumper-go](https://github.com/ssut/payload-dumper-go)) and grab the **boot, dtbo, init_boot, recovery and vendor_boot** images.
3. Reboot to **fastboot** by holding **Power + Volume Down**, or with `adb reboot bootloader`.
4. Flash the following partitions **one by one**:

```
fastboot flash boot <drag-&-drop-boot.img>
```
```
fastboot flash dtbo <drag-&-drop-dtbo.img>
```
```
fastboot flash init_boot <drag-&-drop-init_boot.img>
```
```
fastboot flash recovery <drag-&-drop-recovery.img>
```
```
fastboot flash vendor_boot <drag-&-drop-vendor_boot.img>
```
5. Reboot to **recovery**:

```
fastboot reboot recovery
```
6. Select **Factory reset → Format data/factory reset**.
7. Select **Apply update → Apply from ADB**, then sideload the ROM:

```
adb sideload <drag-&-drop-rom.zip>
```
8. After the sideload completes, select **YES** to reboot to recovery if you have extra packages (i.e., GApps) to install and **NO** if you have none.
9. Select **Factory reset → Format data/factory reset** again.
10. Select **Reboot system now**.

---

## Update (Dirty Flash)

> [!NOTE]
> Dirty flashing **will not work** for major Android version upgrades
> (example: **1.x → 2.x**).

Install the update with the built-in updater (**System update** in Settings), or sideload it:

1. Reboot to recovery: `adb reboot recovery`
2. Select **Apply update → Apply from ADB**, then sideload the new ROM zip:

```
adb sideload <drag-&-drop-rom.zip>
```

3. Select **Reboot system now**.

---

> [!IMPORTANT]
> For **vanilla builds**, **GApps must be reflashed after every update**.

---

## Support / Bug Reports

📢 **[Telegram Group](https://t.me/axion_uke)**
