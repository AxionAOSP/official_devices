# Installation Guide — POCO X7 Pro (rodin)

> [!WARNING]
> - Your warranty is void.
> - All official release builds are tested and safe to use.
> - If you decide to experiment, mess something up, corrupt your storage, turn your phone into a fancy paperweight, or brick it beyond recovery — **don’t blame us**.
> - You are doing this at **your own risk** and take full responsibility for anything that may happen.

> [!NOTE]
> - The device must have an **unlocked bootloader**.
> - Make a **full data backup** before flashing.
> - Ensure your fingerprint data and lockscreen settings deleted and swipe to unlock by default.
> - Ensure your device has at least **30% battery**.
> - Flash **only** files meant for **POCO X7 Pro (rodin)**.
> - Make sure you're on HyperOS 2.x or 6.6.56 kernel based firmware.
> - First boot may take 5–10 minutes.Do **not** interrupt or force reboot unless it exceeds 10 minutes.

---

## Clean Installation / Recovery Flash

1. Flash vendor_boot on bootloader/fastboot orange mode. `fastboot flash vendor_boot vendor_boot.img`
2. Boot into the **recovery**.
3. Perform a **Format data**.
4. Flash the **ROM** using sideload method. (Choose `Apply update -> ADB sideload`) then execute this on your terminal. `adb sideload axion-xxxx-xxxxxxxxx.zip`.
5. *If you are using the **vanilla build**, reboot to recovery once again then flash **GApps**.* Else *If you are using the **GMS build**, skip this step.*
6. Reboot to **System**. 

---

## Update (Dirty Flash)

> [!NOTE]
> Dirty flashing **will not work** for major Android version upgrades  
> (example: **1.x → 2.x**).

### Method 1: OTA Update

1. Go to **Settings → System → System updates**.
2. Download the latest available build.
3. Tap **Reboot** once the download finishes.
4. Device should boot with the new update.

---

> [!IMPORTANT]
> For **vanilla builds**, **GApps must be reflashed after every update**,  
> including **OTA** and **recovery-based dirty flashes**.

---

## Support / Bug Reports

📢 **[Telegram Group](https://t.me/rexp_discussion)** 
