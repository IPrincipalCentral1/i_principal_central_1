












import os


cwd = os.path.dirname(os.path.abspath(__file__))






'''


---------------------------------------------------------------------------







this language should be between 2 person :




    ( agent , agent )
    
    
    ( agent , human )


    ( human , agent )


    ( human , human )

























---------------------------------------------------------------------------

'''










'''


---------------------------------------------------------------------------


char_pointer,

struct_variable_0,

char_,

int64_t_,

int8_t_,






---------------------------------------------------------------------------

'''


list_of_types_of_variable = [
                            
                                                        
                            ["char_pointer", "char*"],
                            
                            ["struct_variable_0", "struct variable_0"],
                            
                            ["char_", "char"],
                            
                            ["int64_t_", "int64_t"],
                            
                            ["int8_t_", "int8_t"],
                            
                            
                            
                            

                            ]



section_of_types_of_variable = "\n\n\n\n"



counter_0 = 0


while (counter_0 < len(list_of_types_of_variable)):


    section_of_types_of_variable += f"#define type_of_variable_0_{list_of_types_of_variable[counter_0][0]} {counter_0} \n\n\n"

    counter_0 += 1






file_0 = os.path.join(os.getcwd(), "i_compilor_0.c")

with open(file_0, "r") as f_:

    content = f_.read(os.path.getsize(file_0))



content = content.replace("_____all_types_of_variable_____", section_of_types_of_variable)


file_1 = os.path.join(os.getcwd(), "i_compilor_2.c")







counter_0 = 0


while (counter_0 < len(list_of_types_of_variable)):

    
    
    content = content.replace(f" {list_of_types_of_variable[counter_0][0]} ", f" {list_of_types_of_variable[counter_0][1]} ")
    
    
    counter_0 += 1









with open(file_1, "w") as f_:

    f_.write(content)



os.system(f"gcc i_compilor_2.c -o i_compilor_2")


os.system(f"./i_compilor_2")

















