# Install AxionOS on cheetah

> [!WARNING]
> Do not relock the bootloader while AxionOS is installed. It will fail verified boot, wipe your data, and may brick the device.

## Before you start

- Read this page through once before doing anything.
- Install `adb` and `fastboot` on your computer.
- Enable USB debugging on the device.
- Boot the stock OS at least once and confirm calls, SMS and mobile data work.
- Sign out of any Google accounts to avoid Factory Reset Protection.
- Back up anything you want to keep. Unlocking the bootloader wipes the device.
- The device must be on the **Android 16** stock firmware before installing AxionOS. Mismatched firmware can cause boot failures or damage.

## Unlock the bootloader

Only needs to be done once.

1. In *Developer options*, enable **OEM unlocking**.
2. Reboot to the bootloader:
   ```
   adb reboot bootloader
   ```
3. Confirm the device shows up:
   ```
   fastboot devices
   ```
4. Unlock:
   ```
   fastboot flashing unlock
   ```
   Confirm on the device when prompted.
5. The device reboots and wipes itself. Re-enable USB debugging when it's back up.

## Flash the AxionOS recovery

1. Download `vendor_boot.img` for **cheetah** from the [AxionOS website](https://cdn.axionos.org).
2. Reboot to the bootloader:
   ```
   adb reboot bootloader
   ```
3. Flash it:
   ```
   fastboot flash vendor_boot vendor_boot.img
   ```
4. From the bootloader menu, use the volume keys to highlight **Recovery mode** and press the power button to select.

## Install AxionOS

1. Download `axion-*-cheetah.zip` from the [AxionOS website](https://cdn.axionos.org).
2. In recovery, pick **Factory reset → Format data / factory reset** and confirm.
3. Back at the main menu, pick **Apply update → Apply from ADB**.
4. Sideload the ROM:
   ```
   adb sideload axion-*-cheetah.zip
   ```
5. Do **not** reboot yet if you need to install GApps.

## Add-ons (vanilla builds only)

> [!NOTE]
> GMS builds already ship with Google Apps. Skip this section.

GApps must be installed before the first boot.

1. Pick **Apply update → Apply from ADB** again.
2. Sideload the GApps zip:
   ```
   adb sideload /path/to/gapps.zip
   ```
3. If you see *Signature verification failed*, accept it. Add-ons aren't signed with the AxionOS key.

## Reboot

Pick **Reboot system now** from the recovery menu. First boot can take up to 15 minutes.

## Updating

### OTA

*Settings → System → System update*. Download, install, reboot.

### Recovery sideload

Boot into recovery and repeat the sideload step with the new ROM zip. Formatting data is not required for a dirty flash.

> [!IMPORTANT]
> Vanilla builds need GApps re-sideloaded after every update, including OTAs. GMS builds do not.

## Support

- [Telegram group](https://t.me/AxionAOSP_PixelsSupport)
