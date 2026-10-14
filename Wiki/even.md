# Installation Guide — Realme C25 / C25s / Narzo 50A (even)

> [!WARNING]
> - Your warranty is void.
> - All official release builds are tested and safe to use.
> - If you decide to experiment, mess something up, corrupt your storage, turn your phone into a fancy paperweight, or brick it beyond recovery — **don’t blame us**.
> - You are doing this at **your own risk** and take full responsibility for anything that may happen.

> [!NOTE]
> - Supported devices: **Realme C25 (RMX3191 / RMX3193) / Realme C25s (RMX3195 / RMX3197) / Realme Narzo 50A (RMX3430)** — codename **even**.
> - The device must have an **unlocked bootloader** and a **recommended custom recovery** (TWRP / OrangeFox / PBRP — ask in the support group for the recommended build).
> - Make a **full data backup** before flashing.
> - Ensure your device has at least **30% battery**.
> - Flash **only** files meant for **even**.
> - First boot may take 5–10 minutes. Do **not** interrupt or force reboot unless it exceeds 10 minutes.

---

## Clean Installation

1. Boot into your **custom recovery**.
2. Go to **Wipe → Advanced Wipe** and wipe Cache, Dalvik / ART cache, Data, Metadata.
3. Flash the **ROM**.
4. *If you are using the **vanilla build**, flash **GApps** now.* *If you are using the **GMS build**, skip this step.*
5. Reboot back into **Recovery**.
6. Select **Wipe → Format Data** and type `yes`.
7. Reboot to **System**.

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
5. Reboot to **System**.

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

## Support / Bug Reports

 **[Telegram Group](https://t.me/c25series_official)**
