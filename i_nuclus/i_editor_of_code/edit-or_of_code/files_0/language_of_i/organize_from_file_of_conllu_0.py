















import os





import os
import re

def parse_conllu_file(filepath):
    sentences = []  # قائمة الجمل، كل جملة عبارة عن dict فيه: comments, tokens
    comments = []
    tokens = []

    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()

            if not line:
                if tokens or comments:
                    sentences.append({
                        "comments": comments,
                        "tokens": tokens
                    })
                    comments = []
                    tokens = []
                continue

            if line.startswith("#"):
                comments.append(line)
                continue

            parts = line.split('\t')
            if len(parts) != 10:
                continue

            token_data = {
                "id": parts[0],
                "form": parts[1],
                "lemma": parts[2],
                "upos": parts[3],
                "xpos": parts[4],
                "feats": parts[5],
                "head": parts[6],
                "dep": parts[7],
                "misc": parts[9]
            }

            # استخراج معلومات من misc
            misc_info = {}
            for field in token_data["misc"].split('|'):
                if '=' in field:
                    key, value = field.split('=', 1)
                    misc_info[key] = value

            token_data["gloss"] = misc_info.get("Gloss")
            token_data["root"] = misc_info.get("Root")

            tokens.append(token_data)

        # إضافة آخر جملة إن وجدت
        if tokens or comments:
            sentences.append({
                "comments": comments,
                "tokens": tokens
            })

    return sentences


def print_conllu_info(sentences, file):


    content = ""

    for i, sentence_data in enumerate(sentences):
        #print(f"\n🔹 الجملة رقم {i + 1}:")
        
        content += f"\n sentence {i + 1} :\n"

        for comment in sentence_data["comments"]:
            content += f"    - comment : {comment}\n"

        for token in sentence_data["tokens"]:
            content += f"  - form : [{token['form']}]\n"
            
            content += f"    - upos : ({token['upos']})\n"
            
            content += f"    - Lemma : {token['lemma']}\n"
            
            content += f"    - POS : {token['upos']}\n"
            
            content += f"    - Feats : {token['feats']}\n"
            
            content += f"    - Dep : {token['dep']}\n"
            
            content += f"    - Head_ID: {token['head']}\n"
            
            if token['gloss'] or token['root']:
                
                content += f"    - Root : {token['root']}\n"
                
                content += f"    - Gloss : {token['gloss']}\n"
        

    with open(file, "w") as f_:
    
        f_.write(content)





duplication_place = os.path.join(os.getcwd(), "space_0", "space_of_language_1")





place_0 = os.path.join(os.getcwd(), "space_of_language_0")


dirs = []



for root, dirs, files in os.walk(place_0):

    break
    
    




counter_3 = 0


while (counter_3 < len(dirs)):



    
    
    
    
    folder_of_source = os.path.join(os.getcwd(), "space_of_language_0", "new_folder_" + str(counter_3))
    
    
    
    
    
    
    
    dirs = [""]
    
    srcs = [""]
    
    
    
    
    counter_0 = 0
    
    while (counter_0 < len(dirs)):
    
        for root, dirs_, files in os.walk(os.path.join(folder_of_source, dirs[counter_0])):
    
            break
    
    
    
        counter_1 = 0
    
        while (counter_1 < len(dirs_)):
    
            dirs.append(os.path.join(dirs[counter_0], dirs_[counter_1]))
    
            srcs.append(os.path.join(srcs[counter_0], dirs_[counter_1]))
    
            counter_1 += 1
    
            
        src_ = os.path.join(folder_of_source, srcs[counter_0])
        
        dist_ = os.path.join(duplication_place, dirs[counter_0])
    

        counter_1 = 0
    
        while (counter_1 < len(files)):
    
            try:
    
    
    
                if (files[counter_1].endswith(".conllu")):
                    
                    sentences = parse_conllu_file(os.path.join(src_, files[counter_1]))
                    
                    print_conllu_info(sentences, file=os.path.join(duplication_place, files[counter_1].split(".conllu")[0] + ".txt"))
                    
    
                    print(f"file = {files[counter_1]}")
     
    
            except:
    
                            
                traceback.print_exc()
                
                error = traceback.format_exc()
                
                semaphore = True
    
                print(f"Erreur : {str(error)}")
    
    
    
            
            counter_1 += 1
    
    
        counter_0 += 1
    
    
    

    counter_3 += 1

















