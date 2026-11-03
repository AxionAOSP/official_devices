# Installation Guide — POCO X4 GT / Redmi Note 11T Pro (+) / Redmi K50i (xaga)

> [!WARNING]
> - Your warranty is void.
> - All official release builds are tested and safe to use.
> - If you decide to experiment, mess something up, corrupt your storage, turn your phone into a fancy paperweight, or brick it beyond recovery — **don’t blame us**.
> - You are doing this at **your own risk** and take full responsibility for anything that may happen.

> [!NOTE]
> This guide covers the requirements, driver setup, and flashing steps for AOSP fastboot ROMs on **xaga** (POCO X4 GT / Redmi Note 11T Pro (+) / Redmi K50i).

---

## Requirements

- **Unlocked bootloader** ([Guide](https://aosp.angxddeep.com/unlock-bootloader))
- **PC** (Windows, macOS, or Linux)
- **USB cable** (reliable data cable)
- Make sure device battery is at least **30%**
- Make a **full data backup** before proceeding

---

## Getting Drivers

> [!INFO]
> If you have already flashed a ROM before and your device was detected correctly in fastboot, you can skip this step and go straight to the [flashing instructions](#flashing-instructions).

1. Join the [main Telegram group](https://t.me/PocoX4GT) for POCO X4 GT / Redmi Note 11T Pro (+) / Redmi K50i (xaga).
2. Complete the captcha verification.
3. Send `#drivers` in the group to get the drivers note.
4. Install all 3 drivers listed in the `#drivers` note.
5. Restart your PC.

---

## Flashing Instructions

### Prerequisite: Install Android Platform Tools

Ensure you have the latest platform tools installed on your operating system before following the instructions:

- **Windows**:
  ```powershell
  winget install -e --id Google.PlatformTools
  ```
- **macOS**:
  ```bash
  brew install android-platform-tools
  ```
- **Linux**:
  ```bash
  sudo apt install android-sdk-platform-tools
  ```

Alternatively, you can manually download the [latest Android SDK Platform-Tools](https://developer.android.com/tools/releases/platform-tools).

---

### Step-by-Step Instructions

1. **Back up your data**  
   Back up all critical files to an external drive or cloud storage. The device bootloader must be unlocked and ADB/Fastboot drivers installed on your PC.

2. **Boot into Fastboot Mode**  
   - Power off the device completely.
   - Hold **Volume Down + Power** simultaneously until the Fastboot logo appears.
   - Connect the device to your PC with a reliable USB cable and verify the connection:
     ```bash
     fastboot devices
     ```

3. **Flash Boot and Vendor Boot Images**  
   Flash the downloaded `boot.img` and `vendor_boot.img` partitions:
   ```bash
   fastboot flash boot boot.img
   fastboot flash vendor_boot vendor_boot.img
   ```
   *(Replace with the actual paths or drag and drop the image files into the terminal)*

4. **Boot into Axion Recovery**  
   > [!WARNING]
   > Do **NOT** use `fastboot reboot recovery` as it does not work properly on this device.

   Manually reboot into recovery from fastboot by pressing and holding **Power + Volume Up** simultaneously until the recovery screen appears.

5. **Format Data / Factory Reset**  
   Inside Axion Recovery, navigate using the volume buttons and power key (or touch):
   - Select **Factory Reset → Format Data/Factory Reset**.
   - Confirm the format operation.

6. **Enable ADB Sideload**  
   On the recovery main menu, select:
   - **Apply update → ADB sideload** (or **Apply from ADB**)

7. **Sideload the ROM Package**  
   Execute the sideload command from your terminal:
   ```bash
   adb sideload <rom_filename>.zip
   ```
   *(e.g., `adb sideload axion-*-xaga.zip`)*

   > [!TIP]
   > **Normal Sideload Behavior:**  
   > While sideloading, the progress stopping at **47%** or **94%** is completely normal (often showing `Total xfer: 1.00x` or `adb: failed to read command: Success`). Do not disconnect your device until the terminal finishes or returns to the recovery menu.

8. **Additional Packages Prompt**  
   If the recovery screen asks:
   > *"Do you want to Install additional packages?"*
   - Choose **NO** if you have no additional packages.
   - If you need to flash GApps (on a Vanilla build) or other add-ons, choose **YES** to reboot back into recovery and sideload them.
   - Finally, select **Reboot system now**.

---

## Update (Dirty Flash)

> [!NOTE]
> Dirty flashing will not work for major Android version upgrades (e.g., 1.x → 2.x).

### Method 1: OTA Update
1. Go to **Settings → System → System updates**.
2. Download the latest available build.
3. Tap **Reboot** once the download finishes.
4. The device will reboot into recovery and install the update automatically.
5. Reboot to **System**.

---

### Method 2: Recovery Sideload
1. Reboot to **Recovery**.
2. Select **Apply update → Apply from ADB**.
3. Sideload the update ROM:
   ```bash
   adb sideload <rom_filename>.zip
   ```
4. After sideload completes, select **NO** (*unless reflashing additional packages*).
5. Select **Reboot system now**.

---

> [!IMPORTANT]
> For **vanilla builds**, **GApps must be reflashed after every update**, including **OTA** and **recovery-based dirty flashes**.

