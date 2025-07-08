

















#include <stdio.h>

#include <stdlib.h>

#include <stdbool.h>

#include <sys/time.h>

#include <stdint.h>

#include <string.h>

#include <unistd.h>

#include <limits.h>

#include <time.h>

#include <wchar.h>

#include <locale.h>

#include <malloc.h>






#define length_of_input 1000000


#define length_of_output 1000000









_____all_types_of_variable_____









//enum all_types_of_variable
//{


    //char_pointer,

    //struct_variable_0,

    //char_,

    //int64_t_,

    //int8_t_,




//};




// this is the variable


struct variable_0
{


    char *name_of_variable;

    int64_t type_of_variavle;
    
    void *element;
    
    struct variable_0 *suiv;


};






// this is astruct of the creation of variable 


void create_variable_0(struct variable_0 *head_of_list, struct variable_0 *position)
{


    
    


}






void create_variable_0_char_pointer(struct variable_0 *head_of_list, struct variable_0 *position, )
{


    
    


}
















void make_the_input(char *input)
{



    strcpy(input, "i hello");


    

}




void compilor(char *input, char *output)
{


    
    strcpy(output, "i welcome");


    
    

}




int main()
{




    struct variable_0 *head_of_list = NULL;





    char *input = malloc(length_of_input), *output = malloc(length_of_output); 


    make_the_input(input);


    printf("\n\n\n    input = '%s' .\n\n\n", input);
    

    compilor(input, output);

    
    printf("\n\n\n    output = '%s' .\n\n\n", output);


    return 0;

}

















