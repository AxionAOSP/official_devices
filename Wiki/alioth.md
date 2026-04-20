# Installation Guide — POCO F3(alioth)

> [!WARNING]
> - Your warranty is void.
> - All official release builds are tested and safe to use.
> - If you decide to experiment, mess something up, corrupt your storage, turn your phone into a fancy paperweight, or brick it beyond recovery — **don’t blame us**.
> - You are doing this at **your own risk** and take full responsibility for anything that may happen.

> [!NOTE]
> - The device must have an **unlocked bootloader** and the **required recovery**.
> - Make a **full data backup** before flashing.
> - Ensure your device has at least **30% battery**.
> - Flash **only** files meant for **POCO F3**.
> - First boot may take 5–10 minutes. Do **not** interrupt or force reboot unless it exceeds 10 minutes.
> - Please make an IMEI backup.

---

## Clean Flash Guide (TWRP/OFOX)

###  Encrypted

1. Reboot **recovery**
2. Flash Firmware **ALIOTHGlobal_OS1.0.2.0.TKHMIXM**
3. Flash **ROM**
4. Reflash **OrangeFox.zip** or **TWRP.zip** *(or tick “Reflash OFOX/TWRP” if available)*
5. Reboot **Recovery**
6. Flash **GApps** *(only if using Vanilla ROM)*
7. **Format Data**
8. Reboot to **system**

---

###  Decrypted

1. Reboot **recovery**
2. Flash Firmware **ALIOTHGlobal_OS1.0.2.0.TKHMIXM**
3. Flash **ROM**
4. Reflash **OrangeFox.zip** or **TWRP.zip** *(or tick “Reflash OFOX/TWRP” if available)*
5. Reboot **Recovery**
6. Flash **GApps** *(only if using Vanilla ROM)*
7. **Format Data** *(only for first time DFE flash)*
8. Wipe:
   - Cache  
   - Dalvik  
   - Metadata  
   - Data *(only if previously decrypted)*
9. Reboot to **System**

## Clean Flash Guide (AxionOS Recovery)

1. Download the latest **axion-*-alioth.zip** from the [website](https://cdn.axionos.org).
2. Extract the rom and get the **vendor_boot.img**
3. Connect your phone to PC and reboot to **fastboot** by holding both power button and volume down keys.
4. Flash **vendor_boot.img** powershell/cmd:

```
fastboot flash vendor_boot <drag-&-drop-vendor_boot.img>
```
5. Reboot to **recovery** using:

```
fastboot reboot recovery
```
6. Select **Factory Reset**
7. Tap **Format Data / Factory Reset** and confirm
8. Go to **Apply Update**
9. Choose:
   - **ADB Sideload**
10. Flash the **ROM**
8. Reboot to **System**

---

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
> - **OrangeFox**, **TWRP**, and **AxionOS Recovery** are supported  
> - First boot may take **5–10 minutes**  
> - Do not interrupt the process  

---

## Support / Bug Reports

📢 **[Telegram Group](https://t.me/yaseaprjktchat)** 