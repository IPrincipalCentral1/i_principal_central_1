










import os



cwd = os.path.dirname(os.path.abspath(__file__))







# section of function and procedure 



def execute_command_0(command_0):
    
        
    
    #command_0 = f"nasm -felf64 {name_of_file_0}.asm -o {name_of_file_0}.o" 
    
    print(f"\n\n{command_0}")
    
    os.system(command_0)
    
    
    
    


def execute_list_of_command_0(list_of_command_0):
    
    
    
    i_counter_0 = 0
    
    while (i_counter_0 < len(list_of_command_0)):
        
        
        execute_command_0(command_0=list_of_command_0[i_counter_0])
        
        i_counter_0 += 1
        
    
    
    
    







def main():

    
    
    
    content_of_file_0 = r"""
    
    
    
    
    ; file: hello.asm
    ; هدفه: طباعة i_hello على الطرفية ثم الخروج
    
    BITS 64
    
    section .data
        msg     db  "i_hello", 10      ; أضفت سطر جديد (LF). احذف الـ 10 إن كنت لا تريده.
        msg_len equ $ - msg
    
    section .text
        global _start
    
    _start:
        ; write(1, msg, msg_len)
        mov     rax, 1          ; رقم syscall للـ write
        mov     rdi, 1          ; fd = 1 (stdout)
        mov     rsi, msg        ; المؤشر إلى الرسالة
        mov     rdx, msg_len    ; طول الرسالة
        syscall                 ; نفّذ نداء النظام
    
        ; exit(0)
        mov     rax, 60         ; رقم syscall للـ exit
        xor     rdi, rdi        ; status = 0
        syscall
    
    
    
    
    
    
    """
    
    
    
    
    
    
    
    
    '''
    
    nasm -felf64 hello.asm -o hello.o
    ld hello.o -o hello
    ./hello
    
    
    
    
    
    
    '''
    
    
    
    name_of_file_0 = "i_file_0"
    
    file_of_assembly_0 = os.path.join(cwd, f"{name_of_file_0}.asm")
    
    
    with open(file_of_assembly_0, "w") as f_:
        
        f_.write(content_of_file_0)
        
    
    
    
    list_of_command_0 = [
                        
                        f"nasm -felf64 {name_of_file_0}.asm -o {name_of_file_0}.o",
                        
                        f"ld {name_of_file_0}.o -o {name_of_file_0}",
                        
                        f"./{name_of_file_0}",
                        
                        
                        ]
    
    
    list_of_command_1 = [
                        
                        
                        
                        f"readelf -S {name_of_file_0}.o",
                        
                        f"objdump -d {name_of_file_0}.o",
                        
                        f"objdump -d -M intel -m i386:x86-64 {name_of_file_0}.o",
                        
                        
                        f"hexdump -C {name_of_file_0}.o",
                        
                        
                        
                        ]
    
    
    


    #command_0 = f"nasm -felf64 {name_of_file_0}.asm -o {name_of_file_0}.o" 

    #execute_command_0(command_0=command_0)


    #command_1 = f"ld {name_of_file_0}.o -o {name_of_file_0}"

    #execute_command_0(command_0=command_1)


    #command_2 = f"./{name_of_file_0}"

    #execute_command_0(command_0=command_2)

    
    
    
    execute_list_of_command_0(list_of_command_0=list_of_command_0)
    
    
    print("\n" * 10)
    
    
    
    execute_list_of_command_0(list_of_command_0=list_of_command_1)
    

    #command_3 = f"readelf -S {name_of_file_0}.o"

    #execute_command_0(command_0=command_3)
    
    
    
    






if __name__ == "__main__":
    
    
    main()
    
    
    
    










    
    



