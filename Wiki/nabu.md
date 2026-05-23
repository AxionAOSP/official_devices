# Installation Guide — Xiaomi Pad 5 (nabu)

> [!WARNING]
> - Your warranty is now void.
> - All official release builds are tested and safe to use.
> - If you decide to experiment, mess something up, corrupt your storage, turn your tablet into a huge fancy paperweight, or brick it beyond recovery — **don’t blame us**.
> - You are doing this at **your own risk** and take full responsibility for anything that may happen.

> [!NOTE]
> - Your tablet must have an **unlocked bootloader**.
> - Make a **full data backup** before flashing.
> - Ensure your tablet has at least **30% battery**.
> - Flash **only** files meant for **Xiaomi Pad 5 (nabu)**.
> - First boot may take 5–10 minutes. Do **not** interrupt or force reboot unless it exceeds 10 minutes.

---

## Clean Installation

1. Download the latest **axion-*-nabu.zip**, **boot.img**, **dtbo.img**, and **vendor_boot.img** from the [website](https://cdn.axionos.org).
2. Connect your tablet to your PC and reboot to **Fastboot Mode** by pressing and holding both the **Power** and **Volume Down** buttons.
3. Flash the following partitions **one by one** through PowerShell/Terminal using:

```
fastboot flash boot_ab <drag-&-drop-boot.img>
```
```
fastboot flash dtbo_ab <drag-&-drop-dtbo.img>
```
```
fastboot flash vendor_boot_ab <drag-&-drop-vendor_boot.img>
```
4. Reboot to **Recovery** using:

```
fastboot reboot recovery
```
5. Select **Factory reset** → **Format data/factory reset** and confirm.

6. Return to the main menu and select **Apply update** → **Apply from ADB**.

7. **Sideload** the ROM using:

   ```
   adb sideload <drag-&-drop-rom.zip>
   ```
> [!TIP]
> ADB sideload may stop at **47%** and report **Total xfer: 1.00x**. This is completely normal behavior and the flashing process was successful.

> [!NOTE]
> Regarding GApps / Extra Packages:
> - After the sideload, the recovery will ask if you want to install additional packages.
> - If you need to flash GApps (on a Vanilla build), select **YES** to reboot back into recovery.
> - If you are on a GMS build, select **NO**.

8. Select **Factory reset** → **Format data/factory reset** one last time to ensure encryption is wiped.

9. Select **Reboot system now**.

---

## Update (Dirty Flash)

> [!WARNING]
> Dirty flashing **will not work** for major Android version upgrades  
> (example: **1.x → 2.x**).

### Method 1: OTA Update
1. Go to **Settings** → **System** → **System updates**.

2. Download the **latest** available build.

3. Tap **Reboot** once the download and initialization finish.

4. The device will automatically install and reboot to the System.

### Method 2: Recovery Sideload
1. Reboot to **Recovery**.

2. Select **Apply update** → **Apply from ADB**.

3. **Sideload** the ROM:

    ```
    adb sideload <drag-&-drop-rom.zip>
    ```
4. After the sideload completes, select **NO** (**unless you need to reflash GApps**).

5. Select **Reboot system now**.

> [!IMPORTANT]
> For **vanilla builds**, **GApps must be reflashed after every update**,  
> including **OTA** and **recovery-based dirty flashes**.

---

## Support / Bug Reports

📢 **[Telegram Group](https://t.me/+12Ja1iBatW9lNTNl)** 
