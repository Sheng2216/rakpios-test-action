#!/bin/bash -e

on_chroot << EOF

pip3 install pyserial
pip3 install smbus
pip3 install smbus2
pip3 install adafruit-ads1x15
pip3 install adafruit-circuitpython-bme280
pip3 install RPi.GPIO
pip3 install gpiod
pip3 install adafruit-circuitpython-shtc3
pip3 install psutil
pip3 install iperf3
pip3 install adafruit-extended-bus
pip3 install adafruit-circuitpython-atecc
pip3 install luma.core
pip3 install luma.oled
pip3 install LoRaRF
pip3 install adafruit-circuitpython-mcp230xx

#Replace the dt-blob.bin to enable the display and dual cameras on RAK7391
wget https://datasheets.raspberrypi.com/cmio/dt-blob-disp1-cam2.bin -O /boot/dt-blob.bin

EOF

# 2.5G Ethernet Port Status LED
cp files/pgdrv_once "${ROOTFS_DIR}/etc/init.d/"
cp -r files/linuxpg "${ROOTFS_DIR}/usr/local/"
on_chroot << EOF
systemctl enable pgdrv_once
EOF

#Copy production-testing script
cp -r files/hardware-test "${ROOTFS_DIR}/home/rak"
#chown -R ${FIRST_USER_NAME}:${FIRST_USER_NAME} "${ROOTFS_DIR}/home/rak/hardware-test"
#Update config.txt
cp files/config.txt "${ROOTFS_DIR}/boot/"

#Set the mofo static IP for testing
#eth0
cp files/ethernet-eth0.nmconnection "${ROOTFS_DIR}/etc/NetworkManager/system-connections/"
chmod -R 600 "${ROOTFS_DIR}/etc/NetworkManager/system-connections/ethernet-eth0.nmconnection"
chown -R root:root "${ROOTFS_DIR}/etc/NetworkManager/system-connections/ethernet-eth0.nmconnection"
#eth1
cp files/ethernet-eth1.nmconnection "${ROOTFS_DIR}/etc/NetworkManager/system-connections/"
chmod -R 600 "${ROOTFS_DIR}/etc/NetworkManager/system-connections/ethernet-eth1.nmconnection"
chown -R root:root "${ROOTFS_DIR}/etc/NetworkManager/system-connections/ethernet-eth1.nmconnection"



