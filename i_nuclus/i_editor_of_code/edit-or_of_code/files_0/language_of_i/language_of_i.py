













The → DET




import subprocess

# تحميل النموذج en_core_web_sm باستخدام الأمر system
subprocess.run(["python3", "-m", "spacy", "download", "en_core_web_sm"])



import os


os.system("pip install spacy")




import spacy.cli

spacy.cli.download("en_core_web_sm")



from nltk.corpus import wordnet as wn

import nltk


from nltk.corpus import wordnet as wn





# for derivative related forms


'''

example :

    perfect -> perfecting



استخراج المشتقات الدلالية:

مثال لاشتقاق اسم أو فعل من صفة:



'''


adj = wn.synsets('perfect', pos=wn.ADJ)[0]
lemmas = adj.lemmas()

for lemma in lemmas:
    derivs = lemma.derivationally_related_forms()
    for d in derivs:
        print(f"{lemma.name()} → {d.name()} ({d.synset().pos()})")






# تأكد من تحميل WordNet
nltk.download('wordnet')

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






# الكود: الحصول على تصريفات كل فعل من WordNet

import spacy
import nltk
from nltk.corpus import wordnet as wn

# تحميل الموارد
nltk.download('wordnet')
nlp = spacy.load("en_core_web_sm")

# تجميع الأفعال من WordNet
lemmas = set()
for synset in wn.all_synsets(pos=wn.VERB):
    for lemma in synset.lemmas():
        lemmas.add(lemma.name())

# الحصول على التصريفات المختلفة
verb_forms = {}

for lemma in sorted(lemmas):
    doc = nlp(lemma)
    token = doc[0]
    # استخدام pyinflect للحصول على التصريفات
    forms = {
        "base": lemma,
        "3rd_person_singular": token._.inflect("VBZ"),
        "past": token._.inflect("VBD"),
        "past_participle": token._.inflect("VBN"),
        "present_participle": token._.inflect("VBG"),
        "present_plural": token._.inflect("VBP"),
    }
    verb_forms[lemma] = forms

# طباعة عينة
import random
sample = random.sample(list(verb_forms.items()), 10)
for base, forms in sample:
    print(forms)








#  الكود: الحصول على تصريفات كل فعل من WordNet

import spacy
import nltk
from nltk.corpus import wordnet as wn

# تحميل الموارد
nltk.download('wordnet')
nlp = spacy.load("en_core_web_sm")

# تجميع الأفعال من WordNet
lemmas = set()
for synset in wn.all_synsets(pos=wn.VERB):
    for lemma in synset.lemmas():
        lemmas.add(lemma.name())

# الحصول على التصريفات المختلفة
verb_forms = {}

for lemma in sorted(lemmas):
    doc = nlp(lemma)
    token = doc[0]
    # استخدام pyinflect للحصول على التصريفات
    forms = {
        "base": lemma,
        "3rd_person_singular": token._.inflect("VBZ"),
        "past": token._.inflect("VBD"),
        "past_participle": token._.inflect("VBN"),
        "present_participle": token._.inflect("VBG"),
        "present_plural": token._.inflect("VBP"),
    }
    verb_forms[lemma] = forms

# طباعة عينة
import random
sample = random.sample(list(verb_forms.items()), 10)
for base, forms in sample:
    print(forms)










#  اشتقاق الأشكال الأخرى باستخدام spaCy و pyinflect

import spacy
import pyinflect

# تحميل نموذج spaCy
nlp = spacy.load("en_core_web_sm")

# وظيفة لاشتقاق صيغ أخرى
def get_derivatives(word):
    doc = nlp(word)
    token = doc[0]
    
    # صيغة حال adverb (عادة بإضافة -ly)
    adverb = word + 'ly' if not word.endswith('ly') else word

    # محاولة اشتقاق الفعل إن أمكن
    verb_ing = token._.inflect("VBG")
    verb_past = token._.inflect("VBD")

    return {
        "adjective": word,
        "adverb": adverb,
        "verb_present_participle": verb_ing,
        "verb_past": verb_past,
    }

# تجربة على مجموعة من الصفات
results = {}
for adj in sorted(list(adjectives))[:100]:  # مثلاً أول 100 صفة فقط للتجربة
    results[adj] = get_derivatives(adj)

# طباعة مثال
from pprint import pprint
pprint(results['perfect'])







'''

المكونات الأساسية لـ WordNet:
1. Synset (مجموعة مرادفات):

كل Synset هو مجموعة من الكلمات تشترك في نفس المعنى، ويحتوي أيضًا على تعريف وتعابير استخدام.

مثال:

'''


from nltk.corpus import wordnet as wn

syn = wn.synsets('run', pos=wn.VERB)[0]

print(syn.name())        # run.v.01

print(syn.definition())  # move fast by using one's feet

print(syn.examples())    # ['Don't run--you'll be out of breath']




'''
 Lemmas (الكلمات):

كل synset يحتوي على واحدة أو أكثر من lemmas (الكلمات الأصلية).


'''



for lemma in syn.lemmas():
    print(lemma.name())
# output: run, go, move









'''

تفضل، إليك سكربت Python باستخدام مكتبة nltk وwordnet، يقوم بطباعة جميع الكلمات الممكنة في WordNet مصنّفة حسب نوعها:
✅ السكربت الكامل:



'''



from nltk.corpus import wordnet as wn
import nltk

# تأكد من تحميل WordNet
nltk.download('wordnet')

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







'''

اعطني مثال يشمل كل هاذا : .hypernyms()    العلاقة العليا    dog → animal
.hyponyms()    العلاقة الجزئية    animal → dog, cat, horse...
.instance_hypernyms()    علاقة "نوع من..." كاسم علم    Einstein → physicist
.member_holonyms()    علاقة الكل (عضو في مجموعة)    tree → forest
.part_meronyms()    علاقة جزء من شيء    wheel → car
ChatGPT said:

رائع! إليك مثالًا شاملًا يغطي كل هذه العلاقات الدلالية باستخدام nltk.corpus.wordnet، وكل جزء فيه مشروح بسطر واضح لتتعلم بالضبط ما يحصل.
🧪 السكربت الكامل: WordNet مع كل العلاقات المطلوبة


'''



from nltk.corpus import wordnet as wn
import nltk

# تأكد من تحميل WordNet
nltk.download('wordnet')

# أمثلة كلمات لاستخدام العلاقات المختلفة
examples = {
    'hypernyms': ('dog', wn.NOUN),
    'hyponyms': ('animal', wn.NOUN),
    'instance_hypernyms': ('Einstein', wn.NOUN),
    'member_holonyms': ('tree', wn.NOUN),
    'part_meronyms': ('wheel', wn.NOUN),
}

print("="*60)
for relation, (word, pos) in examples.items():
    synsets = wn.synsets(word, pos=pos)
    if not synsets:
        print(f"{word}: ❌ لا يوجد synsets")
        continue

    syn = synsets[0]  # نستخدم أول synset فقط للتبسيط
    print(f"\n🔹 {relation.upper()} — كلمة: {word} ({syn.name()})")
    print(f"   📝 التعريف: {syn.definition()}")

    if relation == 'hypernyms':
        results = syn.hypernyms()
    elif relation == 'hyponyms':
        results = syn.hyponyms()
    elif relation == 'instance_hypernyms':
        results = syn.instance_hypernyms()
    elif relation == 'member_holonyms':
        results = syn.member_holonyms()
    elif relation == 'part_meronyms':
        results = syn.part_meronyms()
    else:
        results = []

    if not results:
        print("   ⚠️ لا توجد نتائج لهذه العلاقة.")
    else:
        for rel in results:
            print(f"   ➤ {rel.name()} — {rel.definition()}")
print("="*60)









'''


رائع! إليك مثالًا كاملًا في Python يوضح كيفية استخراج:

    ✅ جمل مثال على الكلمة باستخدام synset.examples()

    ✅ مضادات الكلمة (antonyms) باستخدام lemma.antonyms()

✅ السكربت الكامل:



'''


from nltk.corpus import wordnet as wn
import nltk

# تحميل WordNet
nltk.download('wordnet')

# الكلمة المراد اختبارها
word = "good"
pos = wn.ADJ  # يمكن تغييره إلى wn.NOUN أو wn.VERB أو wn.ADV

# جلب أول Synset للكلمة
synsets = wn.synsets(word, pos=pos)

if not synsets:
    print(f"❌ لم يتم العثور على Synset للكلمة: {word}")
else:
    syn = synsets[0]
    print(f"🔹 الكلمة: {word}")
    print(f"🔸 Synset: {syn.name()}")
    print(f"📝 التعريف: {syn.definition()}")

    # 1. ✅ أمثلة على استخدام الكلمة في جمل
    examples = syn.examples()
    if examples:
        print("\n🗣️ أمثلة:")
        for ex in examples:
            print(f"   ➤ {ex}")
    else:
        print("\n⚠️ لا توجد أمثلة لهذه الكلمة.")

    # 2. ✅ مضادات الكلمة (antonyms)
    print("\n🔁 مضادات الكلمة (Antonyms):")
    found_antonyms = False
    for lemma in syn.lemmas():
        antonyms = lemma.antonyms()
        if antonyms:
            found_antonyms = True
            for ant in antonyms:
                print(f"   ➤ {lemma.name()} ↔ {ant.name()}")
    if not found_antonyms:
        print("   ⚠️ لا توجد مضادات مسجلة لهذه الكلمة.")

































