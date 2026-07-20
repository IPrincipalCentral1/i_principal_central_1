















import os



os.system("pip install nltk")


os.system("pip install spacy")


os.system("pip install spacy-wordnet")


os.system("pip install spacy-wordnet")




import nltk

# تحميل wordnet و omw-1.4 من داخل الكود

#nltk.download('wordnet')

#nltk.download('omw-1.4')






import spacy.cli

# تحميل النموذج


#spacy.cli.download("en_core_web_sm")




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

import traceback




def min_string_function(min_, ele, n):


    v = min_[0]



    v1 = ele

    one_ = True

    one = True

    # anné

    if (v <= v1):

        if (v < v1):

            one_ = False


    else:

        one = False


    if (not one_):

        return min_

    elif (one):

        return min_

    else:

        return (ele, n, )



def sort_element_0_0(l):


    l_ = []

    while (0 < len(l)):

        i = 0

        min_ = (l[i][0], i, )



        while (i < len(l)):

            min_0 = min_string_function(min_=min_, ele=l[i][0], n=i)



            if (min_0 != min_):

                min_ = min_0

            i += 1
        
        #print("min_ = ", min_)

        l_.append(l[min_[1]])

        l.pop(min_[1])

    return l_





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
    
    





def show_relations(list_of_word, word):


    try:

    
        synsets = wn.synsets(word)
        
        #print(f"word = {word}")
    
        if not synsets:

            
            print(f"word = {word}")
            
    
            print("لا توجد synsets لهذه الكلمة.")


    
        else:
        
        
        
        
            list_of_word.append([word, []])
        
            for syn in synsets:
           
           
                #print(f"\nSynset: {syn.name()}")
                #print(f"  تعريف: {syn.definition()}")
        
                list_of_word[-1][1].append([syn.name(), []])
                
                        
                # العلاقات
           
                #print(f"  🔷 (أسماء مفرطة) Hypernyms: {[s.name() for s in syn.hypernyms()]}")
                
                list_of_word[-1][1][-1][1].append(["Hypernyms", [s.name() for s in syn.hypernyms()]])
                
                #print(f"  🔷 (الترادفات) Hyponyms: {[s.name() for s in syn.hyponyms()]}")
                
                list_of_word[-1][1][-1][1].append(["Hyponyms", [s.name() for s in syn.hyponyms()]])
                
                
                #print(f"  🔷 (أسماء مفرطة للمثيلات) Instance Hypernyms: {[s.name() for s in syn.instance_hypernyms()]}")
        
        
                list_of_word[-1][1][-1][1].append(["Instance Hypernyms", [s.name() for s in syn.instance_hypernyms()]])
        
                #print(f"  🔷 (أمثلة على المرادفات) Instance Hyponyms: {[s.name() for s in syn.instance_hyponyms()]}")
        
        
                list_of_word[-1][1][-1][1].append(["Instance Hyponyms", [s.name() for s in syn.instance_hyponyms()]])
        
                #print(f"  🔷 (أسماء الأعضاء المتجانسة) Member Holonyms: {[s.name() for s in syn.member_holonyms()]}")
         
         
                list_of_word[-1][1][-1][1].append(["Member Holonyms", [s.name() for s in syn.member_holonyms()]])
         
                #print(f"  🔷 (جزء من الكلمات المتجانسة) Part Holonyms: {[s.name() for s in syn.part_holonyms()]}")
        
        
                list_of_word[-1][1][-1][1].append(["Part Holonyms", [s.name() for s in syn.part_holonyms()]])
        
                #print(f"  🔷 (مرادفات المادة) Substance Holonyms: {[s.name() for s in syn.substance_holonyms()]}")
        
        
        
                list_of_word[-1][1][-1][1].append(["Substance Holonyms", [s.name() for s in syn.substance_holonyms()]])
        
                #print(f"  🔷 (أسماء الأعضاء) Member Meronyms: {[s.name() for s in syn.member_meronyms()]}")
        
        
        
                list_of_word[-1][1][-1][1].append(["Member Meronyms", [s.name() for s in syn.member_meronyms()]])
        
                #print(f"  🔷 (مرادفات الأجزاء) Part Meronyms: {[s.name() for s in syn.part_meronyms()]}")
        
        
        
                list_of_word[-1][1][-1][1].append(["Part Meronyms", [s.name() for s in syn.part_meronyms()]])
        
        
                #print(f"  🔷 (مرادفات المواد) Substance Meronyms: {[s.name() for s in syn.substance_meronyms()]}")
         
         
                list_of_word[-1][1][-1][1].append(["Substance Meronyms", [s.name() for s in syn.substance_meronyms()]])
         
         
         
                #print(f"  🔷 (انظر أيضا) Also See: {[s.name() for s in syn.also_sees()]}")
        
        
        
                list_of_word[-1][1][-1][1].append(["Also See", [s.name() for s in syn.also_sees()]])
                
                
        
                #print(f"  🔷 (مشابه ل) Similar To: {[s.name() for s in syn.similar_tos()]}")
        
        
                list_of_word[-1][1][-1][1].append(["Similar To", [s.name() for s in syn.similar_tos()]])
        
        
        
    except:
    
    
                
                    
        traceback.print_exc()
        
        error = traceback.format_exc()
        
        semaphore = True
        
        print(f"Erreur : {str(error)}")
        
        
    

    return list_of_word







print(f"start .")


list_of_word = []


list_0 = []

list_1 = []



#for synset in wn.all_synsets():




    #for lemma in synset.lemmas():


        #word = lemma.name().lower()



        #if (not word in list_0):

            #list_0.append(word)




#print(f"finish gather-ing words .")


#print(f"start sort-ing list_0 .")


#list_0 = sort_element_0_0(l=list_0)








file_0 = os.path.join(os.getcwd(), "space_0", "space_of_language_2", "word_0.txt")

with open(file_0, "r") as f_:


    content = f_.read(os.path.getsize(file_0))




list_0 = content.split("\n")





file_0 = os.path.join(os.getcwd(), "space_0", "space_of_language_2", "all_word_0.txt")

with open(file_0, "w") as f_:


    counter_0 = 0

    while (counter_0 < len(list_0)):


        if (list_0[counter_0] != ""):

            f_.write(f"{counter_0}. " + str(list_0[counter_0]) + "\n")



        counter_0 += 1

















