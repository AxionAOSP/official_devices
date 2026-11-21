# Installation Guide — OnePlus 9 Pro (lemonadep)

> [!WARNING]
> - Your warranty is void.
> - All official release builds are tested and safe to use.
> - If you decide to experiment, mess something up, corrupt your storage, turn your phone into a fancy paperweight, or brick it beyond recovery — **don't blame us**.
> - You are doing this at **your own risk** and take full responsibility for anything that may happen.

> [!NOTE]
> - The device must have an **unlocked bootloader**.
> - Working **ADB and fastboot** drivers must be installed on your computer, on the [latest](https://developer.android.com/tools/releases/platform-tools) platform tools.
> - Make a **full data backup** before flashing.
> - Ensure your device has at least **30% battery**.
> - Flash **only** files meant for **OnePlus 9 Pro (lemonadep)**: models LE2120, LE2121, LE2123, LE2125. The T-Mobile model (LE2127) has to be converted to the global firmware first.
> - First boot may take 5–10 minutes. Do **not** interrupt or force reboot unless it exceeds 10 minutes.

---

## First Time Install

### Step 1 — Flash firmware (required)

1. Download the firmware zip *(get it from the [Telegram support group](https://t.me/axionos_op9))*.
2. Reboot to **Recovery** and navigate to **Apply update → Apply from ADB**.
3. Sideload the firmware:
   ```
   adb sideload firmware.zip
   ```

### Step 2 — Flash the ROM

1. Download the ROM zip and the **dtbo.img**, **vbmeta.img**, **vendor_boot.img** and **boot.img** for your device from [here](https://cdn.axionos.org/#lemonadep).
2. Reboot to **bootloader** and flash the boot images:
   ```
   fastboot flash dtbo dtbo.img
   fastboot flash vbmeta vbmeta.img
   fastboot flash vendor_boot vendor_boot.img
   fastboot flash boot boot.img
   ```
3. Reboot to **Recovery** → **Factory reset** → **Format data/factory reset**.
4. From the main menu, navigate to **Apply update → Apply from ADB**.
5. Sideload the ROM (replace `rom` with the actual filename):
   ```
   adb sideload rom.zip
   ```
6. Reboot to **System** & **Enjoy**

> [!NOTE]
> For **Vanilla builds**, reboot to recovery and sideload **MindTheGapps.zip** before step 6 (optional).

---

## Update (Dirty Flash)

> Dirty flashing **will not work** for major Android version upgrades (example: **1.x → 2.x**).

1. Reboot to **Recovery**.
2. From the main menu, navigate to **Apply update → Apply from ADB**.
3. Sideload the ROM (replace `rom` with the actual filename):
   ```
   adb sideload rom.zip
   ```
4. Reboot to **System** & **Enjoy**

> [!IMPORTANT]
> For **vanilla builds**, **GApps must be reflashed after every update**.

---

## Support / Bug Reports

📢 **[Telegram Group](https://t.me/axionos_op9)**
