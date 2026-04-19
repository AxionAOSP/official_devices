# Installation Guide — Oneplus Nord (avicii)

> [!WARNING]
> - Your warranty is now void.
> - All official release builds are tested and safe to use.
> - If you decide to experiment, mess something up, corrupt your storage, turn your phone into a fancy paperweight, or brick it beyond recovery — **don't blame us**.
> - You are doing this at **your own risk** and take full responsibility for anything that may happen.

> [!NOTE]
> - The device must have an **unlocked bootloader**.
> - Ensure you are using the [latest](https://developer.android.com/tools/releases/platform-tools) Platform Tools.
> - Make a **full data backup** before flashing.
> - Ensure your device has at least **30%** battery.
> - Ensure you've logged out of your Google Account before installing to avoid factory reset protection.
---

## Clean Installation

1. Boot to **Recovery**.

2. Flash the ROM zip from internal storage, USB OTG, or via ADB sideload:

   ```bash
   adb sideload <rom.zip>
   ```

   > [!TIP]
   > ADB sideload may stop at **47%** and report **Total xfer: 1.00x**. This is completely normal behavior & the flashing process was successful.

3. Select **Factory reset** → **Format data/factory reset** and confirm.

4. Select **Reboot system now**.

---

## Update (Dirty Flash)

> [!NOTE]
> Dirty flashing will not work for major Android version upgrades (e.g., 1.x → 2.x).

### Method 1: OTA Update

1. Simply upgrade via the built-in OTA updater — either from a pushed update or by importing a local update package.

### Method 2: Recovery Sideload

1. Reboot to **Recovery**.

2. Flash the ROM zip from internal storage, USB OTG, or via ADB sideload:

   ```bash
   adb sideload <rom.zip>
   ```

3. Select **Reboot system now**.

---

> [!IMPORTANT]
> For vanilla builds, GApps must be reflashed after every update, including OTA and recovery-based dirty flashes.

## Support / Bug Reports
- **[Telegram Group](https://t.me/sanjusprjkt)**
