




















import socket

import time

import threading







global i_semaphore_of_server_0_i, i_semaphore_of_client_0_i, i_counter_of_Byte_per_second_0_i


i_semaphore_of_server_0_i = True


i_semaphore_of_client_0_i = True





i_content_0_i = ""


i_counter_0_i = 0


while (i_counter_0_i < 10_000):
    
    
    i_content_0_i += "0"
    
    i_counter_0_i += 1
    
    
    



i_content_1_i = ""

i_counter_0_i = 0


while (i_counter_0_i < 1_000):
    
    
    i_content_1_i += i_content_0_i
    
    i_counter_0_i += 1
    
    
    





def server_program():
    
    
    global i_semaphore_of_server_0_i, i_semaphore_of_client_0_i, i_counter_of_Byte_per_second_0_i
    
    
    host = "127.0.0.1"   # localhost
    port = 5000          # أي رقم بين 1024 و 65535
    
    server_socket = socket.socket()
    server_socket.bind((host, port))

    # استماع لاتصالات قادمة
    server_socket.listen(1)
    print(f"🚀 Server يعمل على {host}:{port} وينتظر اتصال ...")

    conn, address = server_socket.accept()
    print("✅ تم الاتصال من:", address)
    
    i_t_1_i = time.time()
    
    i_message_0_i = ""
    
    while True:
        data = conn.recv(len(i_content_1_i)).decode()   # استقبل رسالة من العميل
        if not data:
            break
        #print("📩 رسالة من العميل:", data)
        
        i_message_0_i += data
        
        #reply = input("💬 رد السيرفر: ")  # رد من السيرفر
        #conn.send(reply.encode())
    
    
    i_t_2_i = time.time()
    
    speed = len(i_message_0_i) // (i_t_2_i - i_t_1_i)
    
    print(f"time = {i_t_2_i - i_t_1_i} second . len(i_message_0_i) = {len(i_message_0_i)} . speed = {speed} Byte per second .")
    
    i_counter_of_Byte_per_second_0_i = speed
    
    
    conn.close()
    
    i_semaphore_of_server_0_i = False
    
    
    print(f"i_semaphore_of_server_0_i = {i_semaphore_of_server_0_i} .")
    








def client_program():
    
    
    global i_semaphore_of_server_0_i, i_semaphore_of_client_0_i, i_counter_of_Byte_per_second_0_i
    
    
    
    host = "127.0.0.1"  # نفس الـ host للسيرفر
    port = 5000         # نفس البورت

    client_socket = socket.socket()
    client_socket.connect((host, port))

    message = i_content_1_i
    
    while message.lower().strip() != 'quit':
        client_socket.send(message.encode())     # أرسل الرسالة
        #data = client_socket.recv(1024).decode() # استقبل الرد
        #print("📩 رد السيرفر:", data)

        message = "quit"
        
    client_socket.close()
    
    i_semaphore_of_client_0_i = False
    
    print(f"i_semaphore_of_client_0_i = {i_semaphore_of_client_0_i} .")
    
    
    



def i_emeter_0_i():
    
    
    
    
    
    client_program()
    
    
    
    









def i_receiver_0_i():
    
    
    # server :
    
    
    
    server_program()
    
    
    



def i_wait_0_i(amount_of_time):
    
    
    time.sleep(amount_of_time)
    
    
    



def i_tester_of_speed_of_transfer_0_i():
    
    
    
    i_p_2_i = threading.Thread(target=i_receiver_0_i, daemon=True).start()
    
    
    i_wait_0_i(amount_of_time=3.0)
    
    
    i_p_1_i = threading.Thread(target=i_emeter_0_i, daemon=True).start()
    
    
    while ((i_semaphore_of_server_0_i == True) or (i_semaphore_of_client_0_i == True)):
        
        
        pass
        
        
        
        
    
    
    
    
    return i_counter_of_Byte_per_second_0_i
    
    
    
    
    



if __name__ == "__main__":
    
    
    
    i_counter_of_Byte_per_second_0_i = i_tester_of_speed_of_transfer_0_i()
    
    
    print(f"i_counter_of_Byte_per_second_0_i = {i_counter_of_Byte_per_second_0_i} Byte per second .")
    
    
    













