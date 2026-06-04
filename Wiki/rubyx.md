# Installation Guide — Redmi Note 12 Pro/Plus/Discovery 5G (rubyx)

> [!WARNING]
> - Your warranty is now void.
> - All official release builds are tested and safe to use.
> - If you decide to experiment, mess something up, corrupt your storage, turn your phone into a fancy paperweight, or brick it beyond recovery — **don’t blame us**.
> - You are doing this at **your own risk** and take full responsibility for anything that may happen.

> [!NOTE]
> - The device must have an **unlocked bootloader**.
> - Ensure you are using the [latest](https://developer.android.com/tools/releases/platform-tools) Platform Tools.
> - Make a **full data backup** before flashing.
> - Ensure your device has at least **30%** battery.
> - Flash **only** files meant for **Redmi Note 12 Pro/Plus/Discovery 5G** (*rubyx*).
> - First boot may take 5–10 minutes. Do **not** interrupt or force reboot unless it exceeds 10 minutes.

---

## Clean Installation

1. Download the latest **axion-*-rubyx.zip** and **boot.img** from the [website](https://cdn.axionos.org/#rubyx).
2. Connect your phone to your PC and reboot to **fastboot** (Hold Power + Volume Down).
3. Flash the **boot.img** using the following command:
   ```bash
   fastboot flash boot <drag-&-drop-boot.img>
   ```
4. Reboot to **Recovery** (Hold Power + Volume Up or run ```fastboot reboot recovery```).

5. Select **Factory reset** → **Format data/factory reset** and confirm.

6. Return to the main menu and select **Apply update** → **Apply from ADB**.

7. **Sideload** the ROM using:

   ```bash
   adb sideload <drag-&-drop-rom.zip>
   ```
> [!TIP]
> ADB sideload may stop at **47%** and report **Total xfer: 1.00x**. This is completely normal behavior & the flashing process was successful.

8. Regarding GApps / Extra Packages:

   > - After the sideload, the recovery will ask if you want to install additional packages.

   > - If you need to flash GApps (on a Vanilla build), select **YES** to reboot back into recovery.

   > - If you are on a GMS build, select **NO**.

9. Select **Factory reset** → **Format data/factory reset** one last time to ensure encryption is wiped.

10. Select **Reboot system now**.

## Update (Dirty Flash)
> [!NOTE]
> Dirty flashing will not work for major Android version upgrades (e.g., 1.x → 2.x).

### Method 1: OTA Update
1. Go to **Settings** → **System** → **System updates**.

2. Download the **latest** available build.

3. Tap **Reboot** once the download and initialisation finishes.

4. The device will automatically install and reboot to System.

### Method 2: Recovery Sideload
1. Reboot to **Recovery**.

2. Select **Apply update** → **Apply from ADB**.

3. **Sideload** the ROM:

     ```bash
    adb sideload <drag-&-drop-rom.zip>
    ```
4. After sideload completes, select **NO** (**unless you need to reflash GApps**).

5. Select **Reboot system now**.

> [!IMPORTANT]
> For vanilla builds, GApps must be reflashed after every update, including OTA and recovery-based dirty flashes.

## Support / Bug Reports
📢 **[Telegram Group](https://t.me/casanovas_cult)** 
