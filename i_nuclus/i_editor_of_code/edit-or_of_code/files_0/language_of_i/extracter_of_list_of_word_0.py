











'''



i want :

    NOUN

    VERB
    
    ADJ
    
    ADV
    
    question

pos_tags = {

    'NOUN': wn.NOUN,

    'VERB': wn.VERB,

    'ADJECTIVE': wn.ADJ,

    'ADVERB': wn.ADV

}



'''






list_of_word = []






import os


cwd = os.path.dirname(os.path.abspath(__file__))







list_of_liberary_to_install = [

                            ["spacy"] ,
                            
                            
                            ["nltk"] ,
                            
                            


]











import traceback

import sys


import subprocess





try:
    
    counter_0 = 0
    
    
    while (counter_0 < len(list_of_liberary_to_install)):
    

                
        try:
        
        
            print(f"\n\n\npip install {list_of_liberary_to_install[counter_0][0]}\n\n\n")
            
            
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
    
    








import spacy.cli



spacy.cli.download("en_core_web_sm")




import nltk



nltk.download('wordnet')





from nltk.corpus import wordnet as wn

import spacy


from collections import defaultdict





nlp = spacy.load("en_core_web_sm")

vocab = nlp.vocab

question_words_by_tag = defaultdict(set)

# نمر على كل الكلمات في vocab
for lexeme in vocab:
    if lexeme.is_alpha and lexeme.is_lower:
        # تحليل الكلمة كجملة
        doc = nlp(lexeme.text)
        token = doc[0]
        if token.tag_ in {"WP", "WRB", "WP$", "WDT"}:
            question_words_by_tag[token.tag_].add(token.text.lower())




# تحويل النتيجة إلى dict جاهز للطباعة





list_0 = [[tag, list(sorted(words))] for tag, words in question_words_by_tag.items()]



list_of_word.extend(list_0)



result = {tag: sorted(words) for tag, words in question_words_by_tag.items()}






print(f"result = {result} .")




# تأكد من تحميل WordNet





# نوع الكلمات المراد استخراجها


pos_tags = {

    'NOUN': wn.NOUN,

    'VERB': wn.VERB,

    'ADJECTIVE': wn.ADJ,

    'ADVERB': wn.ADV

}

# تجميع الكلمات لكل نوع
for label, pos in pos_tags.items():
    print(f"\n🔹 كل الكلمات من نوع {label}:\n{'-'*40}")
    
    words = set()
    for synset in wn.all_synsets(pos=pos):
        for lemma in synset.lemmas():
            words.add(lemma.name())

    # تحويل إلى قائمة وفرزها
    
    words = sorted(words)

    # طباعة أول 50 كلمة فقط كمثال (اختياري)
    
    list_of_word.append([label, list(words)])
    
    for word in words[:50]:
        
        print(word)
    
    print(f"\n✅ العدد الكلي للكلمات من نوع {label}: {len(words)}\n")







file_0 = os.path.join(os.getcwd(), "space_0", "space_of_language_2", "list_of_word.txt")



with open(file_0, "w") as f_:

    counter_0 = 0
    
    
    while (counter_0 < len(list_of_word)):
    
    
        element = list_of_word[counter_0]
        
        f_.write(f"{element[0]} :\n")
        
        
        counter_1 = 0
        
        while (counter_1 < len(element[1])):
        
            
            f_.write(f"    {element[1][counter_1]}\n")
    
    
            print(f"counter_1 = {counter_1} . element[0] = {element[0]} . element[1][counter_1] = {element[1][counter_1]}")
        
            counter_1 += 1
    
        counter_0 += 1












