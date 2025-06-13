

















list_of_link = [


            r"https://github.com/UniversalDependencies/UD_English-GUM/tree/master",
            
            
            r"https://github.com/UniversalDependencies/UD_English-EWT/tree/master",
            
            
            r"https://github.com/UniversalDependencies/UD_English-ParTUT/tree/master",
            
            
            r"https://github.com/UniversalDependencies/UD_English-GENTLE/tree/master",
            
            
            r"https://github.com/UniversalDependencies/UD_English-LinES/tree/master",
            
            
            r"https://github.com/UniversalDependencies/UD_English-PUD/tree/master",
            
            
            r"https://github.com/UniversalDependencies/UD_English-Pronouns/tree/master",
            
            
            r"https://github.com/UniversalDependencies/UD_English-CHILDES/tree/dev",
            
            
            r"https://github.com/UniversalDependencies/UD_English-GUMReddit/tree/master",
            
            
            r"https://github.com/UniversalDependencies/UD_English-Atis/tree/master",
            
            
            r"https://github.com/UniversalDependencies/UD_English-ESLSpok/tree/master",
            
            
            r"https://github.com/UniversalDependencies/UD_English-CTeTex/tree/master",
            
            
            
            
            ]













link_of_repozitory = []


counter_0 = 0


while (counter_0 < len(list_of_link)):





    if (list_of_link[counter_0].startswith("https://github.com/")):
    
        
        v_0 = list_of_link[counter_0].split("https://github.com/")
    
        v_1 = v_0[-1].split("/")
        
        link = "https://github.com/" + v_1[0] + "/" + v_1[1] + ".git"
    
        if (not link in link_of_repozitory):
    
        
            link_of_repozitory.append(link)
        
        
            print(f"link_of_repozitory[{counter_0}] = {link_of_repozitory[counter_0]} .")
    
    
    
    
    elif (list_of_link[counter_0].startswith("http://github.com/")):
    
        v_0 = list_of_link[counter_0].split("http://github.com/")
    
        v_1 = v_0[-1].split("/")
        
        link = "http://github.com/" + v_1[0] + "/" + v_1[1] + ".git"
    
        if (not link in link_of_repozitory):
    
            link_of_repozitory.append(link)

    
            print(f"link_of_repozitory[{counter_0}] = {link_of_repozitory[counter_0]} .")


    counter_0 += 1















