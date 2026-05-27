# Installation Guide — Redmi 9 (lancelot)

> [!WARNING]
> - Your warranty is now void.
> - All official release builds are tested and safe to use.
> - If you decide to experiment, mess something up, corrupt your storage, turn your phone into a fancy paperweight, or brick it beyond recovery — **don’t blame us**.
> - You are doing this at **your own risk** and take full responsibility for anything that may happen.
> - Ensure that you have a IMEI Backup before flash!

> [!NOTE]
> - The device must have an **unlocked bootloader**.
> - Ensure you are using the [latest](https://developer.android.com/tools/releases/platform-tools) Platform Tools.
> - Make a **full data backup** before flashing.
> - Ensure your device has at least **30%** battery.
> - Ensure you've logged out of your Google Account before installing to avoid factory reset protection.

## Firmware

1. First of all, download and extract MIUI 12.5.6.0 RJCMIXM fastboot version.
2. Download and extract platform-tools inside the folder where you extracted MIUI 12.5.6.0.
3. Connect your phone in fastboot, then run flash_all.bat.
4. Wait for the device to restart automatically.
---

## Clean Installation

1. Download the latest **axion-*-lancelot.zip** and **recovery.img** from the [website](https://cdn.axionos.org/#lancelot).
2. Connect your phone to your PC and reboot to **fastboot** (Hold Power + Volume Down).
3. Flash the **recovery.img** using the following command:
   ```bash
   fastboot flash recovery <drag-&-drop-recovery.img>
   ```
4. Reboot to **Recovery** (Use volume buttons to choose reboot to recovery in the menu or run ```fastboot reboot recovery```).

5. Select **Factory reset** → **Format data/factory reset** and confirm.

6. Return to the main menu and select **Apply update** → **Apply from ADB**.

7. **Sideload** the ROM using:

   ```bash
   adb sideload <drag-&-drop-rom.zip>
   ```
> [!TIP]
> ADB sideload may stop at **47%** and report **Total xfer: 1.00x**. This is completely normal behavior & the flashing process was successful.

1. Regarding GApps / Extra Packages:

   > - If you are on a GMS build, just skip.

   > - If you need to flash GApps (on a Vanilla build), follow the next steps.

2. Select **Factory reset** → **Format data/factory reset** one last time to ensure encryption is wiped.

3.  Select **Reboot system now**.

## Update (Dirty Flash)
> [!NOTES]
> Dirty flash is not recommended!
> Dirty flashing will not work for major Android version upgrades (e.g., 1.x → 2.x).

### Method 1: OTA Update
1. Go to **Settings** → **System** → **System updates**.

2. Download the **latest** available build.

3. Tap **Reboot** once the download and initialization finishes.

4. The device will automatically install and reboot to System.

### Method 2: Recovery Sideload
1. Reboot to **Recovery**.

2. Select **Apply update** → **Apply from ADB**.

3. **Sideload** the ROM:

     ```bash
    adb sideload <drag-&-drop-rom.zip>
    ```
4. After sideload completes, Install the gapps if you need them.

5. Select **Reboot system now**.

> [!IMPORTANT]
> For vanilla builds, GApps must be reflashed after every update, including OTA and recovery-based dirty flashes.

## Support / Bug Reports
- **[Telegram Group](https://t.me/doissmchat)** 
