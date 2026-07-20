
























global i

i = {}


i["pricipal-central"] = "i am here"


i["i am you"] = True


if (i["i am you"] == True):


    # i_Economic_Partner_official_receiver_with_wifi_0.py


    '''
    
    
        If you are in a certain situation and you want to transfer money from one place to another. 
        
        Then you should use this program. First you should send the money (files) from the sender to 
        
        the receiver. Then delete those files from the sender so that the files are now present in the 
        
        receiver. Now replace ___folder_of_files_that_have_been_received_into_it___ to the link of folder of files that have been received into it from sender .
    
        and replace ___folder_of_organize_the_money_in_it___ to folder of organize my money in it .
        
        so than run this program it will save you from errors .
        
    
    
    
    
    '''








    import os

    import socket

    import time

    import traceback

    from pathlib import Path










    i["i_cwd"] = os.getcwd()







    def i_number_to_str(i_number):


        global i

        i["i_string_of_i_number_to_str_0"] = str(i_number)

        i["i_counter_of_i_number_to_str_4"] = len(i["i_string_of_i_number_to_str_0"]) - 1

        i["i_counter_of_i_number_to_str_5"] = 0

        i["i_string_of_i_number_to_str_1"] = ""

        while (i["i_counter_of_i_number_to_str_4"] >= 0):

            if (i["i_counter_of_i_number_to_str_5"] == 3):

                i["i_string_of_i_number_to_str_1"] = "_" + i["i_string_of_i_number_to_str_1"]

                i["i_counter_of_i_number_to_str_5"] = 0

            i["i_string_of_i_number_to_str_1"] = i["i_string_of_i_number_to_str_0"][i["i_counter_of_i_number_to_str_4"]] + i["i_string_of_i_number_to_str_1"]


            i["i_counter_of_i_number_to_str_4"] -= 1

            i["i_counter_of_i_number_to_str_5"] += 1


        return i["i_string_of_i_number_to_str_1"]





    def i_get_ip_of_wifi():


        i_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        try:

            i_s.connect(("8.8.8.8", 80))

            i_ip = i_s.getsockname()[0]

        except Exception:

            i_ip = "NULL"

        finally:

            i_s.close()

        return i_ip






    i["i_semaphore"] = False



    try:


        try:

            i["i_folder_for_receive"] = os.path.join(i["i_cwd"], "i_folder_for_receive")

            os.mkdir(i["i_folder_for_receive"])


        except Exception as i_e:


            i["i_semaphore_1"] = True




        try:

            i["i_folder_of_history"] = os.path.join(i["i_cwd"], "i_folder_for_receive", "i_folder_of_history")

            os.mkdir(i["i_folder_of_history"])


        except Exception as i_e:


            i["i_semaphore_1"] = True



        try:


            i["i_folder_for_send"] = os.path.join(i["i_cwd"], "i_folder_for_send")

            os.mkdir(i["i_folder_for_send"])


        except Exception as i_e:


            i["i_semaphore_1"] = True





        i["i_t1"] = time.time()
        




        #i["folder_of_files_that_have_been_received_into_it"] = "___folder_of_files_that_have_been_received_into_it___"
        
        
        i["folder_of_files_that_have_been_received_into_it"] = r"___folder_of_files_that_have_been_received_into_it___"
        
        
        #i["folder_of_organize_the_money_in_it"] = "___folder_of_organize_the_money_in_it___"
        
        
        
        
        i["folder_of_organize_the_money_in_it"] = r"___folder_of_organize_the_money_in_it___"
        
        
        i["i_folder_for_receive"] = i["folder_of_organize_the_money_in_it"]
        
        
        


        i["i_file-s"] = []


        for root, dirs, i["i_file-s"] in os.walk(i["folder_of_files_that_have_been_received_into_it"]):

            break
        
        
        
        
        
        




        if (len(i["i_file-s"]) > 0):





            i["i_counter"] = 0


            while (i["i_counter"] < len(i["i_file-s"])):




                
                


                i["i_name_of_file"] = i["i_file-s"][i["i_counter"]]



                i["i_file"] = i["i_file-s"][i["i_counter"]]
                
                
                
                

                i["i_v"] = i["i_name_of_file"].split(".")

                if (os.path.exists(os.path.join(i["i_folder_for_receive"], i["i_file"]))):


                    i["i_counter_2"] = len(i["i_v"][0]) - 1

                    
                    while ((i["i_counter_2"] > 0) and ((i["i_v"][0])[i["i_counter_2"]] != "_")):

                        i["i_counter_2"] -= 1




                    try:

                        i["i_v_1"] = i["i_v"][0][:i["i_counter_2"]]

                        i["i_counter_1"] = int((i["i_v_1"])[i["i_counter_2"] + 1:])



                        i["i_v"][0] = i["i_v"][0][:i["i_counter_2"]]


                    except:

                        i["i_counter_1"] = 0






                    while (os.path.exists(os.path.join(i["i_folder_for_receive"], i["i_v"][0] + "_" + str(i["i_counter_1"]) + "." + i["i_v"][1]))):

                        i["i_counter_1"] += 1


                    i["i_file"] = os.path.join(i["i_folder_for_receive"], i["i_v"][0] + "_" + str(i["i_counter_1"]) + "." + i["i_v"][1])



                    #print(f"i_hello . i['i_name_of_file'] = {i["i_name_of_file"]} . i['i_file'] = {i["i_file"]} .")


                else:
                
                
                    i["i_file"] =  os.path.join(i["i_folder_for_receive"], i["i_file"]) 


                    #print(f"i_hello_1 . i['i_name_of_file'] = {i["i_name_of_file"]} . i['i_file'] = {i["i_file"]} .")


                i["i_d_1"] = Path(os.path.join(i["folder_of_files_that_have_been_received_into_it"], i["i_file-s"][i["i_counter"]]))

                i["i_d"] = Path(i["i_file"])

                i["i_d"].write_bytes(i["i_d_1"].read_bytes())


                i["i_counter"] += 1



            try:

                i["i_calcul"] = {}


                i["i_counter"] = 0


                while (i["i_counter"] < len(i["i_file-s"])):

                    
                    try:

    
    
                        i["i_quantity"] = 0
    
                        i["i_v_1"] = (i["i_file-s"][i["i_counter"]]).split("quantity_")
    
    
                        i["i_v_1"] = i["i_v_1"][1].split("_")
    
                        try:
    
                            i["i_quantity"] = int(i["i_v_1"][0])
    
                        except:
    
                            i["i_semaphore_5"] = True
    
    
                        i["i_v_1"] = (i["i_file-s"][i["i_counter"]]).split("unity_")
    
                        i["i_v_1"] = i["i_v_1"][1].split("_")
    
                        i["i_unity"] = i["i_v_1"][0]
    
    
    
    
    
                        if (i["i_unity"] in i["i_calcul"]):
    
                            i["i_calcul"][i["i_unity"]] += i["i_quantity"]
    
                        else:
    
                            i["i_calcul"][i["i_unity"]] = i["i_quantity"]


                    except:
                    
                        i["i_semaphore_4"] = True




                    i["i_counter"] += 1

                i["i_string_of_i_calcul"] = ""

                i["i_string_of_i_calcul"] += time.strftime("\n\n{receive : ' %Y/%m/%d %H:%M:%S ' : \n\n    ")

                print("i . ", time.strftime("' %Y/%m/%d %H:%M:%S '"), " . i['i_calcul'] ==  {")
                
                for i["i_unity"] in i["i_calcul"]:


                    i["i_string_of_i_calcul"] += "     '" + i["i_unity"] + "' : " + i_number_to_str(i["i_calcul"][i["i_unity"]]) + " ,"
                    
                    print("     '", i["i_unity"], "' : ", i_number_to_str(i["i_calcul"][i["i_unity"]]), " ,")


                i["i_string_of_i_calcul"] += "    \n\n}\n\n,\n\n"
                
                print("    }")




                try:

                    i["i_file_of_history_of_receive"] = os.path.join(os.getcwd(), "i_file_of_history_of_receive.txt")

                    i["i_d"] = Path(i["i_file_of_history_of_receive"])

                    i["i_content"] = i["i_d"].read_text()

                    i["i_content"] = i["i_string_of_i_calcul"] + i["i_content"]
                    
                    i["i_d"].write_text(i["i_content"])

                except:

                    i["i_semaphore_2"] = True

                    i["i_file_of_history_of_receive"] = os.path.join(os.getcwd(), "i_file_of_history_of_receive.txt")

                    i["i_d"] = Path(i["i_file_of_history_of_receive"])

                    i["i_content"] = i["i_string_of_i_calcul"]
                    
                    i["i_d"].write_text(i["i_content"])


            except:


                i["i_semaphore_3"] = True



        i["i_t2"] = time.time()


        print("i . file-s receive-ed with success . i_time = ", i["i_t2"] - i["i_t1"], " second")




        print("i . the operation is finish-ed with success .")


    except Exception as i_e:


        i["i_semaphore"] = True

        print("i . i_e = ", i_e)

        traceback.print_exc()

        i_e_ = str(traceback.format_exc())

        print("i . i_e_ = ", i_e_)



    print("i['i_semaphore'] = ", i["i_semaphore"])



    print("finish .")











                
                

                

                
                

                