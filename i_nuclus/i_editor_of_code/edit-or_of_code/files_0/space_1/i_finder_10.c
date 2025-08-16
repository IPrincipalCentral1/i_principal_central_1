













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




struct list_of_element_0
{
    
    char *element_0;
    
    char *content_0;
    
    struct list_of_element_0 *suiv;
    
    
    
};






void add_element_list_of_element_0(struct list_of_element_0 **head, char *element_0, char *content_0, int64_t index)
{

    struct list_of_element_0 *p = *head;
    
    struct list_of_element_0 *q = p;
    
    int64_t counter_0 = 0;
    
    while ((p != NULL) && (counter_0 < index))
    {
        
        q = p;
        
        p = p->suiv;
        
        counter_0 += 1;
        
    }

    if (counter_0 == index)
    {

        if ((index == 0) || (q == NULL))
        {
            
            
            q = (struct list_of_element_0 *) malloc(sizeof(struct list_of_element_0));
            
            
            
            q->element_0 = (char *) malloc(strlen(element_0) + 1);
            
            strcpy(q->element_0, element_0);
            
            
            
            q->content_0 = (char *) malloc(strlen(content_0) + 1);
            
            strcpy(q->content_0, content_0);
            
            
            
            q->suiv = *head;
            
            *head = q;
            
            
            
            
            
        }
        else
        {
            
            
            struct list_of_element_0 *k;
            
            k = (struct list_of_element_0 *) malloc(sizeof(struct list_of_element_0));
            
            
            
            
            k->element_0 = (char *) malloc(strlen(element_0) + 1);
            
            strcpy(k->element_0, element_0);
            
            
            
            k->content_0 = (char *) malloc(strlen(content_0) + 1);
            
            strcpy(k->content_0, content_0);
            
            
            
            k->suiv = q->suiv;
            
            q->suiv = k;
            
            
        }
        
    }
    
}







void remove_element_list_of_element_0(struct list_of_element_0 **head, int64_t index)
{

    struct list_of_element_0 *p = *head;

    struct list_of_element_0 *q = p;

    struct list_of_element_0 *g = q;


    int64_t counter_0 = 0;

    while ((p != NULL) && (counter_0 <= index))
    {

        g = q;
    
        q = p;

        p = p->suiv;

        counter_0 += 1;

        
    }

    if ((g != NULL) && (counter_0 > index))
    {
        
        if (index == 0)
        {
            
            
            if (*head != NULL)
            {
                
                *head = (*head)->suiv;
                
                free(q);
                
            }
            
        }
        else
        {
            
            g->suiv = p;
            
            free(q);
            
        }
        
        
    }
    
}






int64_t len_list_of_element_0(struct list_of_element_0 *head)
{

    int64_t counter_0 = 0;

    struct list_of_element_0 *p = head;

    while (p != NULL)
    {

        counter_0 += 1;

        p = p->suiv;

    }

    return counter_0;

}








void print_list_of_element_0(struct list_of_element_0 *head)
{
    
    struct list_of_element_0 *p = head;
    
    while (p != NULL)
    {
        
        printf("element_0 = %s . content_0 = %s .\n", p->element_0, p->content_0);
        
        p = p->suiv;
        
    }
    
}















int64_t get_size_of_file(char *path_of_file)
{

    FILE *fp;
    
    int64_t size;

    fp = fopen(path_of_file, "rb"); // افتح الملف في وضع القراءة الثنائية
    if (fp == NULL) {
        perror("error in open-ing the file .");
        return 1;
    }

    fseek(fp, 0, SEEK_END);   // تحريك المؤشر إلى نهاية الملف
    
    size = ftell(fp);         // إرجاع الموضع الحالي (عدد البايتات)
    
    fclose(fp);

    //printf("حجم الملف = %ld بايت\n", size);

    return size;
    
}





void read_ing_in_file(char *i_string_0, char *path_of_file)
{




    FILE *file = fopen(path_of_file, "r");


    bool semaphore;

    semaphore = false;

    if (file == NULL)
    {

        semaphore = true;

    }
    else
    {




        char i_char, i_s[2];
        
        
        // strcpy(i_string_0, "");
        
        
        char i_word[get_size_of_file(path_of_file) + 1];
        
        
        while (fscanf(file, "%s", i_word) != EOF)
        {
            
            
        }
        
        i_word[strlen(i_word)] = '\0';


        //printf("\n\n\n i_hello . i_word = %s .\n\n\n", i_word);


        strcpy(i_string_0, i_word);
        
        

        fclose(file);

     
     

    }




}







void finder_0(char *word, char *link_to_the_file)
{
    
    char *content_of_file = NULL;
    
    read_ing_in_file(content_of_file, link_to_the_file);
    
    char *element_0 = NULL;
    
    char *content_0 = NULL;
    
    
    
    
}




int main()
{
    
    char *link_to_the_file = "/mnt/mydisk/shared_directory_on_PC/my_link_updated/i_directory/main_editor_of_code/edit-or_of_code_for_program/edit-or_of_code/files_0/all_my_i_0/space_0/all_what_i_have/all_what_i_have_1.txt";
    
    char *word = "name_of_thing : \"com";
    
    struct list_of_element_0 *head = NULL;
    
    
    printf("before -> \n");
    
    print_list_of_element_0(head);
    
    add_element_list_of_element_0(&head, "element_for_test_0", "content_for_test_0", len_list_of_element_0(head));
    
    add_element_list_of_element_0(&head, "element_for_test_1", "content_for_test_1", len_list_of_element_0(head));
    
    add_element_list_of_element_0(&head, "element_for_test_2", "content_for_test_2", len_list_of_element_0(head));
    
    add_element_list_of_element_0(&head, "element_for_test_3", "content_for_test_3", len_list_of_element_0(head));
    
    
    printf("after -> \n");
    
    print_list_of_element_0(head);
    
    
    //finder_0(word, link_to_the_file);
    
    
    
    
    return 0;
    
}















