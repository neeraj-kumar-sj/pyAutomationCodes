import os
import WebServer_automation as wsa
# ------------->>        CREATING A PARTITION       <<--------

def create_partition():
    print("\t\t YOU HAVE CHOSEN DISK PARTITION OPTION \n\n")
    d = input("Enter the Disk Name: ")
    ps = input("Enter the Partition Size: ")
    i = "(echo 'n' ; echo 'p' ; echo -ne '\n' ; echo -ne '\n' ; echo '+'+ps+'G';) | fdisk /dev/"+d
    os.system(i)
    os.system("udevadm settle")
    os.system("lsblk")

# -------------->>         formatting a disk        <<-------


def format_disk():
    d = input("Enter disk name")
    os.system("mkfs.ext4 /dev/"+d)

# ------------->>   To mount a disk                 <<-------


def mount_disk():
    f = input("Enter disk name: ")
    p = input("Enter a participation name(example drive3): ")
    os.system("mkdir /"+p)
    os.system("lsblk")
    os.system("mount /dev/"+f + " " + "/"+p)
    os.system("cd /"+p)
    os.system("lsblk")


# -------------->>         formatting a disk        <<-------

def format_disk():
    d = input("Enter disk name")
    os.system("mkfs.ext4 /dev/"+d)

# ------------->>   To mount a disk                 <<-------


def mount_disk():
    f = input("Enter disk name: ")
    p = input("Enter a participation name(example drive3): ")
    os.system("mkdir /"+p)
    os.system("lsblk")
    os.system("mount /dev/"+f + " " + "/"+p)
    os.system("cd /"+p)
    os.system("lsblk")


# ------------->>   To configure yum                <<-------

def configure_yum():
    os.system("cd /etc/yum.repos.d")
    f1 = open("yum1.repo", "w")
    f1.write('''
[dvd1]
baseurl=/run/media/root/RHEL-8-0-0-BaseOS-x86_64/AppStream
gpgcheck=0

[dvd2]
baseurl=/run/media/root/RHEL-8-0-0-BaseOS-x86_64/BaseOS
gpgcheck=0''')
    f1.close()
    loc = input(
        "Enter the director name where your menu Program is save (/arth/menu.py: ")
    os.system("cp "+loc+"/yum1.repo /etc/yum.repos.d")
    os.system(
        "dnf install https://dl.fedoraproject.org/pub/epel/epel-release-latest-8.noarch.rpm -y")


# ------------->>   To configure apache web server  <<-------

def configure_appache_web_server():
    wsa.menu()
#    os.system("dnf install httpd -y")
#    os.system("systemctl enable httpd")


# ------------->>   To create a Lvm Storage         <<-------


def create_lvm_storage():
    d1 = input("Enter first disk name: ")
    d2 = input("Enter second disk name: ")
    v = input("Enter the name of the volume group: ")
    n = input("Enter the name of the LVM: ")
    s = input("Enter the size of the LVM: ")
    dr = input("Input the LVM mountpoint name i.e Create a Directory: ")
    # pv creation
    os.system("pvcreate /dev/"+d1)
    os.system("pvcreate /dev/"+d2)
    # vg creation
    os.system("vgcreate "+v+" /dev/"+d1+" /dev/"+d2)
    os.system("vgdisplay "+v)
    # lvm creation
    os.system("lvcreate --size +"+s+"G --name "+n+" "+v)
    # formatting
    os.system("mkfs.ext4 /dev/"+v+"/"+n)
    # mounting
    os.system("mkdir /"+dr)
    os.system("mount /dev/"+v+"/"+n+" "+"/"+dr)
    os.system("cd /"+dr)


# ------------->>   To create a namenode on hadoop  <<-------


