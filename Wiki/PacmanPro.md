# Installation Guide - Nothing Phone 2a Plus (PacmanPro)

>[!WARNING]
> - Your warrenty is void. 
> - All official builds are tested and safe to use
> - If you decide to experiment, mess something up, corrupt your storage, turn your phone into a fancy paperweight, or brick it beyond recovery — **don’t blame us**.
> - You are doing this at **your own risk** and take full responsibility for anything that may happen.
> - Flashing a Pacman build on PacmanPro will instantly **brick** your device.

>[!NOTE]
> - The device must have an **unlocked bootloader**.
> - Make a **full data backup** before flashing.
> - Do backup your IMEI.
> - Ensure your device has at least **30% battery**.
> - Flash **only** files meant for **Nothing Phone (2a) Plus (PacmanPro)**.
> - First boot may take 5–10 minutes. Do **not** interrupt or force reboot unless it exceeds 10 minutes.
> - Coming from another ROM will require a clean flash.

---

## Clean Installtion

1. Download the latest **axion-*-PacmanPro.zip** from the [website](https://cdn.axionos.org/#PacmanPro).
2. Connect your phone to PC and reboot to **fastboot** by using:
``` 
adb reboot bootloader 
```

3. Flash the following partitions **one by one** through powershell/terminal using:

```
fastboot flash boot <drag-&-drop-boot.img>
```
```
fastboot flash vendor_boot <drag-&-drop-vendor_boot.img>
```

4. if you are flashing from stock ROM , wipe super empty as well 

```
fastboot wipe-super <drag-&-drop-super_empty.img>
```

5. Reboot to **recovery** using:

```
fastboot reboot recovery
```
6. Select **Factory reset → Format data/factory reset**.
7. Select **Apply update → Apply from ADB**, then sideload the rom using:

```
adb sideload <drag-&-drop-rom.zip>
```
8. After sideload completes, select **YES** to reboot if you want extra packages to install and **NO** if you have none.
9. Select **Factory reset → Format data/factory reset**.
10. Select **Reboot system now**.
---

## Update (dirty flashing)

>[!WARNING]
> - If you have fenrir installed on your phone , Dirty flashing will not work and your phone may get bricked. Please Perform a clean flash.

#### Method 1 - OTA Update

1. Go to Settings > System > System Updates.
2. Select Download to download the update.
3. Click on Install after the Download is complete.
4. Reboot after the installation is successful.


#### Method 2 - Local Update

1. Download the latest **axion-*-PacmanPro.zip** from the [website](https://cdn.axionos.org/#PacmanPro).
2. Go to Settings > System > System Updates.
3. Click on 3-dots in upper-right corner and select **Local update**.
4. Navigate to the folder where **axion-*-PacmanPro.zip** is located and Select it.
5. Reboot after the update is finished.
6. **Enjoy**

#### Method 3 - Recovery sideload

1. Reboot to **Recovery** using:
```
adb reboot recovery
```
2. While in recovery, navigate to **Apply update → Apply from ADB**.
3. Sideload the ROM (replace `rom` with the actual filename):
   ```
   adb sideload rom.zip
   ```
4. *(Optional)* Reboot to recovery to sideload any add-ons.

5. Reboot to **System** & **Enjoy**

---

> [!IMPORTANT]
> For **vanilla builds**, **GApps must be reflashed after every update**,  
> including **OTA** and **recovery-based dirty flashes**.

---

## Support / Bug Reports

📢 **[Telegram Group](https://t.me/exediscuss)** 