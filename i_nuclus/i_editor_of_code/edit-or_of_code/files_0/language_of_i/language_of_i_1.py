















import os


import re

def parse_conllu_file(filepath):
    sentences = []
    with open(filepath, 'r', encoding='utf-8') as f:
        sentence = []
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                if sentence:
                    sentences.append(sentence)
                    sentence = []
                continue
            parts = line.split('\t')
            if len(parts) != 10:
                continue  # skip malformed lines
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

            # استخراج خصائص إضافية من misc
            misc_info = {}
            for field in token_data["misc"].split('|'):
                if '=' in field:
                    key, value = field.split('=', 1)
                    misc_info[key] = value
            token_data["gloss"] = misc_info.get("Gloss")
            token_data["root"] = misc_info.get("Root")

            sentence.append(token_data)
        if sentence:
            sentences.append(sentence)
    return sentences

def print_conllu_info(sentences):
    for i, sent in enumerate(sentences):
        print(f"\n🔹 الجملة رقم {i+1}:")
        for token in sent:
            print(f"🔸 [{token['form']}]  ({token['upos']})")
            print(f"   ↳ Lemma: {token['lemma']}")
            print(f"   ↳ POS: {token['upos']}")
            print(f"   ↳ Feats: {token['feats']}")
            print(f"   ↳ Dep: {token['dep']} → Head ID: {token['head']}")
            if token['gloss'] or token['root']:
                print(f"   ↳ Root: {token['root']} | Gloss: {token['gloss']}")
            print("")


        if (i > 10):
        
            break


# 🟡 ضع هنا مسار ملف .conllu الذي لديك:





file_path = os.path.join(os.getcwd(), "space_0", "ar_padt-ud-dev.conllu")


sentences = parse_conllu_file(file_path)


print_conllu_info(sentences)
















