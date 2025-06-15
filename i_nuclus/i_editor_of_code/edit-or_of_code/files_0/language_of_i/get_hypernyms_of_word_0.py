















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

def show_relations(word):
    synsets = wn.synsets(word)
    if not synsets:
        print("لا توجد synsets لهذه الكلمة.")
        return

    for syn in synsets:
        print(f"\nSynset: {syn.name()}")
        print(f"  تعريف: {syn.definition()}")
        
        # العلاقات
        print(f"  🔷 Hypernyms: {[s.name() for s in syn.hypernyms()]}")
        print(f"  🔷 Hyponyms: {[s.name() for s in syn.hyponyms()]}")
        print(f"  🔷 Instance Hypernyms: {[s.name() for s in syn.instance_hypernyms()]}")
        print(f"  🔷 Instance Hyponyms: {[s.name() for s in syn.instance_hyponyms()]}")
        print(f"  🔷 Member Holonyms: {[s.name() for s in syn.member_holonyms()]}")
        print(f"  🔷 Part Holonyms: {[s.name() for s in syn.part_holonyms()]}")
        print(f"  🔷 Substance Holonyms: {[s.name() for s in syn.substance_holonyms()]}")
        print(f"  🔷 Member Meronyms: {[s.name() for s in syn.member_meronyms()]}")
        print(f"  🔷 Part Meronyms: {[s.name() for s in syn.part_meronyms()]}")
        print(f"  🔷 Substance Meronyms: {[s.name() for s in syn.substance_meronyms()]}")
        print(f"  🔷 Also See: {[s.name() for s in syn.also_sees()]}")
        print(f"  🔷 Similar To: {[s.name() for s in syn.similar_tos()]}")





show_relations("car")





