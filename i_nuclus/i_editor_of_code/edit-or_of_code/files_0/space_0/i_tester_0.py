













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
            
            n_0 = int(v_1[0]) + (int(v_1[1]) / (10 ** 2))
            
            list_of_result.append([v_2[1], n_0, v_2[3]])
            
        counter_0 += 1

    return list_of_result


def finder_0(list_0, element):

    counter_0 = 0
    
    while ((counter_0 < len(list_0)) and (list_0[counter_0][0] != element)):
    
        counter_0 += 1

    
    return counter_0


def finder_1(list_0, element_0, element_1):

    counter_0 = 0
    
    while ((counter_0 < len(list_0)) and (list_0[counter_0][0] != element_0)):
    
        counter_0 += 1

    if (counter_0 < len(list_0)):
    
                
        while ((counter_0 < len(list_0)) and (list_0[counter_0][2] != element_1)):
        
            counter_0 += 1
            
    else:
    
        counter_0 = len(list_0)
        
        
    
    return counter_0




def transformer_0(list_0, unity_0, unity_1, amount):

    counter_0 = finder_1(list_0=list_0, element_0=unity_0, element_1=unity_1)
    
    semaphore_of_error = False

    amount_of_result = 0.0

    if ((counter_0 < len(list_0))):
    
        amount_of_result = amount * list_0[counter_0][1]
        
    else:
    
        semaphore_of_error = True
        
    
    return  [semaphore_of_error, amount_of_result]

    
    
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

n_0 = 1

print(f"list_of_result[{n_0}] = {list_of_result[n_0]}")




'''

1;USD;0.87;EUR;PayPal;0.82;EUR;extract-ed;0.04

1;EUR;1.15;USD;PayPal;1.10;USD;extract-ed;0.06


1 USD = 0.82 EUR

1 EUR = 1.15 USD








'''



list_of_unity = ["EUR", "AUD", "USD", "EUR"]



result_1 = [False, 5.0]

print(f"\n\n list_of_unity = {list_of_unity} \n\n result_1 = {result_1} \n\n")


counter_0 = 0


while (counter_0 + 1 < len(list_of_unity)):

    
    result_1 = transformer_0(list_0=list_of_result, unity_0=list_of_unity[counter_0], unity_1=list_of_unity[counter_0 + 1], amount=result_1[1])
    
    counter_0 += 1



print(f"\n\n\n new : result_1 = {result_1} \n\n\n")





'''

start


'''

print("\n\nstart :")



os.system("python3 refresher_0.py")







file_1 = os.path.join(os.getcwd(), "Economic_Partner_official_produced_mixer_8.c")


with open(file_1, "r") as f_:

    content = f_.read(os.path.getsize(file_1))
    



content = content.replace("___number_of_chunk___", "10")



content = content.replace("___postion_of_max_range___", str(len(list_of_unity) - 1))



file_2 = os.path.join(os.getcwd(), "Economic_Partner_official_produced_mixer_8_0.c")


with open(file_2, "w") as f_:

    f_.write(content)







os.system("gcc Economic_Partner_official_produced_mixer_8_0.c -o E_P_o_p_mixer_8_0")









print(f"finish .")




























