# Installation Guide — Motorola G57 Power (mumba)

> [!WARNING]
> - Your warranty is void.
> - All official release builds are tested and safe to use.
> - If you decide to experiment, mess something up, corrupt your storage, turn your phone into a fancy paperweight, or brick it beyond recovery — **don’t blame us**.
> - You are doing this at **your own risk** and take full responsibility for anything that may happen.
> * It is **COMPULSORY** to sideload **[copy-partitions-20220613-signed.zip](https://mirrorbits.lineageos.org/tools/copy-partitions-20220613-signed.zip)**, failing to do so will **HARD-BRICK** your device.

> [!NOTE]
> - The device must have an **unlocked bootloader** and the **required recovery**.
> - Make a **full data backup** before flashing.
> - Ensure your device has at least **30% battery**.
> - Flash **only** files meant for **Motorola G57 Power (mumba))**.
> - First boot may take 5–10 minutes. Do **not** interrupt or force reboot unless it exceeds 10 minutes.
> - Please make an IMEI backup.

---

## Clean Flash Guide

1. Download the latest **axion-*-mumba.zip** from the [website](https://cdn.axionos.org/#mumba).
2. Extract the rom and get the **recovery.img**
3. Connect your phone to PC and reboot to **fastboot** by holding both power button and volume down keys.
4. Flash **recovery.img** **vendor_boot.img** powershell/cmd:

```
fastboot flash recovery <drag-&-drop-recovery.img>
fastboot flash vendor_boot <drag-&-drop-vendor_boot.img>
```
5. Reboot to **recovery** using:

```
fastboot reboot recovery
```
6. Select **Factory Reset**
7. Tap **Format Data / Factory Reset** and confirm
8. Select **Apply update → Apply from ADB**, then sideload **[copy-partitions-20220613-signed.zip](https://mirrorbits.lineageos.org/tools/copy-partitions-20220613-signed.zip)**.
9. Select **Apply update → Apply from ADB**, then sideload the rom using:

```
adb sideload <drag-&-drop-rom.zip>
```
10. After sideload completes, select **YES** to reboot if you have extra packages (i.e., GApps) to install and **NO** if you have none.
11. Select **Factory reset → Format data/factory reset**.
12. Select **Reboot system now**.

---

> [!IMPORTANT]
> For **vanilla builds**, **GApps must be reflashed after every update**,  
> including **OTA** and **recovery-based dirty flashes**.

## Dirty Flash (Update)

> [!NOTE]
> - Dirty flash keeps your data  
> - Not supported for **major Android upgrades** *(example: 1.x → 2.x)*  

### 📡 OTA Update

1. Go to **Settings → System → System Update**
2. Download the latest build
3. Tap **Reboot**
4. Device will reboot to recovery and install automatically
5. Reboot to **System**

---

###  Local Update

1. Download the **Update Package**
2. Go to **Settings → System → System Update**
3. Tap **Local Update / Select Package** *(option name may vary)*
4. Choose the downloaded file
5. Tap **Reboot**

## Notes

> [!IMPORTANT]
> - First boot may take **5–10 minutes**  
> - Do not interrupt the process  
