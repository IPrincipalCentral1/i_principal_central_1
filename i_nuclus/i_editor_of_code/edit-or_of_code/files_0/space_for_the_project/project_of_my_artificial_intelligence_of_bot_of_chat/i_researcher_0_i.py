













list_of_liberary_to_install = [

                            ["playwright"] ,
                            
                            



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
            
            # تشغيل Chromium
            
            browser = p.chromium.launch(headless=False)  # غيّر إلى True إذا أردت بدون نافذة
            
            page = browser.new_page()
            
            # الذهاب لصفحة البحث في ويكيبيديا
            
            url = f"https://{i_lenguage_0_i}.wikipedia.org/wiki/Special:Search?search={query}"
            
            page.goto(url)
            
            # انتظار تحميل الصفحة
            
            page.wait_for_selector("body")
            
            # جلب النص الكامل
            
            i_text_of_result_0_i = page.inner_text("body")
            
            #print("\n--- مقتطف من النص ---\n")
            
            #print(text)  # اطبع أول 2000 حرف
            
            
            browser.close()
    except:
        
        
                    
        traceback.print_exc()
        
        error = traceback.format_exc()
        
        semaphore = True
        
        print(f"Erreur : {str(error)}")
        
        
        
        
    
    
    
    return i_text_of_result_0_i
        
if __name__ == "__main__":
    
    
    
    i_text_of_result_0_i = search_wikipedia("Python (programming \n language)", "en")
    
    
    
    




















