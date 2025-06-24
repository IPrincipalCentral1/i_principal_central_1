













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



import time








def get_paypal_like_rate(from_currency, to_currency, paypal_margin=0.05):



    url = f"https://open.er-api.com/v6/latest/{from_currency}"


    response = requests.get(url)

    print("Status:", response.status_code)

    data = response.json()


    if "rates" not in data or to_currency not in data["rates"]:
        raise Exception("فشل في الحصول على سعر الصرف.")


    real_rate = data["rates"][to_currency]

    paypal_rate = real_rate * (1 - paypal_margin)

    extract_ed = real_rate * paypal_margin

    return real_rate, extract_ed, paypal_rate

# تجربة





def mixer_0(list_0, file):

    list_1 = [0, 0]


    #file_0 = os.path.join(os.getcwd(), "currency_0.csv")

    with open(file, "w") as f_:
    
        
    
        counter_0 = 0
        
        while (counter_0 < len(list_0)):
        
            
            counter_1 = 0
            
            while (counter_1 < len(list_0)):
                
                
                            
                try:
                
                
                    real, extract_ed, paypal_like = get_paypal_like_rate(list_0[counter_0], list_0[counter_1])
                
                    print(f" 1 {list_0[counter_0]} = {real:.2f} {list_0[counter_1]} (PayPal ≈ {paypal_like:.2f} {list_0[counter_1]})")
                
                    f_.write(f"1;{list_0[counter_0]};{real:.2f};{list_0[counter_1]};PayPal;{paypal_like:.2f};{list_0[counter_1]};extract-ed;{extract_ed:.2f}\n")
                
                
                except Exception as e:
                
                
                    print(f"❌ فشل التحويل إلى : {e}")
                
                
                
                counter_1 += 1
            
            
            counter_0 += 1
        
    
    
def get_from_file(file):


    list_of_result = []

    with open(file, "r") as f_:
    
        content = f_.read(os.path.getsize(file))
    
    
    v_0 = content.split("\n")
    
    counter_0 = 0
    
    while (counter_0 < len(v_0)):
    
    
        if (v_0[counter_0] != ""):
        
            v_2 = v_0[counter_0].split(";")
        
            s_0 = v_2[5]
            
            v_1 = s_0.split(".")
            
            n_0 = int(v_1[0]) + (int(v_1[1]) * (10 ** 2))
            
            list_of_result.append([v_2[1], n_0, v_2[3]])
            
        counter_0 += 1

    return list_of_result

    
target_currencies = ["EUR", "GBP", "JPY", "CAD", "AUD", "CHF", "USD"]


paypal_supported_currencies = [

                            "AUD", "BRL", "CAD", "CNY", "CZK", "DKK", "EUR", "HKD",

                            "HUF", "INR", "ILS", "JPY", "MYR", "MXN", "TWD", "NZD",

                            "NOK", "PHP", "PLN", "GBP", "RUB", "SGD", "SEK", "CHF",

                            "THB", "TRY", "USD"

                            ]




t1 = time.time()


file_0 = os.path.join(os.getcwd(), "currency_0.csv")

#mixer_0(list_0=paypal_supported_currencies, file=file_0)

list_of_result = get_from_file(file=file_0)



t2 = time.time()



print(f"\n\n\ntime = {t2 - t1} second .\n\n\n")

n_0 = 0

print(f"list_of_result[{n_0}] = {list_of_result[n_0]}")




'''

1;USD;0.87;EUR;PayPal;0.82;EUR;extract-ed;0.04

1;EUR;1.15;USD;PayPal;1.10;USD;extract-ed;0.06


1 USD = 0.82 EUR

1 EUR = 1.15 USD








'''


eur = 5


usd = eur * 1.10

eur_1 = usd * 0.82


print(f"eur = {eur} . usd = {usd} . eur_1 = {eur_1} .")


























