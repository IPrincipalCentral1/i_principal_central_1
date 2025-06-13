











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








import os


os.system("pip install spacy")


os.system("pip install nltk")







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
    for word in words[:50]:
        
        print(word)
    
    print(f"\n✅ العدد الكلي للكلمات من نوع {label}: {len(words)}\n")
























