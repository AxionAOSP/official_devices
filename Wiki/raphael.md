# Installation Guide — Redmi K20 Pro/Mi 9T Pro (raphael/in)

> [!WARNING]
> - Your warranty is void.
> - All official release builds are tested and safe to use.
> - If you decide to experiment, mess something up, corrupt your storage, turn your phone into a fancy paperweight, or brick it beyond recovery — **don’t blame us**.
> - You are doing this at **your own risk** and take full responsibility for anything that may happen.

> [!NOTE]
> - The device must have an **unlocked bootloader** and a **recommended custom recovery**.
> - Make a **full data backup** before flashing.
> - Ensure your device has at least **30% battery**.
> - Flash **only** files meant for **Redmi K20 Pro/Mi 9T Pro (raphael/in)**.
> - First boot may take 5–10 minutes.Do **not** interrupt or force reboot unless it exceeds 10 minutes.

---

## Clean Installation

1. Boot into your **recommended recovery**.
2. Flash **legacy to retrofit zip** (if coming from legacy rom)
3. Flash **A11 firmware of your region** (if coming from MIUI/HyperOS or older android version)
4. Flash the **ROM**.
5. *If you are using the **vanilla build**, flash **GApps** now.* *If you are using the **GMS build**, skip this step.*
6. Reboot back into **Recovery**.
7. Select **Wipe → Format Data** and type `yes`.
8. Change **cache and data partitions to F2FS**
9. Reboot to **System**. 

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
2. Select **Install → Choose ROM → Swipe to flash**.
3. Reboot to **System**.

---

> [!IMPORTANT]
> For **vanilla builds**, **GApps must be reflashed after every update**,  
> including **OTA** and **recovery-based dirty flashes**.

---

## Support / Bug Reports / Resources

- **[Telegram Group](https://t.me/Al_Arabis_Support)**
- **[Recommended Recoveries](https://t.me/Al_Arabis_Cloud/348)**
- **[Legacy to retrofit zip](https://t.me/Al_Arabis_Cloud/293)**
- **[Recommended Firmware](https://t.me/Al_Arabis_Cloud/346)**
