













list_of_liberary_to_install = [

                            #["playwright"] ,
                            
                            



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
    
    
    


#print("\n" * 10)




'''



you can change this program to be for your side .




'''



#os.system(f"playwright install")




#from playwright.sync_api import sync_playwright




def i_search_0_i(i_query_0_i, i_lenguage_0_i, i_url_0_i):
    
    
    
    
    
    
    
    i_result_0_i = ""
    
    
    try:
        
        
        
        
        
        '''
        
        right here you can make your code .
        
        this is the place for your remplacent of wikipedia .
        
        
        
        you should keep your code inside try . and put you result into i_result_0_i .
        
        
        '''
        

        #with sync_playwright() as p:



            ## الذهاب لصفحة البحث في ويكيبيديا

            ##url = f"https://{i_lenguage_0_i}.wikipedia.org/wiki/Special:Search?search={i_query_0_i}"


            #i_v_0_i = i_url_0_i.split("{i_lenguage_0_i}")

            #if (len(i_v_0_i) > 1):

                #i_counter_0_i = 0

                #i_url_1_i = ""

                #while (i_counter_0_i < len(i_v_0_i) - 1):


                    #i_url_1_i += f"{i_v_0_i[i_counter_0_i]}{i_lenguage_0_i}"

                    #i_counter_0_i += 1



                #i_url_1_i += f"{i_v_0_i[i_counter_0_i]}"


            #i_v_0_i = i_url_1_i.split("{i_query_0_i}")


            #if (len(i_v_0_i) > 1):

                #i_counter_0_i = 0

                #i_url_1_i = ""

                #while (i_counter_0_i < len(i_v_0_i) - 1):


                    #i_url_1_i += f"{i_v_0_i[i_counter_0_i]}{i_query_0_i}"

                    #i_counter_0_i += 1



                #i_url_1_i += f"{i_v_0_i[i_counter_0_i]}"



            #print(f"i_url_1_i = {i_url_1_i} .")






            ## تشغيل Chromium

            #browser = p.chromium.launch(headless=False)  # غيّر إلى True إذا أردت بدون نافذة

            #page = browser.new_page()


            #page.goto(i_url_1_i)

            ## انتظار تحميل الصفحة

            #page.wait_for_selector("body")

            ## جلب النص الكامل

            #i_result_0_i = page.inner_text("body")

            ##print("\n--- مقتطف من النص ---\n")

            ##print(i_result_0_i) 


            #browser.close()

            
            
    except:
        
        
                    
        traceback.print_exc()
        
        error = traceback.format_exc()
        
        semaphore = True
        
        print(f"Erreur : {str(error)}")
        
        
        
        
    
    
    
    return i_result_0_i
        
if __name__ == "__main__":
    
    
    i_link_0_i = "https://{i_lenguage_0_i}.wikipedia.org/wiki/Special:Search?search={i_query_0_i}"
    
    i_result_0_i = i_search_0_i(i_query_0_i="Python (programming \n language)", i_lenguage_0_i="en", i_url_0_i=i_link_0_i)
    
    
    
    




















