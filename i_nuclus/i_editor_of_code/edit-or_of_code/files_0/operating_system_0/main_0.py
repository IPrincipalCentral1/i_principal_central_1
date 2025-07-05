











import os


content = """


ASM = nasm

SRC_DIR = src
BUILD_DIR = build

$(BUILD_DIR)/main_floppy.img: $(BUILD_DIR)/main.bin
__t__cp $(BUILD_DIR)/main.bin $(BUILD_DIR)/main_floppy.img
    truncate -s 1440k $(BUILD_DIR)/main_floppy.img

$(BUILD_DIR)/main.bin: $(SRC_DIR)/main.asm
__t__$(ASM) $(SRC_DIR)/main.asm -f bin -o $(BUILD_DIR)/main.bin




"""


content = content.replace("__t__", "\t")



os.system("make")

















