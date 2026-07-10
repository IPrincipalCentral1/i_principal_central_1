

















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












// this is the variable


struct variable_0
{


    char *name_of_variable;

    int64_t type_of_variavle;

    char *comment;
    
    void *element;
    
    struct variable_0 *previous;
    
    struct variable_0 *suiv;


};






// this is astruct of the creation of variable 


void create_variable_0(struct variable_0 **position, char_pointer element)
{


    

    
    


}






void create_variable_0_char_pointer(struct variable_0 **position, char_pointer element, char_pointer comment)
{
    
    
    
    struct variable_0 *p;
    



    if ()
    {
        
        
        q = (struct variable_0 *) malloc(sizeof(struct variable_0));
        
        
        *position = q
    
    
    
    }


    
    
}





void add_ele_list_of_Accounts_of_Amount(struct list_of_Accounts_of_Amount **t, struct Unity_of_Number unity_, struct number *amount_, int64_t index)
{



    struct list_of_Accounts_of_Amount *p = *t;

    struct list_of_Accounts_of_Amount *q = p;

    int64_t i = 0;

    while ((p != NULL) && (i < index))// && (char_equal(p->unity.name_of_unity, unity_.name_of_unity) == false))
    {

        q = p;

        p = p->suiv;

        i += 1;

    }


    if (i == index)
    {

        if ((index == 0) || (q == NULL))
        {


            q = (struct list_of_Accounts_of_Amount *) malloc(sizeof(struct list_of_Accounts_of_Amount));


            // q->unity.name_of_unity = (char *)malloc(strlen(unity_.name_of_unity) + 2);

            // strcpy(q->unity.name_of_unity, unity_.name_of_unity);
            


            q->unity.name_of_unity = (wchar_t *)malloc(wcslen(unity_.name_of_unity) * sizeof(wchar_t) + 2);

            wcscpy(q->unity.name_of_unity, unity_.name_of_unity);

            q->amount.length_of_num = 0;

            int_copy(&(q->amount), amount_);


            q->suiv = *t;

            *t = q;





        }
        else
        {


            struct list_of_Accounts_of_Amount *k;

            k = (struct list_of_Accounts_of_Amount *) malloc(sizeof(struct list_of_Accounts_of_Amount));

            // k->unity.name_of_unity = (char *) malloc(strlen(unity_.name_of_unity) + 2);

            // strcpy(k->unity.name_of_unity, unity_.name_of_unity);
        



            k->unity.name_of_unity = (wchar_t *)malloc(wcslen(unity_.name_of_unity) * sizeof(wchar_t) + 2);

            wcscpy(k->unity.name_of_unity, unity_.name_of_unity);


            k->amount.length_of_num = 0;

            int_copy(&(k->amount), amount_);


            k->suiv = q->suiv;

            q->suiv = k;

            
        }

    }


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

















