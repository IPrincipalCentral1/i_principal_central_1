












'''


i should have : 

    nasm 
    
    make
    
    qemu
    
    
    
the command to install those are :

        
    sudo add-apt-repository universe
    
    sudo apt update

    sudo apt install qemu-system-x86 qemu-utils
    
    sudo apt install qemu-kvm qemu-system qemu-utils virt-manager

    sudo apt install make nasm qemu-system-x86 qemu-utils


for verification :

    qemu-system-x86_64 --version





 


'''



import os



content = """
ASM = nasm

SRC_DIR = src
BUILD_DIR = build

$(BUILD_DIR)/main_floppy.img: $(BUILD_DIR)/main.bin
__t__cp $(BUILD_DIR)/main.bin $(BUILD_DIR)/main_floppy.img
__t__truncate -s 1440k $(BUILD_DIR)/main_floppy.img

$(BUILD_DIR)/main.bin: $(SRC_DIR)/main.asm
__t__$(ASM) $(SRC_DIR)/main.asm -f bin -o $(BUILD_DIR)/main.bin




"""


content = content.replace("__t__", "\t")


file_0 = os.path.join(os.getcwd(), "makefile")

with open(file_0, "w") as f_:

    f_.write(content)



os.system("make")


os.system("qemu-system-x86_64 -fda build/main_floppy.img")














