














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











void save_ing_in_file(char *content)
{




    char i_cwd[PATH_MAX];

    bool semaphore = false;

    if (getcwd(i_cwd, sizeof(i_cwd)) != NULL)
    {

        semaphore = true;

    }


    

    strcat(i_cwd, "/i_run_mixer_1.txt");

    // strcat(file_path, "/Data_Base/payment_with_unity_for_project/");



    //"printing_personal_account.info"

    printf("i_cwd = %s .\n", i_cwd);



    FILE *file = fopen(i_cwd, "w");


    semaphore = false;

    if (file == NULL)
    {

        semaphore = true;

         printf("Error opening the file .\n");

    }
    else
    {


        fprintf(file, "%s", content);

        fclose(file);


         printf("the file is printed succefuly .");

    }





}







int main()
{


    char *message = "true";

    save_ing_in_file(message);


    return 0;


}















