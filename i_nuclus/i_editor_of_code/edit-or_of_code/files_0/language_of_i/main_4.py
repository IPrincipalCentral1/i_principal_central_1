











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

# تحميل النموذج

nlp = spacy.load("en_core_web_sm")



# نجرب تمرير الكثير من الجمل لتجميع كل الكلمات التي تعرفها spaCy وتُصنفها بـ tag_ = WP أو WRB
# لكن مكتبة spaCy لا توفر مباشرة قائمة بكل الكلمات المعرفة داخلياً مع tag_.
# الحل البديل: نستخدم مفردات اللغة الإنجليزية المخزنة في النموذج + فلترة حسب التحليل النحوي.

# نبدأ بالوصول إلى مفردات النموذج


vocab = nlp.vocab


# سنجمع الكلمات التي لو تم تمريرها ستحصل على tag_ من نوع WH

question_words_by_tag = defaultdict(set)


# نمر على كل كلمة موجودة في الـ vocab

for lexeme in vocab:

    if lexeme.is_alpha and lexeme.has_vector:
        # نحلل الكلمة كجملة مفردة
        doc = nlp(lexeme.text)
        token = doc[0]
        if token.tag_ in {"WP", "WRB", "WP$", "WDT"}:
            question_words_by_tag[token.tag_].add(token.text.lower())

# نحول النتيجة إلى قائمة لعرضها
result = {tag: sorted(list(words)) for tag, words in question_words_by_tag.items()}






print(f"result = {result} .")























