















import os



os.system("pip install nltk")


os.system("pip install spacy")


os.system("pip install spacy-wordnet")


os.system("pip install spacy-wordnet")




import nltk

# تحميل wordnet و omw-1.4 من داخل الكود

nltk.download('wordnet')

nltk.download('omw-1.4')






import spacy.cli

# تحميل النموذج


spacy.cli.download("en_core_web_sm")




'''

pip install nltk
pip install spacy
pip install spacy-wordnet
python -m nltk.downloader wordnet omw-1.4
python -m spacy download en_core_web_sm




'''







from nltk.corpus import wordnet as wn






from nltk.corpus import wordnet as wn
from collections import defaultdict



def func():

    word_definitions = defaultdict(set)
    
    # مرّ على كل الـ synsets في WordNet
    for synset in wn.all_synsets():
        
        
        #definition = synset.definition()
    
    
    
        
        # لكل lemma (كلمة) في synset
        for lemma in synset.lemmas():
            word = lemma.name().lower()
            
            
            
            
            word_definitions[word].add(definition)
    
    
    
    # تحويل المجموعات إلى قوائم
    
    word_definitions = {word: list(defs) for word, defs in word_definitions.items()}
    
    
    
    word_with_definition = [[word, sorted(list(defs))] for word, defs in word_definitions.items()]
    
    
    
    word_with_definition = sort_element_0_0(l=word_with_definition)
    
    





def show_relations(word):
    synsets = wn.synsets(word)
    if not synsets:
        print("لا توجد synsets لهذه الكلمة.")
        return

    for syn in synsets:
        print(f"\nSynset: {syn.name()}")
        print(f"  تعريف: {syn.definition()}")
        
        # العلاقات
        print(f"  🔷 (أسماء مفرطة) Hypernyms: {[s.name() for s in syn.hypernyms()]}")
        print(f"  🔷 (الترادفات) Hyponyms: {[s.name() for s in syn.hyponyms()]}")
        print(f"  🔷 (أسماء مفرطة للمثيلات) Instance Hypernyms: {[s.name() for s in syn.instance_hypernyms()]}")
        print(f"  🔷 (أمثلة على المرادفات) Instance Hyponyms: {[s.name() for s in syn.instance_hyponyms()]}")
        print(f"  🔷 (أسماء الأعضاء المتجانسة) Member Holonyms: {[s.name() for s in syn.member_holonyms()]}")
        print(f"  🔷 (جزء من الكلمات المتجانسة) Part Holonyms: {[s.name() for s in syn.part_holonyms()]}")
        print(f"  🔷 (مرادفات المادة) Substance Holonyms: {[s.name() for s in syn.substance_holonyms()]}")
        print(f"  🔷 (أسماء الأعضاء) Member Meronyms: {[s.name() for s in syn.member_meronyms()]}")
        print(f"  🔷 (مرادفات الأجزاء) Part Meronyms: {[s.name() for s in syn.part_meronyms()]}")
        print(f"  🔷 (مرادفات المواد) Substance Meronyms: {[s.name() for s in syn.substance_meronyms()]}")
        print(f"  🔷 (انظر أيضا) Also See: {[s.name() for s in syn.also_sees()]}")
        print(f"  🔷 (مشابه ل) Similar To: {[s.name() for s in syn.similar_tos()]}")


        print("-" * 10)
        
        print("-" * 10)
        
        print("-" * 10)

        print(f"  🔷 (الترادفات) Hyponyms: {[s.name() for s in syn.hyponyms()]}")


        print("-" * 10)
        
        print("-" * 10)

        print(f"  🔷 (مرادفات الأجزاء) Part Meronyms: {[s.name() for s in syn.part_meronyms()]}")


        print("-" * 10)
        
        print("-" * 10)
        
        print("-" * 10)



show_relations("fish")





