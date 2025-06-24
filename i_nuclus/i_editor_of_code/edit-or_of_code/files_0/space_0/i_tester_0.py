













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












def get_paypal_like_rate(from_currency, to_currency, paypal_margin=0.04):



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





def mixer_0(list_0):

    list_1 = [0, 0]


    file_0 = os.path.join(os.getcwd(), "currency_0.csv")

    with open(file_0, "w") as f_:
    
        
    
        counter_0 = 0
        
        while (counter_0 < len(list_0)):
        
            
            counter_1 = 0
            
            while (counter_1 < len(list_0)):
                
                
                            
                try:
                
                
                    real, paypal_like = get_paypal_like_rate(list_0[counter_0], list_0[counter_1])
                
                    print(f" 1 {list_0[counter_0]} = {real:.2f} {list_0[counter_1]} (PayPal ≈ {paypal_like:.2f} {list_0[counter_1]})")
                
                    f_.write(f" 1 {list_0[counter_0]};{real:.2f} {list_0[counter_1]};(PayPal ≈ {paypal_like:.2f} {list_0[counter_1]})\n")
                
                
                except Exception as e:
                
                
                    print(f"❌ فشل التحويل إلى : {e}")
                
                
                
                counter_1 += 1
            
            
            counter_0 += 1
        
    
    
    
target_currencies = ["EUR", "GBP", "JPY", "CAD", "AUD", "CHF", "USD"]



mixer_0(list_0=target_currencies)


#for curr in target_currencies:

    #try:


        #real, paypal_like = get_paypal_like_rate("USD", curr)

        #print(f" 1 USD = {real:.2f} {curr} (PayPal ≈ {paypal_like:.2f} {curr})")


    #except Exception as e:


        #print(f"❌ فشل التحويل إلى {curr}: {e}")








