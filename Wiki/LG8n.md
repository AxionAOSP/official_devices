# Installation Guide — TECNO POVA 4 Pro(LG8n)

> [!WARNING]
> - Your warranty is void.
> - All official release builds are tested and safe to use.
> - If you decide to experiment, mess something up, corrupt your storage, turn your phone into a fancy paperweight, or brick it beyond recovery — **don’t blame us**.
> - You are doing this at **your own risk** and take full responsibility for anything that may happen.

> [!NOTE]
> - The device must have an **unlocked bootloader** and the **required recovery**.
> - Make a **full data backup** before flashing.
> - Ensure your device has at least **30% battery**.
> - Flash **only** files meant for **TECNO POVA 4 Pro**.
> - First boot may take 5–10 minutes. Do **not** interrupt or force reboot unless it exceeds 10 minutes.
> - Please make an IMEI backup.

>[!CAUTION]
> - DO NOT USE ORANGEFOX

---

## Flash required recovery

1. Boot into bootloader mode(not fastboot)
2. `fastboot flash vendor_boot --slot=all vendor_boot.img`
3. Reboot to Recovery

## Clean Installation (same for AOSP Recovery)

1. Boot into **AxionOS Recovery**.
2. Select **Factory reset -> **Wipe data/factory reset** and choose yes.
3. Flash the **ROM**. *For flashing can use adb sideload or using micro sd card.*
4. Reboot to **System**. 

---

## Update (Dirty Flash)

> [!NOTE]
> Dirty flashing **will not work** for major Android version upgrades  
> (example: **1.x → 2.x**).

### Method 1: OTA Update

1. Go to **Settings → System → System updates**.
2. Download the latest available build.
3. Tap **Reboot** once the download finishes.
4. The device will reboot into recovery and install the update.
6. Reboot to **System**.

---

### Method 2: Recovery Flash

1. Reboot to **Recovery**.
2. Select **Apply Update** -> **Apply from SD Card (or ADB sideload if you do not have an SD Card)**.
3. Reboot to **System**.

---

> [!IMPORTANT]
> **DO NOT** use **OrangeFox or TWRP**

---

## Support / Bug Reports

📢 **[Telegram Group](https://t.me/millenniumdiscussion)** 
