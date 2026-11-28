


















'''




this is a good example of how to use my mixer





Suppose we want to mix, for example: (water, stone, air).

We must arrange these objects in sequential order. For example:



{

"water" : 0

"stone" : 1

"air"   : 2

}


Then we create a range from 0 to 2 .


Then we place only the number 2 in position i_number_of_element__minus_1__0_i .



and then we have many mix :
    
    
    [] : nothing 
    
    [0] : ["water"]
    
    [1] : ["stone"]
    
    [2] : ["air"]
    
    [0, 0] : ["water", "water"]
    
    [1, 0] : ["stone", "water"]
    
    
    ...
    
    and so on 
    
    



we allways start from : 
    
    
    [] : nothing 
    
    




if you want to use it do like this :
    
    
    
    
    import i_my_mixer_1_i
    
    
    
    i_list_0_i = []
    
    
    i_number_of_element__minus_1__0_i = 2
    
    
    
    i_list_0_i = i_my_mixer_1_i.i_next_step_0_i(i_list_0_i=i_list_0_i, i_number_of_element__minus_1__0_i=i_number_of_element__minus_1__0_i)
    
    
    
    
    
    
    
    

if you want to start from a point . like for example :
    
    
    [0, 0, 0]
    
    


do like that :
    
    
    
    
    
    import i_my_mixer_1_i
    
    
    
    i_number_of_element__minus_1__0_i = 2
    
    
    
    i_list_0_i = [0, 0, 0] # right here you do the init . condition : all( [ (  0 <= i_list_0_i[i_counter_0_i] <= i_number_of_element__minus_1__0_i ) for i_counter_0_i in range(0, len(i_list_0_i)) ] )
    
    
    
    
    i_list_0_i = i_my_mixer_1_i.i_next_step_0_i(i_list_0_i=i_list_0_i, i_number_of_element__minus_1__0_i=i_number_of_element__minus_1__0_i)
    
    
    

    









'''
























































































import copy








def i_next_step_0_i(i_list_0_i, i_number_of_element__minus_1__0_i):
    
    
    
    '''
    
    this is everything number 0 .
    
    
    
    '''
    
    
    i_counter_0_i = 0
    
    
        
    
    i_semaphore_of_add_0_i = True
    
    
    
    while ((i_counter_0_i < len(i_list_0_i)) and (i_semaphore_of_add_0_i == True)):
        
        
        if (i_list_0_i[i_counter_0_i] > i_number_of_element__minus_1__0_i):
            
            
            i_list_0_i[i_counter_0_i] = 0
            
            
            i_counter_0_i += 1
            
            
            
            
            
            
        else:
            
            
            i_list_0_i[i_counter_0_i] += 1
            
            if (i_list_0_i[i_counter_0_i] <= i_number_of_element__minus_1__0_i):
                
                
                i_semaphore_of_add_0_i = False
                
                
            
        
        
    
    if (i_semaphore_of_add_0_i == True):
        
        
        
        i_list_0_i.append(0)
        
        
        
        
        
    
    return i_list_0_i












def i_next_step_1_i(i_list_0_i, i_number_of_element__minus_1__0_i):
    
    
    
    '''
    
    this is everything number 1 .
    
    
    
    '''
    
    
    i_counter_0_i = len(i_list_0_i) - 1
    
    
    
    i_semaphore_of_add_0_i = True
    
    
    
    while ((i_counter_0_i >= 0) and (i_semaphore_of_add_0_i == True)):
        
        
        if (i_list_0_i[i_counter_0_i] > i_number_of_element__minus_1__0_i):
            
            
            i_list_0_i[i_counter_0_i] = 0
            
            
            i_counter_0_i -= 1
            
            
            
        else:
            
            
            i_list_0_i[i_counter_0_i] += 1
            
            if (i_list_0_i[i_counter_0_i] <= i_number_of_element__minus_1__0_i):
                
                
                i_semaphore_of_add_0_i = False
                
                
            
        
        
    
    if (i_semaphore_of_add_0_i == True):
        
        
        
        i_list_0_i.insert(0, 0)
        
        
        
        
    
    return i_list_0_i











def i_next_step_2_i(i_list_0_i, i_number_of_element__minus_1__0_i):
    
    
    
    '''
    
    this is everything number 2 .
    
    
    
    '''
    
    
    i_counter_0_i = 0
    
    
        
    
    i_semaphore_of_add_0_i = True
    
    
    
    while ((i_counter_0_i < len(i_list_0_i)) and (i_semaphore_of_add_0_i == True)):
        
        
        if (i_list_0_i[i_counter_0_i] <= 0):
            
            
            i_list_0_i[i_counter_0_i] = i_number_of_element__minus_1__0_i
            
            
            i_counter_0_i += 1
            
            
            
            
            
        else:
            
            
            i_list_0_i[i_counter_0_i] -= 1
            
            if (i_list_0_i[i_counter_0_i] >= 0):
                
                
                i_semaphore_of_add_0_i = False
                
                
            
        
        
    
    if (i_semaphore_of_add_0_i == True):
        
        
        
        i_list_0_i.append(i_number_of_element__minus_1__0_i)
        
        
        
        
        
    
    return i_list_0_i












def i_next_step_3_i(i_list_0_i, i_number_of_element__minus_1__0_i):
    
    
    
    '''
    
    this is everything number 3 .
    
    
    
    '''
    
    
    i_counter_0_i = len(i_list_0_i) - 1
    
    
    
    i_semaphore_of_add_0_i = True
    
    
    
    while ((i_counter_0_i >= 0) and (i_semaphore_of_add_0_i == True)):
        
        
        if (i_list_0_i[i_counter_0_i] <= 0):
            
            
            i_list_0_i[i_counter_0_i] = i_number_of_element__minus_1__0_i
            
            
            i_counter_0_i -= 1
            
            
            
            
            
        else:
            
            
            i_list_0_i[i_counter_0_i] -= 1
            
            if (i_list_0_i[i_counter_0_i] >= 0):
                
                
                i_semaphore_of_add_0_i = False
                
                
            
        
        
    
    if (i_semaphore_of_add_0_i == True):
        
        
        
        i_list_0_i.insert(0, i_number_of_element__minus_1__0_i)
        
        
        
        
    
    return i_list_0_i
















def i_next_step_in_asm_0_i(i_list_0_i, i_number_of_element__minus_1__0_i, i_capacity_of_list_0_i):
    
    
    
    '''
        
        this is everything number 0 .
        
        in asm .
        
        
        
    '''
    
    
    
    if i_capacity_of_list_0_i < len(i_list_0_i):
        
        raise ValueError("Capacity is smaller than list length.")
        
    
    
    
    
    
    
    
    i_content_0_i = r"""




default rel

global main

extern printf


section .data

; =====================================================
; INPUTS: MODIFY YOUR INPUTS HERE
; =====================================================

i_list_0_i:
    dq _____i_list_0_i_____

i_list_0_i_length:
    dq _____i_list_0_i_length_____

i_number_of_element__minus_1__0_i:
    dq _____i_number_of_element__minus_1__0_i_____

i_list_0_i_capacity:
    dq _____i_list_0_i_capacity_____


; =====================================================
; PRINT FORMAT
; =====================================================

i_print_number_0_i:
    db "%ld", 0

i_print_separator_0_i:
    db ", ", 0

i_print_start_0_i:
    db "i_list_0_i = [", 0

i_print_end_0_i:
    db "]", 10, 0


section .text


main:

    ; =================================================
    ; CALL i_next_step_0_i
    ; =================================================

    lea rdi, [i_list_0_i]
    lea rsi, [i_list_0_i_length]
    mov rdx, [i_number_of_element__minus_1__0_i]
    mov rcx, [i_list_0_i_capacity]

    call i_next_step_0_i


    ; =================================================
    ; PRINT LIST
    ; =================================================

    lea rdi, [i_print_start_0_i]
    xor eax, eax
    call printf


    xor r12, r12

print_loop_0_i:

    mov rax, [i_list_0_i_length]

    cmp r12, rax
    jge print_end_0_i


    ; Print current element

    lea rdi, [i_print_number_0_i]

    mov rsi, [i_list_0_i + r12*8]

    xor eax, eax
    call printf


    ; Determine whether to print separator

    mov rax, [i_list_0_i_length]

    inc r12

    cmp r12, rax
    jge print_loop_0_i


    lea rdi, [i_print_separator_0_i]

    xor eax, eax
    call printf

    jmp print_loop_0_i


print_end_0_i:

    lea rdi, [i_print_end_0_i]

    xor eax, eax
    call printf


    ; Return 0

    xor eax, eax
    ret



; =====================================================
; FUNCTION: i_next_step_0_i
;
; Input:
; RDI = list address
; RSI = address of list length
; RDX = maximum element
; RCX = list capacity
;
; =====================================================

i_next_step_0_i:

    ; Save registers that we need to preserve

    push rbx
    push r12
    push r13
    push r14
    push r15


    ; -------------------------------------------------
    ; Store input values
    ; -------------------------------------------------

    mov r12, rdi
    mov r13, rsi
    mov r14, rdx
    mov r15, rcx


    ; -------------------------------------------------
    ; i_counter_0_i = 0
    ; -------------------------------------------------

    xor rbx, rbx


    ; -------------------------------------------------
    ; i_semaphore_of_add_0_i = True
    ;
    ; R10 = 1 means True
    ; R10 = 0 means False
    ; -------------------------------------------------

    mov r10, 1


while_0_i:


    ; =================================================
    ; while (
    ;     counter < list_length
    ;     and semaphore == True
    ; )
    ; =================================================

    mov rax, [r13]

    cmp rbx, rax
    jge end_while_0_i


    cmp r10, 1
    jne end_while_0_i


    ; =================================================
    ; if list[counter] > maximum
    ; =================================================

    mov rax, [r12 + rbx*8]

    cmp rax, r14

    jg if_greater_0_i


    ; =================================================
    ; ELSE:
    ; list[counter] += 1
    ; =================================================

    inc qword [r12 + rbx*8]


    ; =================================================
    ; if list[counter] <= maximum:
    ;
    ; semaphore = False
    ; =================================================

    mov rax, [r12 + rbx*8]

    cmp rax, r14

    jg continue_0_i


    mov r10, 0


continue_0_i:

    jmp while_0_i


    ; =================================================
    ; IF list[counter] > maximum
    ;
    ; list[counter] = 0
    ; counter += 1
    ; =================================================

if_greater_0_i:

    mov qword [r12 + rbx*8], 0

    inc rbx

    jmp while_0_i



end_while_0_i:


    ; =================================================
    ; if semaphore == True:
    ;     list.append(0)
    ; =================================================

    cmp r10, 1
    jne no_append_0_i


    ; -------------------------------------------------
    ; Check capacity before appending
    ; -------------------------------------------------

    mov rax, [r13]

    cmp rax, r15
    jge no_append_0_i


    ; -------------------------------------------------
    ; list[length] = 0
    ; -------------------------------------------------

    mov qword [r12 + rax*8], 0


    ; -------------------------------------------------
    ; length += 1
    ; -------------------------------------------------

    inc qword [r13]


no_append_0_i:


    ; =================================================
    ; Restore registers
    ; =================================================

    pop r15
    pop r14
    pop r13
    pop r12
    pop rbx

    ret


section .note.GNU-stack noalloc noexec nowrite progbits


"""
    
    
    
    i_v_0_i = ""
    
    
    i_counter_0_i = 0
    
    while (i_counter_0_i < len(i_list_0_i) - 1):
        
        
        i_v_0_i += str(i_list_0_i[i_counter_0_i]) + ", "
        
        
        i_counter_0_i += 1
        
        
    
    
    
    i_v_0_i += str(i_list_0_i[i_counter_0_i])
    
    
    
    
    
    # =====================================================
    # RESERVE THE REMAINING CAPACITY
    # =====================================================
    
    i_number_of_remaining_elements_0_i = (
        i_capacity_of_list_0_i - len(i_list_0_i)
    )
    
    
    if (i_number_of_remaining_elements_0_i > 0):
    
        i_v_0_i += (
            "\n\n"
            + "    times "
            + str(i_number_of_remaining_elements_0_i)
            + " dq 0"
        )
    
    
    i_content_0_i = i_content_0_i.replace("_____i_list_0_i_____", i_v_0_i)
    
    
    i_content_0_i = i_content_0_i.replace("_____i_list_0_i_length_____", str(len(i_list_0_i)))
    
    
    i_content_0_i = i_content_0_i.replace("_____i_number_of_element__minus_1__0_i_____", str(i_number_of_element__minus_1__0_i))
    
    
    i_content_0_i = i_content_0_i.replace("_____i_list_0_i_capacity_____", str(i_capacity_of_list_0_i))
    
    
    
    
    
    
    
    i_name_0_i = "i_main_4_i"
    
    
    i_file_0_i = os.path.join(cwd, i_name_0_i + ".asm")
    
    
    i_d_0_i = Path(i_file_0_i)
    
    
    i_d_0_i.write_text(i_content_0_i)
    
    
    
    
    os.system(f"nasm -f elf64 {i_name_0_i}.asm -o {i_name_0_i}.o")
    
    
    os.system(f"gcc -no-pie {i_name_0_i}.o -o {i_name_0_i}")
    
    
    os.system(f"./{i_name_0_i}")
    
    
    
    
    i_list_0_i = i_next_step_0_i(i_list_0_i=i_list_0_i, i_number_of_element__minus_1__0_i=i_number_of_element__minus_1__0_i)
    
    
    
    
    return i_list_0_i
    
    
    
    
    
    
    '''
    
    
    
    # in the main you do like that .
    
    
    i_number_of_element__minus_1__0_i = 1
    
    i_list_0_i = [0]
    
    i_capacity_of_list_0_i = 100
    
    
    
    
    i_counter_0_i = 0
    
    
    while (i_counter_0_i < 15):
        
        
        i_list_0_i = i_next_step_in_asm_0_i(
                                            
                                            i_list_0_i=i_list_0_i, 
                                            
                                            
                                            i_number_of_element__minus_1__0_i=i_number_of_element__minus_1__0_i, 
                                            
                                            
                                            i_capacity_of_list_0_i=i_capacity_of_list_0_i
                                            
                                            )
        
        
        
        i_counter_0_i += 1
        
    
    
    
    
    '''
    
    
    
    
    
    
    








def i_next_step_in_asm_1_i(i_list_0_i, i_number_of_element__minus_1__0_i, i_capacity_of_list_0_i):
    
    
    
    
    '''
        
        this is everything number 1 .
        
        in asm .
        
        
        
    '''
    
    
    
    
    if i_capacity_of_list_0_i < len(i_list_0_i):
        
        raise ValueError("Capacity is smaller than list length.")
        
    
    
    i_content_0_i = r"""

section .data

i_list_0_i:
    dq _____i_list_0_i_____

i_list_0_i_length:
    dq _____i_list_0_i_length_____

i_number_of_element__minus_1__0_i:
    dq _____i_number_of_element__minus_1__0_i_____

i_list_0_i_capacity:
    dq _____i_list_0_i_capacity_____


i_format_0_i:
    db "i_list_0_i = [", 0

i_format_1_i:
    db "%ld", 0

i_format_2_i:
    db "]", 10, 0

i_format_3_i:
    db ", ", 0


section .text

global main

extern printf


main:

    push r12
    push r13
    push r14
    push r15

    lea r12, [rel i_list_0_i]

    mov r13, [rel i_list_0_i_length]

    mov r14, [rel i_number_of_element__minus_1__0_i]

    mov r15, [rel i_list_0_i_capacity]


    mov rbx, r13

    dec rbx


    mov r10, 1


i_loop_0_i:


    cmp rbx, 0

    jl i_end_of_loop_0_i


    cmp r10, 1

    jne i_end_of_loop_0_i


    mov rax, [r12 + rbx * 8]


    cmp rax, r14

    jg i_if_0_i


    jmp i_else_0_i



i_if_0_i:


    mov qword [r12 + rbx * 8], 0

    dec rbx

    jmp i_loop_0_i



i_else_0_i:


    inc qword [r12 + rbx * 8]


    mov rax, [r12 + rbx * 8]


    cmp rax, r14

    jle i_semaphore_false_0_i


    jmp i_loop_0_i



i_semaphore_false_0_i:

    mov r10, 0

    jmp i_end_of_loop_0_i



i_end_of_loop_0_i:


    cmp r10, 1

    jne i_print_0_i


    cmp r13, r15

    jge i_print_0_i


    ; Insert zero at the beginning.
    ; Shift elements right by one position.

    mov rbx, r13

    dec rbx


i_shift_loop_0_i:


    cmp rbx, 0

    jl i_insert_zero_0_i


    mov rax, [r12 + rbx * 8]

    mov [r12 + rbx * 8 + 8], rax

    dec rbx

    jmp i_shift_loop_0_i



i_insert_zero_0_i:

    mov qword [r12], 0

    inc r13



i_print_0_i:


    lea rdi, [rel i_format_0_i]

    xor eax, eax

    call printf


    mov rbx, 0


i_print_loop_0_i:


    cmp rbx, r13

    jge i_print_end_0_i


    cmp rbx, 0

    je i_print_number_0_i


    lea rdi, [rel i_format_3_i]

    xor eax, eax

    call printf



i_print_number_0_i:


    mov rsi, [r12 + rbx * 8]

    lea rdi, [rel i_format_1_i]

    xor eax, eax

    call printf


    inc rbx

    jmp i_print_loop_0_i



i_print_end_0_i:


    lea rdi, [rel i_format_2_i]

    xor eax, eax

    call printf



    pop r15
    pop r14
    pop r13
    pop r12


    xor eax, eax

    ret


section .note.GNU-stack noalloc noexec nowrite progbits

"""
    
    
    
    
    i_v_0_i = ""
    
    
    i_counter_0_i = 0
    
    while (i_counter_0_i < len(i_list_0_i) - 1):
        
        
        i_v_0_i += str(i_list_0_i[i_counter_0_i]) + ", "
        
        
        i_counter_0_i += 1
        
        
    
    
    
    i_v_0_i += str(i_list_0_i[i_counter_0_i])
    
    
    
    
    
    # =====================================================
    # RESERVE THE REMAINING CAPACITY
    # =====================================================
    
    i_number_of_remaining_elements_0_i = (
        i_capacity_of_list_0_i - len(i_list_0_i)
    )
    
    
    if (i_number_of_remaining_elements_0_i > 0):
    
        i_v_0_i += (
            "\n\n"
            + "    times "
            + str(i_number_of_remaining_elements_0_i)
            + " dq 0"
        )
    
    
    i_content_0_i = i_content_0_i.replace("_____i_list_0_i_____", i_v_0_i)
    
    
    i_content_0_i = i_content_0_i.replace("_____i_list_0_i_length_____", str(len(i_list_0_i)))
    
    
    i_content_0_i = i_content_0_i.replace("_____i_number_of_element__minus_1__0_i_____", str(i_number_of_element__minus_1__0_i))
    
    
    i_content_0_i = i_content_0_i.replace("_____i_list_0_i_capacity_____", str(i_capacity_of_list_0_i))
    
    
    
    
    
    
    
    i_name_0_i = "i_main_4_i"
    
    
    i_file_0_i = os.path.join(cwd, i_name_0_i + ".asm")
    
    
    i_d_0_i = Path(i_file_0_i)
    
    
    i_d_0_i.write_text(i_content_0_i)
    
    
    
    
    os.system(f"nasm -f elf64 {i_name_0_i}.asm -o {i_name_0_i}.o")
    
    
    os.system(f"gcc -no-pie {i_name_0_i}.o -o {i_name_0_i}")
    
    
    os.system(f"./{i_name_0_i}")
    
    
    
    
    i_list_0_i = i_next_step_1_i(i_list_0_i=i_list_0_i, i_number_of_element__minus_1__0_i=i_number_of_element__minus_1__0_i)
    
    
    
    
    return i_list_0_i
    
    
    
    
    
    '''
    
    
    
    # in the main you do like that .
    
    
    i_number_of_element__minus_1__0_i = 1
    
    i_list_0_i = [0]
    
    i_capacity_of_list_0_i = 100
    
    
    
    
    i_counter_0_i = 0
    
    
    while (i_counter_0_i < 15):
        
        
        i_list_0_i = i_next_step_in_asm_1_i(
                                            
                                            i_list_0_i=i_list_0_i, 
                                            
                                            
                                            i_number_of_element__minus_1__0_i=i_number_of_element__minus_1__0_i, 
                                            
                                            
                                            i_capacity_of_list_0_i=i_capacity_of_list_0_i
                                            
                                            )
        
        
        
        i_counter_0_i += 1
        
    
    
    
    
    '''
    
    
    
    
    
    
    






def i_next_step_in_asm_2_i(i_list_0_i, i_number_of_element__minus_1__0_i, i_capacity_of_list_0_i):
    
    
    
    
    
    '''
        
        this is everything number 2 .
        
        in asm .
        
        
        
    '''
    
    
    
    
    if i_capacity_of_list_0_i < len(i_list_0_i):
        
        raise ValueError("Capacity is smaller than list length.")
        
    
    
    
    
    i_content_0_i = r"""

section .data

i_list_0_i:
    dq _____i_list_0_i_____

i_list_0_i_length:
    dq _____i_list_0_i_length_____

i_number_of_element__minus_1__0_i:
    dq _____i_number_of_element__minus_1__0_i_____

i_list_0_i_capacity:
    dq _____i_list_0_i_capacity_____


i_format_0_i:
    db "i_list_0_i = [", 0

i_format_1_i:
    db "%ld", 0

i_format_2_i:
    db "]", 10, 0

i_format_3_i:
    db ", ", 0


section .text

global main

extern printf


main:

    push r12
    push r13
    push r14
    push r15

    lea r12, [rel i_list_0_i]

    mov r13, [rel i_list_0_i_length]

    mov r14, [rel i_number_of_element__minus_1__0_i]

    mov r15, [rel i_list_0_i_capacity]


    mov rbx, 0

    mov r10, 1


i_loop_0_i:


    cmp rbx, r13

    jge i_end_of_loop_0_i


    cmp r10, 1

    jne i_end_of_loop_0_i


    mov rax, [r12 + rbx * 8]


    cmp rax, 0

    jle i_if_0_i


    jmp i_else_0_i



i_if_0_i:


    mov [r12 + rbx * 8], r14

    inc rbx

    jmp i_loop_0_i



i_else_0_i:


    dec qword [r12 + rbx * 8]


    mov rax, [r12 + rbx * 8]


    cmp rax, 0

    jge i_semaphore_false_0_i


    jmp i_loop_0_i



i_semaphore_false_0_i:

    mov r10, 0

    jmp i_end_of_loop_0_i



i_end_of_loop_0_i:


    cmp r10, 1

    jne i_print_0_i


    cmp r13, r15

    jge i_print_0_i


    ; Append maximum value.

    mov qword [r12 + r13 * 8], 0

    mov [r12 + r13 * 8], r14

    inc r13



i_print_0_i:


    lea rdi, [rel i_format_0_i]

    xor eax, eax

    call printf


    mov rbx, 0


i_print_loop_0_i:


    cmp rbx, r13

    jge i_print_end_0_i


    cmp rbx, 0

    je i_print_number_0_i


    lea rdi, [rel i_format_3_i]

    xor eax, eax

    call printf



i_print_number_0_i:


    mov rsi, [r12 + rbx * 8]

    lea rdi, [rel i_format_1_i]

    xor eax, eax

    call printf


    inc rbx

    jmp i_print_loop_0_i



i_print_end_0_i:


    lea rdi, [rel i_format_2_i]

    xor eax, eax

    call printf



    pop r15
    pop r14
    pop r13
    pop r12


    xor eax, eax

    ret


section .note.GNU-stack noalloc noexec nowrite progbits

"""

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    i_v_0_i = ""
    
    
    i_counter_0_i = 0
    
    while (i_counter_0_i < len(i_list_0_i) - 1):
        
        
        i_v_0_i += str(i_list_0_i[i_counter_0_i]) + ", "
        
        
        i_counter_0_i += 1
        
        
    
    
    
    i_v_0_i += str(i_list_0_i[i_counter_0_i])
    
    
    
    
    
    # =====================================================
    # RESERVE THE REMAINING CAPACITY
    # =====================================================
    
    i_number_of_remaining_elements_0_i = (
        i_capacity_of_list_0_i - len(i_list_0_i)
    )
    
    
    if (i_number_of_remaining_elements_0_i > 0):
    
        i_v_0_i += (
            "\n\n"
            + "    times "
            + str(i_number_of_remaining_elements_0_i)
            + " dq 0"
        )
    
    
    
    i_content_0_i = i_content_0_i.replace("_____i_list_0_i_____", i_v_0_i)
    
    
    i_content_0_i = i_content_0_i.replace("_____i_list_0_i_length_____", str(len(i_list_0_i)))
    
    
    i_content_0_i = i_content_0_i.replace("_____i_number_of_element__minus_1__0_i_____", str(i_number_of_element__minus_1__0_i))
    
    
    i_content_0_i = i_content_0_i.replace("_____i_list_0_i_capacity_____", str(i_capacity_of_list_0_i))
    
    
    
    
    
    
    
    i_name_0_i = "i_main_4_i"
    
    
    i_file_0_i = os.path.join(cwd, i_name_0_i + ".asm")
    
    
    i_d_0_i = Path(i_file_0_i)
    
    
    i_d_0_i.write_text(i_content_0_i)
    
    
    
    
    os.system(f"nasm -f elf64 {i_name_0_i}.asm -o {i_name_0_i}.o")
    
    
    os.system(f"gcc -no-pie {i_name_0_i}.o -o {i_name_0_i}")
    
    
    os.system(f"./{i_name_0_i}")
    
    
    
    
    i_list_0_i = i_next_step_2_i(i_list_0_i=i_list_0_i, i_number_of_element__minus_1__0_i=i_number_of_element__minus_1__0_i)
    
    
    
    
    return i_list_0_i
    
    
    
    
    
    '''
    
    
    
    # in the main you do like that .
    
    
    i_number_of_element__minus_1__0_i = 1
    
    i_list_0_i = [0]
    
    i_capacity_of_list_0_i = 100
    
    
    
    
    i_counter_0_i = 0
    
    
    while (i_counter_0_i < 15):
        
        
        i_list_0_i = i_next_step_in_asm_2_i(
                                            
                                            i_list_0_i=i_list_0_i, 
                                            
                                            
                                            i_number_of_element__minus_1__0_i=i_number_of_element__minus_1__0_i, 
                                            
                                            
                                            i_capacity_of_list_0_i=i_capacity_of_list_0_i
                                            
                                            )
        
        
        
        i_counter_0_i += 1
        
    
    
    
    
    '''
    
    
    
    
    
    








def i_next_step_in_asm_3_i(i_list_0_i, i_number_of_element__minus_1__0_i, i_capacity_of_list_0_i):
    
    
    
    
    
    '''
        
        this is everything number 3 .
        
        in asm .
        
        
        
    '''
    
    
    
    
    if i_capacity_of_list_0_i < len(i_list_0_i):
        
        raise ValueError("Capacity is smaller than list length.")
        
    
    
    
    i_content_0_i = r"""

section .data

i_list_0_i:
    dq _____i_list_0_i_____

i_list_0_i_length:
    dq _____i_list_0_i_length_____

i_number_of_element__minus_1__0_i:
    dq _____i_number_of_element__minus_1__0_i_____

i_list_0_i_capacity:
    dq _____i_list_0_i_capacity_____


i_format_0_i:
    db "i_list_0_i = [", 0

i_format_1_i:
    db "%ld", 0

i_format_2_i:
    db "]", 10, 0

i_format_3_i:
    db ", ", 0


section .text

global main

extern printf


main:

    push r12
    push r13
    push r14
    push r15

    lea r12, [rel i_list_0_i]

    mov r13, [rel i_list_0_i_length]

    mov r14, [rel i_number_of_element__minus_1__0_i]

    mov r15, [rel i_list_0_i_capacity]


    ; counter = length - 1

    mov rbx, r13

    dec rbx


    ; semaphore = True

    mov r10, 1



i_loop_0_i:


    ; while counter >= 0

    cmp rbx, 0

    jl i_end_of_loop_0_i


    ; while semaphore == True

    cmp r10, 1

    jne i_end_of_loop_0_i


    ; Read current element.

    mov rax, [r12 + rbx * 8]


    ; if element <= 0

    cmp rax, 0

    jle i_if_0_i


    jmp i_else_0_i



i_if_0_i:


    ; list[counter] = maximum

    mov [r12 + rbx * 8], r14


    ; counter -= 1

    dec rbx

    jmp i_loop_0_i



i_else_0_i:


    ; list[counter] -= 1

    dec qword [r12 + rbx * 8]


    ; if list[counter] >= 0

    mov rax, [r12 + rbx * 8]

    cmp rax, 0

    jge i_semaphore_false_0_i


    jmp i_loop_0_i



i_semaphore_false_0_i:

    ; semaphore = False

    mov r10, 0

    jmp i_end_of_loop_0_i



i_end_of_loop_0_i:


    ; if semaphore == True

    cmp r10, 1

    jne i_print_0_i


    ; Check capacity.

    cmp r13, r15

    jge i_print_0_i


    ; Insert maximum at the beginning.
    ; Shift all existing elements one position right.


    mov rbx, r13

    dec rbx



i_shift_loop_0_i:


    cmp rbx, 0

    jl i_insert_element_0_i


    mov rax, [r12 + rbx * 8]

    mov [r12 + rbx * 8 + 8], rax


    dec rbx

    jmp i_shift_loop_0_i



i_insert_element_0_i:


    mov [r12], r14

    inc r13



i_print_0_i:


    lea rdi, [rel i_format_0_i]

    xor eax, eax

    call printf


    mov rbx, 0



i_print_loop_0_i:


    cmp rbx, r13

    jge i_print_end_0_i


    cmp rbx, 0

    je i_print_number_0_i


    lea rdi, [rel i_format_3_i]

    xor eax, eax

    call printf



i_print_number_0_i:


    mov rsi, [r12 + rbx * 8]

    lea rdi, [rel i_format_1_i]

    xor eax, eax

    call printf


    inc rbx

    jmp i_print_loop_0_i



i_print_end_0_i:


    lea rdi, [rel i_format_2_i]

    xor eax, eax

    call printf



    pop r15
    pop r14
    pop r13
    pop r12


    xor eax, eax

    ret


section .note.GNU-stack noalloc noexec nowrite progbits

"""

    
    
    
    
    
    
    
    
    
    
    
    
    
    i_v_0_i = ""
    
    
    i_counter_0_i = 0
    
    while (i_counter_0_i < len(i_list_0_i) - 1):
        
        
        i_v_0_i += str(i_list_0_i[i_counter_0_i]) + ", "
        
        
        i_counter_0_i += 1
        
        
    
    
    
    i_v_0_i += str(i_list_0_i[i_counter_0_i])
    
    
    
    
    
    # =====================================================
    # RESERVE THE REMAINING CAPACITY
    # =====================================================
    
    i_number_of_remaining_elements_0_i = (
        i_capacity_of_list_0_i - len(i_list_0_i)
    )
    
    
    if (i_number_of_remaining_elements_0_i > 0):
    
        i_v_0_i += (
            "\n\n"
            + "    times "
            + str(i_number_of_remaining_elements_0_i)
            + " dq 0"
        )
    
    
    
    i_content_0_i = i_content_0_i.replace("_____i_list_0_i_____", i_v_0_i)
    
    
    i_content_0_i = i_content_0_i.replace("_____i_list_0_i_length_____", str(len(i_list_0_i)))
    
    
    i_content_0_i = i_content_0_i.replace("_____i_number_of_element__minus_1__0_i_____", str(i_number_of_element__minus_1__0_i))
    
    
    i_content_0_i = i_content_0_i.replace("_____i_list_0_i_capacity_____", str(i_capacity_of_list_0_i))
    
    
    
    
    
    
    
    i_name_0_i = "i_main_4_i"
    
    
    i_file_0_i = os.path.join(cwd, i_name_0_i + ".asm")
    
    
    i_d_0_i = Path(i_file_0_i)
    
    
    i_d_0_i.write_text(i_content_0_i)
    
    
    
    
    os.system(f"nasm -f elf64 {i_name_0_i}.asm -o {i_name_0_i}.o")
    
    
    os.system(f"gcc -no-pie {i_name_0_i}.o -o {i_name_0_i}")
    
    
    os.system(f"./{i_name_0_i}")
    
    
    
    
    i_list_0_i = i_next_step_3_i(i_list_0_i=i_list_0_i, i_number_of_element__minus_1__0_i=i_number_of_element__minus_1__0_i)
    
    
    
    
    return i_list_0_i
    
    
    
    
    
    
    
    '''
    
    
    
    # in the main you do like that .
    
    
    i_number_of_element__minus_1__0_i = 1
    
    i_list_0_i = [0]
    
    i_capacity_of_list_0_i = 100
    
    
    
    
    i_counter_0_i = 0
    
    
    while (i_counter_0_i < 15):
        
        
        i_list_0_i = i_next_step_in_asm_3_i(
                                            
                                            i_list_0_i=i_list_0_i, 
                                            
                                            
                                            i_number_of_element__minus_1__0_i=i_number_of_element__minus_1__0_i, 
                                            
                                            
                                            i_capacity_of_list_0_i=i_capacity_of_list_0_i
                                            
                                            )
        
        
        
        i_counter_0_i += 1
        
    
    
    
    
    '''
    
    










'''






javascript' ' '


function i_next_step_0_i(i_list_0_i, i_number_of_element__minus_1__0_i) 
{
    
    
    /*
        
        this is everything number 0 .
        
    */
    
    
    
    let i_counter_0_i = 0;
    
    
    let i_semaphore_of_add_0_i = true;
    
    
    while ( (i_counter_0_i < i_list_0_i.length) && (i_semaphore_of_add_0_i === true) ) 
    {
        
        if ( i_list_0_i[i_counter_0_i] > i_number_of_element__minus_1__0_i ) 
        {
            
            i_list_0_i[i_counter_0_i] = 0;
            
            
            i_counter_0_i++;
            
            
        }
        
        else 
        {
            
            i_list_0_i[i_counter_0_i] += 1;
            
            
            if ( i_list_0_i[i_counter_0_i] <= i_number_of_element__minus_1__0_i ) 
            {
                
                
                i_semaphore_of_add_0_i = false;
                
                
            }
            
        }
        
    }
    
    if (i_semaphore_of_add_0_i === true) 
    {
        
        
        i_list_0_i.push(0);
        
        
    }
    
    
    
    
    return i_list_0_i;
    
    
    
}





function i_next_step_1_i(i_list_0_i, i_number_of_element__minus_1__0_i) 
{
    
    /*
        
        this is everything number 1 .
        
    */
    
    
    
    let i_counter_0_i = i_list_0_i.length - 1;
    
    
    let i_semaphore_of_add_0_i = true;
    
    
    
    
    while ( (i_counter_0_i >= 0) && (i_semaphore_of_add_0_i === true) ) 
    {
        
        
        if ( i_list_0_i[i_counter_0_i] > i_number_of_element__minus_1__0_i ) 
        {
            
            
            i_list_0_i[i_counter_0_i] = 0;
            
            
            i_counter_0_i--;
            
            
        }
        
        else 
        {
            
            i_list_0_i[i_counter_0_i] += 1;
            
            if ( i_list_0_i[i_counter_0_i] <= i_number_of_element__minus_1__0_i ) 
            {
                
                i_semaphore_of_add_0_i = false;
                
            }
            
        }
        
    }

    if (i_semaphore_of_add_0_i === true) 
    {
        
        i_list_0_i.unshift(0);
        
    }
    
    
    
    return i_list_0_i;
    
    
}




function i_next_step_2_i(i_list_0_i, i_number_of_element__minus_1__0_i) 
{
    
    
    /*
        
        this is everything number 2 .
        
    */
    
    
    
    let i_counter_0_i = 0;
    
    
    let i_semaphore_of_add_0_i = true;
    
    
    
    while ( (i_counter_0_i < i_list_0_i.length) && (i_semaphore_of_add_0_i === true) ) 
    {
        
        
        if (i_list_0_i[i_counter_0_i] <= 0) 
        {
            
            
            i_list_0_i[i_counter_0_i] = i_number_of_element__minus_1__0_i;
            
            
            i_counter_0_i++;
            
            
        }

        else 
        {
            
            
            i_list_0_i[i_counter_0_i] -= 1;
            
            
            if (i_list_0_i[i_counter_0_i] >= 0) 
            {
            
                
                i_semaphore_of_add_0_i = false;
                
                
            }
            
        }
        
    }
    
    if (i_semaphore_of_add_0_i === true) 
    {
        
        
        i_list_0_i.push(i_number_of_element__minus_1__0_i);
        
        
    }
    
    
    return i_list_0_i;
    
    
    
}






function i_next_step_3_i(i_list_0_i, i_number_of_element__minus_1__0_i) 
{
    
    /*
        
        this is everything number 3 .
        
    */
    
    
    let i_counter_0_i = i_list_0_i.length - 1;
    
    
    let i_semaphore_of_add_0_i = true;
    
    
    
    while ( (i_counter_0_i >= 0) && (i_semaphore_of_add_0_i === true) ) 
    {
        
        
        if (i_list_0_i[i_counter_0_i] <= 0) 
        {
            
            
            i_list_0_i[i_counter_0_i] = i_number_of_element__minus_1__0_i;
            
            
            i_counter_0_i--;
            
            
        }

        else 
        {
            
            
            i_list_0_i[i_counter_0_i] -= 1;
            
            
            if (i_list_0_i[i_counter_0_i] >= 0) 
            {
                
                
                i_semaphore_of_add_0_i = false;
                
                
            }
            
        }
        
    }
    
    if (i_semaphore_of_add_0_i === true) 
    {
        
        
        i_list_0_i.unshift(i_number_of_element__minus_1__0_i);
        
        
    }
    
    
    return i_list_0_i;
    
    
}





' ' '









java' ' '






import java.util.ArrayList;

public class IPrincipalCentral 
{
    
    public static ArrayList<Integer> i_next_step_0_i( ArrayList<Integer> i_list_0_i, int i_number_of_element__minus_1__0_i ) 
    {
        
        /*
            
            this is everything number 0 .
            
        */
        
        int i_counter_0_i = 0;
        
        boolean i_semaphore_of_add_0_i = true;
        
        while ( ( i_counter_0_i < i_list_0_i.size() ) && ( i_semaphore_of_add_0_i == true ) ) 
        {
            
            if ( i_list_0_i.get(i_counter_0_i) > i_number_of_element__minus_1__0_i ) 
            {
                
                i_list_0_i.set(i_counter_0_i, 0);
                
                i_counter_0_i++;
                
                
            } 
            else 
            {
                
                i_list_0_i.set( i_counter_0_i, i_list_0_i.get(i_counter_0_i) + 1 );
                
                if ( i_list_0_i.get(i_counter_0_i) <= i_number_of_element__minus_1__0_i ) 
                {
                    
                    i_semaphore_of_add_0_i = false;
                    
                }
                
            }
            
        }
        
        if ( i_semaphore_of_add_0_i == true ) 
        {
            
            i_list_0_i.add(0);
            
        }
        
        return i_list_0_i;
        
    }
    
}











import java.util.ArrayList;

public class IPrincipalCentral 
{
    
    public static ArrayList<Integer> i_next_step_1_i( ArrayList<Integer> i_list_0_i, int i_number_of_element__minus_1__0_i ) 
    {
        
        /*
            
            this is everything number 1 .
            
        */
        
        
        int i_counter_0_i = i_list_0_i.size() - 1;
        
        boolean i_semaphore_of_add_0_i = true;
        
        while ( ( i_counter_0_i >= 0 ) && ( i_semaphore_of_add_0_i == true ) ) 
        {
            
            if ( i_list_0_i.get(i_counter_0_i) > i_number_of_element__minus_1__0_i ) 
            {
                
                i_list_0_i.set(i_counter_0_i, 0);
                
                i_counter_0_i--;
                
            } 
            else 
            {
                
                i_list_0_i.set( i_counter_0_i, i_list_0_i.get(i_counter_0_i) + 1 );
                
                if ( i_list_0_i.get(i_counter_0_i) <= i_number_of_element__minus_1__0_i ) 
                {
                    
                    i_semaphore_of_add_0_i = false;
                    
                }
                
            }
            
        }
        
        if ( i_semaphore_of_add_0_i == true ) 
        {
            
            i_list_0_i.add(0, 0);
            
        }
        
        return i_list_0_i;
        
    }
    
}










import java.util.ArrayList;

public class IPrincipalCentral 
{
    
    public static ArrayList<Integer> i_next_step_2_i( ArrayList<Integer> i_list_0_i, int i_number_of_element__minus_1__0_i ) 
    {
        
        /*
            
            this is everything number 2 .
            
        */
        
        
        int i_counter_0_i = 0;
        
        boolean i_semaphore_of_add_0_i = true;
        
        
        while ( ( i_counter_0_i < i_list_0_i.size() ) && ( i_semaphore_of_add_0_i == true ) ) 
        {
            
            if ( i_list_0_i.get(i_counter_0_i) <= 0 ) 
            {
                
                i_list_0_i.set( i_counter_0_i, i_number_of_element__minus_1__0_i );
                
                i_counter_0_i++;
                
                
            } 
            else 
            {
                
                i_list_0_i.set( i_counter_0_i, i_list_0_i.get(i_counter_0_i) - 1 );
                
                if ( i_list_0_i.get(i_counter_0_i) >= 0 ) 
                {
                    
                    i_semaphore_of_add_0_i = false;
                    
                }
                
            }
            
        }
        
        if ( i_semaphore_of_add_0_i == true ) 
        {
            
            i_list_0_i.add(i_number_of_element__minus_1__0_i);
            
        }
        
        return i_list_0_i;
        
    }
    
}








import java.util.ArrayList;

public class IPrincipalCentral 
{
    
    public static ArrayList<Integer> i_next_step_3_i( ArrayList<Integer> i_list_0_i, int i_number_of_element__minus_1__0_i ) 
    {
        
        /*
            
            this is everything number 3 .
            
        */
        
        
        int i_counter_0_i = i_list_0_i.size() - 1;
        
        boolean i_semaphore_of_add_0_i = true;
        
        
        while ( ( i_counter_0_i >= 0 ) && ( i_semaphore_of_add_0_i == true ) ) 
        {
            
            if ( i_list_0_i.get(i_counter_0_i) <= 0 ) 
            {
                
                i_list_0_i.set( i_counter_0_i, i_number_of_element__minus_1__0_i );
                
                i_counter_0_i--;
                
            } 
            else 
            {
                
                i_list_0_i.set( i_counter_0_i, i_list_0_i.get(i_counter_0_i) - 1 );
                
                if ( i_list_0_i.get(i_counter_0_i) >= 0 ) 
                {
                    
                    i_semaphore_of_add_0_i = false;
                    
                }
                
            }
            
        }
        
        if ( i_semaphore_of_add_0_i == true ) 
        {
            
            i_list_0_i.add( 0, i_number_of_element__minus_1__0_i );
            
        }
        
        return i_list_0_i;
        
    }
    
}










' ' '










csharp' ' '






using System;

using System.Collections.Generic;

public class IPrincipalCentral
{
    
    public static List<int> i_next_step_0_i( List<int> i_list_0_i, int i_number_of_element__minus_1__0_i )
    {
        
        /*
            
            this is everything number 0 .
            
        */
        
        
        int i_counter_0_i = 0;
        
        bool i_semaphore_of_add_0_i = true;
        
        while ( ( i_counter_0_i < i_list_0_i.Count ) && ( i_semaphore_of_add_0_i == true ) )
        {
            
            if ( i_list_0_i[i_counter_0_i] > i_number_of_element__minus_1__0_i )
            {
                
                i_list_0_i[i_counter_0_i] = 0;
                
                i_counter_0_i++;
                
            }
            else
            {
                
                
                i_list_0_i[i_counter_0_i] += 1;
                
                if ( i_list_0_i[i_counter_0_i] <= i_number_of_element__minus_1__0_i )
                {
                    
                    i_semaphore_of_add_0_i = false;
                    
                }
                
            }
            
        }
        
        
        if ( i_semaphore_of_add_0_i == true )
        {
            
            i_list_0_i.Add(0);
            
        }
        
        
        return i_list_0_i;
        
    }
    
}






using System;

using System.Collections.Generic;

public class IPrincipalCentral
{
    
    
    public static List<int> i_next_step_1_i( List<int> i_list_0_i, int i_number_of_element__minus_1__0_i )
    {
        
        /*
            
            this is everything number 1 .
            
        */
        
        
        int i_counter_0_i = i_list_0_i.Count - 1;
        
        bool i_semaphore_of_add_0_i = true;
        
        while ( ( i_counter_0_i >= 0 ) && ( i_semaphore_of_add_0_i == true ) )
        {
            
            if ( i_list_0_i[i_counter_0_i] > i_number_of_element__minus_1__0_i )
            {
                
                i_list_0_i[i_counter_0_i] = 0;
                
                i_counter_0_i--;
                
                
            }
            else
            {
                
                i_list_0_i[i_counter_0_i] += 1;
                
                if ( i_list_0_i[i_counter_0_i] <= i_number_of_element__minus_1__0_i )
                {
                    
                    i_semaphore_of_add_0_i = false;
                    
                }
                
            }
            
        }
        
        if ( i_semaphore_of_add_0_i == true )
        {
            
            i_list_0_i.Insert(0, 0);
            
        }
        
        return i_list_0_i;
        
    }
    
}









using System;

using System.Collections.Generic;

public class IPrincipalCentral
{
    
    public static List<int> i_next_step_2_i( List<int> i_list_0_i, int i_number_of_element__minus_1__0_i )
    {
        
        /*
            
            this is everything number 2 .
            
        */
        
        
        int i_counter_0_i = 0;
        
        bool i_semaphore_of_add_0_i = true;
        
        while ( ( i_counter_0_i < i_list_0_i.Count ) && ( i_semaphore_of_add_0_i == true ) )
        {
            
            if ( i_list_0_i[i_counter_0_i] <= 0 )
            {
                
                i_list_0_i[i_counter_0_i] = i_number_of_element__minus_1__0_i;
                
                
                i_counter_0_i++;
                
                
            }
            else
            {
                
                i_list_0_i[i_counter_0_i] -= 1;
                
                if ( i_list_0_i[i_counter_0_i] >= 0 )
                {
                    
                    i_semaphore_of_add_0_i = false;
                    
                }
                
            }
            
        }
        
        if ( i_semaphore_of_add_0_i == true )
        {
            
            i_list_0_i.Add(i_number_of_element__minus_1__0_i);
            
        }
        
        
        return i_list_0_i;
        
    }
    
}









using System;

using System.Collections.Generic;

public class IPrincipalCentral
{
    
    public static List<int> i_next_step_3_i( List<int> i_list_0_i, int i_number_of_element__minus_1__0_i )
    {
        
        /*
            
            this is everything number 3 .
            
        */
        
        
        int i_counter_0_i = i_list_0_i.Count - 1;
        
        
        bool i_semaphore_of_add_0_i = true;
        
        
        while ( ( i_counter_0_i >= 0 ) && ( i_semaphore_of_add_0_i == true ) )
        {
            
            if ( i_list_0_i[i_counter_0_i] <= 0 )
            {
                
                i_list_0_i[i_counter_0_i] = i_number_of_element__minus_1__0_i;
                
                
                i_counter_0_i--;
                
                
            }
            else
            {
                
                i_list_0_i[i_counter_0_i] -= 1;
                
                if ( i_list_0_i[i_counter_0_i] >= 0 )
                {
                    
                    i_semaphore_of_add_0_i = false;
                    
                }
                
            }
            
        }
        
        
        if ( i_semaphore_of_add_0_i == true )
        {
            
            i_list_0_i.Insert( 0, i_number_of_element__minus_1__0_i );
            
        }
        
        return i_list_0_i;
        
    }
    
}







' ' '










Rust' ' '





fn i_next_step_0_i( i_list_0_i: &mut Vec<u64>, i_number_of_element__minus_1__0_i: u64 ) -> &mut Vec<u64> 
{
    
    
    /*
        
        this is everything number 0 .
        
    */
    
    
    
    let mut i_counter_0_i: usize = 0;
    
    let mut i_semaphore_of_add_0_i: bool = true;
    
    
    while ( ( i_counter_0_i < i_list_0_i.len() ) && ( i_semaphore_of_add_0_i == true ) ) 
    {
        
        if ( i_list_0_i[i_counter_0_i] > i_number_of_element__minus_1__0_i )
        {
            
            i_list_0_i[i_counter_0_i] = 0;
            
            i_counter_0_i += 1;
            
        }
        else 
        {
            
            i_list_0_i[i_counter_0_i] += 1;
            
            if ( i_list_0_i[i_counter_0_i] <= i_number_of_element__minus_1__0_i )  
            {
                
                i_semaphore_of_add_0_i = false;
                
            }
            
        }
        
    }
    
    
    
    if ( i_semaphore_of_add_0_i == true )
    {
        
        i_list_0_i.push(0);
        
    }
    
    return i_list_0_i;
    
}










fn i_next_step_1_i( i_list_0_i: &mut Vec<u64>, i_number_of_element__minus_1__0_i: u64 ) -> &mut Vec<u64> 
{
    
    
    /*
        
        this is everything number 1 .
        
    */
    
    
    let mut i_counter_0_i: isize = i_list_0_i.len() as isize - 1;
    
    let mut i_semaphore_of_add_0_i: bool = true;
    
    
    while ( ( i_counter_0_i >= 0 ) && ( i_semaphore_of_add_0_i == true ) ) 
    {
        
        
        if ( i_list_0_i[i_counter_0_i as usize] > i_number_of_element__minus_1__0_i ) 
        {
            
            
            i_list_0_i[i_counter_0_i as usize] = 0;
            
            
            i_counter_0_i -= 1;
            
            
        }
        else 
        {
            
            
            i_list_0_i[i_counter_0_i as usize] += 1;
            
            
            if ( i_list_0_i[i_counter_0_i as usize] <= i_number_of_element__minus_1__0_i )
            {
                
                i_semaphore_of_add_0_i = false;
                
            }
            
        }
        
    }
    
    
    
    if ( i_semaphore_of_add_0_i == true ) 
    {
        
        i_list_0_i.insert(0, 0);
        
    }
    
    return i_list_0_i;
    
}










fn i_next_step_2_i( i_list_0_i: &mut Vec<i64>, i_number_of_element__minus_1__0_i: i64 ) -> &mut Vec<i64> 
{
    
    
    /*
        
        this is everything number 2 .
        
    */
    
    
    
    
    let mut i_counter_0_i: usize = 0;
    
    
    let mut i_semaphore_of_add_0_i: bool = true;
    
    
    
    while ( ( i_counter_0_i < i_list_0_i.len() ) && ( i_semaphore_of_add_0_i == true ) ) 
    {
        
        
        if ( i_list_0_i[i_counter_0_i] <= 0 ) 
        {
            
            
            i_list_0_i[i_counter_0_i] = i_number_of_element__minus_1__0_i;
            
            
            i_counter_0_i += 1;
            
            
        }
        else 
        {
            
            i_list_0_i[i_counter_0_i] -= 1;
            
            if ( i_list_0_i[i_counter_0_i] >= 0 ) 
            {
                
                i_semaphore_of_add_0_i = false;
                
            }
            
        }
        
    }
    
    
    if ( i_semaphore_of_add_0_i == true ) 
    {
        
        i_list_0_i.push( i_number_of_element__minus_1__0_i );
        
    }
    
    return i_list_0_i;
    
}







fn i_next_step_3_i( i_list_0_i: &mut Vec<i64>, i_number_of_element__minus_1__0_i: i64 ) -> &mut Vec<i64> 
{
    
    
    /*
        
        this is everything number 3 .
        
    */
    
    
    let mut i_counter_0_i: isize = i_list_0_i.len() as isize - 1;
    
    
    let mut i_semaphore_of_add_0_i: bool = true;
    
    
    
    
    while ( (i_counter_0_i >= 0) && (i_semaphore_of_add_0_i == true) ) 
    {
        
        if ( i_list_0_i[i_counter_0_i as usize] <= 0 ) 
        {
            
            
            i_list_0_i[i_counter_0_i as usize] = i_number_of_element__minus_1__0_i;
            
            
            i_counter_0_i -= 1;
            
            
            
        }
        else 
        {
            
            
            i_list_0_i[i_counter_0_i as usize] -= 1;
            
            if ( i_list_0_i[i_counter_0_i as usize] >= 0 )
            {
                
                i_semaphore_of_add_0_i = false;
                
            }
            
        }
        
    }
    
    
    if ( i_semaphore_of_add_0_i == true )
    {
        
        i_list_0_i.insert( 0, i_number_of_element__minus_1__0_i );
        
    }
    
    
    return i_list_0_i;
    
}










' ' ' 












'''













def i_next_step_4_i(i_list_0_i, i_number_of_element__minus_1__0_i, i_number_of_first_appear_0_i):
    
    
    
    '''
   
   
   
    this should be :
       
       
        i_number_of_first_appear_0_i == 1
       
       
       
   
   
   
   
   
   
    ''' 
    
    
    
    
    i_counter_0_i = 0
    
    
        
    
    i_semaphore_of_add_0_i = True
    
    
    
    while ((i_counter_0_i < len(i_list_0_i)) and (i_semaphore_of_add_0_i == True)):
        
        
        if (i_list_0_i[i_counter_0_i] > i_number_of_element__minus_1__0_i):
            
            
            i_list_0_i[i_counter_0_i] = 0
            
            
            i_counter_0_i += 1
            
            
            
            
            
            
        else:
            
            
            i_list_0_i[i_counter_0_i] += 1
            
            if (i_list_0_i[i_counter_0_i] <= i_number_of_element__minus_1__0_i):
                
                
                i_semaphore_of_add_0_i = False
                
                
            
        
        
    
    if (i_semaphore_of_add_0_i == True):
        
        
        if (len(i_list_0_i) == 0):
            
            i_list_0_i.append(0)
            
        else:
            
            i_list_0_i.append(i_number_of_first_appear_0_i)
        
        
        
        
        
    
    return i_list_0_i










def i_next_step_5_i(i_list_0_i, i_number_of_element__minus_1__0_i, i_number_of_first_appear_0_i):
    
    
    
    '''
    
    
       
    this should be :
       
       
        i_number_of_first_appear_0_i == 1
       
       
       
       
       
    
    '''
    
    
        
    i_counter_0_i = len(i_list_0_i) - 1
    
    
    
    i_semaphore_of_add_0_i = True
    
    
    
    while ((i_counter_0_i >= 0) and (i_semaphore_of_add_0_i == True)):
        
        
        if (i_list_0_i[i_counter_0_i] > i_number_of_element__minus_1__0_i):
            
            
            i_list_0_i[i_counter_0_i] = 0
            
            
            i_counter_0_i -= 1
            
            
            
        else:
            
            
            i_list_0_i[i_counter_0_i] += 1
            
            if (i_list_0_i[i_counter_0_i] <= i_number_of_element__minus_1__0_i):
                
                
                i_semaphore_of_add_0_i = False
                
                
            
        
        
    
    if (i_semaphore_of_add_0_i == True):
        
        
        
        if (len(i_list_0_i) == 0):
            
            
            i_list_0_i.append(0)
            
            
        else:
            
            
            i_list_0_i.insert(0, i_number_of_first_appear_0_i)
            
        
        
        
    
    return i_list_0_i











def i_next_step_6_i(i_list_0_i, i_number_of_element__minus_1__0_i, i_number_of_first_appear_0_i):
    
    
    
    
    '''
    
    
    
       
    this should be :
       
       
        i_number_of_first_appear_0_i == 1
       
       
       
       
       
    
    
    '''
    
    
    
    i_counter_0_i = 0
    
    
        
    
    i_semaphore_of_add_0_i = True
    
    
    i_semaphore_of_add_1_i = False
    
    
    
    
    while ((i_counter_0_i < len(i_list_0_i)) and (i_semaphore_of_add_0_i == True) and (i_semaphore_of_add_1_i == False)):
        
        
        if (i_list_0_i[i_counter_0_i] <= 0):
            
            
            i_list_0_i[i_counter_0_i] = i_number_of_element__minus_1__0_i
            
            
            i_counter_0_i += 1
            
            
            
            
            
        else:
            
            
            i_list_0_i[i_counter_0_i] -= 1
            
            if ((i_list_0_i[i_counter_0_i] >= 0)):
                
                
                i_semaphore_of_add_0_i = False
                
                
            
            
            
            
            
            if ((i_list_0_i[i_counter_0_i] < i_number_of_first_appear_0_i) and (i_counter_0_i == len(i_list_0_i) - 1) and (len(i_list_0_i) > 1)):
                
                
                
                i_semaphore_of_add_1_i = True
                
                
                
                i_semaphore_of_add_0_i = True
                
                
            
            
            
        
    
    
    
    
    if (i_semaphore_of_add_1_i == True):
    
        
        i_counter_1_i = 0
        
        
        while (i_counter_1_i < len(i_list_0_i)):
            
            
            
            i_list_0_i[i_counter_1_i] = i_number_of_element__minus_1__0_i
            
            
            
            i_counter_1_i += 1
            
            
            
    
    
    
    
    
    
    
    if (i_semaphore_of_add_0_i == True):
        
        
        
        i_list_0_i.append(i_number_of_element__minus_1__0_i)
        
        
        
        
        
    
    return i_list_0_i












def i_next_step_7_i(i_list_0_i, i_number_of_element__minus_1__0_i, i_number_of_first_appear_0_i):
    
    
    
    '''
    
    
       
    this should be :
       
       
        i_number_of_first_appear_0_i == 1
       
       
       
       
       
    
    
    
    '''
    
    
    
    
    i_counter_0_i = len(i_list_0_i) - 1
    
    
    
    i_semaphore_of_add_0_i = True
    
    
    i_semaphore_of_add_1_i = False
    
    
    while ((i_counter_0_i >= 0) and (i_semaphore_of_add_0_i == True) and (i_semaphore_of_add_1_i == False)):
        
        
        if (i_list_0_i[i_counter_0_i] <= 0):
            
        
            
            
            i_list_0_i[i_counter_0_i] = i_number_of_element__minus_1__0_i
                
            
            
            i_counter_0_i -= 1
                
            
            
            
        else:
            
            
            i_list_0_i[i_counter_0_i] -= 1
            
            
            
            
            
            if ((i_list_0_i[i_counter_0_i] >= 0)):
            
                
                
                
                i_semaphore_of_add_0_i = False
                
                
                
                
                
                
                
            
            
            
            if ((i_list_0_i[i_counter_0_i] < i_number_of_first_appear_0_i) and (i_counter_0_i == 0) and (len(i_list_0_i) > 1)):
                
                
                
                i_semaphore_of_add_1_i = True
                
                
                
                i_semaphore_of_add_0_i = True
                
                
                
                
            
            
        
     
    
    
    
    if (i_semaphore_of_add_1_i == True):
    
        
        i_counter_1_i = 0
        
        
        while (i_counter_1_i < len(i_list_0_i)):
            
            
            i_list_0_i[i_counter_1_i] = i_number_of_element__minus_1__0_i
            
            
            i_counter_1_i += 1
            
            
            
    
    
    
    
    if (i_semaphore_of_add_0_i == True):
        
        
        
        i_list_0_i.insert(0, i_number_of_element__minus_1__0_i)
        
        
        
        
    
    return i_list_0_i




























def i_check_if_repetition_exist_0_i(i_list_0_i):
    
    
    
    i_semaphore_of_result_0_i = False
    
    
    
    i_counter_0_i = 0
    
    
    while ((i_counter_0_i < len(i_list_0_i)) and (i_semaphore_of_result_0_i == False)):
        
        
        i_counter_of_repetition_0_i = 0
        
        
        i_counter_1_i = i_counter_0_i
        
        
        while ((i_counter_1_i < len(i_list_0_i))):
            
            
            if (i_list_0_i[i_counter_1_i] == i_list_0_i[i_counter_0_i]):
                
                
                i_counter_of_repetition_0_i += 1
                
                
            
            
            i_counter_1_i += 1
            
        
        
        
        if (i_counter_of_repetition_0_i > 1):
            
            
            i_semaphore_of_result_0_i = True
            
            
        
        
        
        
        i_counter_0_i += 1
        
        
        
    
    
    
    i_element_that_repeats_0_i = i_counter_0_i - 1
    
    
    
    return [i_semaphore_of_result_0_i, i_element_that_repeats_0_i]
    
    
    





def i_main_0_i():
    
    
    
    i_max_number_0_i = 9
    
    
    
    i_number_of_loop_0_i = 1500
    
    
    
    i_list_0_i = []
    
    
    i_list_of_all_items_0_i = []
    
    
    i_list_1_i = []
    
    
    i_list_of_all_items_1_i = []
    
    
    i_list_2_i = []
    
    
    i_list_of_all_items_2_i = []
    
    
    i_list_3_i = []
    
    
    i_list_of_all_items_3_i = []
    
    
    
    
    
    
    
    
    
    
    print(f"i_list_0_i = {i_list_0_i} . i_list_1_i = {i_list_1_i} . i_list_2_i = {i_list_2_i} . i_list_3_i = {i_list_3_i} .")
        
        
    
    i_counter_0_i = 0
    
    
    while (i_counter_0_i < i_number_of_loop_0_i):
        
        
        
        i_list_of_all_items_0_i.append(copy.deepcopy(i_list_0_i))
        
        
        i_list_0_i = i_next_step_0_i(i_list_0_i=i_list_0_i, i_number_of_element__minus_1__0_i=i_max_number_0_i)
        
        
        
        
        i_list_of_all_items_1_i.append(copy.deepcopy(i_list_1_i))
        
        
        i_list_1_i = i_next_step_1_i(i_list_0_i=i_list_1_i, i_number_of_element__minus_1__0_i=i_max_number_0_i)
        
        
        
        
        i_list_of_all_items_2_i.append(copy.deepcopy(i_list_2_i))
        
        
        i_list_2_i = i_next_step_2_i(i_list_0_i=i_list_2_i, i_number_of_element__minus_1__0_i=i_max_number_0_i)
        
        
        
        
        i_list_of_all_items_3_i.append(copy.deepcopy(i_list_3_i))
        
        
        i_list_3_i = i_next_step_3_i(i_list_0_i=i_list_3_i, i_number_of_element__minus_1__0_i=i_max_number_0_i)
        
        
        
        
        
        
        print(f"i_list_0_i = {i_list_0_i} . i_list_1_i = {i_list_1_i} . i_list_2_i = {i_list_2_i} . i_list_3_i = {i_list_3_i} .")
        
        
        
        i_counter_0_i += 1
        
        
        
        
    
    
    
    
    i_semaphore_of_result_0_i = i_check_if_repetition_exist_0_i(i_list_0_i=i_list_of_all_items_0_i)
    
    
    
    i_semaphore_of_result_1_i = i_check_if_repetition_exist_0_i(i_list_0_i=i_list_of_all_items_1_i)
    
    
    
    i_semaphore_of_result_2_i = i_check_if_repetition_exist_0_i(i_list_0_i=i_list_of_all_items_2_i)
    
    
    
    i_semaphore_of_result_3_i = i_check_if_repetition_exist_0_i(i_list_0_i=i_list_of_all_items_3_i)
    
    
    
    
    
    i_list_of_semaphores_of_result_0_i = [
                    
                    
                    i_semaphore_of_result_0_i,
                    
                    
                    i_semaphore_of_result_1_i,
                    
                    
                    i_semaphore_of_result_2_i,
                    
                    
                    i_semaphore_of_result_3_i,
                    
                    
                    
                    ]
    
    
    
    
    print(f"\n\n\n    i_list_of_semaphores_of_result_0_i = {i_list_of_semaphores_of_result_0_i} .\n\n\n")
    
    
    
    
    
    # -----------------------------------------------------------------------------------------------------------------------------
    
    # -----------------------------------------------------------------------------------------------------------------------------
    
    # -----------------------------------------------------------------------------------------------------------------------------
    
    
    
    
    i_number_of_first_appear_0_i = 1
    
    
    
    i_list_0_i = []
    
    
    i_list_of_all_items_0_i = []
    
    
    i_list_1_i = []
    
    
    i_list_of_all_items_1_i = []
    
    
    i_list_2_i = []
    
    
    i_list_of_all_items_2_i = []
    
    
    i_list_3_i = []
    
    
    i_list_of_all_items_3_i = []
    
    
    
    
    
    print(f"i_list_0_i = {i_list_0_i} . i_list_1_i = {i_list_1_i} . i_list_2_i = {i_list_2_i} . i_list_3_i = {i_list_3_i} .")
    
    
    
    
    i_counter_0_i = 0
    
    
    while (i_counter_0_i < i_number_of_loop_0_i):
        
        
        
        i_list_of_all_items_0_i.append(copy.deepcopy(i_list_0_i))
        
        
        i_list_0_i = i_next_step_4_i(i_list_0_i=i_list_0_i, i_number_of_element__minus_1__0_i=i_max_number_0_i, i_number_of_first_appear_0_i=i_number_of_first_appear_0_i)
        
        
        
        
        i_list_of_all_items_1_i.append(copy.deepcopy(i_list_1_i))
        
        
        i_list_1_i = i_next_step_5_i(i_list_0_i=i_list_1_i, i_number_of_element__minus_1__0_i=i_max_number_0_i, i_number_of_first_appear_0_i=i_number_of_first_appear_0_i)
        
        
        
        
        i_list_of_all_items_2_i.append(copy.deepcopy(i_list_2_i))
        
        
        i_list_2_i = i_next_step_6_i(i_list_0_i=i_list_2_i, i_number_of_element__minus_1__0_i=i_max_number_0_i, i_number_of_first_appear_0_i=i_number_of_first_appear_0_i)
        
        
        
        
        i_list_of_all_items_3_i.append(copy.deepcopy(i_list_3_i))
        
        
        i_list_3_i = i_next_step_7_i(i_list_0_i=i_list_3_i, i_number_of_element__minus_1__0_i=i_max_number_0_i, i_number_of_first_appear_0_i=i_number_of_first_appear_0_i)
        
        
        
        
        
        
        print(f"i_list_0_i = {i_list_0_i} . i_list_1_i = {i_list_1_i} . i_list_2_i = {i_list_2_i} . i_list_3_i = {i_list_3_i} .")
        
        
        
        i_counter_0_i += 1
        
        
        
        
    
    
    
    
    i_semaphore_of_result_0_i = i_check_if_repetition_exist_0_i(i_list_0_i=i_list_of_all_items_0_i)
    
    
    
    i_semaphore_of_result_1_i = i_check_if_repetition_exist_0_i(i_list_0_i=i_list_of_all_items_1_i)
    
    
    
    i_semaphore_of_result_2_i = i_check_if_repetition_exist_0_i(i_list_0_i=i_list_of_all_items_2_i)
    
    
    
    i_semaphore_of_result_3_i = i_check_if_repetition_exist_0_i(i_list_0_i=i_list_of_all_items_3_i)
    
    
    
    
    i_list_of_semaphores_of_result_0_i = [
                    
                    
                    i_semaphore_of_result_0_i,
                    
                    
                    i_semaphore_of_result_1_i,
                    
                    
                    i_semaphore_of_result_2_i,
                    
                    
                    i_semaphore_of_result_3_i,
                    
                    
                    
                    ]
    
    
    
    
    print(f"\n\n\n    i_list_of_semaphores_of_result_0_i = {i_list_of_semaphores_of_result_0_i} .\n\n\n")
    
    
    
    
    
    
    
    


if __name__ == "__main__":
    
    
    
    i_main_0_i()
    
    











