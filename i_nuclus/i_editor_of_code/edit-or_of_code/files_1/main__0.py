




















import i_principal_central

import os

import time



cwd = os.path.dirname(os.path.abspath(__file__))


print(f"\n\n\n cwd = {cwd} .\n\n\n")



global i


i = {}

i["i_class"] = i_principal_central.i_class()

i["i_class"].i_am_you()

i["i_class"].i_develope()




'''



'''



#i["i_class"].i_function("i")









print("\n\n\n---------------------------------------------------------------------------------------------------------------")

print("---------------------------------------------------------------------------------------------------------------")


print("\nprint_specific_amount\n\n")

path_0 = os.path.dirname(cwd)

var_0 = i["i_class"].print_specific_amount(element=["I", 10], folder=os.path.join(cwd, "new_folder"), folder_of_source_of_unity=cwd)

print(f"var_0 = {var_0}\n\n\n ---- \n")



var_0 = i["i_class"].print_specific_amount(element=["USD", 10], folder=os.path.join(cwd, "new_folder"), folder_of_source_of_unity=cwd)


print(f"var_0 = {var_0}")



print("\n\n\n---------------------------------------------------------------------------------------------------------------")

print("---------------------------------------------------------------------------------------------------------------")


print("\nprint_specific_amount\n\n")

path_0 = os.path.dirname(cwd)

var_0 = i["i_class"].print_specific_amount(element=["I", 11], folder=os.path.join(cwd, "new_folder"), folder_of_source_of_unity=cwd)

print(f"var_0 = {var_0}")






print("\n\n\n---------------------------------------------------------------------------------------------------------------")

print("---------------------------------------------------------------------------------------------------------------")

print("---------------------------------------------------------------------------------------------------------------")

print("i calculate how much there is in a specific folder .\n\n\n\n")




new_folder_2 = os.path.join(cwd, "new_folder")

print(f"from new_folder_2 = {new_folder_2} .")


i["i_i_calcul_from_folder"] = i["i_class"].i_calcul_from_folder(i_folder=new_folder_2)



#
#
#print("\n\n\n---------------------------------------------------------------------------------------------------------------")
#
#print("---------------------------------------------------------------------------------------------------------------")
#
#print("---------------------------------------------------------------------------------------------------------------")
#
#print("i get the list of the content of the unity-s of unity that i have here .\n\n\n\n")
#
#
#i["i_list_of_i_unity"] = i["i_class"].i_get_list_of_i_unity(folder_of_source_of_unity=cwd)
#
#
#print("i['i_list_of_i_unity'] = ", i["i_list_of_i_unity"])
#
#


#print("\n\n\n---------------------------------------------------------------------------------------------------------------")
#
#print("---------------------------------------------------------------------------------------------------------------")
#
#print("---------------------------------------------------------------------------------------------------------------")
#
#print("i get the list of the content of the unity-s of money that i have here .\n\n\n\n")
#
#
#
#
#i["i_list_of_i_money"] = i["i_class"].i_get_list_of_i_money(folder_of_source_of_unity=cwd)
#
#
#print("i['i_list_of_i_money'] = ", i["i_list_of_i_money"])
#
#


new_folder_2 = os.path.join(cwd, "new_folder_2")


i["i_class"].i_print_from_unity(i_unity="I", i_quantity=10, i_folder=new_folder_2, i_number=2, folder_of_source_of_unity=cwd)



#i["i_class"].i_print_from_money(i_unity="USD", i_quantity=10, i_folder=new_folder_2, i_number=2)




print("\n\n\n---------------------------------------------------------------------------------------------------------------")




print("\n\n\n re_arange\n\n\n")




path_0 = os.path.dirname(cwd)



new_folder_of_temporarly = os.path.join(path_0, "space_1")




var_of_re_arange = i["i_class"].re_arange(folder=new_folder_2, folder_of_temporarly=new_folder_of_temporarly, folder_of_source_of_unity=cwd)



print("\n\n\n---------------------------------------------------------------------------------------------------------------")

print("---------------------------------------------------------------------------------------------------------------")

print("---------------------------------------------------------------------------------------------------------------")

print("i calculate how much there is in a specific folder .\n\n\n\n")






print(f"from new_folder_2 = {new_folder_2} .")


i["i_i_calcul_from_folder"] = i["i_class"].i_calcul_from_folder(i_folder=new_folder_2)



print("i['i_i_calcul_from_folder'] = ", i["i_i_calcul_from_folder"])









print("\n\n\n---------------------------------------------------------------------------------------------------------------")

print("---------------------------------------------------------------------------------------------------------------")

print("---------------------------------------------------------------------------------------------------------------")

print("extract_cash .\n\n\n\n")




new_folder = os.path.join(cwd, "new_folder")



i["i_i_calcul_from_folder"] = i["i_class"].extract_cash(folder_from=new_folder_2, folder_to=new_folder, unity="I", quantity=9, folder_of_source_of_unity=cwd)


print(f"i['i_i_calcul_from_folder'] = {i["i_i_calcul_from_folder"]} .")



print("\n\n\n---------------------------------------------------------------------------------------------------------------")

print("---------------------------------------------------------------------------------------------------------------")

print("---------------------------------------------------------------------------------------------------------------")


print("i calculate how much there is in a specific folder .\n\n\n\n")

print(f"from new_folder = {new_folder} .")


i["i_i_calcul_from_folder"] = i["i_class"].i_calcul_from_folder(i_folder=new_folder)



print("i['i_i_calcul_from_folder'] = ", i["i_i_calcul_from_folder"])





i["i_list_of_dictionary"] = []

i["i_dict_to_list"] = list(i["i_i_calcul_from_folder"])


i["i_dict_to_list_1"] = list(i["i_i_calcul_from_folder"].items())

print(f"\n\n\ni['i_dict_to_list_1'] = {i["i_dict_to_list_1"]}\n\n\n")



i["i_counter"] = 0


while (i["i_counter"] < len(i["i_dict_to_list"])):
    
    
    if ((len(i["i_dict_to_list"][i["i_counter"]]) > len("TheQualityOf"))):
        
        if ((not (i["i_dict_to_list"][i["i_counter"]] in i["i_list_of_dictionary"]))):
       
            if ((i["i_dict_to_list"][i["i_counter"]][:len("TheQualityOf")] != "TheQualityOf")):
    
    
               i["i_list_of_dictionary"].append(i["i_dict_to_list"][i["i_counter"]])
    
    else:
    
        if ((not (i["i_dict_to_list"][i["i_counter"]] in i["i_list_of_dictionary"]))):
    
    
            i["i_list_of_dictionary"].append(i["i_dict_to_list"][i["i_counter"]])
    
    
    i["i_counter"] += 1
    
    

print("\n\n\n\ni['i_list_of_dictionary'] = ", i["i_list_of_dictionary"])









print("\n\n\n---------------------------------------------------------------------------------------------------------------")

print("---------------------------------------------------------------------------------------------------------------")

print("---------------------------------------------------------------------------------------------------------------")

print("i print aspecific number from the list of i money in a specific folder .\n\n\n\n")





i["i_class"].i_print_from_money(i_unity="USD", i_quantity=1, i_folder=os.path.join(cwd, "i", "i_main"), i_number=2, folder_of_source_of_unity=cwd)








print("\n\n\n---------------------------------------------------------------------------------------------------------------")

print("---------------------------------------------------------------------------------------------------------------")

print("---------------------------------------------------------------------------------------------------------------")

print("i print aspecific number from the list of i unity in a specific folder .\n\n\n\n")





i["i_class"].i_print_from_unity(i_unity="I", i_quantity=1, i_folder=os.path.join(cwd, "i", "i_main"), i_number=2, folder_of_source_of_unity=cwd)



i["i_class"].i_print_from_unity(i_unity="Point", i_quantity=1, i_folder=os.path.join(cwd, "i", "i_main"), i_number=2, folder_of_source_of_unity=cwd)










print("\n\n\n---------------------------------------------------------------------------------------------------------------")

print("---------------------------------------------------------------------------------------------------------------")

print("---------------------------------------------------------------------------------------------------------------")

print("i get all the qualtity-s that are disponible in a specific unity from money .\n\n\n\n")


i["i_list_of_unity_in_i_money"] = i["i_class"].i_get_quanity_from_money(i_unity="PowerSupplyMoney", folder_of_source_of_unity=cwd)


print("i['i_list_of_unity_in_i_money'] = ", i["i_list_of_unity_in_i_money"])











print("\n\n\n---------------------------------------------------------------------------------------------------------------")

print("---------------------------------------------------------------------------------------------------------------")

print("---------------------------------------------------------------------------------------------------------------")

print("i get all the qualtity-s that are disponible in a specific unity from unity .\n\n\n\n")


i["i_list_of_unity_in_i_unity"] = i["i_class"].i_get_quanity_from_unity(i_unity="Lust", folder_of_source_of_unity=cwd)



i["list_"] = list(i["i_list_of_unity_in_i_unity"].items())



i["list_sort-ed"] = i["list_"]


print("i['list_sort-ed'] = ", i["list_sort-ed"])









print("\n\n\n---------------------------------------------------------------------------------------------------------------")

print("---------------------------------------------------------------------------------------------------------------")

print("---------------------------------------------------------------------------------------------------------------")

print("i get all the qualtity-s that are disponible in a specific unity from a specific folder .\n\n\n\n")


i["i_list_of_unity_in_i_unity_from_folder"] = i["i_class"].i_get_quanity_of_unity_from_folder(i_unity="NotSleep", i_folder=os.path.join(cwd, "i", "i_unity"))



i["list_"] = list(i["i_list_of_unity_in_i_unity_from_folder"].items())



i["list_sort-ed"] = i["list_"]


print("i['list_sort-ed'] = ", i["list_sort-ed"])



















