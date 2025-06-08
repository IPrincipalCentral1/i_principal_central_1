















import os


#import re

#def parse_conllu_file(filepath):

    #list_of_text = []

    #list_of_small_text = []


    #sentences = []
    #with open(filepath, 'r', encoding='utf-8') as f:
        #sentence = []


        #for line in f:
            #line = line.strip()



            #if not line or line.startswith('#'):

                #list_of_small_text.append(line)

                #if sentence:
                    #sentences.append(sentence)
                    #sentence = []
                #continue



            #list_of_text.append([0])



            ##list_of_text[-1].extend(list_of_small_text)


            ##list_of_small_text = []

            #while (len(list_of_small_text) > 0):


                #list_of_text[-1].append(list_of_small_text[0])

                #list_of_small_text.pop(0)

            #parts = line.split('\t')
            #if len(parts) != 10:
                #continue  # skip malformed lines
            #token_data = {
                #"id": parts[0],
                #"form": parts[1],
                #"lemma": parts[2],
                #"upos": parts[3],
                #"xpos": parts[4],
                #"feats": parts[5],
                #"head": parts[6],
                #"dep": parts[7],
                #"misc": parts[9]
            #}

            ## استخراج خصائص إضافية من misc
            #misc_info = {}
            #for field in token_data["misc"].split('|'):
                #if '=' in field:
                    #key, value = field.split('=', 1)
                    #misc_info[key] = value
            #token_data["gloss"] = misc_info.get("Gloss")
            #token_data["root"] = misc_info.get("Root")

            #sentence.append(token_data)
        #if sentence:
            #sentences.append(sentence)

            #sentence = []

    #return sentences, list_of_text

#def print_conllu_info(sentences):
    #for i, sent in enumerate(sentences[0]):
        #print(f"\n🔹 الجملة رقم {i+1}:")

        #counter_0 = 0

        #while ((i < len(sentences[1])) and (counter_0 < len(sentences[1][i]))):

            #print(f"sentences[1][i][counter_0] = {sentences[1][i][counter_0]}")

            #counter_0 += 1


        #for token in sent:
            #print(f"🔸 [{token['form']}]  ({token['upos']})")
            #print(f"   ↳ Lemma: {token['lemma']}")
            #print(f"   ↳ POS: {token['upos']}")
            #print(f"   ↳ Feats: {token['feats']}")
            #print(f"   ↳ Dep: {token['dep']} → Head ID: {token['head']}")
            #if token['gloss'] or token['root']:
                #print(f"   ↳ Root: {token['root']} | Gloss: {token['gloss']}")
            #print("")

        #print(f"\n\n\n i = {i} .\n\n\n")


        #if (i > 1):

            #break


## 🟡 ضع هنا مسار ملف .conllu الذي لديك:





#file_path = os.path.join(os.getcwd(), "space_0", "ar_padt-ud-dev.conllu")


#sentences = parse_conllu_file(file_path)


#print_conllu_info(sentences)



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


def print_conllu_info(sentences):


    content = ""

    for i, sentence_data in enumerate(sentences):
        print(f"\n🔹 الجملة رقم {i + 1}:")
        
        content += f"\n sentence {i + 1} :\n"

        for comment in sentence_data["comments"]:
            content += f"    - comment : {comment}\n"

        for token in sentence_data["tokens"]:
            content += f"  - form : [{token['form']}]\n"
            
            content += "    - upos : ({token['upos']})\n"
            
            content += f"    - Lemma : {token['lemma']}\n"
            
            content += f"    - POS : {token['upos']}\n"
            
            content += f"    - Feats : {token['feats']}\n"
            
            content += f"    - Dep : {token['dep']}\n"
            
            content += f"    - Head_ID: {token['head']}\n"
            
            if token['gloss'] or token['root']:
                
                content += f"    - Root : {token['root']}\n"
                
                content += f"    - Gloss : {token['gloss']}\n"
                
                
            #print("")

        #print(f"\n-----------------------------\n")

        if i > 1:
            break



    file = os.path.join(os.getcwd(), "space_0", "information.txt")

    with open(file, "w") as f_:
    
        f_.write(content)


# 🟡 ضع هنا مسار ملف .conllu الذي لديك:
file_path = os.path.join(os.getcwd(), "space_0", "ar_padt-ud-dev.conllu")

sentences = parse_conllu_file(file_path)
print_conllu_info(sentences)













