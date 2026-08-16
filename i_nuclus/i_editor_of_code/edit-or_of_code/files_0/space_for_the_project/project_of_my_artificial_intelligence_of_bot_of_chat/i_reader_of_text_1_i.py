
















import subprocess


import sys


import os



cwd = os.path.dirname(os.path.abspath(__file__))



i_list_0_i = [
            
            
            
            "gTTS", 
            
            "pydub", 
            
            "langdetect",
            
            
            ]
            
            
            



i_counter_0_i = 0


while (i_counter_0_i < len(i_list_0_i)):
    
    
    
    subprocess.check_call([sys.executable, "-m", "pip", "install", f"{i_list_0_i[i_counter_0_i]}"])
    
    
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








* الجزائر – * . * في – * . * في اعثر * . * (08:00 اعثر * . * في على * . * (08:00 على * . * (08:00 principal_central * . * – principal_central * . * (08:00 give * . * – give * . * (08:00 me * . * – me * . * اعثر me * . * – chance * . * اعثر chance * . * – المبنى * . * اعثر المبنى * . * على المبنى * . * اعثر الرئيسي * . * على الرئيسي * . * اعثر لبريد * . * على لبريد * . * principal_central لبريد * . * على المركزي * . * principal_central المركزي * . * على يقع * . * principal_central يقع * . * give يقع * . * على قلب * . * principal_central قلب * . * give قلب * . * principal_central العاصمة: * . * give العاصمة: * . * me العاصمة: * . * principal_central **بريد * . * give **بريد * . * me **بريد * . * give المركزي** * . * me المركزي** * . * chance المركزي** * . * give **الموقع:** * . * me **الموقع:** * . * chance **الموقع:** * . * me تقاطع * . * chance تقاطع * . * المبنى تقاطع * . * me شارع * . * chance شارع * . * المبنى شارع * . * chance محمد * . * المبنى محمد * . * الرئيسي محمد * . * chance خميستي * . * المبنى خميستي * . * الرئيسي خميستي * . * chance وشارع * . * المبنى وشارع * . * الرئيسي وشارع * . * لبريد وشارع * . * المبنى العربي * . * الرئيسي العربي * . * لبريد العربي * . * المبنى بن * . * الرئيسي بن * . * لبريد بن * . * المركزي بن * . * الرئيسي مهيدي، * . * لبريد مهيدي، * . * المركزي مهيدي، * . * الرئيسي بلدية * . * لبريد بلدية * . * المركزي بلدية * . * يقع بلدية * . * لبريد الوسطى * . * المركزي الوسطى * . * يقع الوسطى * . * لبريد **الرمز * . * المركزي **الرمز * . * يقع **الرمز * . * قلب **الرمز * . * المركزي البريدي:** * . * يقع البريدي:** * . * قلب البريدي:** * . * المركزي 16000 * . * يقع 16000 * . * قلب 16000 * . * العاصمة: 16000 * . * المركزي **ساعات * . * يقع **ساعات * . * قلب **ساعات * . * العاصمة: **ساعات * . * يقع العمل:** * . * قلب العمل:** * . * العاصمة: العمل:** * . * **بريد العمل:** * . * يقع من * . * قلب من * . * العاصمة: من * . * **بريد من * . * قلب السبت * . * العاصمة: السبت * . * **بريد السبت * . * المركزي** السبت * . * قلب إلى * . * العاصمة: إلى * . * **بريد إلى * . * المركزي** إلى * . * العاصمة: الأربعاء * . * **بريد الأربعاء * . * المركزي** الأربعاء * . * **الموقع:** الأربعاء * . * العاصمة: 18:00)، * . * **بريد 18:00)، * . * المركزي** 18:00)، * . * **الموقع:** 18:00)، * . * **بريد والخميس * . * المركزي** والخميس * . * **الموقع:** والخميس * . * تقاطع والخميس * . * **بريد 16:00) * . * المركزي** 16:00) * . * **الموقع:** 16:00) * . * تقاطع 16:00) * . * المركزي** --- * . * **الموقع:** --- * . * تقاطع --- * . * شارع --- * . * المركزي** ### * . * **الموقع:** ### * . * تقاطع ### * . * شارع ### * . * **الموقع:** أماكن * . * تقاطع أماكن * . * شارع أماكن * . * محمد أماكن * . * **الموقع:** وخدمات * . * تقاطع وخدمات * . * شارع وخدمات * . * محمد وخدمات * . * تقاطع مجاورة * . * شارع مجاورة * . * محمد مجاورة * . * خميستي مجاورة * . * تقاطع **ساحة * . * شارع **ساحة * . * محمد **ساحة * . * خميستي **ساحة * . * تقاطع البريد * . * شارع البريد * . * محمد البريد * . * خميستي البريد * . * وشارع البريد * . * شارع المركزي:** * . * محمد المركزي:** * . * خميستي المركزي:** * . * وشارع المركزي:** * . * شارع الساحة * . * محمد الساحة * . * خميستي الساحة * . * وشارع الساحة * . * العربي الساحة * . * محمد العامة * . * خميستي العامة * . * وشارع العامة * . * العربي العامة * . * محمد المقابلة * . * خميستي المقابلة * . * وشارع المقابلة * . * العربي المقابلة * . * بن المقابلة * . * خميستي للمبنى * . * وشارع للمبنى * . * العربي للمبنى * . * بن للمبنى * . * خميستي المقصد * . * وشارع المقصد * . * العربي المقصد * . * بن المقصد * . * مهيدي، المقصد * . * وشارع للأنشطة * . * العربي للأنشطة * . * بن للأنشطة * . * مهيدي، للأنشطة * . * وشارع والتجمع * . * العربي والتجمع * . * بن والتجمع * . * مهيدي، والتجمع * . * بلدية والتجمع * . * العربي Grande * . * بن Grande * . * مهيدي، Grande * . * بلدية Grande * . * العربي Poste * . * بن Poste * . * مهيدي، Poste * . * بلدية Poste * . * الوسطى Poste * . * بن D'alger *









"""







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



parts = []

for word in words:

    try:
        
        #lang = detect(word)
        
        lang = detect_language(word)
        
        
        print(f"word = {word} . lang = {lang} .")       
        
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


# تجميع الكلمات التي لها نفس اللغة

#groups = []



#for word, lang in parts:

    #if groups and groups[-1][1] == lang:
        #groups[-1] = (groups[-1][0] + " " + word, lang)
    #else:
        #groups.append((word, lang))



groups = parts

# إنشاء ملف صوتي لكل مجموعة
audio = AudioSegment.empty()

for i, (text_part, lang) in enumerate(groups):

    filename = os.path.join(cwd, f"part_{i}.mp3")

    print(f"{lang}: {text_part}")

    tts = gTTS(
        text=text_part,
        lang=lang
    )

    tts.save(filename)

    segment = AudioSegment.from_mp3(filename)

    audio += segment

    os.remove(filename)


# حفظ الملف النهائي
audio.export(os.path.join(cwd, "i_output_0_i.mp3"), format="mp3")

print("تم إنشاء output.mp3")












