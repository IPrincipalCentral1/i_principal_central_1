







































































































/*


this program is for i . principal-central i_0  i am i .



*/




/*







i_bank : 
    
    identificator : "0" 
        
        name : "Billal" 
        
        pre_name : "Debouci" 
        
        number_of_phone : "+213 561577437" 
        
        e_mail : "deboubil24@gmail.com" 
        
        pass_word : "i_principal_central__i_0__i" 
        
        pocket : 
            
            
            
            name_of_unity : "i" 
            
                amount : "1" 
            
            
            
            name_of_unity : "the quality of i" 
            
                amount : 
            
            
            
            


*/











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




#define i_macro_of_length_of_text_0_i 1000000









void save_into_file(char *content, char *file_path)
{



    
    
    FILE *file = fopen(file_path, "w");

    bool semaphore;

    semaphore = false;

    if (file == NULL)
    {

        semaphore = true;

        // printf("Error opening the file .\n");

    }
    else
    {
        
        
        
        fprintf(file, "%s", content);
        
        
        fflush(file);
        
        
        //fclose(file);
        
        
        // printf("the file is printed succefuly .");

    }




}










int main()
{


    //int64_t i_counter_0_i = 0, i_counter_1_i = 10000000000;

    //int64_t i_counter_2_i = i_counter_1_i / 100000;



    int64_t i_counter_0_i = 0, i_counter_1_i = 10000;

    int64_t i_counter_2_i = i_counter_1_i / 100;

    
    
    int64_t i_number_0_i = 10000;
    
    
    char *i_string_0_i = malloc(10000 + 1), *i_string_1_i = malloc(i_counter_2_i  + 2);
    
    
    
    
    
    

    
    char *file_path = malloc(10000);
    
    
    
    char i_cwd_0_i[PATH_MAX];
    
    
    
    
    bool semaphore = false;
    
    if (getcwd(i_cwd_0_i, sizeof(i_cwd_0_i)) != NULL)
    {
    
        semaphore = true;
    
    }
    
    
    strcpy(file_path, i_cwd_0_i);
    
    
    strcat(file_path, "/i_bank_official_0_0_i.i_bank_0_i");
    
    
    
    
    FILE *file = fopen(file_path, "w");
    
    semaphore = false;
    
    if (file == NULL)
    {
    
        semaphore = true;
    
        // printf("Error opening the file .\n");
    
    }
    else
    {
        
            
        
        
        
        
        
        
        
        strcpy(i_string_0_i, "\n\ni_bank : \n\n");
        
        
        strcat(i_string_0_i, "    identificator : \"0\" \n\n");
        
        
        strcat(i_string_0_i, "        name : \"Billal\" \n\n");
        
        
        strcat(i_string_0_i, "        pre_name : \"Debouci\" \n\n");
        
        
        strcat(i_string_0_i, "        number_of_phone : \"+213 561577437\" \n\n");
        
        
        strcat(i_string_0_i, "        e_mail : \"deboubil24@gmail.com\" \n\n");
        
        
        strcat(i_string_0_i, "        pass_word : \"i_principal_central__i_0__i\" \n\n");
        
        
        strcat(i_string_0_i, "        pocket : \n\n");
        
        
        strcat(i_string_0_i, "            name_of_unity : \"i\" \n\n");
        
        
        strcat(i_string_0_i, "                amount : \"1\" \n\n");
        
        
        strcat(i_string_0_i, "            name_of_unity : \"the quality of i\" \n\n");
        
        
        strcat(i_string_0_i, "                amount : ");
        
        
        
        strcat(i_string_0_i, "\"1");
        
        
        
        fprintf(file, "%s", i_string_0_i);
        
        
        
        
        
        strcpy(i_string_1_i, "");
        
        
        i_counter_0_i = 0;
        
        
        while (i_counter_0_i < i_counter_2_i)
        {
            
            strcat(i_string_1_i, "0");
            
            
            i_counter_0_i += 1;
            
            
        }
        
        
        
        
        //strcat(i_string_0_i, ".");
        
        
        
        i_counter_0_i = 0;
            
        
        while (i_counter_0_i < i_counter_1_i / i_counter_2_i)
        {
            
            
            
            //strcat(i_string_0_i, "0");
            
            
            fprintf(file, "%s", i_string_1_i);
            
            
            i_counter_0_i += 1;
            
            
        }
            
        
        
        fprintf(file, "%s", ".");
        
        
        fprintf(file, "%s", i_string_1_i);
        
        
        fprintf(file, "%s", "\"\n\n");
        
        
        
        //strcat(i_string_0_i, "\"\n\n");
        
        
        
        
        //fprintf(file, "%s", i_string_0_i);
        
        
        fflush(file);
        
        
        //fclose(file);
        
        
        // printf("the file is printed succefuly .");
    
    }
    
    
    
    
    return 0;
    
    
    
}

























