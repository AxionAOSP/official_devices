# Installation Guide — OnePlus 8T (kebab)

> [!WARNING]
> - Your warranty is void.
> - All official release builds are tested and safe to use.
> - If you decide to experiment, mess something up, corrupt your storage, turn your phone into a fancy paperweight, or brick it beyond recovery — **don't blame us**.
> - You are doing this at **your own risk** and take full responsibility for anything that may happen.

> [!NOTE]
> - The device must have an **unlocked bootloader**.
> - Working **ADB and fastboot** drivers must be installed on your computer.
> - Make a **full data backup** before flashing.
> - Ensure your device has at least **30% battery**.
> - Flash **only** files meant for **OnePlus 8T (kebab)**.
> - First boot may take 5–10 minutes. Do **not** interrupt or force reboot unless it exceeds 10 minutes.

> [!IMPORTANT]
> These releases **do not include firmware**. You **must** flash the required firmware
> (**OOS 14.0.0.603 (EX01)**, model **KB2005**) before flashing the ROM.

---

## First Time Install

### Step 1 — Flash firmware (required)

1. Download the **recovery** & **ROM** for your device from [here](https://cdn.axionos.org/#kebab).
2. Download the required firmware — **OOS 14.0.0.603 (EX01)** for the OnePlus 8T — from [here](https://github.com/luk1337/oplus_archive/releases).
3. Use the search box and filter by your model, e.g. **KB2005 (kebab)**, like [this](https://github.com/luk1337/oplus_archive/releases?q=14.0.0.601%28EX01%29&expanded=true).
4. Flash the firmware using the [LineageOS firmware update guide for kebab](https://wiki.lineageos.org/devices/kebab/fw_update/), then continue with the steps below.

### Step 2 — Flash the ROM

1. Reboot to **bootloader**.
2. Flash the images and boot to recovery:
   ```
   fastboot flash recovery recovery.img
   fastboot reboot recovery
   ```
3. While in recovery, navigate to **Factory reset → Format data/factory reset** and confirm to format the device.
4. When done formatting, go back to the main menu and navigate to **Apply update → Apply from ADB**.
5. Sideload the ROM (replace `rom` with the actual filename):
   ```
   adb sideload rom.zip
   ```
6. *(Optional)* Reboot to recovery (fully) to sideload any add-ons (e.g. Magisk).
7. Reboot to **System** & **Enjoy**

---

## Update

1. Reboot to **Recovery**.
2. While in recovery, navigate to **Apply update → Apply from ADB**.
3. Sideload the ROM (replace `rom` with the actual filename):
   ```
   adb sideload rom.zip
   ```
4. *(Optional)* Reboot to recovery to sideload any add-ons (e.g. Magisk).
5. Reboot to **System** & **Enjoy**
