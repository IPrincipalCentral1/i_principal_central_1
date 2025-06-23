













list_of_liberary_to_install = [

                            ["requests"] ,
                            
                            

]










import os



import sys

import subprocess




counter_0 = 0


while (counter_0 < len(list_of_liberary_to_install)):

        
    try:
    
    
        print(f"\n\n\npip install {list_of_liberary_to_install[counter_0][0]}\n\n\n")
    
        #os.system(f"pip3 install {list_of_liberary_to_install[counter_0][0]}")
    
        
        
        subprocess.check_call([sys.executable, "-m", "pip", "install", f"{list_of_liberary_to_install[counter_0][0]}"])
    
    
            
    except:
    
            
                    
        traceback.print_exc()
        
        error = traceback.format_exc()
        
        semaphore = True
        
        print(f"Erreur : {str(error)}")
        
    
    
    counter_0 += 1
    



import requests



def get_paypal_like_rate(from_currency, to_currency, paypal_margin=0.035):

    url = f"https://open.er-api.com/v6/latest/{from_currency}"

    response = requests.get(url)
    print("Status:", response.status_code)
    data = response.json()

    if "rates" not in data or to_currency not in data["rates"]:
        raise Exception("فشل في الحصول على سعر الصرف.")

    real_rate = data["rates"][to_currency]
    paypal_rate = real_rate * (1 - paypal_margin)

    return real_rate, paypal_rate

# تجربة

target_currencies = ["EUR", "GBP", "JPY", "CAD", "AUD", "CHF"]


for curr in target_currencies:

    try:


        real, paypal_like = get_paypal_like_rate("USD", curr)

        print(f" 1 USD = {real:.2f} {curr} (PayPal ≈ {paypal_like:.2f} {curr})")


    except Exception as e:


        print(f"❌ فشل التحويل إلى {curr}: {e}")








