
















import subprocess


import sys


import os



cwd = os.path.dirname(os.path.abspath(__file__))



i_list_0_i = [
            
            
            
            "gTTS", 
            
            "pydub", 
            
            "langdetect",
            
            "opencv-python",
            
            "Pillow",
            
            "imageio-ffmpeg",
            
            "arabic-reshaper",
            
            "python-bidi",
        
            
            
            
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


import time








#text = """

#Hello, how are you?
#مرحبا، كيف حالك؟
#Bonjour mon ami.
#I am fine شكراً.


#"""




text = """








i want there i . i to there i . i to am i . i be am i . i to continue i . i be continue i . i be height i . i there height i . i be quality i . i there quality i . i be believe i . i there believe i . i am believe i . i there is i . i am is i . i there a i . i am a i . i continue a i . i am مشوي i . i continue مشوي i . i am right i . i continue right i . i height right i . i am degust i . i continue degust i . i height degust i . i continue in i . i height in i . i quality in i . i continue my i . i height my i . i quality my i . i height hotel i







ieni . itni . itai . ihai . itoi . ihoi . ihui . inui . ihgi . ingi . ihmi . inmi . iami . inri . iari . inbi . iabi . iobi . iali . ioli . iaci . ioci . iuci . iayi . ioyi . iuyi . iosi . iusi . igsi . iowi . iuwi . igwi . iuqi . igqi . imqi . iuvi . igvi . imvi . igdi . imdi . irdi . igمi . imمi . irمi . imشi . irشi . ibشi . imوi . irوi . ibوi . irيi







i am height i . i continue height i . i continue to i . i there to i . i continue be i . i there be i . i there want i . i height want i . i there quality i . i height quality i . i there believe i . i height believe i . i to believe i . i height a i . i to a i . i height right i . i to right i . i be right i . i to degust i . i be degust i . i to in i . i be in i . i want in i . i be my i . i want my i . i be is i . i want is i . i quality is i . i be مشوي i . i want مشوي i . i quality مشوي i . i want hotel i . i quality hotel i . i believe hotel i . i want ieni i . i quality ieni i . i believe ieni i . i quality itni i . i believe itni i . i a itni i . i quality itai i . i believe itai i . i a itai i . i believe ihai i . i a ihai i . i right ihai i . i believe itoi i . i a itoi i . i right itoi i . i a ihoi i . i right ihoi i . i degust ihoi i . i a ihui i . i right ihui i . i degust ihui i . i a inui i . i right inui i . i degust inui i . i in inui i . i right ihgi i . i degust ihgi i . i in ihgi i . i right ingi i . i degust ingi i . i in ingi i . i my ingi i . i degust ihmi i . i in ihmi i . i my ihmi i . i degust inmi i . i in inmi i . i my inmi i . i is inmi i . i in iami i . i my iami i . i is iami i . i in inri i . i my inri i . i is inri i . i مشوي inri i . i my iari i . i is iari i . i مشوي iari i . i my inbi i . i is inbi i . i مشوي inbi i . i hotel inbi i . i is iabi i . i مشوي iabi i . i hotel iabi i . i is iobi i . i مشوي iobi i . i hotel iobi i . i ieni iobi i . i is iali i . i مشوي iali i . i hotel iali i . i ieni iali i . i مشوي ioli i . i hotel ioli i . i ieni ioli i . i itni ioli i . i مشوي iaci i . i hotel iaci i . i ieni iaci i . i itni iaci i . i hotel ioci i . i ieni ioci i . i itni ioci i . i itai ioci i . i hotel iuci i . i ieni iuci i . i itni iuci i . i itai iuci i . i ieni iayi i . i itni iayi i . i itai iayi i . i ihai iayi i . i ieni ioyi i . i itni ioyi i . i itai ioyi i . i ihai ioyi i . i itni iuyi i . i itai iuyi i . i ihai iuyi i . i itoi iuyi i . i itni iosi i . i itai iosi i . i ihai iosi i . i itoi iosi i . i itai iusi i . i ihai iusi i . i itoi iusi i . i ihoi iusi i . i itai igsi i . i ihai igsi i . i itoi igsi i . i ihoi igsi i . i ihai iowi i . i itoi iowi i . i ihoi iowi i . i ihui iowi i . i ihai iuwi i . i itoi iuwi i . i ihoi iuwi i . i ihui iuwi i . i ihai igwi i . i itoi igwi i . i ihoi igwi i . i ihui igwi i . i inui igwi i . i itoi iuqi i . i ihoi iuqi i . i ihui iuqi i . i inui iuqi i . i itoi igqi i . i ihoi igqi i . i ihui igqi i . i inui igqi i . i ihgi igqi i . i ihoi imqi i . i ihui imqi i . i inui imqi i . i ihgi imqi i . i ihoi iuvi i . i ihui iuvi i . i inui iuvi i . i ihgi iuvi i . i ingi iuvi i . i ihui igvi i . i inui igvi i . i ihgi igvi i . i ingi igvi i . i ihui imvi i . i inui imvi i . i ihgi imvi i . i ingi imvi i . i ihmi imvi i . i inui igdi i . i ihgi igdi i . i ingi igdi i . i ihmi igdi i . i inui imdi i . i ihgi imdi i . i ingi imdi i . i ihmi imdi i . i inmi imdi i . i ihgi irdi i . i ingi irdi i . i ihmi irdi i . i inmi irdi i . i ihgi igمi i . i ingi igمi i . i ihmi igمi i . i inmi igمi i . i iami igمi i . i ingi imمi i . i ihmi imمi i . i inmi imمi i . i iami imمi i . i ingi irمi i . i ihmi irمi i . i inmi irمi i . i iami irمi i . i inri irمi i . i ihmi imشi i . i inmi imشi i . i iami imشi i . i inri imشi i . i ihmi irشi i . i inmi irشi i . i iami irشi i . i inri irشi i . i iari irشi i . i ihmi ibشi i . i inmi ibشi i . i iami ibشi i . i inri ibشi i . i iari ibشi i . i inmi imوi i . i iami imوi i . i inri imوi i . i iari imوi i . i inbi imوi i . i inmi irوi i . i iami irوi i . i inri irوi i . i iari irوi i . i inbi irوi i . i iami ibوi i . i inri ibوi i . i iari ibوi i . i inbi ibوi i . i iabi ibوi i . i iami irيi i







ithi . iehi . ieai . inai . iegi . ingi . inmi . ihmi . inui . ihui . inoi . ihoi . iaoi . ihri . iari . ihbi . iabi . igbi . iali . igli . iasi . igsi . imsi . iayi . igyi . imyi . igوi . imوi . iuوi . igمi . imمi . iuمi . imشi . iuشi . ioشi . imvi . iuvi . iovi . iuwi . iowi . irwi . iuqi . ioqi . irqi . iodi . irdi . ibdi . ioci . irci . ibci . irيi







i inmi inui i . i be inui i . i be ingi i . i height ingi i . i be ihmi i . i height ihmi i . i height to i . i inui to i . i height there i . i inui there i . i height is i . i inui is i . i ingi is i . i inui مشوي i . i ingi مشوي i . i inui right i . i ingi right i . i ihmi right i . i ingi in i . i ihmi in i . i ingi ihoi i . i ihmi ihoi i . i to ihoi i . i ihmi ihui i . i to ihui i . i ihmi iami i . i to iami i . i there iami i . i ihmi want i . i to want i . i there want i . i to quality i . i there quality i . i is quality i . i to believe i . i there believe i . i is believe i . i there a i . i is a i . i مشوي a i . i there degust i . i is degust i . i مشوي degust i . i is my i . i مشوي my i . i right my i . i is hotel i . i مشوي hotel i . i right hotel i . i مشوي ihai i . i right ihai i . i in ihai i . i مشوي itoi i . i right itoi i . i in itoi i . i مشوي ihgi i . i right ihgi i . i in ihgi i . i ihoi ihgi i . i right continue i . i in continue i . i ihoi continue i . i right ieni i . i in ieni i . i ihoi ieni i . i ihui ieni i . i in itni i . i ihoi itni i . i ihui itni i . i in itai i . i ihoi itai i . i ihui itai i . i iami itai i . i ihoi inri i . i ihui inri i . i iami inri i . i ihoi am i . i ihui am i . i iami am i . i want am i . i ihui iari i . i iami iari i . i want iari i . i ihui inbi i . i iami inbi i . i want inbi i . i quality inbi i . i iami iuvi i . i want iuvi i . i quality iuvi i . i iami imvi i . i want imvi i . i quality imvi i . i believe imvi i . i iami igمi i . i want igمi i . i quality igمi i . i believe igمi i . i want imوi i . i quality imوi i . i believe imوi i . i a imوi i . i want iabi i . i quality iabi i . i believe iabi i . i a iabi i . i quality iali i . i believe iali i . i a iali i . i degust iali i . i quality ioci i . i believe ioci i . i a ioci i . i degust ioci i . i believe iayi i . i a iayi i . i degust iayi i . i my iayi i . i believe igsi i . i a igsi i . i degust igsi i . i my igsi i . i a iowi i . i degust iowi i . i my iowi i . i hotel iowi i . i a iuwi i . i degust iuwi i . i my iuwi i . i hotel iuwi i . i degust igwi i . i my igwi i . i hotel igwi i . i ihai igwi i . i degust iuqi i . i my iuqi i . i hotel iuqi i . i ihai iuqi i . i my igqi i . i hotel igqi i . i ihai igqi i . i itoi igqi i . i my imdi i . i hotel imdi i . i ihai imdi i . i itoi imdi i . i my irdi i . i hotel irdi i . i ihai irdi i . i itoi irdi i . i ihgi irdi i . i hotel imمi i . i ihai imمi i . i itoi imمi i . i ihgi imمi i . i hotel irمi i . i ihai irمi i . i itoi irمi i . i ihgi irمi i . i continue irمi i . i ihai imشi i . i itoi imشi i . i ihgi imشi i . i continue imشi i . i ihai irشi i . i itoi irشi i . i ihgi irشi i . i continue irشi i . i ieni irشi i . i itoi ibشi i . i ihgi ibشi i . i continue ibشi i . i ieni ibشi i . i itoi irوi i . i ihgi irوi i . i continue irوi i . i ieni irوi i . i itni irوi i . i ihgi ibوi i . i continue ibوi i . i ieni ibوi i . i itni ibوi i . i ihgi iobi i . i continue iobi i . i ieni iobi i . i itni iobi i . i itai iobi i . i continue ioli i . i ieni ioli i . i itni ioli i . i itai ioli i . i continue iaci i . i ieni iaci i . i itni iaci i . i itai iaci i . i inri iaci i . i ieni iuci i . i itni iuci i . i itai iuci i . i inri iuci i . i ieni ioyi i . i itni ioyi i . i itai ioyi i . i inri ioyi i . i am ioyi i . i ieni iuyi i . i itni iuyi i . i itai iuyi i . i inri iuyi i . i am iuyi i . i itni iosi i . i itai iosi i . i inri iosi i . i am iosi i . i iari iosi i . i itni iusi i . i itai iusi i . i inri iusi i . i am iusi i . i iari iusi i . i itai imqi i . i inri imqi i . i am imqi i . i iari imqi i . i inbi imqi i . i itai igvi i . i inri igvi i . i am igvi i . i iari igvi i . i inbi igvi i . i inri igdi i . i am igdi i . i iari igdi i . i inbi igdi i . i iuvi igdi i . i inri irيi i . i am irيi i . i iari irيi i . i inbi irيi i . i iuvi irيi i . i am ithi i . i iari ithi i . i inbi ithi i . i iuvi ithi i . i imvi ithi i . i am iehi i . i iari iehi i . i inbi iehi i . i iuvi iehi i . i imvi iehi i . i iari ieai i . i inbi ieai i . i iuvi ieai i . i imvi ieai i . i igمi ieai i . i iari inai i . i inbi inai i . i iuvi inai i . i imvi inai i . i igمi inai i . i inbi iegi i . i iuvi iegi i . i imvi iegi i . i igمi iegi i . i imوi iegi i . i inbi inoi i . i iuvi inoi i . i imvi inoi i . i igمi inoi i . i imوi inoi i . i iuvi iaoi i . i imvi iaoi i . i igمi iaoi i . i imوi iaoi i . i iabi iaoi i . i iuvi ihri i . i imvi ihri i . i igمi ihri i . i imوi ihri i . i iabi ihri i . i imvi ihbi i . i igمi ihbi i . i imوi ihbi i . i iabi ihbi i . i iali ihbi i . i imvi igbi i . i igمi igbi i . i imوi igbi i . i iabi igbi i . i iali igbi i . i igمi igli i . i imوi igli i . i iabi igli i . i iali igli i . i ioci igli i . i igمi iasi i . i imوi iasi i . i iabi iasi i . i iali iasi i . i ioci iasi i . i igمi imsi i . i imوi imsi i . i iabi imsi i . i iali imsi i . i ioci imsi i . i iayi imsi i . i imوi igyi i . i iabi igyi i . i iali igyi i . i ioci igyi i . i iayi igyi i . i imوi imyi i . i iabi imyi i . i iali imyi i . i ioci imyi i . i iayi imyi i . i igsi imyi i . i iabi igوi i . i iali igوi i . i ioci igوi i . i iayi igوi i . i igsi igوi i . i iabi iuوi i . i iali iuوi i . i ioci iuوi i . i iayi iuوi i . i igsi iuوi i . i iowi iuوi i . i iali iuمi i . i ioci iuمi i . i iayi iuمi i . i igsi iuمi i . i iowi iuمi i . i iali iuشi i . i ioci iuشi i . i iayi iuشi i . i igsi iuشi i . i iowi iuشi i . i iuwi iuشi i . i ioci ioشi i . i iayi ioشi i . i igsi ioشi i . i iowi ioشi i . i iuwi ioشi i . i ioci iovi i . i iayi iovi i . i igsi iovi i . i iowi iovi i . i iuwi iovi i . i igwi iovi i . i iayi irwi i . i igsi irwi i . i iowi irwi i . i iuwi irwi i . i igwi irwi i . i iayi ioqi i . i igsi ioqi i . i iowi ioqi i . i iuwi ioqi i . i igwi ioqi i . i iuqi ioqi i . i igsi irqi i . i iowi irqi i . i iuwi irqi i . i igwi irqi i . i iuqi irqi i . i igsi iodi i . i iowi iodi i . i iuwi iodi i . i igwi iodi i . i iuqi iodi i . i igqi iodi i . i iowi ibdi i . i iuwi ibdi i . i igwi ibdi i . i iuqi ibdi i . i igqi ibdi i . i iowi irci i . i iuwi irci i . i igwi irci i . i iuqi irci i . i igqi irci i . i imdi irci i . i iuwi ibci i







iani . itni . ithi . iehi . itoi . ieoi . iegi . ingi . ieui . inui . iemi . inmi . ihmi . inri . ihri . inbi . ihbi . iobi . ihli . ioli . ihyi . ioyi . igyi . ihsi . iosi . igsi . iowi . igwi . iuwi . iovi . igvi . iuvi . igوi . iuوi . imوi . igqi . iuqi . imqi . iuci . imci . irci . iuمi . imمi . irمi . imdi . irdi . ibdi . imشi . irشi . ibشi . irيi









"""




#text = "hello . i am here "




i_semaphore_of_video_0_i = True





i_t_0_i = time.time()





i_file_0_i = os.path.join(cwd, "i_file_of_text_of_result_3_i.txt")



'''



with open(i_file_0_i, "r") as f_:
    
    
    text = f_.read(os.path.getsize(i_file_0_i))
    
    


'''



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










import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

import imageio_ffmpeg

import arabic_reshaper
from bidi.algorithm import get_display




word = "مرحبا"

print("قبل:", word)

reshaped = arabic_reshaper.reshape(word)

print("بعد reshaper:", reshaped)

display_word = get_display(reshaped)

print("بعد bidi:", display_word)










groups = parts




if (i_semaphore_of_video_0_i == False):

    
    
    
    i_counter_0_i = 0
    
    
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
    
    
    
else:
    
    
    from gtts import gTTS
    from pydub import AudioSegment
    import os
    
    
    
    
    word_audio_data = []
    
    
    
    
    audio = AudioSegment.empty()
    
    for i, (text_part, lang) in enumerate(groups):
    
        try:
    
            filename = os.path.join(
                cwd,
                f"part_{i}.mp3"
            )
    
            print(
                f"{i} . {lang}: {text_part}"
            )
    
            tts = gTTS(
                text=text_part,
                lang=lang
            )
    
            tts.save(filename)
    
            segment = AudioSegment.from_mp3(filename)
    
            # مدة الكلمة بالثواني
            duration = len(segment) / 1000.0
    
            # بداية الكلمة داخل الملف النهائي
            start_time = len(audio) / 1000.0
    
            # نهاية الكلمة
            end_time = start_time + duration
    
            word_audio_data.append(
                {
                    "word": text_part,
                    "lang": lang,
                    "start": start_time,
                    "end": end_time,
                    "duration": duration,
                }
            )
    
            audio += segment
    
            os.remove(filename)
    
        except Exception as e:
    
            print(
                f"ERROR while creating audio for {text_part}: {e}"
            )
    
    
    # حفظ الصوت النهائي
    audio_file = os.path.join(
        cwd,
        "i_output_0_i.mp3"
    )
    
    audio.export(
        audio_file,
        format="mp3"
    )
    
    
    print(
        f"Audio created: {audio_file}"
    )
    
    
    
    
    
    
    print("\nWORD TIMELINE:\n")
    
    for item in word_audio_data:
    
        print(
            f"{item['word']} "
            f"{item['start']:.3f}s -> "
            f"{item['end']:.3f}s"
        )
        
        
    
    
    import cv2
    import numpy as np
    from PIL import Image, ImageDraw, ImageFont
    
    import imageio_ffmpeg
    
    import arabic_reshaper
    from bidi.algorithm import get_display
    
    
    
    i_background_video_0_i = os.path.join(
        cwd,
        "i_background_0_i.mp4"
    )
    
    i_video_without_audio_0_i = os.path.join(
        cwd,
        "i_video_without_audio_0_i.mp4"
    )
    
    i_video_final_0_i = os.path.join(
        cwd,
        "i_video_final_0_i.mp4"
    )
    
    
    def prepare_text_for_display(text):
    
        try:
    
            reshaped_text = arabic_reshaper.reshape(
                text
            )
            
            #bidi_text = get_display(
                #reshaped_text
            #)
    
            return reshaped_text
    
        except:
    
            return text
    
    
    
    
    def find_font():
    
        i_font_list_0_i = [
    
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    
            "/usr/share/fonts/truetype/freefont/FreeSans.ttf",
            
            
            "C:/Windows/Fonts/arial.ttf",
    
            "C:/Windows/Fonts/Arial.ttf",
    
        ]
    
        for i_font_0_i in i_font_list_0_i:
    
            if os.path.exists(i_font_0_i):
    
                return i_font_0_i
    
        return None
    
    
    i_font_path_0_i = find_font()
    
    
    if i_font_path_0_i is None:
    
        raise Exception(
            "لم أجد خطًا مناسبًا على الجهاز."
        )
    
    
    
    
    def draw_word(
        frame,
        word,
        progress,
        font_path
    ):
    
        height, width = frame.shape[:2]
    
        image = Image.fromarray(
            cv2.cvtColor(
                frame,
                cv2.COLOR_BGR2RGB
            )
        )
    
        draw = ImageDraw.Draw(
            image
        )
    
        font_size = int(
            min(width, height) * 0.10
        )
    
        font = ImageFont.truetype(
            font_path,
            font_size
        )
    
        display_word = prepare_text_for_display(
            word
        )
    
        # الحصول على حجم الكلمة
        bbox = draw.textbbox(
            (0, 0),
            display_word,
            font=font
        )
    
        word_width = bbox[2] - bbox[0]
        word_height = bbox[3] - bbox[1]
    
        # البداية: خارج الشاشة من الأعلى
        start_y = -word_height
    
        # النهاية: أسفل الشاشة
        end_y = height - word_height - 50
    
        # الموضع الرأسي الحالي
        y = (
            start_y
            +
            (end_y - start_y)
            *
            progress
        )
    
        # المنتصف أفقيًا
        x = (
            width - word_width
        ) // 2
    
        # ظل للكلمة
        draw.text(
            (
                x + 4,
                y + 4
            ),
            display_word,
            font=font,
            fill=(0, 0, 0)
        )
    
        # الكلمة
        draw.text(
            (
                x,
                y
            ),
            display_word,
            font=font,
            fill=(255, 255, 255)
        )
    
        return cv2.cvtColor(
            np.array(image),
            cv2.COLOR_RGB2BGR
        )
    
    
    
    
    import cv2
    import numpy as np
    from PIL import Image, ImageDraw, ImageFont
    
    def create_black_text_video(
        word_audio_data,
        output_video,
        font_path,
        width=1080,
        height=1920,
        fps=30
    ):
    
        # مدة الصوت كله
        total_duration = word_audio_data[-1]["end"]
    
        total_frames = int(
            total_duration * fps
        )
    
        fourcc = cv2.VideoWriter_fourcc(
            *"mp4v"
        )
    
        out = cv2.VideoWriter(
            output_video,
            fourcc,
            fps,
            (width, height)
        )
    
        word_index = 0
    
        for frame_number in range(total_frames):
    
            current_time = frame_number / fps
    
            # خلفية سوداء
            frame = np.zeros(
                (height, width, 3),
                dtype=np.uint8
            )
    
            # الانتقال إلى الكلمة الحالية
            while (
                word_index < len(word_audio_data) - 1
                and
                current_time >= word_audio_data[word_index]["end"]
            ):
                word_index += 1
    
            current_word = word_audio_data[word_index]
    
            start = current_word["start"]
            end = current_word["end"]
    
            duration = end - start
    
            if duration > 0:
    
                progress = (
                    current_time - start
                ) / duration
    
            else:
    
                progress = 1.0
    
            progress = max(
                0.0,
                min(1.0, progress)
            )
    
            # إضافة الكلمة البيضاء
            frame = draw_word(
                frame,
                current_word["word"],
                progress,
                font_path
            )
    
            out.write(frame)
    
        out.release()
    
        print(
            f"Video created successfully: {output_video}"
        )
    
    
    
    
    
    i_video_without_audio_0_i = os.path.join(
        cwd,
        "i_video_without_audio_0_i.mp4"
    )
    
    create_black_text_video(
        word_audio_data=word_audio_data,
        output_video=i_video_without_audio_0_i,
        font_path=i_font_path_0_i,
        width=1080,
        height=1920,
        fps=30
    )
    
    
    
    i_ffmpeg_0_i = imageio_ffmpeg.get_ffmpeg_exe()
    
    
    command = [
    
        i_ffmpeg_0_i,
    
        "-y",
    
        "-i",
        i_video_without_audio_0_i,
    
        "-i",
        audio_file,
    
        "-c:v",
        "copy",
    
        "-c:a",
        "aac",
    
        "-b:a",
        "192k",
    
        "-shortest",
    
        i_video_final_0_i,
    ]
    
    
    subprocess.run(
        command,
        check=True
    )
    
    
    print(
        "\n\n"
        "====================================\n"
        "VIDEO CREATED SUCCESSFULLY\n"
        "====================================\n"
    )
    
    print(
        i_video_final_0_i
    )
    




i_t_1_i = time.time()


print(f"time = {i_t_1_i - i_t_0_i} second .")












    
    
        
        
        
        
        
        
    
    
    
    








