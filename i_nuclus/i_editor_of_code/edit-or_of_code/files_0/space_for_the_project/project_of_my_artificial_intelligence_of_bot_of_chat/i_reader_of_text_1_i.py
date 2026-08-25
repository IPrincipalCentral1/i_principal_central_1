
















import subprocess


import sys


import os



cwd = os.path.dirname(os.path.abspath(__file__))



i_list_0_i = [
            
            
            
            "gTTS", 
            
            "pydub", 
            
            "langdetect",
            
            
            ]
            
            
            




print(f"\n\n    pip install --upgrade pip setuptools wheel \n\n\n")


subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip", "setuptools", "wheel"])







i_counter_0_i = 0


while (i_counter_0_i < len(i_list_0_i)):
    
    
    try:
        
        
        
        print(f"\n\n    pip install {i_list_0_i[i_counter_0_i]} \n\n\n")   
         
        
        subprocess.check_call([sys.executable, "-m", "pip", "install", f"{i_list_0_i[i_counter_0_i]}"])
        
    except:
        
        
        i_semaphore_0_i = True
        
        
    
    
    
    i_counter_0_i += 1
    
    



print("\n" * 10)




from gtts import gTTS
from langdetect import detect
from pydub import AudioSegment
import re
import os



import i_reformater_1










#text = """

#Hello, how are you?
#مرحبا، كيف حالك؟
#Bonjour mon ami.
#I am fine شكراً.


#"""




text = """











"""






i_file_0_i = os.path.join(cwd, "i_file_of_text_of_result_3_i.txt")


with open(i_file_0_i, "r") as f_:
    
    
    text = f_.read(os.path.getsize(i_file_0_i))
    
    






def detect_language(word):
    
    
    i_result_0_i = "en"
    
    if re.search(r'[\u0600-\u06FF]', word):
        i_result_0_i = "ar"

    elif re.search(r'[a-zA-Z]', word):
        i_result_0_i = "en"

    return i_result_0_i


# تقسيم النص إلى كلمات مع الاحتفاظ بالمسافات

#words = re.findall(r'\S+', text)





separater_of_words = [" ", "\n", "."]


not_counted_words = [""]


words = i_reformater_1.finder_and_spliter_0(element_0=separater_of_words, element_1=text, not_counted_words=not_counted_words)

words = words[1]




i_counter_0_i = 0


parts = []

for word in words:
    
    lang = "en"
    
    try:
        
        #lang = detect(word)
        
        lang = detect_language(word)
        
        
        # تحويل بعض نتائج langdetect إلى لغات gTTS
        if lang.startswith("ar"):
            lang = "ar"
        elif lang.startswith("en"):
            lang = "en"
        elif lang.startswith("fr"):
            lang = "fr"
        else:
            lang = "en"

        parts.append((word, lang))

    except:
        parts.append((word, "en"))
    
    
    
    print(f"{i_counter_0_i} . word = {word} . lang = {lang} .")       
    
    
    
    
    i_counter_0_i += 1
    
    
    

# تجميع الكلمات التي لها نفس اللغة

#groups = []



#for word, lang in parts:

    #if groups and groups[-1][1] == lang:
        #groups[-1] = (groups[-1][0] + " " + word, lang)
    #else:
        #groups.append((word, lang))




i_counter_0_i = 0


groups = parts

# إنشاء ملف صوتي لكل مجموعة
audio = AudioSegment.empty()

for i, (text_part, lang) in enumerate(groups):
    
    
    try:
        
        filename = os.path.join(cwd, f"part_{i}.mp3")
    
        print(f"{i_counter_0_i} . {lang}: {text_part}")
    
        tts = gTTS(
            text=text_part,
            lang=lang
        )
    
        tts.save(filename)
    
        segment = AudioSegment.from_mp3(filename)
    
        audio += segment
    
        os.remove(filename)
    
    except:
        
        
        i_semaphore_0_i = True
        
        
    
    
    i_counter_0_i += 1
    
    

# حفظ الملف النهائي
audio.export(os.path.join(cwd, "i_output_0_i.mp3"), format="mp3")

print("file created successfully : i_output_0_i.mp3")












