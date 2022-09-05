#!/usr/bin/bash

if [ $USER != "root" ]
then
    echo "please use root user to run!"
    exit
fi


num=`lsblk | grep disk | grep -v boot | wc -l`
names=`lsblk | grep disk | grep -v boot | awk '{print $1}'`
sizes=`lsblk | grep disk | grep -v boot | awk '{print $4}'`
echo ""
echo "Detect Disk Device..."

name=`lsblk | grep disk | grep sd[a-z] | awk '{print $1}'`
size=`lsblk | grep disk | grep sd[a-z] | awk '{print $4}'`
#vendor=$(hwinfo --short | grep -w $name | awk '{print $2}')

echo ""
echo "Find Device! size:$size"

part=`lsblk | grep sd[a-z][1-9] | awk '{print $1}'`
part=${part:2}

echo ""
echo "Mount Device..."
mount /dev/$part /mnt/
echo ""
echo "Write data..."
echo "aabbccddeeff00112233445566"
echo "aabbccddeeff00112233445566" > /mnt/test_file
echo ""
echo "Read data..."
cat /mnt/test_file
echo ""
echo "Umount Device..."
rm /mnt/test_file
umount /dev/$part
echo ""
echo "Done!"


