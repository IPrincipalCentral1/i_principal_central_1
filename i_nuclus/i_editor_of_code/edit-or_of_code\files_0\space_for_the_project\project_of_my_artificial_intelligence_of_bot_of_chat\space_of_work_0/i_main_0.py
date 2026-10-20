













list_of_liberary_to_install = [

                            ["playwright"] ,
                            
                            
                            ["requests"] ,
                            
                            
                            
                            



]










import os


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
    
    
    


print("\n" * 10)








os.system(f"playwright install")




from playwright.sync_api import sync_playwright




def search_wikipedia(query, i_lenguage_0_i):
    
    i_text_of_result_0_i = ""
    
    try:
    
        with sync_playwright() as p:
                browser = p.chromium.launch(headless=True)  # headless=True حتى لا يفتح نافذة
                page = browser.new_page()
                
                # فتح صفحة المقالة
                url = f"https://{i_lenguage_0_i}.wikipedia.org/wiki/Special:Search?search={query}"
                page.goto(url)
                
                page.wait_for_selector("div.mw-parser-output")
                
                # 1. أول فقرة (التعريف)
                try:
                    intro = page.inner_text("div.mw-parser-output > p")
                except:
                    intro = ""
                
                # 2. أول كود أو مثال
                try:
                    example = page.inner_text("div.mw-parser-output pre")
                except:
                    example = ""
                
                i_text_of_result_0_i = f"--- التعريف ---\n{intro}\n\n--- مثال ---\n{example}"
                
                browser.close()
    
    except:
        
        
        
                    
        traceback.print_exc()
        
        error = traceback.format_exc()
        
        semaphore = True
        
        print(f"Erreur : {str(error)}")
        
        
        
        
    
    return i_text_of_result_0_i



import requests

def wiki_intro(query, lang="en"):
    url = f"https://{lang}.wikipedia.org/api/rest_v1/page/summary/{query}"
    r = requests.get(url)
    if r.status_code == 200:
        data = r.json()
        return data.get("extract", "")
    return ""



if __name__ == "__main__":
    
    
    i_text_of_result_0_i = wiki_intro("Python (programming \n language)", "en")
    
    
    print(f"i_text_of_result_0_i = {i_text_of_result_0_i} .")
    
    
    
    




















