---
date:
    created: 2026-04-16
draft: true
tags:
  - DevOps
---
My note about hardware
<!-- more -->

# 1. Components
## 1.1 Motherboard

- motherboard type for Comptia A+(based on size or form factor):
	- ATX: most common:
		- full-sized
	- mini ATX
	- ITX

- motherboard components:
	- PCI/PCI Express
	- South bridge
	- North bridge
	- BIOS:
		- Read memory chip(ROM chip): store bios
		- Bios chip(CMOS chip): store configuration of Bios Setting
		- Jumper: connector that resets bios settings
	- TPM(Personal PC)/HSM(Server cluster): Manage hardware security keys and encryption function to encrypt files in systems
	- expansion slot

## 1.2 CPU
CPU supports 2 types of sockets on motherboard:
- Land grid array(LGA socket,): data transfer pins on motherboard
- Pocket grid array(PGA socket): data transfer pins on CPU

In addition, make sure CPU socket size on motherboard and from your CPU matches

## 1.3 CPU cooler
Thermal paste:

Type of CPU cooler:
- liquid cooler
- Air cooler([current example](https://www.amazon.ca/Thermalright-Peerless-Assassin-Aluminium-Technology/dp/B0BN59961D/ref=asc_df_B0BN59961D?mcid=660b0e2a36b536ec8fb376073a8d7b14&tag=googleshopc0c-20&linkCode=df0&hvadid=706738331967&hvpos=&hvnetw=g&hvrand=9280114439523908352&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9192341&hvtargid=pla-2161042694072&hvocijid=9280114439523908352-B0BN59961D-&hvexpln=0&gad_source=1&th=1))

Air CPU cooler consists of:
- heat sink 
- fan

Liquid cooler consists of components:
- water block
- radiator

## 1.4 RAM
The RAM types hierachy are as following:
![[Pasted image 20260406102618.png]]
Modern computer uses the `DDR SDRAM` under `DRAM`. Now DDR 5 are coming out

RAMs are located on the DIMM(Dual Inline Memory Module) stick of the motherboard

## 1.5 Storage
2 types of storage:
- HDD
- SSD

HDD uses SATA cables to move data on motherboard, while SSD uses NVM express(in particular it is an expansion slot rather than a cable) to be connected to the motherboard

## 1.6 Power Supply
Power supplies convert the AC current from the wall outlet to DC current for computer.

# 2. Assembling desktop
1. We should be careful with static discharge from our hands: wear anti-static wristband

# 3. Installing Windows System
## 3.1 Install on new machine


## 3.2 Reinstall
Reinstall the same windows system edition if the computer has been installed a system previously.
### 3.2.1 Clean install(Install media)
https://www.youtube.com/watch?v=bP03Y-l9NOM
1. Screenshot the device manager
2. Download bootable program onto the USB
3. Launch the BIOS page and select boot from USB
4. choose the disk partition, just unallocate it for SSD
5. choose windows edition as the previous windows system edition. Otherwise, you have to re-purchase the activation key for that edition. But if you choose the same edition as previous edition, the same activation key you entered at that time can be reused.
6. After the system is installed, open device manager and check with the screenshot in step 1 and ensure every hardware works(If missing sth, you can fix by installing a software called driver booster)

Feature: clean the contents and re-allocate disk partition
## 3.2.2 Windows Reset
1. Settings > Windows Update > Recovery, Reset this computer, choose keep your files(windows will keep files under `C:/Users/<Your_name>`, but remove everything plus contents under `AppData`)

Feature: reset C: drive but leave other drive unchanged and won't re-allocate disk partition

## 3.3 Upgrade

## 3.4 Upgrade Edition
Assume we want to upgrade from windows home to Pro, we need to purchase a new activation key. There are 2 types of windows keys: Retail key and OEM keys. OEM keys can be reused on the same machine when reinstalling the system, while retail key can be reused on another machine when installing systems.

In addition, upgrading edition will not delete your files
tutorial: https://www.youtube.com/watch?v=5oRARXEqrJY
link to buy cheap oem key: https://ca.vip-urcdkey.com/software/p201710180856556150.html?urd=TS10

1. disconnect from the Internet
2. System > activation > Change product key, enter the generic product key in this link(https://learn.microsoft.com/en-us/answers/questions/4199508/upgrade-windows-10-home-(digital-license)-to-windo?forum=windows-all&referrer=answers)


# 4. Directory System

LDAP(light weight directory access protocol): implementation service of this protocol include active directory, openLDAP

# 5. How to enter BIOS
Example: Thinkpad T480s(windows 10)

Methods:
- Bootup: After booting up the laptop from power button, when the logo "lenovo" appears on the screen, press enter and then press F1 to enter
- After launching up: Settings > Update and Security > Restore > Advanced bootup