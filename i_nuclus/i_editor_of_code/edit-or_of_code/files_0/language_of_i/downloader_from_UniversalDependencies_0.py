
















import os


os.system("pip install requests")








import requests

import zipfile

import io

import traceback







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













list_of_link_of_repozitory = []


counter_0 = 0


while (counter_0 < len(list_of_link)):





    if (list_of_link[counter_0].startswith("https://github.com/")):
    
        
        v_0 = list_of_link[counter_0].split("https://github.com/")
    
        v_1 = v_0[-1].split("/")
        
        link = "https://github.com/" + v_1[0] + "/" + v_1[1] + "/archive/refs/heads/master.zip"
    
        if (not link in list_of_link_of_repozitory):
    
        
            list_of_link_of_repozitory.append(link)
        
        
            print(f"list_of_link_of_repozitory[{counter_0}] = {list_of_link_of_repozitory[counter_0]} .")
    
    
    
    
    elif (list_of_link[counter_0].startswith("http://github.com/")):
    
        v_0 = list_of_link[counter_0].split("http://github.com/")
    
        v_1 = v_0[-1].split("/")
        
        link = "http://github.com/" + v_1[0] + "/" + v_1[1] + "/archive/refs/heads/master.zip"
    
        if (not link in list_of_link_of_repozitory):
    
            list_of_link_of_repozitory.append(link)

    
            print(f"list_of_link_of_repozitory[{counter_0}] = {list_of_link_of_repozitory[counter_0]} .")


    counter_0 += 1








counter_0 = 0




while (counter_0 < len(list_of_link_of_repozitory)):




    
    
    
    url = list_of_link_of_repozitory[counter_0]
    
    
    folder_0 = os.path.join(os.getcwd(), "space_of_language_0", "new_folder_" + str(counter_0))
    
    #folder_0 = "new_folder"
    
    
    
    try:
        
        
        
        
        
            
        #print(f"Downloading from: {url}")
    
        response = requests.get(url)
    
        #print(f"Status Code: {response.status_code}")
    
        #print(f"Size of response content: {len(response.content)} bytes")
    
    
    
        
        if response.status_code == 200:
        
            with zipfile.ZipFile(io.BytesIO(response.content)) as zip_ref:
        
                zip_ref.extractall(folder_0)
        
    
    
        
    
    except:    
    
    
        
    
            
        traceback.print_exc()
        
        error = traceback.format_exc()
        
        semaphore = True
        
        print(f"Erreur : {str(error)}")
        
    
    
    
    print(f"counter_0 = {counter_0} . folder_0 = {folder_0} .")
    
    
    counter_0 += 1














