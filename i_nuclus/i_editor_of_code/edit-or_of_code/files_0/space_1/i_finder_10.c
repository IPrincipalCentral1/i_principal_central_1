













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



struct list_of_element_1
{
    
    wchar_t *element_0;
    
    wchar_t *content_0;
    
    struct list_of_element_1 *suiv;
    
    
    
};










wchar_t *str_from_UTF_8(char *utf8_str) {

    size_t len = mbstowcs(NULL, utf8_str, 0);

    if (len == (size_t)-1) 
    {
        
        return NULL; // فشل التحويل
        
    }
    wchar_t *wstr = malloc((len + 1) * sizeof(wchar_t));

    mbstowcs(wstr, utf8_str, len + 1);

    return wstr;

}




double time_()
{

    struct timeval u;

    if (gettimeofday(&u, NULL) == 0)
    {


        return u.tv_sec + (u.tv_usec / 1000000.0);


    }


}





double time_1()
{
    
    struct timespec ts;
    
    // CLOCK_MONOTONIC أدق لقياس الفترات (ما يتأثرش بتغيير ساعة النظام)
    
    if (clock_gettime(CLOCK_MONOTONIC, &ts) == 0) 
    {
    
        return ts.tv_sec + ts.tv_nsec / 1e9;
    
    } 
    else 
    {
    
        return -1.0; // خطأ
    
    }
}



int64_t min_0(int64_t a, int64_t b)
{
    
    if (a < b)
    {
        
        return a;
        
    }
    else
    {
        
        return b;
        
    }
    
    
}




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










void add_element_list_of_element_1(struct list_of_element_1 **head, wchar_t *element_0, wchar_t *content_0, int64_t index)
{

    struct list_of_element_1 *p = *head;
    
    struct list_of_element_1 *q = p;
    
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
            
            
            q = (struct list_of_element_1 *) malloc(sizeof(struct list_of_element_1));
            
            
            
            q->element_0 = (wchar_t *) malloc((wcslen(element_0) + 1) * sizeof(wchar_t));
            
            wcscpy(q->element_0, element_0);
            
            
            
            q->content_0 = (wchar_t *) malloc((wcslen(content_0) + 1) * sizeof(wchar_t));
            
            wcscpy(q->content_0, content_0);
            
            
            
            q->suiv = *head;
            
            *head = q;
            
            
            
            
            
        }
        else
        {
            
            
            struct list_of_element_1 *k;
            
            k = (struct list_of_element_1 *) malloc(sizeof(struct list_of_element_1));
            
            
            
            
            k->element_0 = (wchar_t *) malloc((wcslen(element_0) + 1) * sizeof(wchar_t));
            
            wcscpy(k->element_0, element_0);
            
            
            
            k->content_0 = (wchar_t *) malloc((wcslen(content_0) + 1) * sizeof(wchar_t));
            
            wcscpy(k->content_0, content_0);
            
            
            
            k->suiv = q->suiv;
            
            q->suiv = k;
            
            
        }
        
    }
    
}







void remove_element_list_of_element_1(struct list_of_element_1 **head, int64_t index)
{

    struct list_of_element_1 *p = *head;

    struct list_of_element_1 *q = p;

    struct list_of_element_1 *g = q;


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






int64_t len_list_of_element_1(struct list_of_element_1 *head)
{

    int64_t counter_0 = 0;

    struct list_of_element_1 *p = head;

    while (p != NULL)
    {

        counter_0 += 1;

        p = p->suiv;

    }

    return counter_0;

}








void print_list_of_element_1(struct list_of_element_1 *head)
{
    
    struct list_of_element_1 *p = head;
    
    setlocale(LC_ALL, "");
    
    while (p != NULL)
    {
        
        
        printf("element_0 = %ls . content_0 = %ls .\n", p->element_0, p->content_0);
        
        //printf("element_0 = %ls . content_0 = %ls .\n", str_from_UTF_8(p->element_0), str_from_UTF_8(p->content_0));
        
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





void read_ing_in_file(char *content_of_file, char *path_of_file)
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
        
        
        
        
        int64_t size = get_size_of_file(path_of_file);
        
                
        fread(content_of_file, 1, size, file);
        
        content_of_file[size] = '\0';
        
        
        //printf("i_hello_2 . content_of_file = %s .\n", content_of_file);
        
        
        fclose(file);
        
        
        
        
    }
    
    
    
    
}






struct list_of_element_0* uploader_into_memory(char *link_to_the_file)
{
    
    char content_of_file[get_size_of_file(link_to_the_file) + 1];
    
    read_ing_in_file(content_of_file, link_to_the_file);
    
    //printf("i_hello_0 . get_size_of_file(link_to_the_file) = %ld . content_of_file = %s\n", get_size_of_file(link_to_the_file), content_of_file);
    
    
    char element_0[strlen(content_of_file) + 1];
    
    char content_0[strlen(content_of_file) + 1];
    
    
    
    // upload into the memory 
    
    
    struct list_of_element_0 *head = NULL;
    
    
    
    
    int64_t counter_0 = 0, counter_1;
    
    
    while (counter_0 < strlen(content_of_file))
    {
        
        // cach element_0 
        
        strcpy(element_0, "");
        
        
        strcpy(content_0, "");
        
        
        counter_1 = 0;
        
        while ((counter_0 < strlen(content_of_file)) && (content_of_file[counter_0] != '\n'))
        {
            
            element_0[counter_1] = content_of_file[counter_0];
            
            //printf("i_hello_1 . content_of_file[counter_0] = %c .\n", content_of_file[counter_0]);
            
            
            counter_0 += 1;
            
            counter_1 += 1;
            
            
        }
        
        
        element_0[counter_1] = '\0';
        
        
        counter_0 += 5;
        
                
        counter_1 = 0;
        
        while ((counter_0 < strlen(content_of_file)) && (content_of_file[counter_0] != '\n'))
        {
            
            content_0[counter_1] = content_of_file[counter_0];
            
            
            counter_0 += 1;
            
            counter_1 += 1;
            
            
        }
        
        
        content_0[counter_1] = '\0';
        
        
        
        counter_0 += 1;
        
        
        add_element_list_of_element_0(&head, element_0, content_0, len_list_of_element_0(head));
        
        
        
        
        
    }
    
    
    print_list_of_element_0(head);
    
    
    return head;
    
    
}




void finder_0(char *word, struct list_of_element_0 *head_0)
{
    
    int64_t counter_0, counter_1;
    
    int64_t len_element_0;
    
    struct list_of_element_0 *head_1 = NULL, *p = NULL;
    
    p = head_0;
    
    int64_t len_head_0 = len_list_of_element_0(head_0);
    
    int64_t len_word = strlen(word);
    
    counter_0 = 0;
    
    while (p != NULL)
    {
        
        counter_1 = 0;
        
        len_element_0 = strlen(p->element_0);
        
        while ((counter_1 < len_word) && (counter_1 < len_element_0) && (word[counter_1] == (p->element_0)[counter_1]))
        {
            counter_1 += 1;
        }
        
        
        if (counter_1 == len_word)
        {
            
            add_element_list_of_element_0(&head_1, p->element_0, p->content_0, len_list_of_element_0(head_1));
            
        }
        
        
        p = p->suiv;
        
    }
    
    printf("\n\n\n after_finder -> \n");
    
    print_list_of_element_0(head_1);
    
}











//void read_ing_in_file_1(wchar_t *content_of_file, char *path_of_file)
//{




    //FILE *file = fopen(path_of_file, "rb");


    //bool semaphore;

    //semaphore = false;

    //if (file == NULL)
    //{

        //semaphore = true;

    //}
    //else
    //{




        //int64_t size_in_bytes = get_size_of_file(path_of_file);

        //if (size_in_bytes < 0) {
            //wprintf(L"خطأ في حساب حجم الملف\n");
            //fclose(file);
            //return;
        //}



        //// عدد العناصر من نوع wchar_t

        //size_t count = size_in_bytes / sizeof(wchar_t);


        //int64_t counter_0 = 0, incrementer = 1000, number_0;

        //wchar_t small_content[incrementer + 10], *p_inc, content_of_file_0[get_size_of_file(path_of_file) + 1];

        //size_t read_count;

        //p_inc = wcpcpy(content_of_file_0, L"");


        //while (counter_0 < count)
        //{


            //number_0 = (count - counter_0 < incrementer) ? (count - counter_0) : incrementer;


            //read_count = fread(small_content, sizeof(wchar_t), number_0, file);

            //// إنهاء النص

            //small_content[read_count] = L'\0';        

            //p_inc = wcpcpy(p_inc, small_content);

            //counter_0 += incrementer;

        //}




        ////printf("i_hello_2 . content_of_file = %s .\n", content_of_file);


        //fclose(file);




    //}




//}




void read_ing_in_file_1(wchar_t *content_of_file, const char *path_of_file)
{
    FILE *file = fopen(path_of_file, "rb");
    if (!file) {
        wprintf(L"تعذر فتح الملف: %s\n", path_of_file);
        return;
    }

    // احسب حجم الملف بالبايت
    fseek(file, 0, SEEK_END);
    long size_in_bytes = ftell(file);
    fseek(file, 0, SEEK_SET);

    if (size_in_bytes <= 0) {
        wprintf(L"الملف فارغ أو فيه خطأ\n");
        fclose(file);
        return;
    }

    // اقرأ كل البايتات
    char buffer[size_in_bytes + 1];
    if (!buffer) {
        wprintf(L"فشل في تخصيص الذاكرة\n");
        fclose(file);
        return;
    }

    fread(buffer, 1, size_in_bytes, file);
    buffer[size_in_bytes] = '\0';
    fclose(file);

    // التحويل إلى wchar_t (UTF-8 → wide)
    setlocale(LC_ALL, ""); // ضروري حتى mbstowcs يفهم UTF-8
    mbstate_t state;
    memset(&state, 0, sizeof state);

    const char *src = buffer;
    wchar_t *dst = content_of_file;
    size_t converted = mbsrtowcs(dst, &src, size_in_bytes + 1, &state);

    if (converted == (size_t)-1) {
        wprintf(L"فشل في التحويل من UTF-8 إلى wchar_t\n");
        //free(buffer);
        return;
    }

    //free(buffer);
}




struct list_of_element_1* uploader_into_memory_1(char *link_to_the_file)
{
    
    
    
    setlocale(LC_ALL, "");
    
    
    wchar_t content_of_file[get_size_of_file(link_to_the_file) + 1];
    
    read_ing_in_file_1(content_of_file, link_to_the_file);
    
    printf("i_hello_0 . get_size_of_file(link_to_the_file) = %ld . content_of_file = %ls\n", get_size_of_file(link_to_the_file), content_of_file);
    
    int64_t len_content_of_file = wcslen(content_of_file);
    
    wchar_t element_0[len_content_of_file + 1];
    
    wchar_t content_0[len_content_of_file + 1];
    
    
    
    // upload into the memory 
    
    
    struct list_of_element_1 *head = NULL;
    
    
    
    
    int64_t counter_0 = 0, counter_1;
    
    
    while (counter_0 < wcslen(content_of_file))
    {
        
        // cach element_0 
        
        wcscpy(element_0, L"");
        
        
        wcscpy(content_0, L"");
        
        
        counter_1 = 0;
        
        while ((counter_0 < wcslen(content_of_file)) && (content_of_file[counter_0] != L'\n'))
        {
            
            element_0[counter_1] = content_of_file[counter_0];
            
            //printf("i_hello_1 . content_of_file[counter_0] = %c .\n", content_of_file[counter_0]);
            
            
            counter_0 += 1;
            
            counter_1 += 1;
            
            
        }
        
        
        element_0[counter_1] = L'\0';
        
        
        counter_0 += 5;
        
                
        counter_1 = 0;
        
        while ((counter_0 < wcslen(content_of_file)) && (content_of_file[counter_0] != L'\n'))
        {
            
            content_0[counter_1] = content_of_file[counter_0];
            
            
            counter_0 += 1;
            
            counter_1 += 1;
            
            
        }
        
        
        content_0[counter_1] = L'\0';
        
        
        
        counter_0 += 1;
        
        
        add_element_list_of_element_1(&head, element_0, content_0, len_list_of_element_1(head));
        
        
        
        
        
    }
    
    
    print_list_of_element_1(head);
    
    
    return head;
    
    
}




void finder_1(wchar_t *word, struct list_of_element_1 *head_0)
{
    
    int64_t counter_0, counter_1;
    
    int64_t len_element_0;
    
    struct list_of_element_1 *head_1 = NULL, *p = NULL;
    
    p = head_0;
    
    int64_t len_head_0 = len_list_of_element_1(head_0);
    
    int64_t len_word = wcslen(word);
    
    counter_0 = 0;
    
    while (p != NULL)
    {
        
        counter_1 = 0;
        
        len_element_0 = wcslen(p->element_0);
        
        while ((counter_1 < len_word) && (counter_1 < len_element_0) && (word[counter_1] == (p->element_0)[counter_1]))
        {
            
            counter_1 += 1;
            
        }
        
        
        if (counter_1 == len_word)
        {
            
            add_element_list_of_element_1(&head_1, p->element_0, p->content_0, len_list_of_element_1(head_1));
            
        }
        
        
        p = p->suiv;
        
    }
    
    printf("\n\n\n after_finder -> \n");
    
    print_list_of_element_1(head_1);
    
}



























int main()
{
    
    char *link_to_the_file = "/mnt/mydisk/shared_directory_on_PC/my_link_updated/i_directory/main_editor_of_code/edit-or_of_code_for_program/edit-or_of_code/files_0/space_1/file_1.txt";
    
    wchar_t *word = L"name_of_thing : \"com";
    
    struct list_of_element_1 *head = NULL;
    

    //printf("before -> \n");

    //print_list_of_element_1(head);



    //add_element_list_of_element_1(&head, L"element_for_test_0", L"content_for_test_0", len_list_of_element_1(head));
    
    //add_element_list_of_element_1(&head, L"element_for_test_1", L"content_for_test_1", len_list_of_element_1(head));
    
    //add_element_list_of_element_1(&head, L"element_for_test_2", L"content_for_test_2", len_list_of_element_1(head));
    
    //add_element_list_of_element_1(&head, L"element_for_test_3", L"content_for_test_3", 2);


    //printf("len_ = %ld element .\n", len_list_of_element_1(head));

    //printf("after -> \n");

    //print_list_of_element_1(head);


    
    printf("\n\n\n\n\n ----------------------------------------------------------------------------- \n\n\n\n");
    
    double t1, t2;
    
    
    t1 = time_1();
    

    head = uploader_into_memory_1(link_to_the_file);


    //finder_0(word, head);

    finder_1(word, head);

    
    t2 = time_1();
    
    printf("\n\n time = %.10f second .\n", t2 - t1);
    
    return 0;
    
}















