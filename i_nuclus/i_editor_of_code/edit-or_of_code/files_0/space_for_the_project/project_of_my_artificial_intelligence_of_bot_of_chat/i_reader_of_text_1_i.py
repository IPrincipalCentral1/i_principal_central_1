
















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











"""





i_semaphore_of_video_0_i = True





i_t_0_i = time.time()





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
    
            bidi_text = get_display(
                reshaped_text
            )
    
            return bidi_text
    
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












    
    
        
        
        
        
        
        
    
    
    
    








