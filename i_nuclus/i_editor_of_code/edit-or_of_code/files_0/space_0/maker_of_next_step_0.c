














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


    

    strcpy(i_cwd, "/i_run_mixer_1.txt");

    // strcat(file_path, "/Data_Base/payment_with_unity_for_project/");



    //"printing_personal_account.info"

    //printf("file_path = %s .\n", file_path);



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

        fclose(file);


        // printf("the file is printed succefuly .");

    }



    // if (file_path != NULL)
    // {

    //     free(file_path);

    // }



}







int main()
{


    char *message = "true";

    save_ing_in_file(message);


    return 0;


}















