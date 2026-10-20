






















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
    
    




import nltk

nltk.download('wordnet')

nltk.download('omw-1.4')  # لدعم الترجمات والتعاريف الموسعة






def less_or_equal_string(str_0, str_1):

    counter_0 = 0
    
    
    
    while ((counter_0 < len(str_0)) and (counter_0 < len(str_1)) and (str_0[counter_0] <= str_1[counter_0])):
    
        counter_0 += 1



    if (len(str_0) > len(str_1)):
    
        if (counter_0 == len(str_1)):
        
            return False
            
            
        else:
        
            return True
            
            
    elif (len(str_0) < len(str_1)):
    
        if (counter_0 == len(str_0)):
        
            return True
            
        else:
        
            return False
            
    else:
    
    
        if (counter_0 == len(str_0)):
        
            return True
            
        else:
        
            return False
            




def less_string(str_0, str_1):

    counter_0 = 0
    
    
    
    while ((counter_0 < len(str_0)) and (counter_0 < len(str_1)) and (str_0[counter_0] < str_1[counter_0])):
    
        counter_0 += 1



    if (len(str_0) > len(str_1)):
    
        if (counter_0 == len(str_1)):
        
            return False
            
            
        else:
        
            return True
            
            
    elif (len(str_0) < len(str_1)):
    
        if (counter_0 == len(str_0)):
        
            return True
            
        else:
        
            return False
            
    else:
    
    
        if (counter_0 == len(str_0)):
        
            return True
            
        else:
        
            return False
            



def min_string_function(min_, ele, n):


    v = min_[0]



    v1 = ele

    one_ = True

    one = True

    # anné

    if (less_or_equal_string(v, v1)):

        if (less_string(v, v1)):

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








from nltk.corpus import wordnet as wn
from collections import defaultdict

# قاموس لتجميع التعاريف لكل كلمة
word_definitions = defaultdict(set)


word_with_example = []

# مرّ على كل الـ synsets في WordNet

for synset in wn.all_synsets():
    
    
    #definition = synset.definition()

    examples = synset.examples()

    list_0 = []
    
    # لكل lemma (كلمة) في synset
    for lemma in synset.lemmas():
        word = lemma.name().lower()
        
        list_0.extend(examples)
        


    
    #list_0 = sort_element_0_0(l=list_0)    
    
    print(f"word = {word} . list_0 = {list_0}")
    
    
    counter_0 = 0
    
    while ((counter_0 < len(word_with_example)) and (word_with_example[counter_0][0] > word)):
    
        counter_0 += 1



    
    word_with_example.insert(counter_0, [word, [element for element in list_0]])

    
    #word_with_example.append([word, sorted(list_0)])
    
    
    print(f"word_with_example[counter_0] = {word_with_example[counter_0]}")
    
    
    element_1 = word_with_example[counter_0]
    
    print(f"element_1[1] = {element_1[1]}")
    
    
    #word_with_example[-1][1].extend(sorted(list_0))    
        
        
    #word_with_example = sort_element_0_0(l=word_with_example)
    
    #word_definitions[word].add(tuple(examples))



# تحويل المجموعات إلى قوائم

#word_definitions = {word: list(defs) for word, defs in word_definitions.items()}



#word_with_example = [[word, sorted(list(defs))] for word, defs in word_definitions.items()]



#word_with_example = sort_element_0_0(l=word_with_example)




#file_0 = os.path.join(os.getcwd(), "space_0", "space_of_language_2", "definition_of_word_0.txt")


file_0 = os.path.join(os.getcwd(), "space_0", "space_of_language_2", "example_of_word_0.txt")



with open(file_0, "w") as f_:

    counter_0 = 0
    
    
    while (counter_0 < len(word_with_example)):
    
    
        element = word_with_example[counter_0]
        
        
        
        
        f_.write(f"{counter_0}. {element[0]} :\n")
        
        
        counter_1 = 0
        
        while (counter_1 < len(element[1])):
        
            
            f_.write(f"    {element[1][counter_1]}\n")
    
    
            print(f"counter_1 = {counter_1} . element[0] = {element[0]} . element[1][counter_1] = {element[1][counter_1]}")
        
            print(f"word_with_example[counter_0] = {word_with_example[counter_0]}")
        
        
            counter_1 += 1
    
        counter_0 += 1











