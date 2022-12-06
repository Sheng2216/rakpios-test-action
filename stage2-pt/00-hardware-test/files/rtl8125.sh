#!/bin/bash

pushd /usr/local/linuxpg >> /dev/null
rmmod r8169
insmod pgdrv.ko
./rtnicpg-aarch64-linux-gnu /w /efuse
rmmod pgdrv
modprobe r8169
popd >> /dev/null

