# Installation Guide — OnePlus 8 Pro (instantnoodlep)

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
> - Flash **only** files meant for **OnePlus 8 Pro (instantnoodlep)**.
> - These releases **include firmware**, so no separate firmware flash is required.
> - First boot may take 5–10 minutes. Do **not** interrupt or force reboot unless it exceeds 10 minutes.

---

## First Time Install

1. Download the **recovery** & **ROM** for your device from [here](https://cdn.axionos.org/#instantnoodlep).
2. Reboot to **bootloader**.
3. Flash the images and boot to recovery:
   ```
   fastboot flash recovery recovery.img
   fastboot reboot recovery
   ```
4. While in recovery, navigate to **Factory reset → Format data/factory reset** and confirm to format the device.
5. When done formatting, go back to the main menu and navigate to **Apply update → Apply from ADB**.
6. Sideload the ROM (replace `rom` with the actual filename):
   ```
   adb sideload rom.zip
   ```
7. *(Optional)* Reboot to recovery (fully) to sideload any add-ons (e.g. Magisk).
8. Reboot to **System** & **Enjoy**

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
