













import os

from pathlib import Path






def finder_0(list_of_word_with_definition, word):


    counter_0 = 0
    
    while ((counter_0 < len(list_of_word_with_definition)) and (list_of_word_with_definition[counter_0][0] != word)):

        counter_0 += 1


    return counter_0



def display_0(list_of_word_with_definition, counter_0):

        
    if (counter_0 < len(list_of_word_with_definition)):
    
        
            
        print(f"{counter_0}. {list_of_word_with_definition[counter_0][0]} :")
        
        
        counter_2 = 0
        
        
        while (counter_2 < len(list_of_word_with_definition[counter_0][1])):
        
            
            print(f"    {list_of_word_with_definition[counter_0][1][counter_2]}")
        
            counter_2 += 1
        
    
        



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









folder_1 = os.path.join(os.getcwd(), "space_0", "space_of_language_3")

file_1 = os.path.join(folder_1, "file_of_all_word_on_english_0.word_0")


with open(file_1, "w") as f_:

    
    
    counter_0 = 0
    
    
    number_0 = len(list_of_word_with_definition)
    
    #number_0 = 1200
    
    
    while (counter_0 < number_0):
    
    
        #print(f"{counter_0}. {list_of_word_with_definition[counter_0][0]} :")
        
        v_0 = list_of_word_with_definition[counter_0][0].split("\"")
        
        

        
        content = ""
                    
        
        if (len(v_0) > 1):
        
            
            counter_2 = 0
            
            

            
            while (counter_2 < len(v_0) - 1):
            
                content += v_0[counter_2] + "\\" + '"'
            
                counter_2 += 1
        
            content += v_0[counter_2]
        
        else:
        
            content = list_of_word_with_definition[counter_0][0]
        
        f_.write(f"\"{content}\"\n")
        
        counter_1 = 0
        
        
        while (counter_1 < len(list_of_word_with_definition[counter_0][1])):
        
            
            #print(f"    {list_of_word_with_definition[counter_0][1][counter_1]}")
        
            counter_1 += 1
    
    
    
        counter_0 += 1
    
    
    
v_0 = "hello\"i\"1".split("\"")


content = ""
            

if (len(v_0) > 1):

    
    counter_2 = 0
    
    
    while (counter_2 < len(v_0) - 1):
    
        content += v_0[counter_2] + "\\" + '"'
    
        counter_2 += 1

    content += v_0[counter_2]




print(f"content = {content}")







print("-" * 100)

print("-" * 100)

print("-" * 100)

print("-" * 100)

print("-" * 100)



counter_0 = finder_0(list_of_word_with_definition=list_of_word_with_definition, word="good")



display_0(list_of_word_with_definition=list_of_word_with_definition, counter_0=counter_0)






counter_0 = finder_0(list_of_word_with_definition=list_of_word_with_definition, word="pretty")


display_0(list_of_word_with_definition=list_of_word_with_definition, counter_0=counter_0)




counter_0 = finder_0(list_of_word_with_definition=list_of_word_with_definition, word="mean")


display_0(list_of_word_with_definition=list_of_word_with_definition, counter_0=counter_0)







    
'''



58842. good :
    (often used as a combining form) in a good or proper or satisfactory manner or to a high standard (`good' is a nonstandard dialectal variant for `well')
    agreeable or pleasing
    appealing to the mind
    articles of commerce
    benefit
    capable of pleasing
    completely and absolutely (`good' is sometimes used informally for `thoroughly')
    deserving of esteem and respect
    exerting force or influence
    financially sound
    generally admired
    having desirable or positive qualities especially those suitable for a thing specified
    having or showing knowledge and skill and aptitude
    having the normally expected amount
    in excellent physical condition
    moral excellence or admirableness
    morally admirable
    most suitable or right for a particular purpose
    not forged
    not left to spoil
    of moral excellence
    promoting or enhancing well-being
    resulting favorably
    tending to promote physical well-being; beneficial to health
    that which is pleasing or valuable or useful
    thorough
    with or in a close or intimate relationship
104260. pretty :
    (used ironically) unexpectedly bad
    pleasing by delicacy or grace; not imposing
    to a moderately sufficient extent or degree






'''















