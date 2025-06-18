













import os

from pathlib import Path






def finder_0(list_of_word_with_definition, word):


    counter_0 = 0
    
    while ((counter_0 < len(list_of_word_with_definition)) and (list_of_word_with_definition[counter_0][0] != word)):

        counter_0 += 1


    return counter_0



list_of_word_with_definition = []


content = ""



folder_0 = os.path.join(os.getcwd(), "space_0", "space_of_language_2")



file_0 = os.path.join(folder_0, "definition_of_word_0.txt")





d_0 = Path(file_0)


content = d_0.read_text()





v_0 = content.split("\n")



counter_0 = 0

while (counter_0 < len(v_0)):

    if ((v_0[counter_0] != "")):
    
    
        if (v_0[counter_0][0] != " "):
        
            counter_1 = 0
            
            while ((counter_1 < len(v_0[counter_0])) and (v_0[counter_0][counter_1] != " ")):
            
                counter_1 += 1
            
            
            content = ""
            
            
            counter_1 += 1
            
            
            while ((counter_1 < len(v_0[counter_0])) and (v_0[counter_0][counter_1] != " ")):
            
                content += v_0[counter_0][counter_1]
                
                counter_1 += 1
                
            
            list_of_word_with_definition.append([content, []])
            


        else:
        
                        
            counter_1 = 0
            
            while ((counter_1 < len(v_0[counter_0])) and (v_0[counter_0][counter_1] == " ")):
            
                counter_1 += 1
            
            
            content = ""
            
            

            
            while ((counter_1 < len(v_0[counter_0])) and (v_0[counter_0][counter_1] != "\n")):
            
                content += v_0[counter_0][counter_1]
                
                counter_1 += 1
                
            
            list_of_word_with_definition[-1][1].append(content)
            
            

    counter_0 += 1










counter_0 = 1000


number_0 = len(list_of_word_with_definition)

number_0 = 1200


while (counter_0 < number_0):


    print(f"{counter_0}. {list_of_word_with_definition[counter_0][0]} :")
    
    
    counter_1 = 0
    
    
    while (counter_1 < len(list_of_word_with_definition[counter_0][1])):
    
        
        print(f"    {list_of_word_with_definition[counter_0][1][counter_1]}")
    
        counter_1 += 1



    counter_0 += 1





print("-" * 100)

print("-" * 100)

print("-" * 100)

print("-" * 100)

print("-" * 100)



counter_0 = finder_0(list_of_word_with_definition=list_of_word_with_definition, word="good")

counter_1 = finder_0(list_of_word_with_definition=list_of_word_with_definition, word="pretty")



if ((counter_0 < len(list_of_word_with_definition)) and (counter_1 < len(list_of_word_with_definition))):

    
        
    print(f"{counter_0}. {list_of_word_with_definition[counter_0][0]} :")
    
    
    counter_2 = 0
    
    
    while (counter_2 < len(list_of_word_with_definition[counter_0][1])):
    
        
        print(f"    {list_of_word_with_definition[counter_0][1][counter_2]}")
    
        counter_2 += 1
    

    
        
    print(f"{counter_1}. {list_of_word_with_definition[counter_1][0]} :")
    
    
    counter_2 = 0
    
    
    while (counter_2 < len(list_of_word_with_definition[counter_1][1])):
    
        
        print(f"    {list_of_word_with_definition[counter_1][1][counter_2]}")
    
        counter_2 += 1
    
    
    






















