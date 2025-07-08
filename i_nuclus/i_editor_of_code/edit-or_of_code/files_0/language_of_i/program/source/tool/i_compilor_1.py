












import os




'''




char_pointer,

struct_variable_0,

char_,

int64_t_,

int8_t_,







'''


list_of_types_of_variable = [
                            
                                                        
                            "char_pointer",
                            
                            "struct_variable_0",
                            
                            "char_",
                            
                            "int64_t_",
                            
                            "int8_t_",
                            
                            
                            
                            

                            ]



section_of_types_of_variable = "\n\n\n\n"



counter_0 = 0


while (counter_0 < len(list_of_types_of_variable)):


    section_of_types_of_variable += f"#define {list_of_types_of_variable[counter_0]} {counter_0} \n\n\n"

    counter_0 += 1





file_0 = os.path.join(os.getcwd(), "i_compilor_0.c")

with open(file_0, "r") as f_:

    content = f_.read(os.path.getsize(file_0))



content = content.replace("_____all_types_of_variable_____", section_of_types_of_variable)


file_1 = os.path.join(os.getcwd(), "i_compilor_2.c")


with open(file_1, "w") as f_:

    f_.write(content)



os.system(f"gcc i_compilor_2.c -o i_compilor_2")


os.system(f"./i_compilor_2")

















