













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

def get_paypal_like_rate(from_currency, to_currency, amount=1.0, paypal_margin=0.035):
    url = "https://api.exchangerate.host/convert"
    params = {
        "from": from_currency,
        "to": to_currency,
        "amount": amount
    }

    response = requests.get(url, params=params)
    data = response.json()

    if "result" not in data or data["result"] is None:
        raise Exception("فشل في الحصول على سعر الصرف.")

    real_rate = data["result"] / amount
    paypal_rate = real_rate * (1 - paypal_margin)

    return real_rate, paypal_rate

# جرب:
real, paypal_like = get_paypal_like_rate("USD", "EUR")
print(f"السعر الحقيقي: 1 USD = {real:.4f} EUR")
print(f"سعر تقريبي كما في PayPal: 1 USD ≈ {paypal_like:.4f} EUR")








