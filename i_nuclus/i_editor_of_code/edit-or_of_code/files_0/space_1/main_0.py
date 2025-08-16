







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





void read_ing_in_file_1(wchar_t *content_of_file, char *path_of_file)
{




    FILE *file = fopen(path_of_file, "rb");


    bool semaphore;

    semaphore = false;

    if (file == NULL)
    {

        semaphore = true;

    }
    else
    {
        
        
        
        
        int64_t size_in_bytes = get_size_of_file(path_of_file);
        
        if (size_in_bytes < 0) {
            wprintf(L"خطأ في حساب حجم الملف\n");
            fclose(file);
            return;
        }
    
        
        
        // عدد العناصر من نوع wchar_t
        
        size_t count = size_in_bytes / sizeof(wchar_t);
        
        
        int64_t counter_0 = 0, incrementer = 1000, number_0;
        
        wchar_t small_content[incrementer + 10], *p_inc;
        
        size_t read_count;
        
        p_inc = wcpcpy(content_of_file, L"");
        
        
        while (counter_0 < count)
        {
            
            
            number_0 = (count - counter_0 < incrementer) ? (count - counter_0) : incrementer;
            
            
            read_count = fread(small_content, sizeof(wchar_t), number_0, file);
            
            // إنهاء النص
            
            small_content[read_count] = L'\0';        
            
            p_inc = wcpcpy(p_inc, small_content);
            
            counter_0 += incrementer;
            
        }
        
        //printf("i_hello_2 . content_of_file = %s .\n", content_of_file);
        
        
        fclose(file);
        
        
        
        
    }
    
    
    
    
}



struct list_of_element_0* uploader_into_memory(char *link_to_the_file)
{
    
    char content_of_file[get_size_of_file(link_to_the_file) + 1];
    
    read_ing_in_file(content_of_file, link_to_the_file);
    
    //printf("i_hello_0 . get_size_of_file(link_to_the_file) = %ld . content_of_file = %s\n", get_size_of_file(link_to_the_file), content_of_file);
    
    
    wchar_t element_0[wcslen(content_of_file) + 1];
    
    wchar_t content_0[wcslen(content_of_file) + 1];
    
    
    
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




