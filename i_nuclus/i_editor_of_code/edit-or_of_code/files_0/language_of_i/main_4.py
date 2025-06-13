











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








import subprocess

# تحميل النموذج en_core_web_sm باستخدام الأمر system
subprocess.run(["python3", "-m", "spacy", "download", "en_core_web_sm"])





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

# عرض النتائج
for tag, words in result.items():
    print(f"{tag}: {words}")






print(f"result = {result} .")























