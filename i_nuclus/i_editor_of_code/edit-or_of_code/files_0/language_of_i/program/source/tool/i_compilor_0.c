

















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



    char *input = malloc(length_of_input), *output = malloc(length_of_output); 


    make_the_input(input);


    printf("\n\n\n    input = '%s' .\n\n\n", input);
    

    compilor(input, output);

    
    printf("\n\n\n    output = '%s' .\n\n\n", output);


    return 0;

}

















