











'''


# to import this file use :



import os



cwd = os.path.dirname(os.path.abspath(__file__))


i_path_0_i = cwd


i_palce_of_module_0_i = os.path.join(i_path_0_i, "i_main_0_i.py")


import importlib.util

from pathlib import Path

i_path_1_i = Path(i_palce_of_module_0_i).resolve()

if i_path_1_i.is_file():

    i_spec_0_i = importlib.util.spec_from_file_location(
        "i_main_0_i",
        i_path_1_i
    )

    if i_spec_0_i is None or i_spec_0_i.loader is None:
        raise ImportError("Cannot load module")

    i_main_0_i = importlib.util.module_from_spec(i_spec_0_i)

    i_spec_0_i.loader.exec_module(i_main_0_i)

else:
    raise FileNotFoundError(i_path_1_i)






'''






class i_class_of_i_0_i():
    
    def __init__(self, i_semaphore_of_pip_install_0_i, 
                        
                        i_maximum_length_of_number_0_i=10 ** 10, 
                        
                        i_maximum_length_of_mix_0_i= 10 ** 10
                        
                        ):
        
        
        
        
        
        
        list_of_liberary_to_install = [
                                    
                                    ["flask"],
                                    
                                    ["pillow"],
                                    
                                    ["arabic-reshaper"],
                                    
                                    ["python-bidi"], 
                                    
                                    ["pretty_midi"], 
                                    
                                    ["pyfluidsynth"], 
                                    
                                    ["numpy"], 
                                    
                                    ["scipy"], 
                                    
                                    ["imageio"], 
                                    
                                    ["imageio-ffmpeg"], 
                                    
                                    ["pillow"], 
                                    
                                    ["pydub"], 
                                    
                                    ["psutil"],
                                    
                                    ["cadquery"],
                                    
                                    ["mavsdk"],
                                    
                                    ["pybullet"],
                                    
                                    ["opencv-python"],
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
        
        
        
        ]
        
        
        
        
        
        
        import os
        
        self.os = os
        
        
        import traceback
        
        self.traceback = traceback
        
        
        import sys
        
        self.sys = sys
        
        
        import subprocess
        
        self.subprocess = subprocess
        
        
        from pathlib import Path
        
        self.Path = Path
        
        
        
        
        
        
        
        self.cwd = self.os.path.dirname(self.os.path.abspath(__file__))
        
        
        
        
        
        if (i_semaphore_of_pip_install_0_i == True):
            
            
            print(f"\n\n    pip install --upgrade pip setuptools wheel \n\n\n")
            
            
            self.subprocess.check_call([self.sys.executable, "-m", "pip", "install", "--upgrade", "pip", "setuptools", "wheel"])
            
            
            
            try:
                
                i_counter_0_i = 0
                
                
                while (i_counter_0_i < len(list_of_liberary_to_install)):
                
            
                            
                    try:
                    
                        
                        print(f"\n\n\npip install {list_of_liberary_to_install[i_counter_0_i][0]}\n\n\n")
                        
                        
                        self.subprocess.check_call([self.sys.executable, "-m", "pip", "install", "--upgrade", f"{list_of_liberary_to_install[i_counter_0_i][0]}"])
                        
                        
                        
                    
                            
                    except:
                    
                            
                                    
                        self.traceback.print_exc()
                        
                        error = self.traceback.format_exc()
                        
                        semaphore = True
                        
                        print(f"Erreur : {str(error)}")
                        
                    
                    
                    i_counter_0_i += 1
                    
                    
                
            except:
            
                    
                            
                self.traceback.print_exc()
                
                error = self.traceback.format_exc()
                
                semaphore = True
                
                print(f"Erreur : {str(error)}")
                
                
                
            
        
        print("\n" * 10)
        
        
        
        
        
    
        
        from PIL import Image, ImageDraw, ImageFont
        
        
        self.Image = Image
        
        self.ImageDraw = ImageDraw
        
        self.ImageFont = ImageFont
        
        
        
        import arabic_reshaper
        
        self.arabic_reshaper = arabic_reshaper
        
        
        from bidi.algorithm import get_display
        
        self.get_display = get_display
        
        
        
        import time
        
        self.time = time
        
        
        
        self.i_path_0_i = self.os.path.dirname(self.cwd)
        
        
        self.i_path_0_i = self.os.path.dirname(self.i_path_0_i)
        
        
        self.i_path_0_i = self.os.path.dirname(self.i_path_0_i)
        
        
        self.sys.path.append(self.i_path_0_i)
        
        
        import i_my_mixer_1_i
        
        self.i_my_mixer_1_i = i_my_mixer_1_i
        
        
        import i_reformater_1
        
        self.i_reformater_1 = i_reformater_1
        
        
        import importlib
        
        self.importlib = importlib
        
        
        import threading
        
        self.threading = threading
        
        
        import pretty_midi
        
        self.pretty_midi = pretty_midi
        
        
        try:
            
            i_path_0_i = r"C:\tools\fluidsynth\bin"
            
            self.os.add_dll_directory(i_path_0_i)
            
        except:
            
            i_semaphore_of_error_0_i = True
            
            
        
        
        
        
        
        import fluidsynth
        
        self.fluidsynth = fluidsynth
        
        
        import numpy
        
        self.numpy = numpy
        
        
        
        from scipy.io.wavfile import write
        
        self.write = write
        
        
        import imageio
        
        self.imageio = imageio
        
        
        import PIL
        
        self.PIL = PIL
        
        
        import pydub
        
        self.pydub = pydub
        
        
        from pydub import AudioSegment
        
        self.AudioSegment = AudioSegment
        
        
        import i_math_i_am_i_1_i
        
        self.i_math_i_am_i_1_i = i_math_i_am_i_1_i
        
        
        import psutil
        
        self.psutil = psutil
        
        
        import platform
        
        self.platform = platform
        
        
        
        import cv2
        
        self.cv2 = cv2
        
        
        
        
        
        
        
        
        self.i_number_of_move_0_i = 100
        
        
        self.i_maximum_length_of_number_0_i = i_maximum_length_of_number_0_i
        
        
        self.i_maximum_length_of_mix_0_i = i_maximum_length_of_mix_0_i
        
        
        self.i_file_semaphore_of_process_of_compute_0_i = self.os.path.join(self.cwd, "i_file_semaphore_of_process_of_compute_0_i.txt")
        
        i_d_0_i = self.Path(self.i_file_semaphore_of_process_of_compute_0_i)
        
        i_d_0_i.write_text("False")
        
        
        
        self.i_bank_move_9_i()
        
        
        
        
        
        
    
    def i_push_content_0_i(self, i_content_0_i):
        
        self.i_content_0_i = i_content_0_i
        
        
    
    
    def i_bank_move_0_i(self):
        
        
        self.i_account_of_bank_0_i = {
                        
                        "identificater": "0",
                        
                        "name": "Bilale",
                        
                        "pre_name": "Debouci",
                        
                        "pass_word": "i_principal_central_i",
                        
                        "content": [
                                    
                                    {"name_of_unity": "i", "amount": ""},
                                    
                                    {"name_of_unity": "the quality of i", "amount": ""},
                                    
                                    {"name_of_unity": "real", "amount": ""},
                                    
                                    {"name_of_unity": "the quality of real", "amount": ""},
                                    
                                    {"name_of_unity": "power", "amount": ""},
                                    
                                    {"name_of_unity": "the quality of power", "amount": ""},
                                    
                                    {"name_of_unity": "work", "amount": ""},
                                    
                                    {"name_of_unity": "the quality of work", "amount": ""},
                                    
                                    
                                    
                        ]
                        
                        
        }
        
        
    
    def i_bank_move_1_i(self):
        
        
        
        
        i_counter_0_i = 0
        
        while (i_counter_0_i < len(self.i_account_of_bank_0_i.get("content"))):
            
            
            self.i_account_of_bank_0_i.get("content")[i_counter_0_i]["amount"] = "0.00"
            
            
            i_counter_0_i += 1
            
            
        
    
    def i_bank_move_2_i(self):
            
            
            
            
            i_counter_0_i = 0
            
            while (i_counter_0_i < len(self.i_account_of_bank_0_i.get("content"))):
                
                
                self.i_account_of_bank_0_i.get("content")[i_counter_0_i]["amount"] = "0.01"
                
                
                i_counter_0_i += 1
                
                
            
        
    
    def i_bank_move_3_i(self):
            
            
            
            
            i_counter_0_i = 0
            
            while (i_counter_0_i < len(self.i_account_of_bank_0_i.get("content"))):
                
                
                self.i_account_of_bank_0_i.get("content")[i_counter_0_i]["amount"] = "1.00"
                
                
                i_counter_0_i += 1
                
                
            
        
    
    
    def i_bank_move_4_i(self):
            
            
            
            
            i_counter_0_i = 0
            
            while (i_counter_0_i < len(self.i_account_of_bank_0_i.get("content"))):
                
                
                if (self.i_account_of_bank_0_i.get("content")[i_counter_0_i]["name_of_unity"] in 
                
                ["i", "real"]
                
                ):
                
                    self.i_account_of_bank_0_i.get("content")[i_counter_0_i]["amount"] = "1.00"
                    
                    
                elif (self.i_account_of_bank_0_i.get("content")[i_counter_0_i]["name_of_unity"] in 
                                
                                ["power", "work"]
                    ):
                    
                    
                    self.i_account_of_bank_0_i.get("content")[i_counter_0_i]["amount"] = "10 ** 100_000"
                    
                    
                else:
                    
                    
                    self.i_account_of_bank_0_i.get("content")[i_counter_0_i]["amount"] = "10 ** 300_000"
                    
                    
                    
                
                
                
                i_counter_0_i += 1
                
                
            
        
    
    def i_bank_move_5_i(self):
        
        
        
        self.i_bank_move_0_i()
        
        
        self.i_bank_move_1_i()
        
        
        self.i_bank_move_2_i()
        
        
        self.i_bank_move_3_i()
        
        
        self.i_bank_move_4_i()
        
        
        
    
    def i_bank_move_6_i(self, i_number_of_move_0_i):
        
        
        i_counter_0_i = 0
        
        while (i_counter_0_i < i_number_of_move_0_i):
            
            self.i_bank_move_5_i()
            
            i_counter_0_i += 1
            
            
        
        
        
    
    
    def i_bank_move_7_i(self):
        
        
        '''
        
        . i want to print money .
        
        
        '''
        
        
        
        
        i_color_of_background_0_i = (255, 255, 255)
        
        
        i_color_of_writeing_0_i = (0, 0, 0)
        
        
        i_z_0_i = i_color_of_background_0_i
        
        i_color_of_background_0_i = i_color_of_writeing_0_i
        
        i_color_of_writeing_0_i = i_z_0_i
        
        
        
        i_image_0_i = self.Image.new("RGB", (1300, 1300), i_color_of_background_0_i)
        
        
        
        # إنشاء أداة الرسم
        
        i_draw_0_i = self.ImageDraw.Draw(i_image_0_i)
        
        
        
        i_text_0_i = "i_bank , DZD , دينار "
        
        
        i_text_0_i = self.arabic_reshaper.reshape(i_text_0_i)
        
        i_text_0_i = self.get_display(i_text_0_i)
        
        
        
        i_first_value_0_i = 0.01
        
        
        
        
        if self.platform.system() == "Windows":
        
            i_font_path_0_i = r"C:\Windows\Fonts\arial.ttf"
        
        else:
        
            i_font_path_0_i = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
        
        
        i_font_0_i = self.ImageFont.truetype(
            i_font_path_0_i,
            28
        )
        
        
        '''
        
        i_font_0_i = self.ImageFont.truetype(
            r"C:\Windows\Fonts\arial.ttf",
            28
        )
        
        '''
        
        
        # رسم مربع
        
        
        i_x_0_i = 0
        
        i_y_0_i = 100
        
        
        i_width_0_i = 300
        
        i_length_0_i = 100
        
        
        i_counter_2_i = 0
        
        
        
        
        i_counter_0_i = 0
        
        while (i_counter_0_i < 4):
            
            
            i_counter_1_i = 0
            
            
            while (i_counter_1_i < 4):
                
                
                i_v_0_i = (i_x_0_i + i_width_0_i * i_counter_1_i, i_y_0_i + i_length_0_i * i_counter_0_i, i_x_0_i + i_width_0_i * (i_counter_1_i + 1), i_y_0_i + i_length_0_i * (i_counter_0_i + 1))
                
                i_draw_0_i.rectangle(
                    i_v_0_i,
                    outline=i_color_of_writeing_0_i,
                    width=3
                )
                
                
                
                
                if (i_counter_2_i == 0):
                    
                    
                    i_text_1_i = i_text_0_i + "\n" + f"0.00"
                    
                    
                elif (i_counter_2_i == 15):
                    
                    
                    i_text_1_i = i_text_0_i + "\n" + f"10 ** 100_000"
                    
                    
                else:
                    
                    i_text_1_i = i_text_0_i + "\n" + f"{i_first_value_0_i:.2f}"
                    
                    
                    i_first_value_0_i *= 10
                    
                    
                
                
                # كتابة النص
                
                
                
                
                i_draw_0_i.text(
                    (i_v_0_i[0] + i_width_0_i // 1, i_v_0_i[1] + i_length_0_i // 30),
                    i_text_1_i,
                    fill=i_color_of_writeing_0_i,
                    font=i_font_0_i,
                    anchor="ra"
                    )
                
                
                
                i_counter_2_i += 1
                
                i_counter_1_i += 1
                
            
            
            i_counter_0_i += 1
            
        
        
        
        
        i_file_of_image_0_i = self.os.path.join(self.cwd, "i_image_0_i.png")
        
        i_image_0_i.save(i_file_of_image_0_i)
        
        
        
        i_file_of_image_1_i = self.os.path.join(self.cwd, "i_folder_of_resource_0_i", "static", "i_image_0_i.png")
        
        
        i_semaphore_of_exist_0_i = self.os.path.exists(self.os.path.dirname(i_file_of_image_1_i))
        
        
        try:
            
            i_image_0_i.save(i_file_of_image_1_i)
            
            
        except Exception as i_error_0_i:
            
            i_semaphore_of_error_0_i = True
            
            
            
        
    
    
    def i_bank_move_8_i(self, i_number_of_move_0_i):
        
        
        i_counter_0_i = 0
        
        
        while (i_counter_0_i < i_number_of_move_0_i):
            
            
            self.i_bank_move_7_i()
            
            
            i_counter_0_i += 1
            
            
        
        
        
        
    
    def i_bank_move_9_i(self):
        
        
        self.i_bank_move_6_i(i_number_of_move_0_i=self.i_number_of_move_0_i)
        
        self.i_bank_move_8_i(i_number_of_move_0_i=self.i_number_of_move_0_i)
        
        
        i_v_0_i = self.i_bank_move_10_i(i_number_0_i=10000.00)
        
        
        self.i_bank_move_12_i()
        
        
        
        
    
    
    def i_bank_move_10_i(self, i_number_0_i):
        
        
        i_number_1_i = 0.0
        
        i_list_of_numbers_0_i = []
        
        while (i_number_1_i < i_number_0_i):
            
            
            i_list_of_numbers_0_i.append(i_number_1_i)
            
            i_number_1_i += 0.01
            
        
        
        return i_list_of_numbers_0_i
        
        
        
        
        
    
    
    def i_bank_move_11_i(self):
        
        
        
        
        i_d_0_i = self.Path(self.i_file_semaphore_of_process_of_compute_0_i)
        
        i_d_0_i.write_text("True")
        
        
        
        i_number_of_things_to_do_0_i = 2
        
        
        
        i_number_max_0_i = self.i_mesure_power_of_compute_0_i(i_number_of_things_to_do_0_i=i_number_of_things_to_do_0_i, i_maximum_length_of_number_0_i=self.i_maximum_length_of_number_0_i)
        
        
        i_length_max_0_i = self.i_mesure_power_of_compute_1_i(i_number_of_things_to_do_0_i=i_number_of_things_to_do_0_i, i_maximum_length_of_mix_0_i=self.i_maximum_length_of_mix_0_i)
        
        
        
        while (True):    
            
            
            # thing 1 
            
            self.i_compute_from_0_to_number_0_i(i_number_0_i=i_number_max_0_i)
            
            
            # thing 2
            
            self.i_compute_from_0_to_length_0_i(i_length_0_i=i_length_max_0_i)
            
            
            
            
            i_d_0_i = self.Path(self.i_file_semaphore_of_process_of_compute_0_i)
            
            
            i_content_of_semaphore_of_process_of_compute_0_i = i_d_0_i.read_text()
            
            
            if (i_content_of_semaphore_of_process_of_compute_0_i == "False"):
                
                
                break
                
                
            
        
        
        
        
    
    
    
    
    def i_bank_move_12_i(self):
        
        
        i_d_0_i = self.Path(self.i_file_semaphore_of_process_of_compute_0_i)
        
        
        i_content_of_semaphore_of_process_of_compute_0_i = i_d_0_i.read_text()
        
        
        if (i_content_of_semaphore_of_process_of_compute_0_i == "False"):
            
            
            i_p_0_i = self.threading.Thread(target=self.i_bank_move_11_i)
            
            
            i_p_0_i.start()
            
        
        
    
    
    
    
    def i_bank_move_13_i(self, i_folder_of_source_of_numbers_0_i):
        
        
        
        
        i_number_of_file_of_suit_of_number_0_i = 1_800
        
        
        i_length_of_suit_of_number_0_i = 1_000_000
        
        
        i_length_of_suit_of_number_1_i = 1_000
        
        
        
        i_file_of_information_0_i = self.os.path.join(i_folder_of_source_of_numbers_0_i, "i_file_of_information_0_i.txt")
        
        
        i_content_of_file_of_information_0_i = r"""
        
        


in this folder . i will have the source of numbers .


it start with :
    
    
    "i_file_start_of_number_0_i.txt"
    
with the content 1 .

and after that :
    
    
    "i_file_suit_of_number_1_i.txt"
    
    
    "i_file_suit_of_number_2_i.txt"
    
    
    "i_file_suit_of_number_3_i.txt"
    
    ...
    
    and so on 


with the content of many 0 .



the name of the variable that hold the number is :
    
    "i"
    



        
        
        """
        
        
        i_d_0_i = self.Path(i_file_of_information_0_i)
        
        
        i_d_0_i.write_text(i_content_of_file_of_information_0_i)
        
        
        
        i_file_start_of_number_0_i = self.os.path.join(i_folder_of_source_of_numbers_0_i, "i_file_start_of_number_0_i.txt")
        
        
        i_content_of_file_of_information_0_i = "1"
        
        
        i_d_1_i = self.Path(i_file_start_of_number_0_i)
        
        
        i_d_1_i.write_text(i_content_of_file_of_information_0_i)
        
        
        
        i_content_of_suit_of_number_0_i = ""
        
        
        
        i_content_of_suit_of_number_1_i = "0" * 1000
        
        
        
        i_len_0_i = len(i_content_of_suit_of_number_1_i)
        
        i_counter_0_i = 0
        
        
        i_counter_1_i = 0
        
        
        while (i_counter_1_i < i_length_of_suit_of_number_0_i):
            
            
            i_content_of_suit_of_number_0_i += i_content_of_suit_of_number_1_i
            
            
            i_counter_1_i += i_len_0_i
            
            i_counter_0_i += 1
            
            
            
        
        
        
        i_counter_0_i = 0
        
        
        while (i_counter_0_i < i_number_of_file_of_suit_of_number_0_i):
            
            
            i_file_0_i = self.os.path.join(i_folder_of_source_of_numbers_0_i, f"i_file_suit_of_number_{i_counter_0_i + 1}_i.txt")
            
            
            
            self.i_bank_move_14_i(i_file_0_i=i_file_0_i, i_length_of_suit_of_number_1_i=i_length_of_suit_of_number_1_i, i_content_of_suit_of_number_0_i=i_content_of_suit_of_number_0_i)
            
            
            
            print(f"i_counter_0_i = {i_counter_0_i} . i_file_0_i = {i_file_0_i} .")
            
            
            i_counter_0_i += 1
            
            
        
        
        
        
        
        
    
    
    
    def i_bank_move_14_i(self, i_file_0_i, i_length_of_suit_of_number_1_i, i_content_of_suit_of_number_0_i):
        
        
        
        # writing into a file 
        
        
        with open(i_file_0_i, "w") as i_f_0_i:
            
            i_f_0_i.write("")
            
            
        
        
        i_d_0_i = self.Path(i_file_0_i).open("a")
        
        
        i_counter_0_i = 0
        
        while (i_counter_0_i < i_length_of_suit_of_number_1_i):
            
            
            i_d_0_i.write(i_content_of_suit_of_number_0_i)
            
            i_counter_0_i += 1
            
            
        
        
        
        
    
    
    
    def i_bank_move_15_i(self):
        
        
        
        i_place_of_number_0_i = ""
        
        
        i_list_0_i = self.psutil.disk_partitions(all=False)
        
        
        for i_disk_0_i in i_list_0_i:
            
            
            i_disk_1_i = i_disk_0_i.mountpoint
            
            
            #print(f"[i_disk_0_i.mountpoint] = {[i_disk_0_i.mountpoint]}")
            
            
            i_list_of_file_0_i = []
            
            
            for i_root_0_i, i_dir_0_i, i_list_of_file_0_i in self.os.walk(i_disk_1_i):
                
                break
                
            
            
            
            i_name_of_file_semaphore_of_number_0_i = "i_file_semaphore_of_number_0_i.txt"
            
            if ( i_name_of_file_semaphore_of_number_0_i in i_list_of_file_0_i ):
                
                
                i_file_semaphore_of_number_0_i = self.os.path.join(i_disk_1_i, i_name_of_file_semaphore_of_number_0_i)
                
                
                try:
                    
                    i_d_0_i = self.Path(i_file_semaphore_of_number_0_i)
                    
                    
                    i_content_0_i = i_d_0_i.read_text()
                    
                    
                    if (i_content_0_i == "True"):
                        
                        
                        
                        i_place_of_number_0_i = self.os.path.join(i_disk_1_i, "i_folder_0_i")
                        
                        
                        print(f"i_place_of_number_0_i = {i_place_of_number_0_i} .")
                        
                        break
                        
                    
                    
                except:
                    
                    
                    i_semaphore_of_error_0_i = True
                    
                    
                
                
                
            
            
            
        
        
        
        return i_place_of_number_0_i
        
    
    

    
    def i_bank_move_16_i(self):
        
        
        
        '''
        
        
        in the hard disk of number . this file should exists :
            
            
            "i_file_semaphore_of_number_0_i.txt"
            
            
        
        and it should have this content :
            
            
            "True"
            
            
        
        
        
        '''
        
        
        
        while (True):
            
            
            try:
                
                
                i_folder_of_source_of_numbers_0_i = self.i_bank_move_15_i()
                
                
                
                i_number_of_file_of_suit_of_number_0_i = 1_800
                
                
                i_length_of_suit_of_number_0_i = 1_000_000
                
                
                i_length_of_suit_of_number_1_i = 1_000
                
                
                
                i_file_of_information_0_i = self.os.path.join(i_folder_of_source_of_numbers_0_i, "i_file_of_information_0_i.txt")
                
                
                i_content_of_file_of_information_0_i = r"""
                
        


in this folder . i will have the source of numbers .


it start with :
    
    
    "i_file_start_of_number_0_i.txt"
    
with the content 1 .

and after that :
    
    
    "i_file_suit_of_number_1_i.txt"
    
    
    "i_file_suit_of_number_2_i.txt"
    
    
    "i_file_suit_of_number_3_i.txt"
    
    ...
    
    and so on 


with the content of many 0 .




the name of the variable that hold the number is :
    
    "i"
    


        
        
        """
            
                
                
                if (i_folder_of_source_of_numbers_0_i != ""):
                    
                    
                    
                    
                    i_d_0_i = self.Path(i_file_of_information_0_i)
                    
                    
                    i_d_0_i.write_text(i_content_of_file_of_information_0_i)
                    
                    
                    
                    i_file_start_of_number_0_i = self.os.path.join(i_folder_of_source_of_numbers_0_i, "i_file_start_of_number_0_i.txt")
                    
                    
                    i_content_of_file_of_information_0_i = "1"
                    
                    
                    i_d_1_i = self.Path(i_file_start_of_number_0_i)
                    
                    
                    i_d_1_i.write_text(i_content_of_file_of_information_0_i)
                    
                    
                    
                    i_content_of_suit_of_number_0_i = ""
                    
                    
                    
                    i_content_of_suit_of_number_1_i = "0" * 1000
                    
                    
                    
                    i_len_0_i = len(i_content_of_suit_of_number_1_i)
                    
                    i_counter_0_i = 0
                    
                    
                    i_counter_1_i = 0
                    
                    
                    while (i_counter_1_i < i_length_of_suit_of_number_0_i):
                        
                        
                        i_content_of_suit_of_number_0_i += i_content_of_suit_of_number_1_i
                        
                        
                        i_counter_1_i += i_len_0_i
                        
                        i_counter_0_i += 1
                        
                        
                        
                    
                    
                    
                    i_counter_0_i = 0
                    
                    
                    while (i_counter_0_i < i_number_of_file_of_suit_of_number_0_i):
                        
                        
                        i_file_0_i = self.os.path.join(i_folder_of_source_of_numbers_0_i, f"i_file_suit_of_number_{i_counter_0_i + 1}_i.txt")
                        
                        
                        
                        self.i_bank_move_14_i(i_file_0_i=i_file_0_i, i_length_of_suit_of_number_1_i=i_length_of_suit_of_number_1_i, i_content_of_suit_of_number_0_i=i_content_of_suit_of_number_0_i)
                        
                        
                        
                        #print(f"i_counter_0_i = {i_counter_0_i} . i_file_0_i = {i_file_0_i} .")
                        
                        
                        i_counter_0_i += 1
                        
                        
                    
                    
                    
                else:
                    
                    
                    print(f"\n\n\n    the disk of 'number' is not finded .\n\n\n")
                    
                    
            except:
                
                
                i_semaphore_of_error_0_i = True
                
                
                
                            
                self.traceback.print_exc()
                
                error = self.traceback.format_exc()
                
                print(f"Erreur : {str(error)}")
                
                
                
                
        
        
    
    
    
    
    def i_bank_move_17_i(self):
        
        
        i_p_0_i = self.threading.Thread(target=self.i_bank_move_16_i)
        
        
        i_p_0_i.start()
        
        
        
        
        
    
    
    
    def i_compute_0_i(self):
        
        
        i_p_0_i = self.threading.Thread(target=self.i_compute_1_i, daemon=False)
        
        
        i_p_0_i.start()
        
        
        
        
    
    
    
    
    
    
    
    def i_compute_1_i(self):
        
        
        i_number_of_element__minus_1__0_i = 10 ** 18
        
        
        i_list_0_i = []
        
        i_list_1_i = []
        
        i_list_2_i = []
        
        i_list_3_i = []
        
        
        
        
        while (True):
            
            
            i_list_0_i = self.i_my_mixer_1_i.i_next_step_0_i(i_list_0_i=i_list_0_i, i_number_of_element__minus_1__0_i=i_number_of_element__minus_1__0_i)
            
            
            i_list_1_i = self.i_my_mixer_1_i.i_next_step_1_i(i_list_0_i=i_list_1_i, i_number_of_element__minus_1__0_i=i_number_of_element__minus_1__0_i)
            
            
            i_list_2_i = self.i_my_mixer_1_i.i_next_step_2_i(i_list_0_i=i_list_2_i, i_number_of_element__minus_1__0_i=i_number_of_element__minus_1__0_i)
            
            
            i_list_3_i = self.i_my_mixer_1_i.i_next_step_3_i(i_list_0_i=i_list_3_i, i_number_of_element__minus_1__0_i=i_number_of_element__minus_1__0_i)
            
            
        
        
    
    
    
    
    
    def i_end_of_process_of_compute_0_i(self):
        
        
        
        
        i_d_0_i = self.Path(self.i_file_semaphore_of_process_of_compute_0_i)
        
        
        i_d_0_i.write_text("False")
        
        
        
    
    
    def i_compute_from_0_to_number_0_i(self, i_number_0_i):
        
        
        i_counter_0_i = 0
        
        while (i_counter_0_i < i_number_0_i):
            
            
            i_counter_0_i += 1
            
        
        
    
    
    def i_compute_from_0_to_length_0_i(self, i_length_0_i):
        
        
        
        
        i_number_of_element__minus_1__0_i = 1
        
        i_list_0_i = []
        
        
        while (len(i_list_0_i) < i_length_0_i):
            
            
            i_list_0_i = self.i_my_mixer_1_i.i_next_step_0_i(i_list_0_i=i_list_0_i, i_number_of_element__minus_1__0_i=i_number_of_element__minus_1__0_i)
            
            
            
        
    
    
    def i_mesure_power_of_compute_0_i(self, i_number_of_things_to_do_0_i, i_maximum_length_of_number_0_i):
        
        
        
        i_number_0_i = 1 / i_number_of_things_to_do_0_i
        
        i_counter_0_i = 0
        
        i_t_0_i = self.time.time()
        
        
        i_t_1_i = self.time.time()
        
        while (i_t_1_i - i_t_0_i < i_number_0_i):
            
            
            
            i_t_1_i = self.time.time()
            
            
            try:
                
                
                
                i_counter_0_i += 1
                
                
            except:
                
                
                i_semaphore_of_error_0_i = True
                
                break
                
                
            
            i_str_0_i = f"{i_counter_0_i}"
            
            
            if (len(i_str_0_i) > i_maximum_length_of_number_0_i):
                
                break
                
                
            
            
        
        
        return i_counter_0_i
        
        
        
    
    
    
    def i_mesure_power_of_compute_1_i(self, i_number_of_things_to_do_0_i, i_maximum_length_of_mix_0_i):
        
        
        
        i_number_0_i = 1 / i_number_of_things_to_do_0_i
        
        
        i_number_of_element__minus_1__0_i = 1
        
        i_list_0_i = []
        
        
        i_t_0_i = self.time.time()
        
        
        i_t_1_i = self.time.time()
        
        while (i_t_1_i - i_t_0_i < i_number_0_i):
            
            
            
            i_t_1_i = self.time.time()
            
            
            try:
                
                
                i_list_0_i = self.i_my_mixer_1_i.i_next_step_0_i(i_list_0_i=i_list_0_i, i_number_of_element__minus_1__0_i=i_number_of_element__minus_1__0_i)
                
                
            except:
                
                
                i_semaphore_of_error_0_i = True
                
                
                break
                
            
            
            if (len(i_list_0_i) > i_maximum_length_of_mix_0_i):
                
                break
                
                
            
            
        
        
        return len(i_list_0_i)
        
        
        
    
    
    
    
    def i_hello_0_i(self):
        
        
        print(f"i_hello_0_i .")
        
        
    
    
    def i_function_of_math_0_i(self, i_a_0_i, i_a_1_i, i_v_0_i, i_b_0_i, i_c_0_i):
        
        
        return i_a_0_i * i_v_0_i - i_a_1_i * i_v_0_i + i_b_0_i - i_c_0_i
        
        
    
    
    def i_mesure_distance_0_i(self, i_v_a_i, i_v_0_i, i_v_b_i):
        
        
        i_var_of_result_0_i = False
        
        
        i_var_of_result_of_arriving_1_i = False
        
        
        i_v_3_i = abs(i_v_a_i - i_v_b_i)
        
        
        i_v_4_i = abs(i_v_0_i - i_v_b_i)
        
        
        if ( i_v_3_i >= i_v_4_i ):
            
            
            i_var_of_result_0_i = True
            
            
        
        if ( i_v_0_i == i_v_b_i ):
            
            i_var_of_result_of_arriving_1_i = True
            
            
        
        
        
        return [i_var_of_result_0_i, i_var_of_result_of_arriving_1_i, i_v_4_i]
        
        
        
    
    
    def i_get_a_function_0_i(self, i_v_a_i, i_v_b_i):
        
        
        i_list_of_result_0_i = []
        
        
        
        i_v_0_i = i_v_a_i
        
        
        i_v_3_i = i_v_0_i
        
        
        i_v_2_i = [False, False]
        
        
        i_v_4_i = 0
        
        

        i_list_of_all_chose_one_0_i = []
        
        
        i_number_of_element__minus_1__0_i = 1
        
        
        
        while ( i_v_2_i[1] == False ):
            
            
            
            
            
            i_list_0_i = [0, 0, 0, 0]
            
            
            i_lenght_of_mix_0_i = len(i_list_0_i)
            
            
            i_list_of_chose_one_1_i = i_list_0_i.copy()
            
            
    
            i_v_min_0_i = abs(i_v_0_i - i_v_b_i)
            
            #if (i_v_min_0_i == 0):
                
                #i_v_min_0_i = 1
                
            
            
            while ( len(i_list_0_i) == i_lenght_of_mix_0_i ):
            
                
                
                
                i_v_1_i = i_v_0_i + self.i_function_of_math_0_i(i_a_0_i=i_list_0_i[0], 
                                            
                                            i_a_1_i=i_list_0_i[1],
                                            
                                            i_v_0_i=i_v_a_i, 
                                            
                                            i_b_0_i=i_list_0_i[2], 
                                            
                                            i_c_0_i=i_list_0_i[3]
                                            
                                            )
                
                
                
                i_v_2_i = self.i_mesure_distance_0_i(i_v_a_i=i_v_3_i, i_v_0_i=i_v_1_i, i_v_b_i=i_v_b_i)
                
                
                
                
                i_v_min_1_i = i_v_2_i[2]
                
                
                if (( i_v_min_1_i <= i_v_min_0_i ) and ( i_v_2_i[0] == True ) ):
                    
                    
                    
                    
                    i_v_min_0_i = i_v_min_1_i
                    
                    
                    i_list_of_chose_one_1_i = i_list_0_i.copy()
                    
                    
                    i_v_4_i = i_v_1_i
                    
                    #i_v_3_i = i_v_1_i
                    
                    
                    if (i_v_2_i[1] == True):
                        
                        
                        break
                        
                    
                    
                
                
                
                i_list_0_i = self.i_my_mixer_1_i.i_next_step_0_i(i_list_0_i=i_list_0_i, i_number_of_element__minus_1__0_i=i_number_of_element__minus_1__0_i)
                
                
            
            
            
            
            i_v_3_i = i_v_4_i
            
            
            if (( len(i_list_of_all_chose_one_0_i) > 0 ) and ( i_list_of_all_chose_one_0_i[-1][0] == i_list_of_chose_one_1_i )):
                
                
                i_list_of_all_chose_one_0_i[-1][1] += 1 
                
                
                
            else:
                
                i_list_of_all_chose_one_0_i.append([i_list_of_chose_one_1_i, 1, i_v_a_i])
                
            
            
            i_v_0_i = i_v_3_i
                        
                        
            
        
        
        return i_list_of_all_chose_one_0_i
        
        
        
    
    
    
    def i_check_and_get_list_of_all_chose_one_0_i(self, i_list_of_all_chose_one_0_i, i_first_number_0_i, i_last_number_0_i):
        
        
        
        i_var_of_result_0_i = False
        
        i_var_0_i = i_first_number_0_i
        
        i_counter_0_i = 0
        
        while (i_counter_0_i < len(i_list_of_all_chose_one_0_i)):
            
            
            
            
            i_list_0_i = i_list_of_all_chose_one_0_i[i_counter_0_i][0]
            
            
            i_number_0_i = i_list_of_all_chose_one_0_i[i_counter_0_i][1]
            
            
            i_axiom_0_i = i_list_of_all_chose_one_0_i[i_counter_0_i][2]
            
            
            i_counter_1_i = 0
            
            while (i_counter_1_i < i_number_0_i):
                
                
                i_var_0_i += self.i_function_of_math_0_i(i_a_0_i=i_list_0_i[0], 
                                            
                                            i_a_1_i=i_list_0_i[1],
                                            
                                            i_v_0_i=i_axiom_0_i, 
                                            
                                            i_b_0_i=i_list_0_i[2], 
                                            
                                            i_c_0_i=i_list_0_i[3]
                                            
                                            )
                
                
                
                
                i_counter_1_i += 1
                
                
            
            i_counter_0_i += 1
            
            
            
        
        
        if (i_var_0_i == i_last_number_0_i):
            
            
            i_var_of_result_0_i = True
            
            
            
        
        
        return [i_var_of_result_0_i, i_var_0_i]
        
        
    
    
    
    
    def i_check_and_get_list_of_all_chose_one_1_i(self, i_list_of_all_chose_one_0_i, i_list_of_word_0_i, i_list_of_organized_word_0_i, i_first_number_0_i, i_last_number_0_i):
        
        
        
        i_var_of_result_0_i = False
        
        i_var_0_i = i_first_number_0_i
        
        i_counter_0_i = 0
        
        while (i_counter_0_i < len(i_list_of_all_chose_one_0_i)):
            
            
            
            
            i_list_0_i = i_list_of_all_chose_one_0_i[i_counter_0_i][0]
            
            
            i_number_0_i = i_list_of_all_chose_one_0_i[i_counter_0_i][1]
            
            
            i_counter_2_i = i_counter_0_i % len(i_list_of_word_0_i)
            
            
            i_axiom_0_i = self.i_find_element_in_list_0_i(i_element_0_i=i_list_of_word_0_i[i_counter_2_i], i_list_0_i=i_list_of_organized_word_0_i)
            
            
            
            i_counter_1_i = 0
            
            while (i_counter_1_i < i_number_0_i):
                
                
                i_var_0_i += self.i_function_of_math_0_i(i_a_0_i=i_list_0_i[0], 
                                            
                                            i_a_1_i=i_list_0_i[1],
                                            
                                            i_v_0_i=i_axiom_0_i, 
                                            
                                            i_b_0_i=i_list_0_i[2], 
                                            
                                            i_c_0_i=i_list_0_i[3]
                                            
                                            )
                
                
                
                
                i_counter_1_i += 1
                
                
            
            i_counter_0_i += 1
            
            
            
        
        
        if (i_var_0_i == i_last_number_0_i):
            
            
            i_var_of_result_0_i = True
            
            
            
        
        
        return [i_var_of_result_0_i, i_var_0_i]
        
        
    
    
    
    def i_find_element_in_list_0_i(self, i_element_0_i, i_list_0_i):
        
        
        i_counter_0_i = 0
        
        while (( i_counter_0_i < len(i_list_0_i) ) and ( i_list_0_i[i_counter_0_i] != i_element_0_i )):
            
            
            i_counter_0_i += 1
            
            
        
        
        return i_counter_0_i
        
        
        
        
    
    
    
    def i_get_list_of_token_0_i(self, i_text_0_i):
        
        
        i_list_of_all_char_0_i = list(i_text_0_i)
        
        
        i_list_of_all_token_0_i = []
        
        i_counter_0_i = 0
        
        
        while (i_counter_0_i < len(i_list_of_all_char_0_i)):
            
            i_list_of_all_token_0_i.append(ord(i_list_of_all_char_0_i[i_counter_0_i]))
            
            
            i_counter_0_i += 1
            
            
        
        
        return i_list_of_all_token_0_i
        
    
    
    
    
    def i_get_list_of_token_1_i(self, i_list_of_word_0_i, i_list_of_organized_word_0_i):
        
        
        i_list_of_all_word_0_i = i_list_of_word_0_i
        
        
        i_list_of_all_token_0_i = []
        
        i_counter_0_i = 0
        
        
        while (i_counter_0_i < len(i_list_of_all_word_0_i)):
            
            
            i_index_token_0_i = self.i_find_element_in_list_0_i(i_element_0_i=i_list_of_all_word_0_i[i_counter_0_i], i_list_0_i=i_list_of_organized_word_0_i)
            
            
            i_list_of_all_token_0_i.append(i_index_token_0_i)
            
            
            i_counter_0_i += 1
            
            
        
        
        return i_list_of_all_token_0_i
        
    
    
    
    
    
    
    def i_get_list_of_char_from_list_of_token_0_i(self, i_list_of_all_token_0_i):
        
        
        i_list_of_all_char_0_i = []
        
        
        i_file_of_try_chr_0_i = self.os.path.join(self.cwd, "i_file_of_try_chr_0_i.txt")
        
        
        i_counter_0_i = 0
        
        
        while (i_counter_0_i < len(i_list_of_all_token_0_i)):
            
            try:
                
                
                i_str_0_i = chr(i_list_of_all_token_0_i[i_counter_0_i])
                
                
                i_d_0_i = self.Path(i_file_of_try_chr_0_i)
                
                i_d_0_i.write_text(i_str_0_i)
                
                
                
                i_list_of_all_char_0_i.append(i_str_0_i)
                
                
                
            except:
                
                i_semaphore_of_error_0_i = True
                
                
            i_counter_0_i += 1
            
            
        
        
        
        i_str_0_i = "".join(i_list_of_all_char_0_i)
        
        
        
        return [i_list_of_all_char_0_i, i_str_0_i]
        
    
    
    
    
    def i_get_list_of_char_from_list_of_token_1_i(self, i_list_of_all_token_0_i, i_list_of_organized_word_0_i):
        
        
        i_list_of_all_char_0_i = []
        
        
        i_counter_0_i = 0
        
        
        while (i_counter_0_i < len(i_list_of_all_token_0_i)):
            
            try:
                
                
                i_number_0_i = i_list_of_all_token_0_i[i_counter_0_i] % len(i_list_of_organized_word_0_i)
                
                i_str_0_i = i_list_of_organized_word_0_i[i_number_0_i]
                
                
                
                i_list_of_all_char_0_i.append(i_str_0_i)
                
                
                
            except:
                
                i_semaphore_of_error_0_i = True
                
                
            i_counter_0_i += 1
            
            
        
        
        
        i_str_0_i = " ".join(i_list_of_all_char_0_i)
        
        
        
        return [i_list_of_all_char_0_i, i_str_0_i]
        
    
    
    
    
    
    
    def i_get_list_of_recognition_0_i(self, i_text_0_i):
        
        
        i_semaphore_of_error_0_i = False
        
        
        i_list_of_recognition_0_i = [0, []]
        
        
        
        if (len(i_text_0_i) > 1):
            
            
            
            i_list_of_all_token_0_i = self.i_get_list_of_token_0_i(i_text_0_i=i_text_0_i)
            
            
            i_list_of_recognition_0_i[0] = i_list_of_all_token_0_i[0]
            
            
            i_counter_0_i = 0
            
            while (i_counter_0_i < len(i_list_of_all_token_0_i) - 1):
                
                
                i_v_0_i = self.i_get_a_function_0_i(i_v_a_i=i_list_of_all_token_0_i[i_counter_0_i], i_v_b_i=i_list_of_all_token_0_i[i_counter_0_i + 1])
                
                
                i_list_of_recognition_0_i[1].append(i_v_0_i)
                
                
                i_counter_0_i += 1
                
            
            
            
            
        else:
            
            
            
            i_semaphore_of_error_0_i = True
            
            
        
        
        
        return [i_list_of_recognition_0_i, i_list_of_all_token_0_i, i_semaphore_of_error_0_i]
        
        
    
    
    
    
    
    def i_get_list_of_recognition_1_i(self, i_list_of_word_0_i, i_list_of_organized_word_0_i):
        
        
        i_semaphore_of_error_0_i = False
        
        
        i_list_of_recognition_0_i = [0, []]
        
        
        
        if (len(i_list_of_word_0_i) > 1):
            
            
            
            i_list_of_all_token_0_i = self.i_get_list_of_token_1_i(i_list_of_word_0_i=i_list_of_word_0_i, i_list_of_organized_word_0_i=i_list_of_organized_word_0_i)
            
            
            
            i_list_of_recognition_0_i[0] = i_list_of_all_token_0_i[0]
            
            
            i_counter_0_i = 0
            
            while (i_counter_0_i < len(i_list_of_all_token_0_i) - 1):
                
                
                i_v_0_i = self.i_get_a_function_0_i(i_v_a_i=i_list_of_all_token_0_i[i_counter_0_i], i_v_b_i=i_list_of_all_token_0_i[i_counter_0_i + 1])
                
                
                i_list_of_recognition_0_i[1].append(i_v_0_i)
                
                
                i_counter_0_i += 1
                
            
            
            
            
        else:
            
            
            
            i_semaphore_of_error_0_i = True
            
            
        
        
        
        return [i_list_of_recognition_0_i, i_list_of_all_token_0_i, i_semaphore_of_error_0_i]
        
        
    
    
    
    
    
    def i_go_of_trying_0_i(self, i_list_of_recognition_0_i, i_first_token_0_i, i_number_of_maximum_try_0_i):
        
        
        
        
        i_list_of_generated_token_0_i = [i_first_token_0_i]
        
        i_counter_0_i = 0
        
        i_counter_1_i = 0
        
        
        while (i_counter_0_i < i_number_of_maximum_try_0_i):
            
            
            
            
            i_v_1_i = i_list_of_recognition_0_i[i_counter_1_i]
            
            i_v_0_i = self.i_check_and_get_list_of_all_chose_one_0_i(i_list_of_all_chose_one_0_i=i_v_1_i, i_first_number_0_i=i_list_of_generated_token_0_i[i_counter_0_i], i_last_number_0_i=i_list_of_generated_token_0_i[i_counter_0_i])
            
            
            i_list_of_generated_token_0_i.append(i_v_0_i[1])
            
            
            
            i_counter_1_i = ( i_counter_1_i + 1 ) % ( len(i_list_of_recognition_0_i) )
            
            i_counter_0_i += 1
            
            
        
        
        
        
        return i_list_of_generated_token_0_i
        
    
    
    
    
    def i_go_of_trying_1_i(self, i_list_of_recognition_0_i, i_list_of_word_0_i, i_list_of_organized_word_0_i, i_first_token_0_i, i_number_of_maximum_try_0_i):
        
        
        
        
        i_list_of_generated_token_0_i = [i_first_token_0_i]
        
        i_counter_0_i = 0
        
        i_counter_1_i = 0
        
        
        while (i_counter_0_i < i_number_of_maximum_try_0_i):
            
            
            
            
            i_v_1_i = i_list_of_recognition_0_i[i_counter_1_i]
            
            i_v_0_i = self.i_check_and_get_list_of_all_chose_one_1_i(i_list_of_all_chose_one_0_i=i_v_1_i, i_list_of_word_0_i=i_list_of_word_0_i, i_list_of_organized_word_0_i=i_list_of_organized_word_0_i, i_first_number_0_i=i_list_of_generated_token_0_i[i_counter_0_i], i_last_number_0_i=i_list_of_generated_token_0_i[i_counter_0_i])
            
            
            i_list_of_generated_token_0_i.append(i_v_0_i[1])
            
            
            
            i_counter_1_i = ( i_counter_1_i + 1 ) % ( len(i_list_of_recognition_0_i) )
            
            i_counter_0_i += 1
            
            
        
        
        
        
        return i_list_of_generated_token_0_i
        
    
    
    
    def i_get_strange_token_0_i(self, i_text_0_i, i_token_0_i):
        
        
        i_counter_0_i = len(i_text_0_i) - 1
        
        while (( i_counter_0_i > 0 ) and ( ord(i_text_0_i[i_counter_0_i]) == i_token_0_i)):
            
            
            i_counter_0_i -= 1
            
            
        
        
        return ord(i_text_0_i[i_counter_0_i])
        
        
    
    
    def i_min_0_i(self, i_a_0_i, i_b_0_i):
        
        
        if (i_a_0_i <= i_b_0_i):
            
            
            return i_a_0_i
            
            
        else:
            
            return i_b_0_i
            
            
        
    
    
    
    def i_extract_intelligance_from_file_0_i(self, i_file_of_dumping_intelligance_0_i):
        
        
        i_file_0_i = self.os.path.join(self.cwd, "i_file_lib_0_i.py")
        
        i_d_0_i = self.Path(i_file_of_dumping_intelligance_0_i)
        
        i_content_0_i = i_d_0_i.read_text()
        
            
        with open(i_file_0_i, "w") as f_:
            
            f_.write("def i_main_0_i():\n")
            
            
            
            f_.write(f"    i_v_0_i = {i_content_0_i}\n")
            
            
            
            f_.write(f"    return i_v_0_i\n")
        
        
        i_e_0_i = ""
        
        try:
            
            import i_file_lib_0_i
            
            self.importlib.reload(i_file_lib_0_i)
            
            return i_file_lib_0_i.i_main_0_i()
        
        except Exception as i_e_1_i:
            
                
            self.traceback.print_exc()
            
            i_error_1_i = self.traceback.format_exc()
            
            
            i_e_0_i = str(i_e_1_i)
            
            i_semaphore_of_error_0_i = True
            
            
            
        
        
        return []
        
    
    
    
    def i_my_artificial_intelligance_functional_0_i(self, i_v_bool_0_i, i_var_1_i):
        
        
        i_var_0_i = {
        
        
        "i_time_max_of_trys_0_i": 100.0,
        
        "i_max_char_of_input_0_i": 10_000,
        
        "i_max_token_of_input_0_i": 100,
        
        "i_max_token_of_output_0_i": 10000,
        
        "i_semaphore_of_char_xor_word_0_i": False,
        
        "i_semaphore_of_dump_intelligance_into_file_0_i": False,
        
        "i_semaphore_of_extract_intelligance_from_file_0_i": False
        
        
        
        
        
        }
        
        
        
        if (i_v_bool_0_i == True):
            
            
            i_var_0_i = i_var_1_i
            
            
        
        
        
        
        
        
        
        
        i_file_of_input_0_i = self.os.path.join(self.cwd, "i_file_of_input_0_i.txt")
        
        
        i_file_of_input_of_training_0_i = self.os.path.join(self.cwd, "i_file_of_input_of_training_0_i.txt")
        
        
        i_file_of_output_0_i = self.os.path.join(self.cwd, "i_file_of_output_0_i.txt")
        
        
        i_file_of_dumping_intelligance_0_i = self.os.path.join(self.cwd, "i_file_of_dumping_intelligance_0_i.txt")
        
        
        
        
        i_d_0_i = self.Path(i_file_of_input_of_training_0_i)
        
        
        i_text_of_input_of_training_0_i = i_d_0_i.read_text()
        
        
        i_d_0_i = self.Path(i_file_of_input_0_i)
        
        
        i_text_of_input_0_i = i_d_0_i.read_text()
        
        
        
        if (i_var_0_i["i_semaphore_of_extract_intelligance_from_file_0_i"] == True):
            
            
            i_list_of_recognition_1_i = self.i_extract_intelligance_from_file_0_i(i_file_of_dumping_intelligance_0_i=i_file_of_dumping_intelligance_0_i)
            
            
        
        
        
        if (i_var_0_i["i_max_char_of_input_0_i"] > 0):
            
            i_text_of_input_0_i = i_text_of_input_0_i[:self.i_min_0_i(len(i_text_of_input_0_i), i_var_0_i["i_max_char_of_input_0_i"])]
            
        
        
        
        #i_text_of_input_0_i = "hello . how are you doing . are you right ."
        
        
        i_content_of_output_0_i = ""
        
        
        
        if (i_var_0_i["i_semaphore_of_char_xor_word_0_i"] == True):
            
            
            
            
            
            
            
            # i_section_of_recognition_0_i 
            
            # ------------------------------------------------------------------------------------------
            
            # start of section of recognition 
            
            
            
            
            if (i_var_0_i["i_semaphore_of_extract_intelligance_from_file_0_i"] == False):
                
                i_list_of_recognition_0_i = self.i_get_list_of_recognition_0_i(i_text_0_i=i_text_of_input_0_i)
                
            else:
                
                i_list_of_recognition_0_i = i_list_of_recognition_1_i
                
            
            
            # end of section of recognition 
            
            # -------------------------------------------------------------------------------------------
            
            
            
            
            
            # i_section_of_trying_0_i 
            
            # ------------------------------------------------------------------------------------------
            
            # start of section of trying 
            
            
            #i_first_token_0_i = i_list_of_recognition_0_i[0][0]
            
            
            #i_first_token_0_i = ord(i_text_of_input_0_i[-1])
            
            
            
            i_first_token_0_i = self.i_get_strange_token_0_i(i_text_0_i=i_text_of_input_0_i, i_token_0_i=i_list_of_recognition_0_i[0][0])
            
            
            i_v_of_result_0_i = self.i_go_of_trying_0_i(i_list_of_recognition_0_i=i_list_of_recognition_0_i[0][1], i_first_token_0_i=i_first_token_0_i, i_number_of_maximum_try_0_i=i_var_0_i["i_max_token_of_output_0_i"])
            
            
            i_v_of_output_0_i = self.i_get_list_of_char_from_list_of_token_0_i(i_list_of_all_token_0_i=i_v_of_result_0_i)
            
            
            
            # end of section of trying 
            
            # -------------------------------------------------------------------------------------------
            
            
            i_content_of_output_0_i = i_v_of_output_0_i[1]
            
            
        else:
            
            
            
            
            i_text_0_i = i_text_of_input_0_i
            
            
            i_separater_of_words_0_i = [" ", "\n"]
            
            i_not_counted_words_0_i = [""]
            
            
            
            i_v_list_of_all_word_0_i = self.i_reformater_1.finder_and_spliter_1(element_0=i_separater_of_words_0_i, element_1=i_text_0_i, not_counted_words=i_not_counted_words_0_i)
            
            
            if (i_var_0_i["i_max_token_of_input_0_i"] > 0):
                
                i_v_list_of_all_word_1_i = i_v_list_of_all_word_0_i[1][:self.i_min_0_i(i_a_0_i=len(i_v_list_of_all_word_0_i[1]), i_b_0_i=i_var_0_i["i_max_token_of_input_0_i"])].copy()
                
            else:
                
                i_v_list_of_all_word_1_i = i_v_list_of_all_word_0_i[1].copy()
                
                
            
            
            
            #i_v_list_of_all_word_1_i.append("\n")
            
            
            
            i_v_0_i = [i_v_list_of_all_word_0_i[0], i_v_list_of_all_word_1_i]
            
            
            i_v_list_of_all_word_0_i[1].clear()
            
            
            #print(f"\n\n    i_v_0_i = {i_v_0_i} .\n\n")
            
            
            i_list_result_0_i = self.i_reformater_1.i_get_the_occerency_of_all_word_1(list_1=i_v_0_i[1])
            
            
            #print(f"\n\n    i_list_result_0_i = {i_list_result_0_i} .\n\n")
            
            
            
            i_v_result_0_i = self.i_reformater_1.i_get_list_of_individual_amount_0_i(i_list_result_1_i=i_list_result_0_i[0], i_list_result_2_i=i_v_0_i[1])
            
            
            #print(f"\n\n    i_v_result_0_i = {i_v_result_0_i} .\n\n")
            
            
            
            i_v_result_1_i = self.i_reformater_1.i_get_list_of_individual_amount_1_i(i_list_of_result_0_i=i_v_result_0_i)
            
            
            
            #print(f"\n\n    i_v_result_1_i = {i_v_result_1_i} .\n\n")
            
            
            
            i_list_of_organized_word_0_i = i_v_result_1_i
            
            
            #print(f"\n\n    i_v_list_of_all_word_1_i = {i_v_list_of_all_word_1_i} .\n\n")
            
            
            # i_section_of_recognition_0_i 
            
            # ------------------------------------------------------------------------------------------
            
            # start of section of recognition 
            
            
            
            
            
            if (i_var_0_i["i_semaphore_of_extract_intelligance_from_file_0_i"] == False):
                
                i_list_of_recognition_0_i = self.i_get_list_of_recognition_1_i(i_list_of_word_0_i=i_v_list_of_all_word_1_i, i_list_of_organized_word_0_i=i_list_of_organized_word_0_i)
                
            else:
                
                
                i_list_of_recognition_0_i = i_list_of_recognition_1_i
                
            
            # end of section of recognition 
            
            # -------------------------------------------------------------------------------------------
            
            
            
            
            
            # i_section_of_trying_0_i 
            
            # ------------------------------------------------------------------------------------------
            
            # start of section of trying 
            
            
            
            i_first_token_0_i = self.i_get_strange_token_0_i(i_text_0_i=i_text_of_input_0_i, i_token_0_i=i_list_of_recognition_0_i[0][0])
            
            
            #i_first_token_0_i = 0
            
            
            #i_v_of_result_0_i = self.i_go_of_trying_1_i(i_list_of_recognition_0_i=i_list_of_recognition_0_i[0][1], i_list_of_word_0_i=i_v_list_of_all_word_3_i, i_list_of_organized_word_0_i=i_list_of_organized_word_0_i, i_first_token_0_i=i_first_token_0_i, i_number_of_maximum_try_0_i=i_var_0_i["i_max_token_of_output_0_i"])
            
            
            i_v_of_result_0_i = self.i_go_of_trying_0_i(i_list_of_recognition_0_i=i_list_of_recognition_0_i[0][1], i_first_token_0_i=i_first_token_0_i, i_number_of_maximum_try_0_i=i_var_0_i["i_max_token_of_output_0_i"])
            
            
            i_v_of_output_0_i = self.i_get_list_of_char_from_list_of_token_1_i(i_list_of_all_token_0_i=i_v_of_result_0_i, i_list_of_organized_word_0_i=i_list_of_organized_word_0_i)
            
            
            
            # end of section of trying 
            
            # -------------------------------------------------------------------------------------------
            
            
            i_content_of_output_0_i = i_v_of_output_0_i[1]
            
            
            
            
            
        
        
        if (i_var_0_i["i_semaphore_of_dump_intelligance_into_file_0_i"] == True):
            
            
            
            i_d_2_i = self.Path(i_file_of_dumping_intelligance_0_i)
            
            
            i_d_2_i.write_text(str(i_list_of_recognition_0_i))
            
            
            
            
        
        
        
        i_d_1_i = self.Path(i_file_of_output_0_i)
        
        
        
        i_d_1_i.write_text(i_content_of_output_0_i)
        
        
        
        
        
    
    
    
    
    
    # start of section of music 
    
    # -------------------------------------------------------------------------------------
    
    
    
    def i_music_0_i(self):
        
        
        '''
        
        self.pretty_midi.Instrument(program=0)
        
        0    Acoustic Grand Piano
        
        4    Electric Piano
        
        24    Acoustic Guitar
        
        40    Violin
        
        42    Cello
        
        56    Trumpet
        
        73    Flute
        
        
        
        '''
        
        
        
        
        
        i_name_of_file_0_i = "i_file_of_music_0_i.wav"
        
        i_file_0_i = self.os.path.join(self.cwd, "i_folder_0_i", "i_folder_0_i", i_name_of_file_0_i)
        
        i_file_soundfont_0_i = self.os.path.join(self.cwd, "i_folder_0_i", "i_soundfont_0_i.sf2")
        
        
        
        
        # إنشاء ملف MIDI
        i_midi_0_i = self.pretty_midi.PrettyMIDI(
            initial_tempo=120
        )
        
        
        
        '''
        
        
        # إنشاء آلة البيانو
        i_piano_0_i = self.pretty_midi.Instrument(
            program=0
        )
        
        
        # إضافة النغمات
        
        i_notes_0_i = [
            (60, 0, 1),    # C4
            (64, 0, 1),    # E4
            (67, 3, 4),    # G4
            (72, 4, 6),    # C5
        ]
        
        for i_pitch_0_i, i_start_0_i, i_end_0_i in i_notes_0_i:
        
            i_note_0_i = self.pretty_midi.Note(
                velocity=100,
                pitch=i_pitch_0_i,
                start=i_start_0_i,
                end=i_end_0_i
            )
        
            i_piano_0_i.notes.append(i_note_0_i)
        
        
        '''
        
        
        i_list_of_sequance_of_music_0_i = self.i_produce_sequance_of_music_1_i()
        
        
        i_counter_0_i = 0
        
        while (i_counter_0_i < len(i_list_of_sequance_of_music_0_i)):
            
            i_midi_0_i.instruments.append(i_list_of_sequance_of_music_0_i[i_counter_0_i])
            
            i_counter_0_i += 1
            
            
        
        
        '''
        
        
        # إنشاء آلة Cello
        
        i_cello_0_i = self.pretty_midi.Instrument(
            program=42
        )
        
        
        i_notes_cello_0_i = [
        
            (48, 0, 3),    # C3
        
            (55, 3, 5),    # G3
        
            (53, 5, 7),    # F3
        
            (48, 7, 10),   # C3
        
        ]
        
        for i_pitch_0_i, i_start_0_i, i_end_0_i in i_notes_cello_0_i:
            
            i_note_0_i = self.pretty_midi.Note(
                
                velocity=85,
                
                pitch=i_pitch_0_i,
                
                start=i_start_0_i,
                
                end=i_end_0_i
                
            )
            
            
            i_cello_0_i.notes.append(i_note_0_i)
            
            
        
        
        i_midi_0_i.instruments.append(i_cello_0_i)
        
        '''
        
        
        # تحويل MIDI إلى صوت باستخدام SoundFont
        
        
        
        i_audio_0_i = i_midi_0_i.fluidsynth(
            fs=44100,
            sf2_path=i_file_soundfont_0_i
        )
        
        
        # ضبط مستوى الصوت
        
        '''
        
        i_audio_0_i /= max(abs(i_audio_0_i))
        
        '''
        
        i_max_0_i = max(abs(i_audio_0_i))
        
        if i_max_0_i > 0:
            i_audio_0_i /= i_max_0_i
        
        
        # حفظ WAV
        self.write(
            i_file_0_i,
            44100,
            self.numpy.int16(i_audio_0_i * 32767)
        )
        
        
        print(f"file : {i_file_0_i} . printed successfully .")
        
        
    
    
    def i_produce_sequance_of_music_0_i(self, i_pitches_0_i):
        
        
        
        '''
        
        i_silence_0_i :
            
            [-1, i_duration_of_silence_0_i]
            
        i_specification_0_i:
            
            [-2, "i_name_of_instrument_0_i", i_note_0_i]
            
            
        i_specification_1_i:
            
            [-3, "i_name_of_instrument_0_i", i_note_0_i, i_duration_of_note_0_i]
            
            
        i_specification_2_i:
            
            [-4, i_duration_of_the_clip_to_repeate_0_i, "i_name_of_instrument_0_i", i_list_of_note_to_repeate_0_i, i_padding_0_i]
            
            
        
        '''
        
        
        
        i_list_of_sequance_of_music_0_i = []
        
        
        i_piano_0_i = self.pretty_midi.Instrument(
            program=0
        )
        
        
        
        i_cello_0_i = self.pretty_midi.Instrument(
            program=42
        )
        
        
        
        i_Trumpet_0_i = self.pretty_midi.Instrument(
            program=56
        )
        
        
        i_daf_0_i = self.pretty_midi.Instrument(
            program=0,
            is_drum=True
        )
        
        
        i_dict_of_instrument_0_i = {
                                
                                "piano": i_piano_0_i,
                                
                                "cello": i_cello_0_i,
                                
                                "trumpet": i_Trumpet_0_i,
                                
                                "daf": i_daf_0_i,
                                
        }
        
        
        
        i_notes_0_i = []
        
        i_time_0_i = 0
        
        i_silence_0_i = 0.5
        
        i_duration_0_i = 1
        
        '''
        
        i_pitches_0_i = [60, [-1, 1], [-2, "cello", 64], [-2, "trumpet", 67], 
                        
                        [-2, "daf", 45], [-3, "piano", 72, 0.05], [-3, "piano", 72, 0.05], 
                        
                        [-3, "piano", 72, 0.05], [-3, "cello", 72, 5]]
        
        '''
        
        
        i_counter_0_i = 0
        
        while (i_counter_0_i < len(i_pitches_0_i)):
            
            
            i_start_0_i = i_time_0_i
            
            i_end_0_i = i_start_0_i + i_duration_0_i
            
            
            if (type(i_pitches_0_i[i_counter_0_i]) != list):
                
                
                i_pitche_0_i = i_pitches_0_i[i_counter_0_i]
                
                
                '''
                
                i_notes_0_i.append((
                    i_pitche_0_i,
                    i_start_0_i,
                    i_end_0_i
                ))
                
                '''
                
                
                i_note_0_i = self.pretty_midi.Note(
                                    velocity=100,
                                    pitch=i_pitche_0_i,
                                    start=i_start_0_i,
                                    end=i_end_0_i
                                )
                
                
                
                i_piano_0_i.notes.append(i_note_0_i)
                
                
            else:
                
                
                if (i_pitches_0_i[i_counter_0_i][0] == -1):
                    
                    
                    i_time_0_i += i_pitches_0_i[i_counter_0_i][1]
                    
                    
                    
                elif (i_pitches_0_i[i_counter_0_i][0] == -2):
                    
                    
                    if (i_pitches_0_i[i_counter_0_i][1] in i_dict_of_instrument_0_i):
                        
                        
                        i_pitche_0_i = i_pitches_0_i[i_counter_0_i][2]
                        
                        
                        i_note_0_i = self.pretty_midi.Note(
                                            velocity=100,
                                            pitch=i_pitche_0_i,
                                            start=i_start_0_i,
                                            end=i_end_0_i
                                        )
                        
                        
                        
                        
                        i_dict_of_instrument_0_i[i_pitches_0_i[i_counter_0_i][1]].notes.append(i_note_0_i)
                        
                    
                    
                    
                elif (i_pitches_0_i[i_counter_0_i][0] == -3):
                    
                    
                    if (i_pitches_0_i[i_counter_0_i][1] in i_dict_of_instrument_0_i):
                        
                        
                        i_pitche_0_i = i_pitches_0_i[i_counter_0_i][2]
                        
                        
                        
                        i_end_0_i = i_start_0_i + i_pitches_0_i[i_counter_0_i][3]
                        
                        
                        if (i_pitche_0_i > 0):
                            
                            i_note_0_i = self.pretty_midi.Note(
                                                velocity=100,
                                                pitch=i_pitche_0_i,
                                                start=i_start_0_i,
                                                end=i_end_0_i
                                            )
                            
                            
                            
                            
                            i_dict_of_instrument_0_i[i_pitches_0_i[i_counter_0_i][1]].notes.append(i_note_0_i)
                            
                        
                elif (i_pitches_0_i[i_counter_0_i][0] == -4):
                    
                    
                    if (i_pitches_0_i[i_counter_0_i][2] in i_dict_of_instrument_0_i):
                        
                        
                        #i_pitche_0_i = i_pitches_0_i[i_counter_0_i][3]
                        
                        
                        i_v_0_i = i_start_0_i
                        
                        
                        
                        i_counter_1_i = 0
                        
                        
                        i_end_0_i = i_start_0_i + i_pitches_0_i[i_counter_0_i][4]
                        
                        
                        i_time_0_i = i_end_0_i
                        
                        
                        
                        while (i_end_0_i - i_v_0_i < i_pitches_0_i[i_counter_0_i][1]):
                            
                            
                            i_start_0_i = i_time_0_i
                            
                            
                            #i_end_0_i = i_start_0_i + i_pitches_0_i[i_counter_0_i][4]
                            
                            
                            
                            i_counter_1_i = i_counter_1_i % len(i_pitches_0_i[i_counter_0_i][3])
                            
                            
                            i_end_0_i = i_start_0_i + i_pitches_0_i[i_counter_0_i][3][i_counter_1_i][1]
                            
                            
                            i_pitche_0_i = i_pitches_0_i[i_counter_0_i][3][i_counter_1_i][0]
                            
                            
                            
                            if (i_pitche_0_i > 0):
                                
                                
                                i_note_0_i = self.pretty_midi.Note(
                                                    velocity=100,
                                                    pitch=i_pitche_0_i,
                                                    start=i_start_0_i,
                                                    end=i_end_0_i
                                                )
                                
                                
                                
                                
                                i_dict_of_instrument_0_i[i_pitches_0_i[i_counter_0_i][2]].notes.append(i_note_0_i)
                                
                            
                            
                            #i_time_0_i = i_end_0_i + i_silence_0_i
                            
                            
                            i_time_0_i = i_end_0_i 
                            
                            
                            
                            i_counter_1_i += 1
                            
                            
                
                
                
            
            
            i_time_0_i = i_end_0_i
            
            
            #i_time_0_i = i_end_0_i + i_silence_0_i
            
            i_counter_0_i += 1
            
            
        
        
        
        
        #i_piano_0_i.notes.extend(i_notes_0_i)
        
        
        #i_list_of_sequance_of_music_0_i.append(i_piano_0_i)
        
        
        
        i_list_0_i = list(i_dict_of_instrument_0_i.values())
        
        
        
         
        return i_list_0_i
        
    
    
    
    def i_produce_sequance_of_music_1_i(self):
        
        
        i_list_of_sequance_of_music_0_i = []
        
        
        
        i_duration_of_music_0_i = 26
        
        
        
        
        i_list_of_pichtes_0_i = [
                            
                            [
                                
                                [-4, i_duration_of_music_0_i, "daf", [[45, 0.5], [45, 0.5], [55, 0.5], [0, 0.5]], 0.0],
                                
                            ],
                            
                            [
                                
                                
                                [-4, i_duration_of_music_0_i, "piano", [
                                                                            
                                                                            [75, 0.4], [75, 0.4], [65, 0.2], [75, 0.4], [75, 0.4], [65, 0.2], 
                                                                            
                                                                            [75, 0.4], [75, 0.4], [65, 0.2], [0, 0.4], [0, 0.6], [80, 1], [0, 2.0]
                                                                            
                                                                        ], 4.0
                                                                        
                                ],
                                
                                
                                
                            ],
                            
                        ]
        
        
        
        i_list_0_i = []
        
        i_counter_0_i = 0
        
        
        while (i_counter_0_i < len(i_list_of_pichtes_0_i)):
            
            
            
            i_list_0_i.extend(self.i_produce_sequance_of_music_0_i(i_pitches_0_i=i_list_of_pichtes_0_i[i_counter_0_i]))
            
            
            i_counter_0_i += 1
            
            
        
        
        i_counter_0_i = 0
        
        while (i_counter_0_i < len(i_list_0_i)):
            
            if (len(i_list_0_i[i_counter_0_i].notes) > 0):
                
                i_list_of_sequance_of_music_0_i.append(i_list_0_i[i_counter_0_i])
                
                
            
            i_counter_0_i += 1
            
            
        
        
        return i_list_of_sequance_of_music_0_i
        
        
        
        
    
    
    
    
    
    
    # end of section of music 
    
    # -------------------------------------------------------------------------------------
    
    
    
    
    # start of section of video 
    
    # -------------------------------------------------------------------------------------
    
    
    
    def i_video_0_i(self):
        
        
        self.i_video_2_i()
        
        
        
    
    
    
    def i_video_1_i(self):
        
        
        
        '''
        
        i_type_of_text_0_i :
            
            
            0 : DZD دينار  .
            
            1 : EUR euro .
            
            2 : USD Dollar .
            
            
            
        
        
        '''
        
        
        i_type_of_text_0_i = 2
        
        
        # 300_000_000.00
        
        i_incrimenter_0_i = 34567.81
        
        
        # more 
        
        i_incrimenter_0_i = 345678.91
        
        
        #i_str_0_i = f"{i_incrimenter_0_i:.2f}"
        
        
        '''
        
        i_incrimenter_0_i = 3456789101112131415161718.21 . i_n_1_i = 34000000000000000000 . i_v_0_i = 34000000000000000000.00 . i_str_1_i = 34000000000000000000 .
        
        '''
        
        
        i_incrimenter_0_i = "345678.91"
        
        
        i_length_max_of_number_0_i = 60
        
        i_number_of_shift_0_i = 2
        
        
        i_incrimenter_0_i = self.i_get_number_0_i(i_length_max_of_number_0_i=i_length_max_of_number_0_i, i_number_of_shift_0_i=i_number_of_shift_0_i)
        
        
        #i_n_1_i = i_incrimenter_0_i * ( 10 ** ( 4 ) )
        
        
        i_n_1_i = 34 * ( 10 ** ( i_length_max_of_number_0_i - 1 ) )
        
        
        #i_str_1_i = f"{i_n_1_i:.2f}"
        
        i_str_1_i = f"{i_n_1_i}"
        
        i_v_0_i = self.i_give_a_format_to_number_0_i(i_number_str_0_i=i_str_1_i)
        
        print(f"i_incrimenter_0_i = {i_incrimenter_0_i} . i_n_1_i = {i_n_1_i} . i_v_0_i = {i_v_0_i} . i_str_1_i = {i_str_1_i} .")
        
        
        self.i_create_video_0_i(i_n_0_i="0", i_n_1_i=i_str_1_i, i_incrimenter_0_i=i_incrimenter_0_i, i_type_of_text_0_i=i_type_of_text_0_i)
        
        
        
        
    
    
    
    def i_video_2_i(self):
        
        
        
        self.i_video_1_i()
        
        
        
        #self.i_create_video_1_i(i_color_of_frame_0_i=(255, 255, 255), i_time_of_video_0_i=240)
        
        
        
        
        i_name_of_file_0_i = "i_counter_of_numbers_max_small_0_i.mp4"
        
        i_path_of_video_0_i = self.os.path.join(self.cwd, "i_folder_0_i", "i_folder_1_i", i_name_of_file_0_i)
        
        
        
        i_name_of_file_0_i = "i_blank_video_0_i.mp4"
        
        i_path_of_video_1_i = self.os.path.join(self.cwd, "i_folder_0_i", "i_folder_1_i", i_name_of_file_0_i)
        
        
        
        i_name_of_file_0_i = "i_counter_of_numbers_0_i.mp4"
        
        i_path_of_video_result_0_i = self.os.path.join(self.cwd, "i_folder_0_i", "i_folder_1_i", i_name_of_file_0_i)
        
        
        
        
        '''
        
        
        self.i_concatenate_video_0_i(
                                    
                                    
                                    i_path_of_video_0_i=i_path_of_video_0_i, 
                                    
                                    
                                    i_path_of_video_1_i=i_path_of_video_1_i, 
                                    
                                    
                                    i_path_of_video_result_0_i=i_path_of_video_result_0_i
                                    
                                    )
        
        
        
        '''
    
    
    
    
    
    
    
    
    def i_get_number_0_i(self, i_length_max_of_number_0_i, i_number_of_shift_0_i):
        
        
        

        i_digit_of_start_0_i = 3
        
        
        i_incrimenter_0_i = ""
        
        i_counter_0_i = 0
        
        i_counter_1_i = i_digit_of_start_0_i
        
        while (i_counter_0_i < i_length_max_of_number_0_i - i_number_of_shift_0_i):
            
            
            i_incrimenter_0_i = i_incrimenter_0_i + str(i_counter_1_i)
            
            
            i_counter_0_i += 1
            
            
            i_counter_1_i = ( i_counter_1_i + 1 ) % 10
            
        
        
        i_incrimenter_0_i = i_incrimenter_0_i + ".21"
        
        
        
        
        return i_incrimenter_0_i
        
        
        
    
    def i_give_a_format_to_number_0_i(self, i_number_str_0_i):
        
        
        i_number_str_of_result_1_i = ""
        
        
        i_v_0_i = i_number_str_0_i.split(".")
        
        
        
        
        i_v_2_i = i_v_0_i
        
        
        if (len(i_v_0_i) == 2):
            
            
            i_v_2_i = i_v_0_i[0]
            
        
        
        i_counter_0_i = len(i_v_2_i) - 1
        
        i_counter_1_i = 0
        
        while (i_counter_0_i >= 0):
            
            
            if (i_counter_1_i == 3):
                
                i_counter_1_i = 0
                
                i_number_str_of_result_1_i = "_" + i_number_str_of_result_1_i
                
            
            
            i_number_str_of_result_1_i = i_v_2_i[i_counter_0_i] + i_number_str_of_result_1_i
            
                
            
            i_counter_1_i += 1
            
            i_counter_0_i -= 1
            
            
        
        
        if (len(i_v_0_i) == 2):
            
            
            i_v_1_i = i_v_0_i[1][:]
            
            if (len(i_v_0_i[1]) > 2):
                
                i_v_1_i = i_v_0_i[1][:2]
                
            
            
            
            i_number_str_of_result_1_i = i_number_str_of_result_1_i + "." + i_v_1_i
            
            
        else:
            
        
            i_number_str_of_result_1_i = i_number_str_of_result_1_i + ".00"    
            
        
        
        
        return i_number_str_of_result_1_i
        
        
    
    
    
    def i_create_video_0_i(self, i_n_0_i, i_n_1_i, i_incrimenter_0_i, i_type_of_text_0_i):
        
        
        
        
        
        i_width_max_0_i = 1920
        
        i_height_max_0_i = 1080
        
        
        
        i_width_1_i = 5200
        
        i_height_1_i = 1200
        
        
        
        
        
        i_width_0_i = 5000
        
        i_height_0_i = 450
        
        i_fps_0_i = 30
        
        
        
        
        i_name_of_file_0_i = "i_counter_of_numbers_0_i.mp4"
        
        i_file_0_i = self.os.path.join(self.cwd, "i_folder_0_i", "i_folder_1_i", i_name_of_file_0_i)
        
        
        
        
        i_name_of_file_1_i = "i_counter_of_numbers_1_i.mp4"
        
        i_file_1_i = self.os.path.join(self.cwd, "i_folder_0_i", "i_folder_1_i", i_name_of_file_1_i)
        
        
        
        
        i_list_of_image_0_i = []
        
        
        try:
            
            
            i_path_1_i = self.os.path.dirname(self.i_path_0_i)
            
            i_path_1_i = self.os.path.dirname(i_path_1_i)
            
            i_path_1_i = self.os.path.dirname(i_path_1_i)
            
            
            print(f"i_path_1_i = {i_path_1_i} .")
            
            
            
            i_folder_0_i = self.os.path.join(i_path_1_i, "i_space_of_work_1_i", "i_folder_0_i", "i_folder_0_i")
            
            
            i_folder_1_i = self.os.path.join(i_path_1_i, "i_space_of_work_1_i", "i_folder_0_i", "i_folder_1_i")
            
            
            i_folder_2_i = self.os.path.join(i_path_1_i, "i_space_of_work_1_i", "i_folder_0_i", "i_folder_2_i")
            
            
            print(f"i_folder_0_i = {i_folder_0_i} .")
            
            
            i_list_files_0_i = []
            
            
            for i_root_0_i, i_dir_0_i, i_list_files_0_i in self.os.walk(i_folder_0_i):
                
                break
                
            
            
            
            print(f"i_list_files_0_i = {i_list_files_0_i} .")
            
            
            i_counter_0_i = 0
            
            while (i_counter_0_i < len(i_list_files_0_i)):
                
                
                i_f_0_i = self.os.path.join(i_folder_0_i, i_list_files_0_i[i_counter_0_i])
                
                
                i_image_0_i = self.Image.open(i_f_0_i)
                
                i_image_0_i = i_image_0_i.resize((min(2000, i_width_0_i), i_height_0_i))
                
                
                i_list_of_image_0_i.append(i_image_0_i)
                
                    
                
                i_counter_0_i += 1
                
                
            
            
            
            
            
            
        except:
            
            
            i_semaphore_of_error_0_i = True
            
            
            
            self.traceback.print_exc()
            
            i_error_0_i = self.traceback.format_exc()
            
            print(f"Erreur : {str(i_error_0_i)}")
            
            
            
            
        
        
        
        print(f"len(i_list_of_image_0_i) = {len(i_list_of_image_0_i)} .")
        
        
        
        i_writer_0_i = self.imageio.v2.get_writer(
            i_file_0_i,
            fps=i_fps_0_i
        )
        
        
        
        
        if self.platform.system() == "Windows":
        
            i_font_path_0_i = r"C:\Windows\Fonts\arial.ttf"
        
        else:
        
            i_font_path_0_i = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
        
        
        i_font_0_i = self.ImageFont.truetype(
            i_font_path_0_i,
            60
        )
        
        
        '''
        
        i_font_0_i = self.ImageFont.truetype(
            "arial.ttf",
            100
        )
        
        '''
        
        
        
        i_number_of_image_0_i = 0
        
        
        i_semaphore_0_i = True
        
        i_list_of_step_0_i = []
        
        i_time_of_move_0_i = 10
        
        i_time_of_move_1_i = 7
        
        
        i_t_0_i = self.time.time()
        
        

        i_t_2_i = self.time.time()
        
        
        #i_incrimenter_0_i = 1.23
        
        i_counter_0_i = 0
        
        i_counter_str_0_i = i_n_0_i
        
        
        i_countre_of_frame_0_i = 0
        
        i_countre_of_frame_1_i = 0
        
        
        
        i_list_of_step_0_i.append(i_counter_0_i)
        
        
        
        
        
        i_s_2_i = f"{i_n_1_i} + {i_incrimenter_0_i}"
        
        
        i_operation_0_i = i_s_2_i
        
        
        i_m_0_i = self.i_math_i_am_i_1_i.calculatrice_2(s=i_operation_0_i, l_=[], n=0, number_of_digit_after_the_floating_point_=2, e=False)
        
        
        
        i_s_1_i = f"{i_counter_str_0_i}"
        
        i_s_2_i = i_m_0_i[1][0]
        
        
        
        i_bool_0_i = self.i_math_i_am_i_1_i.my_egale_s_n_1(s1=i_s_1_i, s2=i_s_2_i, number_of_digit_after_the_floating_point_=2)
        
        
        i_bool_1_i = self.i_math_i_am_i_1_i.my_inferieur_s_n_1(s1=i_s_1_i, s2=i_s_2_i, number_of_digit_after_the_floating_point_=2)
        
        
        
        while (( i_bool_0_i == True ) or ( i_bool_1_i == True )):
            
            
            
            i_t_1_i = self.time.time()
            
            
            
            
            i_image_0_i = self.Image.new(
                "RGB",
                (i_width_0_i, i_height_0_i),
                (64, 64, 128)
            )
            
            
            
            
            i_image_1_i = self.Image.new(
                "RGB",
                (i_width_1_i, i_height_1_i),
                (0, 0, 0)
            )
            
            
            
            i_draw_0_i = self.ImageDraw.Draw(i_image_0_i)
            
            
            
            #i_text_0_i = f"{i_counter_0_i:.2f}"
            
            
            i_text_0_i = i_counter_str_0_i
            
            
            
            i_text_0_i = self.i_give_a_format_to_number_0_i(i_number_str_0_i=i_text_0_i)
            
            
            if (i_type_of_text_0_i == 0):
                
                i_text_0_i += "\n     دينار "
                
                
                
            elif (i_type_of_text_0_i == 1):
                
                
                i_text_0_i += "\n    euro"
                
                
                
            elif (i_type_of_text_0_i == 2):
                
                
                i_text_0_i += "\n    dollar"
                
                
                
            
            
            
            
            
            
            
            
            
            
            i_text_0_i = self.arabic_reshaper.reshape(i_text_0_i)
            
            i_text_0_i = self.get_display(i_text_0_i)
            
            
            
            i_box_0_i = i_draw_0_i.textbbox(
                (0, 0),
                i_text_0_i,
                font=i_font_0_i,
                
            )
            
            i_text_width_0_i = i_box_0_i[2] - i_box_0_i[0]
            i_text_height_0_i = i_box_0_i[3] - i_box_0_i[1]
            
            i_x_0_i = (i_width_0_i - i_text_width_0_i) // 2
            i_y_0_i = (i_height_0_i - i_text_height_0_i) // 2
            
            i_draw_0_i.text(
                (i_x_0_i, i_y_0_i),
                i_text_0_i,
                fill=(0, 255, 0),
                font=i_font_0_i
                
            )
            
            
            
            
            #i_image_1_i.paste(i_image_0_i, (100, 100))
            
            
            i_image_1_i = i_image_0_i.copy()
            
            
            
            
            '''
            
            
            
            if (i_number_of_image_0_i < len(i_list_of_image_0_i)):
                
                
                i_image_1_i.paste(i_list_of_image_0_i[i_number_of_image_0_i], (100, 700))
                
                
                
                i_number_of_image_1_i = ( i_number_of_image_0_i + 1 ) % len(i_list_of_image_0_i)
                
                i_image_1_i.paste(i_list_of_image_0_i[i_number_of_image_1_i], (3100, 700))
                
                
            
            '''
            
            
            if (i_countre_of_frame_1_i > i_time_of_move_1_i * i_fps_0_i):
                
                
                i_countre_of_frame_1_i = 0
                
                i_number_of_image_0_i = ( i_number_of_image_0_i + 1 ) % len(i_list_of_image_0_i)
                
                
            
            
            
            
            
            
            i_image_1_i = i_image_1_i.resize((i_width_max_0_i, i_height_max_0_i))
            
            
            
            
            
            if (i_semaphore_0_i == True):
                
                
                i_semaphore_0_i = False
                
                try:
                    
                    i_file_1_i = self.os.path.join(self.cwd, "i_folder_0_i", "i_folder_1_i", "i_image_0_i.png")
                    
                    
                    i_image_1_i.save(i_file_1_i)
                    
                    
                except:
                    
                    
                    i_semaphore_of_error_0_i = True
                    
                    
            
            
            
            
            i_array_0_i = self.numpy.array(i_image_1_i)
            
            # إضافة الصورة إلى الفيديو
            
            i_writer_0_i.append_data(i_array_0_i)
            
            
            if (i_t_1_i - i_t_0_i > i_time_of_move_0_i):
                
                
                i_t_0_i = self.time.time()
                
                i_persentage_0_i = i_counter_0_i / ( int(i_n_1_i) )
                
                print(f"i_counter_0_i = {i_counter_0_i} . i_persentage_0_i = {i_persentage_0_i} % at 1.0")
                
                
                i_list_of_step_0_i.append(i_counter_0_i)
                
                
                if (len(i_list_of_step_0_i) >= 2):
                    
                    try:
                        
                        i_v_0_i = i_time_of_move_0_i * ( int(i_n_1_i) ) / abs(i_list_of_step_0_i[-1] - i_list_of_step_0_i[-2])
                        
                        
                        i_time_left_estimated_0_i = i_v_0_i - (len(i_list_of_step_0_i) * i_time_of_move_0_i)
                        
                        
                        print(f"i_time_left_estimated_0_i = {i_time_left_estimated_0_i} second .")
                        
                        
                    except:
                        
                        i_semaphore_of_error_0_i = True
                        
                        
                
            
            
            i_countre_of_frame_0_i += 1
            
            i_countre_of_frame_1_i += 1
            
            
            i_v_0_i = i_incrimenter_0_i.split(".")
            
            
            i_counter_0_i += int(i_v_0_i[0])
            
            
            
            i_operation_0_i = f"{i_counter_str_0_i} + {i_incrimenter_0_i}"
            
            
            i_m_0_i = self.i_math_i_am_i_1_i.calculatrice_2(s=i_operation_0_i, l_=[], n=0, number_of_digit_after_the_floating_point_=2, e=False)
            
            
            i_counter_str_0_i = i_m_0_i[1][0]
            
            
            
            i_s_2_i = f"{i_n_1_i} + {i_incrimenter_0_i}"
            
            
            i_operation_0_i = i_s_2_i
            
            
            i_m_0_i = self.i_math_i_am_i_1_i.calculatrice_2(s=i_operation_0_i, l_=[], n=0, number_of_digit_after_the_floating_point_=2, e=False)
            
            
            
            i_s_1_i = f"{i_counter_str_0_i}"
            
            i_s_2_i = i_m_0_i[1][0]
            
            
            i_bool_0_i = self.i_math_i_am_i_1_i.my_egale_s_n_1(s1=i_s_1_i, s2=i_s_2_i, number_of_digit_after_the_floating_point_=2)
            
            
            i_bool_1_i = self.i_math_i_am_i_1_i.my_inferieur_s_n_1(s1=i_s_1_i, s2=i_s_2_i, number_of_digit_after_the_floating_point_=2)
            
            
            
            
            
        
        i_writer_0_i.close()
        
        
        
        
        '''
        
        i_list_files_1_i = []
        
        for i_root_0_i, i_dir_0_i, i_list_files_1_i in self.os.walk(i_folder_2_i):
            
            break
            
            
        
        
        i_file_of_sound_0_i = self.os.path.join(i_folder_2_i, i_list_files_1_i[0])
        
        i_file_of_audio_loop_0_i = self.os.path.join(self.cwd, "i_folder_0_i", "i_folder_1_i", "i_audio_loop_0_i.wav")
        
        
        i_audio_0_i = self.AudioSegment.from_file(i_file_of_sound_0_i)
                
        i_duration_0_i = ( i_countre_of_frame_0_i // i_fps_0_i ) * 1000
        
        i_audio_1_i = (
            i_audio_0_i * (
                i_duration_0_i // len(i_audio_0_i) + 1
            )
        )[:i_duration_0_i]
        
        i_audio_1_i.export(
            i_file_of_audio_loop_0_i,
            format="wav"
        )
        
        
        
        self.subprocess.run([
            "ffmpeg",
            "-i", i_file_1_i,
            "-i", i_file_of_audio_loop_0_i,
            "-map", "0:v:0",
            "-map", "1:a:0",
            "-c:v", "copy",
            "-c:a", "aac",
            "-shortest",
            i_file_0_i
        ], check=True)
        
        
        
        '''
        
        
        print("Video created successfully:", i_file_0_i)
    
    
    
    
    
    
    
    def i_create_video_1_i(self, i_color_of_frame_0_i, i_time_of_video_0_i):
        
        
        
        
        
        i_width_max_0_i = 1920
        
        i_height_max_0_i = 1080
        
        
        i_fps_0_i = 30
        
        
        
        
        i_name_of_file_0_i = "i_blank_video_0_i.mp4"
        
        i_file_0_i = self.os.path.join(self.cwd, "i_folder_0_i", "i_folder_1_i", i_name_of_file_0_i)
        
        
        
        
        i_name_of_file_1_i = "i_counter_of_numbers_1_i.mp4"
        
        i_file_1_i = self.os.path.join(self.cwd, "i_folder_0_i", "i_folder_1_i", i_name_of_file_1_i)
        
        
        
        
        
        
        i_writer_0_i = self.imageio.v2.get_writer(
            i_file_0_i,
            fps=i_fps_0_i
        )
        
        
        
        
        
        i_number_of_image_0_i = 0
        
        
        i_semaphore_0_i = True
        
        i_list_of_step_0_i = []
        
        i_time_of_move_0_i = 10
        
        i_time_of_move_1_i = 7
        
        
        i_t_0_i = self.time.time()
        
        
    
        i_t_2_i = self.time.time()
        
        
        #i_incrimenter_0_i = 1.23
        
        i_counter_0_i = 0
        
        i_counter_str_0_i = "0"
        
        i_incrimenter_0_i = "1"
        
        
        
        
        i_s_2_i = f"{i_time_of_video_0_i} * {i_fps_0_i} + 1"
        
        
        i_operation_0_i = i_s_2_i
        
        
        i_m_0_i = self.i_math_i_am_i_1_i.calculatrice_2(s=i_operation_0_i, l_=[], n=0, number_of_digit_after_the_floating_point_=2, e=False)
        
        
        
        i_v_2_i = i_m_0_i[1][0]
        
        
        i_n_1_i = i_v_2_i.split(".")[0]
        
        
        
        
        
        
        i_countre_of_frame_0_i = 0
        
        i_countre_of_frame_1_i = 0
        
        
        
        i_list_of_step_0_i.append(i_counter_0_i)
        
        
        
        
        
        i_s_2_i = f"{i_n_1_i}"
        
        
        i_operation_0_i = i_s_2_i
        
        
        i_m_0_i = self.i_math_i_am_i_1_i.calculatrice_2(s=i_operation_0_i, l_=[], n=0, number_of_digit_after_the_floating_point_=2, e=False)
        
        
        
        i_s_1_i = f"{i_counter_str_0_i}"
        
        i_s_2_i = i_m_0_i[1][0]
        
        
        
        i_bool_0_i = self.i_math_i_am_i_1_i.my_egale_s_n_1(s1=i_s_1_i, s2=i_s_2_i, number_of_digit_after_the_floating_point_=2)
        
        
        i_bool_1_i = self.i_math_i_am_i_1_i.my_inferieur_s_n_1(s1=i_s_1_i, s2=i_s_2_i, number_of_digit_after_the_floating_point_=2)
        
        
        
        while (( i_bool_0_i == True ) or ( i_bool_1_i == True )):
            
            
            
            i_t_1_i = self.time.time()
            
            
            
            
            i_image_0_i = self.Image.new(
                "RGB",
                (i_width_max_0_i, i_height_max_0_i),
                i_color_of_frame_0_i
            )
            
            
            
            
            
            
            
            
            
            i_array_0_i = self.numpy.array(i_image_0_i)
            
            # إضافة الصورة إلى الفيديو
            
            i_writer_0_i.append_data(i_array_0_i)
            
            
            
            
            
            
            if (i_t_1_i - i_t_0_i > i_time_of_move_0_i):
                
                
                i_t_0_i = self.time.time()
                
                i_persentage_0_i = i_counter_0_i / ( int(i_n_1_i) )
                
                print(f"i_counter_0_i = {i_counter_0_i} . i_persentage_0_i = {i_persentage_0_i} % at 1.0")
                
                
                i_list_of_step_0_i.append(i_counter_0_i)
                
                
                if (len(i_list_of_step_0_i) >= 2):
                    
                    try:
                        
                        i_v_0_i = i_time_of_move_0_i * ( int(i_n_1_i) ) / abs(i_list_of_step_0_i[-1] - i_list_of_step_0_i[-2])
                        
                        
                        i_time_left_estimated_0_i = i_v_0_i - (len(i_list_of_step_0_i) * i_time_of_move_0_i)
                        
                        
                        print(f"i_time_left_estimated_0_i = {i_time_left_estimated_0_i} second .")
                        
                        
                    except:
                        
                        i_semaphore_of_error_0_i = True
                        
                        
                
            
            
            
            
            
            
            
            i_countre_of_frame_0_i += 1
            
            i_countre_of_frame_1_i += 1
            
            
            i_v_0_i = i_incrimenter_0_i.split(".")
            
            
            i_counter_0_i += int(i_v_0_i[0])
            
            
            
            i_operation_0_i = f"{i_counter_str_0_i} + {i_incrimenter_0_i}"
            
            
            i_m_0_i = self.i_math_i_am_i_1_i.calculatrice_2(s=i_operation_0_i, l_=[], n=0, number_of_digit_after_the_floating_point_=2, e=False)
            
            
            i_counter_str_0_i = i_m_0_i[1][0]
            
            
            
            i_s_2_i = f"{i_n_1_i}"
            
            
            i_operation_0_i = i_s_2_i
            
            
            i_m_0_i = self.i_math_i_am_i_1_i.calculatrice_2(s=i_operation_0_i, l_=[], n=0, number_of_digit_after_the_floating_point_=2, e=False)
            
            
            
            i_s_1_i = f"{i_counter_str_0_i}"
            
            i_s_2_i = i_m_0_i[1][0]
            
            
            i_bool_0_i = self.i_math_i_am_i_1_i.my_egale_s_n_1(s1=i_s_1_i, s2=i_s_2_i, number_of_digit_after_the_floating_point_=2)
            
            
            i_bool_1_i = self.i_math_i_am_i_1_i.my_inferieur_s_n_1(s1=i_s_1_i, s2=i_s_2_i, number_of_digit_after_the_floating_point_=2)
            
            
            
            
            
        
        i_writer_0_i.close()
        
        
        
        print("Video created successfully:", i_file_0_i)
    
    
    
    
    
    
    
    
    def i_concatenate_video_0_i(self, i_path_of_video_0_i, i_path_of_video_1_i, i_path_of_video_result_0_i):
        
        
        
        
        
        
        
        i_width_max_0_i = 1920
        
        i_height_max_0_i = 1080
        
        
        
        i_width_0_i = i_width_max_0_i
        
        i_height_0_i = 100
        
        
        
        i_width_1_i = i_width_max_0_i
        
        i_height_1_i = i_height_max_0_i - i_height_0_i
        
        
        
        
        i_fps_0_i = 30
        
        
        
        
        
        
        
        
        i_writer_0_i = self.imageio.v2.get_writer(
            i_path_of_video_result_0_i,
            fps=i_fps_0_i
        )
        
        
        
        
        
        
        
        i_number_of_image_0_i = 0
        
        
        i_semaphore_0_i = True
        
        i_list_of_step_0_i = []
        
        i_time_of_move_0_i = 10
        
        i_time_of_move_1_i = 7
        
        
        i_t_0_i = self.time.time()
        
        
    
        i_t_2_i = self.time.time()
        
        
        #i_incrimenter_0_i = 1.23
        
        i_counter_0_i = 0
        
        i_counter_str_0_i = 0
        
        i_incrimenter_0_i = 1
        
        
        i_counter_1_i = 0
        
        
        
        
        i_countre_of_frame_0_i = 0
        
        i_countre_of_frame_1_i = 0
        
        
        
        i_list_of_frame_0_i = []
        
        
        
        i_cv2_video_0_i = self.cv2.VideoCapture(i_path_of_video_0_i)
        
        
        i_cv2_video_1_i = self.cv2.VideoCapture(i_path_of_video_1_i)
        
        
        
        
        i_total_frames_0_i = int(
            i_cv2_video_1_i.get(self.cv2.CAP_PROP_FRAME_COUNT)
        )
        
        
        
        
        i_success_0_i, i_frame_0_i = i_cv2_video_0_i.read()
        
        if i_success_0_i:
            
            
            i_list_of_frame_0_i.append(i_frame_0_i)
            
            
        
        
        i_semaphore_of_continue_0_i = True
        
        
        
        
        
        i_list_of_step_0_i.append(i_counter_0_i)
        
        
        
        
        
        while (i_semaphore_of_continue_0_i == True):
            
            
            
            i_t_1_i = self.time.time()
            
            
            
            
            i_image_0_i = self.Image.new(
                "RGB",
                (i_width_max_0_i, i_height_max_0_i),
                (0, 0, 0)
            )
            
            
            
            
            
            
            
            i_success_0_i, i_frame_0_i = i_cv2_video_0_i.read()
            
            if i_success_0_i:
                
                
                i_list_of_frame_0_i.append(i_frame_0_i)
                
                
            else:
                
                
                i_counter_1_i = (i_counter_1_i + 1) % len(i_list_of_frame_0_i)
                
                
                i_frame_0_i = i_list_of_frame_0_i[i_counter_1_i]
                
                
                
            
            
            
            i_frame_rgb_0_i = self.cv2.cvtColor(
                i_frame_0_i,
                self.cv2.COLOR_BGR2RGB
            )
            
            i_image_1_i = self.Image.fromarray(i_frame_rgb_0_i)
            
            
            
            
            
            
            
            
            i_success_0_i, i_frame_0_i = i_cv2_video_1_i.read()
            
            if not i_success_0_i:
                
                
                i_semaphore_of_continue_0_i = False
                
                break
                
                
                
            
            
            
            
            i_frame_rgb_0_i = self.cv2.cvtColor(
                i_frame_0_i,
                self.cv2.COLOR_BGR2RGB
            )
            
            i_image_2_i = self.Image.fromarray(i_frame_rgb_0_i)
            
            
            
            
            
            i_image_1_i = i_image_1_i.resize((i_width_0_i, i_height_0_i))
            
            
            i_image_2_i = i_image_2_i.resize((i_width_1_i, i_height_1_i))
            
            
            
            
            
            
            
            i_image_0_i.paste(i_image_1_i, (0, 0))
            
            
            i_image_0_i.paste(i_image_2_i, (0, i_height_0_i))
            
            
            
            
            i_array_0_i = self.numpy.array(i_image_0_i)
            
            # إضافة الصورة إلى الفيديو
            
            i_writer_0_i.append_data(i_array_0_i)
            
            
            
            
            
            
            if (i_t_1_i - i_t_0_i > i_time_of_move_0_i):
                
                
                i_t_0_i = self.time.time()
                
                i_persentage_0_i = i_counter_0_i / ( int(i_total_frames_0_i) )
                
                print(f"i_counter_0_i = {i_counter_0_i} . i_persentage_0_i = {i_persentage_0_i} % at 1.0")
                
                
                i_list_of_step_0_i.append(i_counter_0_i)
                
                
                if (len(i_list_of_step_0_i) >= 2):
                    
                    try:
                        
                        i_v_0_i = i_time_of_move_0_i * ( int(i_total_frames_0_i) ) / abs(i_list_of_step_0_i[-1] - i_list_of_step_0_i[-2])
                        
                        
                        i_time_left_estimated_0_i = i_v_0_i - (len(i_list_of_step_0_i) * i_time_of_move_0_i)
                        
                        
                        print(f"i_time_left_estimated_0_i = {i_time_left_estimated_0_i} second .")
                        
                        
                    except:
                        
                        i_semaphore_of_error_0_i = True
                        
                        
                
            
            
            
            
            
            
            
            i_countre_of_frame_0_i += 1
            
            i_countre_of_frame_1_i += 1
            
            
            i_counter_0_i += i_incrimenter_0_i
            
            
            
            
            
        
        i_writer_0_i.close()
        
        
        
        print("Video created successfully:")
    
    
    
    
    
    
    
    
    
    
    # end of section of video 
    
    # -------------------------------------------------------------------------------------
    
    
    
    def i_put_names_0_i(self, i_dict_0_i, i_content_of_function_0_i):
        
        
        i_content_of_function_1_i = ""
        
        if ("i_code_0_i" in i_dict_0_i):
            
            i_content_of_function_1_i = i_dict_0_i.get("i_code_0_i")
            
            
        else:
            
            i_content_of_function_1_i = i_content_of_function_0_i.replace("_____name_0_____", i_dict_0_i.get("i_name_of_website_0_i"))
            
            
            i_content_of_function_1_i = i_content_of_function_1_i.replace("_____name_1_____", i_dict_0_i.get("i_file_source_of_website_0_i"))
            
        
        return i_content_of_function_1_i
        
        
        
    
    
    def i_main_0_i(self):
        
        
        i_list_of_website_0_i = [
                                
                                
                                {"i_name_of_website_0_i": "i_example_0_i", "i_file_source_of_website_0_i": "index.html"},
                                
                                
                                {"i_name_of_website_0_i": "i_research_0_i", "i_file_source_of_website_0_i": "i_research_0_i.html", "i_code_0_i": r"""
                                

@app.route("/i_research_0_i", methods=["GET", "POST"])
def i_research_0_i():

    i_search_text_0_i = ""
    i_results_0_i = []

    if request.method == "POST":

        i_search_text_0_i = request.form.get(
            "i_search_text_0_i", ""
        )
        
        i_v_0_i = i_search_text_0_i.split(" ")
        
        print(f"i_hello_0_i . i_search_text_0_i = {i_search_text_0_i} .")
        
        if i_v_0_i:

            i_raw_results_0_i = (
                i_tool_0_i.i_search_expretion_0_i(
                    i_v_0_i
                )
            )

            for i_item_0_i in i_raw_results_0_i:

                i_results_0_i.append({
                    "path": i_item_0_i[1],
                    "matches": i_item_0_i[0]
                })

    return render_template(
        "i_research_0_i.html",
        i_search_text_0_i=i_search_text_0_i,
        i_results_0_i=i_results_0_i,
        i_list_of_website_0_i=i_list_of_website_0_i,
        i_list_of_website_1_i=i_list_of_website_1_i
    )


                                                        
                                                        """},
                                
                                
                                {"i_name_of_website_0_i": "i_horloge_0_i", "i_file_source_of_website_0_i": "i_space_of_work_0_i/i_horloge_0_i.html"},
                                
                                
                                {"i_name_of_website_0_i": "i_example_1_i", "i_file_source_of_website_0_i": "i_space_of_work_0_i/i_index_0_i.html"},
                                
                                
                                {"i_name_of_website_0_i": "i_my_mixer_1_i", "i_file_source_of_website_0_i": "i_space_of_work_0_i/i_page_of_mixer_0_i.html"},
                                
                                
                                
                                ]
        
        
        
        i_str_0_i = self.os.path.join("a", "b")
        
        i_v_0_i = i_str_0_i.split("a")
        
        i_v_0_i = i_v_0_i[1].split("b")
        
        i_str_of_between_0_i = i_v_0_i[0]
        
        
        print(f"i_str_of_between_0_i = {i_str_of_between_0_i} .")
        
        
        i_counter_0_i = 0
        
        while (i_counter_0_i < len(i_list_of_website_0_i)):
            
            i_list_of_website_0_i[i_counter_0_i]["i_ful_path_of_file_of_source_of_website_0_i"] = self.os.path.join(self.cwd, "i_folder_of_resource_0_i", "templates", i_list_of_website_0_i[i_counter_0_i].get("i_file_source_of_website_0_i").replace("/", i_str_of_between_0_i))
            
            i_counter_0_i += 1
            
            
        
        
        
        
        i_list_of_website_1_i = i_list_of_website_0_i[:4] 
        
        
        
        i_file_to_execute_0_i = self.os.path.join(self.cwd, "i_folder_of_resource_0_i", "i_app_0_i.py")
        
        
        i_file_for_generation_0_i = self.os.path.join(self.cwd, "i_folder_of_resource_0_i", "i_app_1_i.py")
        
        
        
        i_content_of_function_0_i = r"""
        
        

@app.route("/_____name_0_____")
def _____name_0_____():
    return render_template("_____name_1_____")


        
        
        """
        
        
        
        i_d_0_i = self.Path(i_file_for_generation_0_i)
        
        
        
        i_content_of_app_1_i = i_d_0_i.read_text()
        
        
        i_content_0_i = ""
        
        
        i_counter_0_i = 0
        
        while (i_counter_0_i < len(i_list_of_website_0_i)):
            
            
            
            i_content_0_i += self.i_put_names_0_i(i_dict_0_i=i_list_of_website_0_i[i_counter_0_i], i_content_of_function_0_i=i_content_of_function_0_i)
            
            
            i_counter_0_i += 1
            
            
        
        
        
        i_content_of_app_1_i = i_content_of_app_1_i.replace("_____i_section_of_websites_0_i_____", i_content_0_i)
        
        
        i_content_of_app_1_i = i_content_of_app_1_i.replace("_____i_list_of_website_0_i_____", f"i_list_of_website_0_i = {i_list_of_website_0_i} \ni_list_of_website_1_i = {i_list_of_website_1_i}")
        
        
        
        
        i_content_of_app_0_i = i_content_of_app_1_i
        
        i_d_1_i = self.Path(i_file_to_execute_0_i)
        
        
        i_d_1_i.write_text(i_content_of_app_0_i)
        
        
        
        
        
        self.os.system(f"{self.sys.executable} {i_file_to_execute_0_i}")
        
        
        
        
        
    



if __name__ == "__main__":
    
    
    
    global i
    
    
    i = i_class_of_i_0_i(i_semaphore_of_pip_install_0_i=True)
    
    
    
    
    i.i_push_content_0_i(i_content_0_i = r"""
    

identificater : 0
    
    
    name : "Bilale"
    
    pre_name : "Debouci"
    
    pass_word : "i_principal_central_i"
    
    content :
        
        # --------------------------------------------------------------------------------------
        
        name_of_unity : "i"
            
            amount_0 : "0.00"
            
        name_of_unity : "the quality of i"
            
            amount_0 : "0.00"
            
        
        name_of_unity : "real"
            
            amount_0 : "0.00"
            
        name_of_unity : "the quality of real"
            
            amount_0 : "0.00"
            
        
        name_of_unity : "power"
            
            amount_0 : "0.00"
            
        name_of_unity : "the quality of power"
            
            amount_0 : "0.00"
            
        
        name_of_unity : "work"
            
            amount_0 : "0.00"
            
        name_of_unity : "the quality of work"
            
            amount_0 : "0.00"
            
        
        
        # --------------------------------------------------------------------------------------
        
        name_of_unity : "i"
            
            amount_0 : "0.01"
            
        name_of_unity : "the quality of i"
            
            amount_0 : "0.01"
            
        
        name_of_unity : "real"
            
            amount_0 : "0.01"
            
        name_of_unity : "the quality of real"
            
            amount_0 : "0.01"
            
        
        name_of_unity : "power"
            
            amount_0 : "0.01"
            
        name_of_unity : "the quality of power"
            
            amount_0 : "0.01"
            
        
        name_of_unity : "work"
            
            amount_0 : "0.01"
            
        name_of_unity : "the quality of work"
            
            amount_0 : "0.01"
            
        
        # --------------------------------------------------------------------------------------
        
        name_of_unity : "i"
            
            amount_0 : "1.00"
            
        name_of_unity : "the quality of i"
            
            amount_0 : "1.00"
            
        
        name_of_unity : "real"
            
            amount_0 : "1.00"
            
        name_of_unity : "the quality of real"
            
            amount_0 : "1.00"
            
        
        name_of_unity : "power"
            
            amount_0 : "1.00"
            
        name_of_unity : "the quality of power"
            
            amount_0 : "1.00"
            
        
        name_of_unity : "work"
            
            amount_0 : "1.00"
            
        name_of_unity : "the quality of work"
            
            amount_0 : "1.00"
            
        
        # --------------------------------------------------------------------------------------
        
        name_of_unity : "i"
            
            amount_0 : "1.00"
            
        name_of_unity : "the quality of i"
            
            amount_0 : "1_000.00"
            
            amount_1 : "4_400_000.00"
            
            amount_2 : "10 ** 300_000"
            
        name_of_unity : "real"
            
            amount_0 : "1.00"
            
        name_of_unity : "the quality of real"
            
            amount_0 : "1_000.00"
            
            amount_1 : "4_400_000.00"
            
            amount_2 : "10 ** 300_000"
            
        
        name_of_unity : "power"
            
            amount_0 : "1_000.00"
            
            amount_1 : "4_400_000.00"
            
            amount_2 : "10 ** 100_000"
            
        
        name_of_unity : "the quality of power"
            
            amount_0 : "1_000.00"
            
            amount_1 : "4_400_000.00"
            
            amount_2 : "10 ** 300_000"
            
        
        name_of_unity : "work"
            
            amount_0 : "1_000.00"
            
            amount_1 : "4_400_000.00"
            
            amount_2 : "10 ** 100_000"
            
            
        name_of_unity : "the quality of work"
            
            amount_0 : "1_000.00"
            
            amount_1 : "4_400_000.00"
            
            amount_2 : "10 ** 300_000"
            
            
        
        
        
    
    
    
    
    


    """
    )
    
    
    
    
    i_t_0_i = i.time.time()
    
    
    i.i_compute_0_i()
    
    
    i.i_bank_move_17_i()
        
    
    i.i_bank_move_9_i()
    
    
    
    i_t_1_i = i.time.time()
    
    
    print(f"\n\n     time = {i_t_1_i - i_t_0_i} second . \n\n")
    
    print(f"i.i_account_of_bank_0_i = {i.i_account_of_bank_0_i} .")
    
    
    
    
    
    
    
    i.i_main_0_i()
    
    
    
    
    






















