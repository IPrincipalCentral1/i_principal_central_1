













list_of_liberary_to_install = [

                            ["requests"] ,
                            
                            

]










import os



import sys

import subprocess

import platform

import traceback



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

from pathlib import Path







def wait(time_in_number):

    t1 = time.time()
    
    
    t2 = time.time()    
   

    while (t2 - t1 < time_in_number):

        t2 = time.time()    



def wait_for_the_next_step_0():


    message = "this file should contain just 'true' for the mixer to make the next step"

    file_0 = os.path.join(os.getcwd(), "i_run_mixer_1.txt")

    with open(file_0, "r") as f_:
    
        content = f_.read(os.path.getsize(file_0))
    
    
    counter_0 = 0
    
    
    while (content != message):
    
                
        with open(file_0, "r") as f_:
        
            content = f_.read(os.path.getsize(file_0))
        

        #counter_0 += 1
        
        

def wait_for_the_next_step_1():


    message = "this file should contain just 'true' for the mixer to affect the step"

    file_0 = os.path.join(os.getcwd(), "i_run_mixer_2.txt")

    with open(file_0, "r") as f_:
    
        content = f_.read(os.path.getsize(file_0))
    
    
    counter_0 = 0
    
    
    while (content != message):
    
                
        with open(file_0, "r") as f_:
        
            content = f_.read(os.path.getsize(file_0))


        #counter_0 += 1



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
                
                    f_.write(f"1;{list_0[counter_0]};{real:.2f};{list_0[counter_1]};bank;{paypal_like:.2f};{list_0[counter_1]};extract-ed;{extract_ed:.2f}\n")
                
                
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

        amount = (amount * 100) // 1
        
        
        amount = amount / 100
        
        
        amount_of_result = amount * list_0[counter_0][1]
        
    else:
    
        semaphore_of_error = True
        
    
    return  [semaphore_of_error, amount_of_result]




def transform_and_calculate_0(list_0, amount):
    
    
    
        
    
    list_of_unity = list_0
    
    
    
    result_1 = [False, amount]
    
    
    #print(f"\n\n list_of_unity = {list_of_unity} \n\n result_1 = {result_1} \n\n")
    
    
    counter_0 = 0
    
    
    while (counter_0 + 1 < len(list_of_unity)):
    
        
        result_1 = transformer_0(list_0=list_of_result, unity_0=list_of_unity[counter_0], unity_1=list_of_unity[counter_0 + 1], amount=result_1[1])
        
        counter_0 += 1
    
    
    
    #print(f"\n\n\n new : result_1 = {result_1} \n\n\n")
    
    
    return result_1
    







def int_to_str_0(number_0):

    str_0 = str(number_0)
    
    counter_0 = len(str_0)
    


    str_result = str_0
    

    if (18 > len(str_0)):
    
    
        counter_1 = 0
    
        while (counter_1 < 18 - counter_0):
            
            str_result = "0" + str_result
            
            counter_1 += 1
        
    
    
    return str_result





def open_popup_terminal(command):
    
    
    system = platform.system()

    if system == "Windows":

        subprocess.run(["cmd", "/c", f"{command}"])

    elif system == "Linux":

        subprocess.run(["gnome-terminal", "--", "bash", "-c", f"{command}; exit"])

    elif system == "Darwin":

        subprocess.run(["osascript", "-e", f'tell app "Terminal" to do script "{command}; exit"'])






def reader_of_possibility_0():



    list_result = ["0"]


    
    folder_0 = os.path.join(os.getcwd(), "space_for_mix")

    list_of_file = []

    for root, dir_, list_of_file in os.walk(folder_0):
    
        break
    

    counter_0 = 0
    
    
    while (counter_0 < len(list_of_file)):
        
        
        str_number_0 = int_to_str_0(number_0=counter_0)
        
        file_0 = os.path.join(folder_0, f"file_part_{str_number_0}.mixer")
        
        with open(file_0, "r") as f_:
        
            content = f_.read(os.path.getsize(file_0))
        
        
        list_result.append(content)
    
    
        counter_0 += 1
    
    
    
    list_result.append("0")
    
    


    return list_result





def next_step_0():

    
    
    file_1 = os.path.join(os.getcwd(), "i_run_mixer_1.txt")
    

    with open(file_1, "w", encoding="utf-8") as f_:

        f_.write("true")



    wait_for_the_next_step_0()
    




def next_step_1():

    
    
    file_1 = os.path.join(os.getcwd(), "i_run_mixer_2.txt")
    

    with open(file_1, "w", encoding="utf-8") as f_:

        f_.write("true")



    wait_for_the_next_step_1()
    




def refresher_0():

        
    os.system("python3 refresher_0.py")
    
    
    
    
    list_of_file = []
    
    
    counter_0 = 0
    
    
    while (counter_0 < 1):
    
    
    
        str_number_0 = int_to_str_0(number_0=counter_0)
    
        file_0 = os.path.join(os.getcwd(), "space_for_mix", f"file_part_{str_number_0}.mixer")
    
    
        with open(file_0, "w") as f_:
    
            f_.write("0")
    
        counter_0 += 1
    




def extract_and_calculate_0(list_of_result, amount):


        
    list_of_unity = []
    
    counter_0 = 0
    
    
    while (counter_0 < len(list_of_result)):
    
        #print(f"\ni_hello_0_i . int(list_of_result[counter_0]) = {int(list_of_result[counter_0])} .\n")
    
        list_of_unity.append(supported_currencies[int(list_of_result[counter_0])])
        
        counter_0 += 1
    
    
    
    result_1 = transform_and_calculate_0(list_0=list_of_unity, amount=amount)
    
    return [result_1, list_of_unity]



wise_supported_currencies = [
    
    
    
    "RUB",  # Russian Ruble
    "USD",  # US Dollar
    "EUR",  # Euro        
    "AED",  # UAE Dirham
    "AUD",  # Australian Dollar
    "BDT",  # Bangladeshi Taka
    "BGN",  # Bulgarian Lev
    "BRL",  # Brazilian Real
    "CAD",  # Canadian Dollar
    "CHF",  # Swiss Franc
    "CLP",  # Chilean Peso
    "CNY",  # Chinese Yuan
    "CRC",  # Costa Rican Colón
    "CZK",  # Czech Koruna
    "DKK",  # Danish Krone
    "EGP",  # Egyptian Pound
    "GBP",  # British Pound
    "GEL",  # Georgian Lari
    "HKD",  # Hong Kong Dollar
    "HRK",  # Croatian Kuna
    "HUF",  # Hungarian Forint
    "IDR",  # Indonesian Rupiah
    "ILS",  # Israeli New 
    "INR",  # Indian Rupee
    "JPY",  # Japanese Yen
    "KES",  # Kenyan Shilling
    "KRW",  # South Korean Won
    "LKR",  # Sri Lankan Rupee
    "MAD",  # Moroccan Dirham
    "MXN",  # Mexican Peso
    "MYR",  # Malaysian Ringgit
    "NGN",  # Nigerian Naira
    "NOK",  # Norwegian Krone
    "NZD",  # New Zealand Dollar
    "PEN",  # Peruvian Sol
    "PHP",  # Philippine Peso
    "PKR",  # Pakistani Rupee
    "PLN",  # Polish Zloty
    "RON",  # Romanian Leu
    "SAR",  # Saudi Riyal
    "SEK",  # Swedish Krona
    "SGD",  # Singapore Dollar
    "THB",  # Thai Baht
    "TRY",  # Turkish Lira
    "TZS",  # Tanzanian Shilling
    "UAH",  # Ukrainian Hryvnia
    "UGX",  # Ugandan Shilling
    "VND",  # Vietnamese Dong
    "ZAR"   # South African Rand

]



target_currencies = ["EUR", "GBP", "JPY", "CAD", "AUD", "CHF", "USD"]


paypal_supported_currencies = [

                            "SAR", "DZD", "CHF", "JPY", "RUB", "USD", "EUR", "AUD", "BRL",   

                            "HUF", "INR", "ILS", "MYR", "MXN", "TWD", "NZD",

                            "NOK", "PHP", "PLN", "GBP", "SGD", "SEK", "CAD",

                            "THB", "TRY", "HKD", "DKK", "CNY", "CZK",

                            ]





paypal_supported_currencies_1 = [


                            "USD", "BHD", "AOA", "SSP", "SDG", "KZT", "IDR", "AUD", "MGA", "NGN", "XOF", "SYP", "IQD", "KWD",            
                            
                            "BYN", "BZD", "BTN", "BOB", "BAM", "BWP", "BND", "BGN", "BIF", "CVE", "KHR", "XAF", "DZD",
                            
                            "CLP", "CNY", "COP", "KMF", "CRC", "HRK", "CZK", "DKK", "DJF", "DOP", "ERN", "ALL", "LBP", "CAD",
                            
                            "SZL", "ETB", "FJD", "GMD", "GEL", "GHS", "GTQ", "GNF", "GYD", "HTG", "HNL", "HUF", "ISK", "INR",
                            
                            "ILS", "JMD", "JPY", "JOD", "KES", "KGS", "LAK", "AZN", "BSD", "XCD", "EGP", "MXN", "CUP",
                            
                            "LSL", "LRD", "LYD", "MOP", "MKD", "MKD", "MWK", "MYR", "MVR", "MUR", "EUR", "AMD", "KPW",
                            
                            "MDL", "MNT", "MAD", "MZN", "MMK", "NAD", "NPR", "ANG", "NZD", "NIO", "NOK", "OMR", "PKR",
                            
                            "PAB", "PGK", "PYG", "PEN", "PHP", "PLN", "QAR", "RON", "RUB", "RWF", "SHP", "WST", "STN", "SAR",
                            
                            "RSD", "SCR", "SLL", "SGD", "SBD", "SOS", "ZAR", "LKR", "SRD", "SEK", "CHF", "MRU", "ARS", "BRL", 
                            
                            "TWD", "TJS", "TZS", "THB", "TOP", "TTD", "TND", "TMT", "UGX", "UAH", "AED", "UYU", "UZS", "BBD",
                            
                            "VUV", "VES", "VND", "YER", "ZMW", "ZWL", "FKP", "GIP", "IMP", "JEP", "KID", "SML", "TVD", "BDT",
                            
                            "GBP", "KRW", "IRR", "AFN", "TRY",

                            
                            ]








#print(f"\n len(paypal_supported_currencies) = {len(paypal_supported_currencies)} .\n")




#supported_currencies = [



        #"go to bed", "eat machwi", "drink water", "produce machwi",

        #"produce water", "produce bed",




                             #]



i_list_of_currency_1_i = [
                        
                        
                        "USD", "EUR", "GBP", "JPY", "CAD", "SGD", "NZD", "HKD",                         
                        
                        
                        ]
                        



supported_currencies = i_list_of_currency_1_i




print(f"\n len(supported_currencies) = {len(supported_currencies)} .\n")



t1 = time.time()


file_0 = os.path.join(os.getcwd(), "currency_bank_7.csv")

#mixer_0(list_0=wise_supported_currencies, file=file_0)

list_of_result = get_from_file(file=file_0)


#list_of_result = [



                    #['go to bed', 1, 'go to bed'] ,

                    #['go to bed', 2, 'eat machwi'] ,

                    #['go to bed', 3, 'drink water'] ,

                    #['go to bed', 4, 'produce machwi'] ,

                    #['go to bed', 5, 'produce water'] ,

                    #['go to bed', 6, 'produce bed'] ,

                    #['eat machwi', 0.5, 'go to bed'] ,

                    #['eat machwi', 1, 'eat machwi'] ,

                    #['eat machwi', 2, 'drink water'] ,

                    #['eat machwi', 3, 'produce machwi'] ,

                    #['eat machwi', 4, 'produce water'] ,

                    #['eat machwi', 5, 'produce bed'] ,

                    #['drink water', 0.3333333333333333, 'go to bed'] ,

                    #['drink water', 0.5, 'eat machwi'] ,

                    #['drink water', 1, 'drink water'] ,

                    #['drink water', 2, 'produce machwi'] ,

                    #['drink water', 3, 'produce water'] ,

                    #['drink water', 4, 'produce bed'] ,

                    #['produce machwi', 0.25, 'go to bed'] ,

                    #['produce machwi', 0.3333333333333333, 'eat machwi'] ,

                    #['produce machwi', 0.5, 'drink water'] ,

                    #['produce machwi', 1, 'produce machwi'] ,

                    #['produce machwi', 2, 'produce water'] ,

                    #['produce machwi', 3, 'produce bed'] ,

                    #['produce water', 0.2, 'go to bed'] ,

                    #['produce water', 0.25, 'eat machwi'] ,

                    #['produce water', 0.3333333333333333, 'drink water'] ,

                    #['produce water', 0.5, 'produce machwi'] ,

                    #['produce water', 1, 'produce water'] ,

                    #['produce water', 2, 'produce bed'] ,

                    #['produce bed', 0.16666666666666666, 'go to bed'] ,

                    #['produce bed', 0.2, 'eat machwi'] ,

                    #['produce bed', 0.25, 'drink water'] ,

                    #['produce bed', 0.3333333333333333, 'produce machwi'] ,

                    #['produce bed', 0.5, 'produce water'] ,

                    #['produce bed', 1, 'produce bed'] ,




        #]






#n_0 = 260.0




#n_1 = 1 / n_0


#n_2 = 233.0

#n_3 = 1 / n_2


##n_1 = 0.0038461538461538464 

#n__0 = (1 - 0.03)


#list_of_result = [

                    #['DZD', 0.9, 'DZD'], ['DZD', n_1 * n__0, 'EUR'], ['DZD', n_3 * n__0, 'USD'], 

                    #['EUR', n_0 * n__0, 'DZD'], ['EUR', 0.9, 'EUR'], ['EUR', 1.04, 'USD'], 

                    #['USD', n_2 * n__0, 'DZD'], ['USD', 0.78, 'EUR'], ['USD', 0.9, 'USD']


                    #]





#print(f"\n\n\n list_of_result = {list_of_result} .\n\n")




#list_0 = [

            #["EUR", n_0, "DZD"],

            #["DZD", n_1, "EUR"],

                        
            #["USD", n_2, "DZD"],
            
            #["DZD", n_3, "USD"],
            
            


            #]







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




list_of_unity = ["EUR", "USD", "AUD", "EUR"]

amount = 5.0


result_1 = transform_and_calculate_0(list_0=list_of_unity, amount=amount)




list_of_unity = ["EUR", "AUD", "USD", "EUR"]




result_1 = transform_and_calculate_0(list_0=list_of_unity, amount=amount)





folder_0 = os.path.join(os.getcwd(), "space_for_mix")


try:

    os.remove(os.path.join(folder_0, "file_for_github_0.txt"))

except:

    semaphore_of_error = True




if ((len(sys.argv) > 1)):


    if (sys.argv[1] == "init"):

        refresher_0()




    file_1 = os.path.join(os.getcwd(), "Economic_Partner_official_produced_mixer_9.c")


    with open(file_1, "r") as f_:

        content = f_.read(os.path.getsize(file_1))




    content = content.replace("___number_of_chunk___", "10")



    content = content.replace("___postion_of_max_range___", str(len(supported_currencies) - 1))



    file_2 = os.path.join(os.getcwd(), "Economic_Partner_official_produced_mixer_9_0.c")


    with open(file_2, "w") as f_:

        f_.write(content)




    os.system("gcc Economic_Partner_official_produced_mixer_9_0.c -o E_P_o_p_mixer_9_0")



    open_popup_terminal(command="./E_P_o_p_mixer_9_0")












'''

-----------------------------------------------------------------------------------

-----------------------------------------------------------------------------------

-----------------------------------------------------------------------------------



start




'''

print("\n\n start :")




'''

wise_supported_currencies 




list_of_unity = ["EUR", "USD", "AUD", "EUR"]

amount = 1000.0


result_1 = transform_and_calculate_0(list_0=list_of_unity, amount=amount)




list_of_unity = ["EUR", "AUD", "USD", "EUR"]




result_1 = transform_and_calculate_0(list_0=list_of_unity, amount=amount)






in wise :

    max_0 = [14.0792, ['EUR', 'VND', 'JPY', 'EUR']]


    ['EUR', 'VND', 'JPY']


in paypal :


    max_0 = [13.6405, ['EUR', 'JPY', 'CHF', 'JPY', 'EUR']] 

    ['EUR', 'JPY', 'CHF']



use-ing 10 % :


     max_0 = [12.2429, ['EUR', 'JPY', 'CHF', 'JPY', 'EUR']] 


use-ing 3 unity and 10 % :

    max_0 = [13.573, ['DZD', 'EUR', 'DZD', 'EUR', 'DZD', 'EUR', 'DZD', 'EUR', 'DZD']] 


use-ing 3 unity and 10 % and amount == 1000.0:

    max_0 = [3390.5353999999998, ['DZD', 'EUR', 'DZD', 'EUR', 'DZD', 'EUR', 'DZD', 'EUR', 'DZD']] .



very use-ing 3 unity and 10 % and amount == 1000.0:


    max_0 = [3038.9946999999997, ['DZD', 'EUR', 'USD', 'DZD', 'EUR', 'DZD', 'EUR', 'DZD', 'EUR', 'DZD']] .


    max_0 = [2618.2866, ['DZD', 'EUR', 'USD', 'DZD', 'EUR', 'DZD', 'EUR', 'DZD', 'USD', 'DZD']] .



    max_0 = [23.818499999999997, ['DZD', 'GBP', 'DZD', 'GBP', 'DZD']] .







i principal central discovered a way to multiply the money by transformation .


for example :
    
    in paypal start with 10.0 EUR : 
    
        max_0 = [24.4859, ['EUR', 'JPY', 'CHF', 'JPY', 'EUR']] .
    
    
    it mean from the amount that you where having wich is 10.0 EUR . you will have 24.4859 EUR after transforming like that :

        and all what are from 'EUR' to 'JPY'
        
        and all what are from 'JPY' to 'CHF'
        
        and all what are from 'CHF' to 'JPY'
        
        and all what are from 'JPY' to 'EUR'

        
    at the end you will have 24.4859 EUR .
    
    and you can repeat all the process but this time with 24.4859 EUR .
    
    and repeat again . and repeat again . and repeat again .
    
    until you have money . until you are satisfied .
    
    
    those are ways to get there also :
    
    
    
    in paypal start with 10.0 USD :    
    
        max_0 = [21.073400000000003, ['USD', 'JPY', 'CHF', 'JPY', 'USD']] .
    
    
    in paypal start with 10.0 RUB :
    
        max_0 = [20.4825, ['RUB', 'JPY', 'CHF', 'JPY', 'EUR', 'RUB']] .
    
    
    
    in paypal start with 10.0 JPY :
    
         max_0 = [25.8768, ['JPY', 'CHF', 'JPY', 'CHF', 'JPY']] .
    
    "LBP", 
    in paypal start with 10.0 CHF :
    
         max_0 = [26.1517, ['CHF', 'JPY', 'CHF', 'JPY', 'CHF']] .
    
    
    
    
    in wise start with 10.0 EUR :
    
        max_0 = [24.4859, ['EUR', 'JPY', 'CHF', 'JPY', 'EUR']] .
    
    
    in wise start with 10.0 USD :
    
        max_0 = [21.073400000000003, ['USD', 'JPY', 'CHF', 'JPY', 'USD']] .
    
    
    
    in wise start with 10.0 RUB :
    
        max_0 = [16.5813, ['RUB', 'CAD', 'JPY', 'CHF', 'RUB']] .
    
    

    start with 10.00 EUR :
    
         [35.1388, ['EUR', 'DZD', 'EUR', 'DZD', 'EUR', 'DZD', 'EUR', 'DZD', 'EUR']] .
        
        
        
        
    start with 10.00 EUR :
        
         [48.107, ['EUR', 'DZD', 'EUR', 'DZD', 'EUR', 'DZD', 'EUR', 'DZD', 'EUR', 'DZD', 'EUR']] .
    



'''



def i_extend_list_0_i(list_of_unity, i_number_of_calcule_0_i):
    
    
    
    i_counter_0_i = 0
    
    while (i_counter_0_i < i_number_of_calcule_0_i):
        
        
        list_of_unity.extend(['DZD', 'EUR'])
        
        i_counter_0_i += 1
        
    
    
    return list_of_unity
    



amount = 50.00

list_of_unity = ['EUR', 'DZD', 'EUR', 'DZD', 'EUR', 'DZD', 'EUR', "DZD", "EUR", "DZD", "EUR"]


list_of_unity = ['EUR']


i_number_of_calcule_0_i = 17


list_of_unity = i_extend_list_0_i(list_of_unity=list_of_unity, i_number_of_calcule_0_i=i_number_of_calcule_0_i)


print(f"\n    i_number_of_calcule_0_i = {i_number_of_calcule_0_i} .\n")



result_1 = transform_and_calculate_0(list_0=list_of_unity, amount=amount)

print(f"\n\n    result_1 = {result_1} .\n\n")



list_of_unity = ['EUR']


i_number_of_calcule_0_i = 16


list_of_unity = i_extend_list_0_i(list_of_unity=list_of_unity, i_number_of_calcule_0_i=i_number_of_calcule_0_i)


print(f"\n    i_number_of_calcule_0_i = {i_number_of_calcule_0_i} .\n")



result_1 = transform_and_calculate_0(list_0=list_of_unity, amount=amount)

print(f"\n\n    result_1 = {result_1} .\n\n")





t1 = time.time()


number_of_calculation = 10_000



amount = 10.0

max_0 = [0.0, []]

counter_2 = 1


while (counter_2 <= number_of_calculation):



    list_of_result_0 = reader_of_possibility_0()



    #print(f"\n\n    counter_2 = {counter_2} . list_of_result_0 = {list_of_result_0} .\n\n\n")



    result = extract_and_calculate_0(list_of_result=list_of_result_0, amount=amount)
    
    
    if ((result[0][1] > max_0[0])):

        


        i_counter_3_i = 0

        while ((i_counter_3_i < len(result[1])) and (result[1][i_counter_3_i] == result[1][0])):


            i_counter_3_i += 2


        if (i_counter_3_i >= len(result[1])):
            
            max_0[0] = result[0][1]
            
            
            
            
            max_0[1].clear()
            
            max_0[1].extend(result[1])
            


    next_step_0()


    counter_2 += 1




file_0 = os.path.join(os.getcwd(), "i_run_mixer_2.txt")

with open(file_0, "w") as f_:

    f_.write("true")



t2 = time.time()

print("-" * 30)


print(f"\n\n max_0 = {max_0} .\n\n time = {t2 - t1} \n\n")









list_0 = max_0[1]


result_2 = transform_and_calculate_0(list_0=list_0, amount=amount)





print(f"\n\n list_0 = {list_0} .\n result_2 = {result_2} .\n\n\n")



q = 1000.0

counter_0 = 0


while (counter_0 < 20):


    q *= 2

    print(f"counter_0 = {counter_0} . q = {q} . day = {(counter_0 + 1) * 8}")

    counter_0 += 1




print(f" finish .\n\n")




























