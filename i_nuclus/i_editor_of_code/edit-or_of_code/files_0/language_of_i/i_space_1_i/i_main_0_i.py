











































































































list_of_liberary_to_install = [
                            
                            
                            ["pillow"] ,
                            
                            



]










import os


import traceback

import sys


import subprocess




cwd = os.path.dirname(os.path.abspath(__file__))



print(f"\n\n    pip install --upgrade pip setuptools wheel \n\n\n")


subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip", "setuptools", "wheel"])



try:
    
    counter_0 = 0
    
    
    while (counter_0 < len(list_of_liberary_to_install)):
    

                
        try:
        
        
            print(f"\n\n\npip install {list_of_liberary_to_install[counter_0][0]}\n\n\n")
            
            #os.system(f"pip3 install {list_of_liberary_to_install[counter_0][0]}")
            
            
            #subprocess.check_call([sys.executable, "-m", "pip", "uninstall", f"{list_of_liberary_to_install[counter_0][0]}"])
            
            subprocess.check_call([sys.executable, "-m", "pip", "install", f"{list_of_liberary_to_install[counter_0][0]}"])
        
        
                
        except:
        
                
                        
            traceback.print_exc()
            
            error = traceback.format_exc()
            
            semaphore = True
            
            print(f"Erreur : {str(error)}")
            
        
        
        counter_0 += 1
        
        
    
except:

        
                
    traceback.print_exc()
    
    error = traceback.format_exc()
    
    semaphore = True
    
    print(f"Erreur : {str(error)}")
    
    
    


print("\n" * 10)











from PIL import Image, ImageDraw









i_file_of_origine_0_i = os.path.join(cwd, "i_image_5_i.png")



# حجم الصورة (العرض، الارتفاع)


width, height = 1200, 700


i_image_0_i = Image.open(i_file_of_origine_0_i)


# تحديد منطقة القص: (left, top, right, bottom)

left = 100

top = 110

right = 900

bottom = 480




i_image_0_i = i_image_0_i.crop((left, top, right, bottom))




## إنشاء صورة بيضاء

#i_image_0_i = Image.new("RGB", (width, height), color="white")


## عرض الإطار الأسود
#border = 20

## إنشاء كائن للرسم
#draw = ImageDraw.Draw(i_image_0_i)

## رسم مستطيل الإطار الأسود
#draw.rectangle(
    #[0, 0, width-1, height-1],      # إطار كامل الصورة
    #outline="black",                # لونه أسود
    #width=border                    # عرض الخط
#)





i_file_0_i = os.path.join(cwd, "i_image_0_i.png")

# حفظ الصورة

i_image_0_i.save(i_file_0_i)









i_image_0_0_i = Image.open(i_file_of_origine_0_i)



# تحديد منطقة القص: (left, top, right, bottom)

left = 100

top = 530

right = 900

bottom = 900




i_image_0_0_i = i_image_0_0_i.crop((left, top, right, bottom))







## إنشاء صورة بيضاء

#i_image_0_0_i = Image.new("RGB", (width, height), color="white")


## عرض الإطار الأسود
#border = 20

## إنشاء كائن للرسم
#draw = ImageDraw.Draw(i_image_0_0_i)

## رسم مستطيل الإطار الأسود
#draw.rectangle(
    #[0, 0, width-1, height-1],      # إطار كامل الصورة
    #outline="black",                # لونه أسود
    #width=border                    # عرض الخط
#)





i_file_0_0_i = os.path.join(cwd, "i_image_0_0_i.png")

# حفظ الصورة

i_image_0_0_i.save(i_file_0_0_i)










# حجم الصورة (العرض، الارتفاع)

width, height = 700, 1200

# إنشاء صورة بيضاء

i_image_1_i = Image.new("RGB", (width, height), color="white")




# لصق الصورة الصغيرة على الكبيرة

i_image_0_i = i_image_0_i.resize((int(width * (4 / 5)), int(height // 4)))


i_image_1_i.paste(i_image_0_i, (0, int(height // 4) * 0))


i_image_1_i.paste(i_image_0_i, (0, int(height // 4) * 1))


i_image_1_i.paste(i_image_0_i, (0, int(height // 4) * 2))


i_image_1_i.paste(i_image_0_i, (0, int(height // 4) * 3))




i_file_1_i = os.path.join(cwd, "i_image_1_i.png")


i_image_1_i.save(i_file_1_i)







# حجم الصورة (العرض، الارتفاع)

width, height = 700, 1200

# إنشاء صورة بيضاء

i_image_2_i = Image.new("RGB", (width, height), color="white")




# لصق الصورة الصغيرة على الكبيرة

i_image_0_0_i = i_image_0_0_i.resize((int(width * (4 / 5)), int(height // 4)))


i_image_2_i.paste(i_image_0_0_i, (int(width * (1 / 5)), int(height // 4) * 0))


i_image_2_i.paste(i_image_0_0_i, (int(width * (1 / 5)), int(height // 4) * 1))


i_image_2_i.paste(i_image_0_0_i, (int(width * (1 / 5)), int(height // 4) * 2))


i_image_2_i.paste(i_image_0_0_i, (int(width * (1 / 5)), int(height // 4) * 3))




i_file_2_i = os.path.join(cwd, "i_image_2_i.png")


i_image_2_i.save(i_file_2_i)










#i_link_0_i = i_file_2_i



#i_counter_0_i = 0

#while (i_counter_0_i < 0):

    #os.system(f"lp -d Canon_LBP631C_USB -o fit-to-page -o media=A4 {i_link_0_i}")

    #i_counter_0_i += 1















