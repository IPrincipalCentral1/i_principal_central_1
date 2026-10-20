






























global i

i = {}





'''







hello i am principal central 



i want to show you how to use the liberary in language of python 'i_principal_central'


and how to send file-s in wifi with that library and receive 


both device-s should have those 2 file-s : 'receiver' and 'sender'



so the receiver should be run-ing first :

and the folder of send in the sender should contain the file-s to send 


now you see the number that are in the receiver '192.168.43.207'


he should be in the program of sender 


right here


so than the send start 


after the connection between the wifi of the sender and the wifi of the receiver



and let see


now let see the folder of receive in the receiver 




and the file of history will apare


i have-ed before do that that is why there is a lot of history 


and the history is with calculation 

it mean 




{' 2025/05/06 18:40:07 ' : 

        'USD' : 400 ,     'DZD' : 4_000 ,    

}



i receive-ed '400 USD' and '4000 DZD'

money




and some-thing :


my format of print-ing money is strict

that is why i calculate with precision my money because it is i who do that 



and now let send those file-s back :


i should copy the file-s from the folder of receive to the folder of send .

you can pause the video and see with detail what you want .


now in order to do this operation the receiver in the other side should be run-ing first .


do you see the number that apare '10.192.233.96'


this number should be in the program of the sender .


right here 


you should copy it exactly and the 2 device-s should be connect-ed with wifi so than the operation can be .



now execute the program of sender 


you will find that the receiver receive-ed the file-s 

and this is tha operation with success ...........................................................................................






'''






i["pricipal-central"] = "i am here"






i["i am you"] = True


if (i["i am you"] == True):


    # i_Economic_Partner_official_receiver_with_wifi_0.py




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



    

    i["i_ip_of_wifi_of_receiver"] = i_get_ip_of_wifi()

    # i["i_ip_of_wifi_of_receiver"] = i_get_public_ip()

    print("\ni . i_ip_of_wifi_of_receiver = ", i["i_ip_of_wifi_of_receiver"])



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







        i["server_socket"] = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        i["server_socket"].bind((i["i_ip_of_wifi_of_receiver"], 12345))
        
        i["server_socket"].listen(1)
        

        print("i . start receiver with success .")



        i["client_socket"], i["client_address"] = i["server_socket"].accept()

        print("i . connect with sender ", i["client_address"]," success .")


        i["i_t1"] = time.time()
        










        i["i_number_of_file-s_byte-s"] = i["client_socket"].recv(8)

        i["i_number_of_file-s"] = int.from_bytes(i["i_number_of_file-s_byte-s"], 'big')




        if (i["i_number_of_file-s"] > 0):

            i["i_file-s"] = []


            i["i_counter"] = 0


            while (i["i_counter"] < i["i_number_of_file-s"]):



                i["i_length_of_name_file_in_byte-s"] = i["client_socket"].recv(8)

                i["i_length_of_name_file"] = int.from_bytes(i["i_length_of_name_file_in_byte-s"], 'big')



                i["i_name_of_file"] = ""

                while len(i["i_name_of_file"]) < i["i_length_of_name_file"]:

                    i["chunk"] = i["client_socket"].recv(1).decode('utf-8')
                    
                    if not i["chunk"]:

                        break

                    i["i_name_of_file"] += i["chunk"]

                    

                i["i_file-s"].append(i["i_name_of_file"])



                i["i_size_of_file_in_byte-s"] = i["client_socket"].recv(8)

                i["i_size_of_file"] = int.from_bytes(i["i_size_of_file_in_byte-s"], 'big')

                print("i . i['i_size_of_file'] = ", i["i_size_of_file"], " . i['i_counter'] = ", i["i_counter"])


                i["i_received_data"] = b''

                while len(i["i_received_data"]) < i["i_size_of_file"]:



                    if (len(i["i_received_data"]) < i["i_size_of_file"] - 10_000_000):

                        i["chunk"] = i["client_socket"].recv(10_000_000)


                    elif (len(i["i_received_data"]) < i["i_size_of_file"] - 1_000_000):

                        i["chunk"] = i["client_socket"].recv(1_000_000)


                    elif (len(i["i_received_data"]) < i["i_size_of_file"] - 100_000):

                        i["chunk"] = i["client_socket"].recv(100_000)


                    elif (len(i["i_received_data"]) < i["i_size_of_file"] - 10_000):

                        i["chunk"] = i["client_socket"].recv(10_000)


                    elif (len(i["i_received_data"]) < i["i_size_of_file"] - 1_000):

                        i["chunk"] = i["client_socket"].recv(1_000)


                    elif (len(i["i_received_data"]) < i["i_size_of_file"] - 100):

                        i["chunk"] = i["client_socket"].recv(100)


                    elif (len(i["i_received_data"]) < i["i_size_of_file"] - 10):

                        i["chunk"] = i["client_socket"].recv(10)

                    else:

                        i["chunk"] = i["client_socket"].recv(1)
                    
                    if not i["chunk"]:

                        break

                    i["i_received_data"] += i["chunk"]

                i["i_file"] = os.path.join(i["i_folder_for_receive"], i["i_name_of_file"])

                i["i_v"] = i["i_name_of_file"].split(".")

                if (os.path.exists(i["i_file"])):


                    i["i_counter_2"] = len(i["i_v"][0]) - 1

                    
                    while ((i["i_counter_2"] > 0) and ((i["i_v"][0])[i["i_counter_2"]] != "_")):

                        i["i_counter_2"] -= 1




                    try:

                        i["i_v"][0] = i["i_v"][0][:i["i_counter_2"]]

                        i["i_counter_1"] = int((i["i_v"][0])[i["i_counter_2"] + 1:])


                    except:

                        i["i_counter_1"] = 0






                    while (os.path.exists(os.path.join(i["i_folder_for_receive"], i["i_v"][0] + "_" + str(i["i_counter_1"]) + "." + i["i_v"][1]))):

                        i["i_counter_1"] += 1


                    i["i_file"] = os.path.join(i["i_folder_for_receive"], i["i_v"][0] + "_" + str(i["i_counter_1"]) + "." + i["i_v"][1])




                i["i_d"] = Path(i["i_file"])

                i["i_d"].write_bytes(i["i_received_data"])


                i["i_counter"] += 1



            try:

                i["i_calcul"] = {}


                i["i_counter"] = 0


                while (i["i_counter"] < len(i["i_file-s"])):


                    i["i_quantity"] = 0

                    i["i_v_1"] = (i["i_file-s"][i["i_counter"]]).split("quantity_")


                    i["i_v_1"] = i["i_v_1"][1].split("_")

                    try:

                        i["i_quantity"] = int(i["i_v_1"][0])

                    except:

                        i["i_semaphore"] = True


                    i["i_v_1"] = (i["i_file-s"][i["i_counter"]]).split("unity_")

                    i["i_v_1"] = i["i_v_1"][1].split("_")

                    i["i_unity"] = i["i_v_1"][0]





                    if (i["i_unity"] in i["i_calcul"]):

                        i["i_calcul"][i["i_unity"]] += i["i_quantity"]

                    else:

                        i["i_calcul"][i["i_unity"]] = i["i_quantity"]

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

                    i["i_file_of_history_of_receive"] = os.path.join(i["i_cwd"], "i_file_of_history_of_receive.txt")

                    i["i_d"] = Path(i["i_file_of_history_of_receive"])

                    i["i_content"] = i["i_d"].read_text()

                    i["i_content"] = i["i_string_of_i_calcul"] + i["i_content"]
                    
                    i["i_d"].write_text(i["i_content"])

                except:

                    i["i_semaphore_2"] = True

                    i["i_file_of_history_of_receive"] = os.path.join(i["i_cwd"], "i_file_of_history_of_receive.txt")

                    i["i_d"] = Path(i["i_file_of_history_of_receive"])

                    i["i_content"] = i["i_string_of_i_calcul"]
                    
                    i["i_d"].write_text(i["i_content"])


            except:


                i["i_semaphore_3"] = True



        i["i_t2"] = time.time()


        print("i . file-s receive-ed with success . i_time = ", i["i_t2"] - i["i_t1"], " second ")



        i["client_socket"].close()

        i["server_socket"].close()

        print("i . the operation is finish-ed with success .")


    except Exception as i_e:


        i["i_semaphore"] = True

        print("i . i_e = ", i_e)

        traceback.print_exc()

        i_e_ = str(traceback.format_exc())

        print("i . i_e_ = ", i_e_)



    print("i['i_semaphore'] = ", i["i_semaphore"])



    print("finish .")











                
                

                

                
                

                