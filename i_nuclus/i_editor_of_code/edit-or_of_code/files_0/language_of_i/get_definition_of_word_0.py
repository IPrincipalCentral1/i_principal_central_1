






















import os


os.system("pip install nltk")




import nltk

nltk.download('wordnet')

nltk.download('omw-1.4')  # لدعم الترجمات والتعاريف الموسعة





from nltk.corpus import wordnet as wn
from collections import defaultdict

# قاموس لتجميع التعاريف لكل كلمة
word_definitions = defaultdict(set)

# مرّ على كل الـ synsets في WordNet
for synset in wn.all_synsets():
    definition = synset.definition()
    
    # لكل lemma (كلمة) في synset
    for lemma in synset.lemmas():
        word = lemma.name().lower()
        word_definitions[word].add(definition)

# تحويل المجموعات إلى قوائم
word_definitions = {word: list(defs) for word, defs in word_definitions.items()}



word_with_definition = [[word, list(defs)] for word, defs in word_definitions.items()]









file_0 = os.path.join(os.getcwd(), "space_0", "space_of_language_2", "definition_of_word_0.txt")



with open(file_0, "w") as f_:

    counter_0 = 0
    
    
    while (counter_0 < len(word_with_definition)):
    
    
        element = word_with_definition[counter_0]
        
        f_.write(f"{element[0]} :\n")
        
        
        counter_1 = 0
        
        while (counter_1 < len(element[1])):
        
            
            f_.write(f"    {element[1][counter_1]}\n")
    
    
            print(f"counter_1 = {counter_1} . element[0] = {element[0]} . element[1][counter_1] = {element[1][counter_1]}")
        
            counter_1 += 1
    
        counter_0 += 1











