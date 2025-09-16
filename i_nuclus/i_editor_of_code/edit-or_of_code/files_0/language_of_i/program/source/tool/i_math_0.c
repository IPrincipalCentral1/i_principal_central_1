










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




#define length_of_the_result 1000000









#define i_Number_of_digits_max 18


#define i_macro_of_number_of_digite_maximum_after_the_floating_point 0


#define i_macro_of_Number_max_of_word_byte 125



#define i_macro_of_length_of_encoding "___postion_of_max_range___"

#define i_macro_of_length_of_encoding_int 1


#define i_name_of_unity_of_encoding L"ASCII"

#define i_max_of_string_of_mixer 10







/*  



    obligation (0) : i_macro_of_number_of_digite_maximum_after_the_floating_point >= 0

    obligation (1) : char *s = NULL; --> str_number(&s, number_var);

    obligation (2) : the account of Billal 'identificator == "0"' should exist

    obligation (3) : i_macro_of_length_of_encoding == (length of encoding) - 1

    obligation (4) : it should be not parallel

    obligation (5) : i_macro_of_Number_max_of_word_byte * 18 >= i_macro_of_number_of_digite_maximum_after_the_floating_point




*/








struct number
{

    int64_t *num;

    int64_t number_of_digite_maximum_after_the_floating_point;

    int64_t length_of_num;

    int8_t signe;

};




struct operation_int
{

    int64_t ele;

    int64_t reminder;

};





struct Unity_of_Number
{

    wchar_t *name_of_unity;

};




struct list_of_Accounts_of_Amount
{

    struct Unity_of_Number unity;

    struct number amount;   

    struct list_of_Accounts_of_Amount *suiv; 

};


struct Pocket
{

    struct list_of_Accounts_of_Amount *head_of_amount_accounts;

};





struct list_of_personal_accounts
{

    struct number identificator; // من عندنا رقم التعريف هاذا

    char *name; //  الإسم  

    char *pre_name; // اللقب

    char *phone_number; // رقم الهاتف

    char *e_mail; // البريد الإلكتروني

    char *pass_word; // كلمة السر


    struct Pocket green_pocket;

    struct Pocket red_pocket;


    struct list_of_personal_accounts *suiv;


};







struct circle_
{

    char *name_of_circle;

    char *type_of_reference;

    void *pointer;

};



typedef struct circle_ circle; 







int64_t my_min(int64_t a, int64_t b)
{

    if (a <= b)

        return a;

    else

        return b;

}



int64_t my_abs_(int64_t a)
{

    if (a < 0)
    {

        return -a;

    }
    else
    {

        return a;

    }

}



double time_()
{

    struct timeval u;

    if (gettimeofday(&u, NULL) == 0)
    {


        return u.tv_sec + (u.tv_usec / 1000000.0);


    }


}






void date_()
{


    time_t t;
    
    struct tm *current_time;

    // الحصول على الوقت الحالي
    
    t = time(NULL);
    
    current_time = localtime(&t);

    // طباعة التاريخ والوقت بالشكل المطلوب


    printf("date : %d-%02d-%02d %02d:%02d:%02d\n",
           current_time->tm_year + 1900,// السنة
           current_time->tm_mon + 1,    // الشهر (نضيف 1 لأن الأشهر تبدأ من 0)
           current_time->tm_mday,        // اليوم
           current_time->tm_hour,       // الساعات
           current_time->tm_min,        // الدقائق
           current_time->tm_sec);       // الثواني




}





char* str_from_UTF_8(wchar_t *wtext)
{

    // إعداد البيئة المحلية لدعم UTF-8

    // نص واسع (wchar_t)

    //wchar_t *wtext = L"مرحبا بالعالم \n";

    // نحسب الحجم المطلوب لتخزين النص بعد التحويل

    size_t size = wcstombs(NULL, wtext, 0) + 1;

    // نحجز مساحة للسلسلة المحوّلة

    char *utf8_text = malloc(size);

    if (!utf8_text) 
    {

        perror("malloc");

    }

    // نحول النص

    wcstombs(utf8_text, wtext, size);

    // نفتح ملف للكتابة بالوضع الثنائي

    return utf8_text;

}




bool char_equal(wchar_t *s1, wchar_t *s2)
{

    if (wcslen(s1) == wcslen(s2))
    {

        int64_t i = 0;

        while ((i < wcslen(s1)) && (s1[i] == s2[i]))
        {

            i += 1;

        }

        if (i == wcslen(s1))
        {

            return true;

        }
        else
        {

            return false;

        }

    }
    else
    {

        return false;

    }


}




bool char_equal_(char *s1, char *s2)
{

    if (strlen(s1) == strlen(s2))
    {

        int64_t i = 0;

        while ((i < strlen(s1)) && (s1[i] == s2[i]))
        {

            i += 1;

        }

        if (i == strlen(s1))
        {

            return true;

        }
        else
        {

            return false;

        }

    }
    else
    {

        return false;

    }


}





int64_t c_to_int(char c)
{

    int64_t n = -1;

    if (c == '0')

        n = 0;

    else if (c == '1')

        n = 1;

    else if (c == '2')

        n = 2;

    else if (c == '3')

        n = 3;

    else if (c == '4')

        n = 4;

    else if (c == '5')

        n = 5;

    else if (c == '6')

        n = 6;

    else if (c == '7')

        n = 7;

    else if (c == '8')

        n = 8;

    else if (c == '9')

        n = 9;


    return n;

}



char int_to_c(int64_t n)
{

    char c;

    if (n == 0)

        c = '0';

    else if (n == 1)

        c = '1';

    else if (n == 2)

        c = '2';

    else if (n == 3)

        c = '3';

    else if (n == 4)

        c = '4';

    else if (n == 5)

        c = '5';

    else if (n == 6)

        c = '6';

    else if (n == 7)

        c = '7';

    else if (n == 8)

        c = '8';

    else if (n == 9)

        c = '9';


    return c;

}


char* int_ND_to_str(int64_t n)
{

    int64_t i = 0, d1, d2;

    char *res = malloc(i_Number_of_digits_max + 1);

    d1 = n;

    d2 = n;

    while (i < i_Number_of_digits_max)
    {

        d1 = d1 / 10;

        d2 = d2 - (d1 * 10);

        res[i_Number_of_digits_max - i - 1] = int_to_c(d2);

        d2 = d1;
     
        i += 1;

    }

    res[i_Number_of_digits_max] = '\0';

    return res;

}




char* int_ND_to_str_1(int64_t n, char* res)
{

    int64_t i = 0, d1, d2;

    d1 = n;

    d2 = n;

    while (i < i_Number_of_digits_max)
    {

        d1 = d1 / 10;

        d2 = d2 - (d1 * 10);

        res[i_Number_of_digits_max - i - 1] = int_to_c(d2);

        d2 = d1;
     
        i += 1;



    }

    res[i_Number_of_digits_max] = '\0';

    return res;

}






// adds and removes


void add_ele_int(struct number *t, int64_t el, int64_t index)
{

    struct number *p = t;


    int64_t *q = malloc((p->length_of_num + 1) * sizeof(int64_t));


    int64_t i = 0;




    while ((i < (p->length_of_num)) && (i < index))
    {
        

        q[i] = (p->num)[i];

        i += 1;

    }

    if (i == index)
    {
        

        q[i] = el;

        i += 1;


        while ((i < ((p->length_of_num) + 1)))
        {

            q[i] = (p->num)[i - 1];

            i += 1;

        }

        if (p->length_of_num > 0)
        {
        
            free((t->num));

        }



        (*t).num = q;

        (*t).length_of_num += 1;

    }

}





void remove_ele_int(struct number *t, int64_t index)
{


    struct number *p = t;


    if ((p->length_of_num) > 0)
    {

        int64_t *q = malloc((((p->length_of_num - 1)) * sizeof(int64_t)));


        int64_t i = 0;


        while ((i < (p->length_of_num)) && (i < index))
        {
            

            q[i] = (p->num)[i];

            i += 1;

        }

        if (i == index)
        {

            

            while ((i + 1) < (p->length_of_num))
            {
                
                q[i] = (p->num)[i + 1];

                i += 1;

            }
            

            if (p->length_of_num > 0)
            {
            
                free((t->num));

            }



            (*t).num = q;

            (*t).length_of_num -= 1;


        }

    }

}




void int_copy(struct number *result, struct number *a)
{




    result->number_of_digite_maximum_after_the_floating_point = (*a).number_of_digite_maximum_after_the_floating_point;

    result->length_of_num = (*a).length_of_num;

    result->signe = (*a).signe;

    int64_t i = 0;

    result->num = malloc(sizeof(int64_t) * (*a).length_of_num);

    while (i < (*a).length_of_num)
    {

        (result->num)[i] = ((*a).num)[i];

        i += 1;

    }


}






void int_copy_(struct number *result, struct number *a)
{



    result->number_of_digite_maximum_after_the_floating_point = (*a).number_of_digite_maximum_after_the_floating_point;

    result->length_of_num = (*a).length_of_num;

    result->signe = (*a).signe;

    int64_t i = 0;

    // result->num = malloc(sizeof(int64_t) * (*a).length_of_num);

    while (i < (*a).length_of_num)
    {

        (result->num)[i] = ((*a).num)[i];

        i += 1;

    }


}





enum add_ele_amount_account_errors 
{

    non_add_ele_amount_account_error,

    repetition_add_ele_amount_account_error

};



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
    
    // if ((p != NULL) && (char_equal(p->unity.name_of_unity, unity_.name_of_unity) == true))
    // {

    //     // printf("there is a repetition . at %s .\n", unity_.name_of_unity);

    //     printf("there is a repetition . at  i = %ld ", i);

    //     setlocale(LC_ALL, "");

    //     size_t size_ = wcstombs(NULL, unity_.name_of_unity, 0) + 1;
        
    //     char *utf8_text = malloc(size_);

    //     wcstombs(utf8_text, unity_.name_of_unity, size_);

    //     printf(" : {%s} .\n", utf8_text);

    //     p = p->suiv;



    //     return repetition_add_ele_amount_account_error;

    // }
    // else
    // {


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

        // return non_add_ele_amount_account_error;

    // }

}









struct list_of_Accounts_of_Amount* add_ele_list_of_Accounts_of_Amount_1(struct list_of_Accounts_of_Amount **t, struct Unity_of_Number unity_, struct number *amount_, int64_t index)
{

    struct list_of_Accounts_of_Amount *p = *t;

    struct list_of_Accounts_of_Amount *q = p;

    int64_t i = 0;

    while ((p != NULL) && (i < index))
    {

        q = p;

        p = p->suiv;

        i += 1;

    }

    if ((i == index))
    {
    

        if ((index == 0) || (q == NULL))
        {

            
            q = (struct list_of_Accounts_of_Amount *) malloc(sizeof(struct list_of_Accounts_of_Amount));

            
            q->unity.name_of_unity = (wchar_t *)malloc(wcslen(unity_.name_of_unity) * sizeof(wchar_t) + 2);
            
            wcscpy(q->unity.name_of_unity, unity_.name_of_unity);
            

            q->amount.length_of_num = 0;

            int_copy(&(q->amount), amount_);

            
            q->suiv = *t;
            
            *t = q;
            
            
            return *t;


        }
        else
        {


            struct list_of_Accounts_of_Amount *k;

            k = (struct list_of_Accounts_of_Amount *) malloc(sizeof(struct list_of_Accounts_of_Amount));


            k->unity.name_of_unity = (wchar_t *)malloc(wcslen(unity_.name_of_unity) * sizeof(wchar_t) + 2);

            wcscpy(k->unity.name_of_unity, unity_.name_of_unity);


            k->amount.length_of_num = 0;

            int_copy(&(k->amount), amount_);


            k->suiv = q->suiv;

            q->suiv = k;


            return k;

            
        }


    }


}



void freeing_in_list_of_Accounts_of_Amount(struct list_of_Accounts_of_Amount **q)
{


    // while (0 < (*q)->amount.length_of_num)
    // {

    //     remove_ele_int(&((*q)->amount), 0);

    // }

    if ((*q)->amount.length_of_num > 0)
    {

        free((*q)->amount.num);

    }

    if (((*q)->unity.name_of_unity != NULL) && (wcslen((*q)->unity.name_of_unity) != 0))
    {

        free((*q)->unity.name_of_unity);

    }



}


void remove_ele_list_of_Accounts_of_Amount(struct list_of_Accounts_of_Amount **t, int64_t index)
{

    struct list_of_Accounts_of_Amount *p = *t;

    struct list_of_Accounts_of_Amount *q = p;

    struct list_of_Accounts_of_Amount *g = q;


    int64_t i = 0;

    while ((p != NULL) && (i <= index))
    {

        g = q;
    
        q = p;

        p = p->suiv;

        i += 1;

        
    }

    if ((g != NULL) && (i > index))
    {

        if (index == 0)
        {


            if (*t != NULL)
            {

                *t = (*t)->suiv;

                freeing_in_list_of_Accounts_of_Amount(&q);

                free(q);

            }

        }
        else
        {

            g->suiv = p;

            freeing_in_list_of_Accounts_of_Amount(&q);

            free(q);

        }


    }

}





int64_t len_list_of_Accounts_of_Amount(struct list_of_Accounts_of_Amount *t)
{

    int64_t i = 0;

    struct list_of_Accounts_of_Amount *p = t;

    while (p != NULL)
    {

        i += 1;

        p = p->suiv;

    }

    return i;

}




struct list_of_Accounts_of_Amount* list_of_Accounts_of_Amount_copy(struct list_of_Accounts_of_Amount *a)
{

    struct list_of_Accounts_of_Amount *p = a, *t = NULL;

    while (p != NULL)
    {

        add_ele_list_of_Accounts_of_Amount(&t, p->unity, &p->amount, len_list_of_Accounts_of_Amount(t));

        p = p->suiv;

    }


    return t;

}







void add_ele_list_of_personal_accounts(struct list_of_personal_accounts **t, struct number *n, char *name_, char *pre_name_, char *phone_number_, char *e_mail_, char *pass_word_, int64_t index)
{

    struct list_of_personal_accounts *p = *t;

    struct list_of_personal_accounts *q = p;

    int64_t i = 0;

    while ((p != NULL) && (i < index))
    {

        q = p;

        p = p->suiv;

        i += 1;

    }

    if (i == index)
    {

        if ((index == 0) || (q == NULL))
        {

            q = (struct list_of_personal_accounts *) malloc(sizeof(struct list_of_personal_accounts));

            q->identificator.length_of_num = 0;

            int_copy(&(q->identificator), n);

            q->name = (char *)malloc(strlen(name_) + 1);

            strcpy(q->name, name_);

            q->pre_name = (char *)malloc(strlen(pre_name_) + 1);

            strcpy(q->pre_name, pre_name_);

            q->phone_number = (char *)malloc(strlen(phone_number_) + 1);

            strcpy(q->phone_number, phone_number_);

            q->e_mail = (char *)malloc(strlen(e_mail_) + 1);

            strcpy(q->e_mail, e_mail_);

            q->pass_word = (char *)malloc(strlen(pass_word_) + 1);

            strcpy(q->pass_word, pass_word_);

            q->green_pocket.head_of_amount_accounts = NULL;

            q->red_pocket.head_of_amount_accounts = NULL;



            q->suiv = *t;

            *t = q;





        }
        else
        {

            struct list_of_personal_accounts *k;

            k = (struct list_of_personal_accounts *) malloc(sizeof(struct list_of_personal_accounts));


            k->identificator.length_of_num = 0;

            int_copy(&(k->identificator), n);

            k->name = (char *)malloc(strlen(name_) + 1);

            strcpy(k->name, name_);

            k->pre_name = (char *)malloc(strlen(pre_name_) + 1);

            strcpy(k->pre_name, pre_name_);

            k->phone_number = (char *)malloc(strlen(phone_number_) + 1);

            strcpy(k->phone_number, phone_number_);

            k->e_mail = (char *)malloc(strlen(e_mail_) + 1);

            strcpy(k->e_mail, e_mail_);

            k->pass_word = (char *)malloc(strlen(pass_word_) + 1);

            strcpy(k->pass_word, pass_word_);

            k->green_pocket.head_of_amount_accounts = NULL;

            k->red_pocket.head_of_amount_accounts = NULL;


            k->suiv = q->suiv;


            q->suiv = k;


        }

    }


}


void freeing_in_list_of_peronal_accounts(struct list_of_personal_accounts **p)
{

    
    
    while (0 < len_list_of_Accounts_of_Amount((*p)->green_pocket.head_of_amount_accounts))
    {


        remove_ele_list_of_Accounts_of_Amount(&((*p)->green_pocket.head_of_amount_accounts), 0);

    }


    while (0 < len_list_of_Accounts_of_Amount((*p)->red_pocket.head_of_amount_accounts))
    {


        remove_ele_list_of_Accounts_of_Amount(&((*p)->red_pocket.head_of_amount_accounts), 0);

    }
        


}



void remove_ele_list_of_personal_accounts(struct list_of_personal_accounts **t, int64_t index)
{

    struct list_of_personal_accounts *p = *t;

    struct list_of_personal_accounts *q = p;

    struct list_of_personal_accounts *g = q;


    int64_t i = 0;

    while ((p != NULL) && (i <= index))
    {

        g = q;
    
        q = p;

        p = p->suiv;

        i += 1;

        
    }

    if ((g != NULL) && (i > index))
    {

        if (index == 0)
        {



            if (*t != NULL)
            {

                *t = (*t)->suiv;

                free(q->name);

                free(q->pre_name);

                free(q->phone_number);

                free(q->e_mail);

                free(q->pass_word);

                freeing_in_list_of_peronal_accounts(&q);

                free(q);

            }

        }
        else
        {

            g->suiv = p;

            free(q->name);

            free(q->pre_name);

            free(q->phone_number);

            free(q->e_mail);

            free(q->pass_word);

            freeing_in_list_of_peronal_accounts(&q);

            free(q);

        }


    }

}




int64_t len_list_of_personal_accounts(struct list_of_personal_accounts *t)
{

    int64_t i = 0;

    struct list_of_personal_accounts *p = t;

    while (p != NULL)
    {

        i += 1;

        p = p->suiv;

    }

    return i;

}




struct list_of_personal_accounts* list_of_personal_accounts_copy(struct list_of_personal_accounts *a)
{

    struct list_of_personal_accounts *p = a, *t = NULL;

    while (p != NULL)
    {


        add_ele_list_of_personal_accounts(&t, &(p->identificator), p->name, p->pre_name, p->phone_number, p->e_mail, p->pass_word, len_list_of_personal_accounts(t));

        p = p->suiv;

    }


    return t;

}









// prints






void print_number(char *s, struct number *t)
{

    int64_t *p = (*t).num, i = 0;

    printf("%snumber : (num, number_of_digite_maximum_after_the_floating_point, length_of_num) = ((", s);

    while (i < (*t).length_of_num)
    {

        printf("%ld, ", p[i]);

        i += 1;

    }

    printf("), (%ld), (%ld), {%d}) .\n", (*t).number_of_digite_maximum_after_the_floating_point, (*t).length_of_num, (*t).signe);


}











void str_number(char **result, struct number *n)
{

    // from number to str


    if ((*n).length_of_num > 0)
    {


    

        if (*result != NULL)
        {
        
            free(*result);

        }


        int64_t i_0 = 0, i_1 = 0;

        while ((i_0 < (*n).length_of_num) && ((*n).num[i_0] == 0))
        {

            i_0 += 1;

        }

        i_1 = (*n).length_of_num - 1;

        if (i_0 > i_1)
        {

            i_0 -= 1;


        }


        
        
        
        //printf("\n\n\n i_hello_1 .\n\n\n");
        

        // i_0 = (*n).length_of_num;

        int64_t len = i_Number_of_digits_max * ((*n).length_of_num), i = 0, j = 0;



        //printf("\n\n\n i_hello_2 . len = %ld .\n\n\n", len);

        char *s = malloc(i_Number_of_digits_max + 2);
        
        
        //printf("\n\n\n i_hello_2_1 .\n\n\n");
        
        char *all_s = malloc(len + 2);
        
        
        //printf("\n\n\n i_hello_2_2 .\n\n\n");
        
        char *s_1 = malloc(i_Number_of_digits_max + 2);
        
        
        //printf("\n\n\n i_hello_2_3 .\n\n\n");
        
        char *i_int_str = NULL;



        //printf("\n\n\n i_hello_3 .\n\n\n");

        while (j < (*n).length_of_num)
        {
        


            
            //printf("\n\n\n i_hello_4 .\n\n\n");

            i_int_str = int_ND_to_str(my_abs_(((*n).num)[j]));

            strcpy(s_1, i_int_str);

            strcpy(all_s + i, s_1);
            
            if (i_int_str != NULL)
            {

                free(i_int_str);

                i_int_str = NULL;

            }



             //printf("all_s = %s . s_1 = %s . (*n).number_of_digite_maximum_after_the_floating_point = %ld . len = %ld .\n", all_s, s_1, (*n).number_of_digite_maximum_after_the_floating_point, len);

            
            
            i += i_Number_of_digits_max;
            
            j += 1;


            
        }
        
        
        // print_string(&t_s);


        // printf("all_s = %s . (*n).number_of_digite_maximum_after_the_floating_point = %ld . len = %ld .\n", all_s, (*n).number_of_digite_maximum_after_the_floating_point, len);


        if (((*n).number_of_digite_maximum_after_the_floating_point >= len))
        {

            // printf("hello .\n");

            // printf("2 .all_s = %s . n.number_of_digite_maximum_after_the_floating_point = %ld . len = %ld . _ = %ld .\n", all_s, n.number_of_digite_maximum_after_the_floating_point, len, n.number_of_digite_maximum_after_the_floating_point - len);


            char *res = malloc((*n).number_of_digite_maximum_after_the_floating_point + 5);

            uint64_t n_m = (*n).number_of_digite_maximum_after_the_floating_point;
            
            i = 0;

            
            
            if (((*n).signe) < 0)
            {
                
                strcpy(res, "-0.");
                
                i += 3;
                
            }
            else
            {
                
                strcpy(res, "0.");
                
                i += 2;
                
            }
            
            
            while (0 < n_m)
            {
                
                if (n_m > len)
                {
                    
                    res[i] = '0';
                    
                }
                else
                {
                    
                    res[i] = all_s[len - n_m];
                    
                }
                
                n_m -= 1;
                
                i += 1;
                
            }
            
            res[i] = '\0';
            
            // printf("1 . res = %s .\n", res);
            
            (*result) = malloc(strlen(res) + 1);
            
            

            strcpy(*result, res);


            if (((*n).number_of_digite_maximum_after_the_floating_point + 5 > 0))
            {
    
                free(res);
    
            }
        
    
        }
        else
        {

            char *res = malloc(len + 5);

            uint64_t n_m = len, k;

            i = 0;
            
            if (((*n).signe) < 0)
            {

                res[i] = '-';
                
                i += 1;


            }


            
            k = 0;
            
            while (all_s[k] == '0')
            {
                
                k += 1;
                
            }

            if (k == strlen(all_s))
            {

                k -= 1;

            }
            
            
            
            if (k < (len - (*n).number_of_digite_maximum_after_the_floating_point))
            {
                
                n_m -= k;
                
            }
            else
            {
                n_m -= (len - (*n).number_of_digite_maximum_after_the_floating_point) - 1;
                
            }
            
            
            
            while (k < (*n).length_of_num * i_Number_of_digits_max)//0 < n_m)
            {
                
                
                if (n_m == (*n).number_of_digite_maximum_after_the_floating_point)
                {
                    
                    res[i] = '.';
                    
                    i += 1;
                    
                    // res[i] = all_s[len - n_m];
                    
                    
                    res[i] = all_s[k];

                }
                else
                {
                    
                    // res[i] = all_s[len - n_m];

                    res[i] = all_s[k];

                    
                }
                
                // printf("n_m = %ld . res[%ld] = %c .\n", n_m, i, res[i]);
                
                n_m -= 1;

                k += 1;
                
                i += 1;
                
            }
            
            res[i] = '\0';

            
            // printf("2 . res = %s .\n", res);

            (*result) = malloc(strlen(res) + 1);

            strcpy(*result, res);
            
    
            if ((len + 5 > 0))
            {
    
                free(res);
    
            }
        
    

        }



        if ((i_Number_of_digits_max + 2 > 0))
        {

            free(s);

        }


        if ((len + 2 > 0))
        {

            free(all_s);

        }
    
    
        if ((i_Number_of_digits_max + 2 > 0))
        {

            free(s_1);

        }
    

    }
    else
    {

        char *res = "NULL";

        (*result) = malloc(strlen(res) + 1);

        strcpy(*result, res);
        

    }




}









void str_number_1(char *result, struct number *n)
{

    // from number to str


    if ((*n).length_of_num > 0)
    {


    

        int64_t i_0 = 0, i_1 = 0;

        while ((i_0 < (*n).length_of_num) && ((*n).num[i_0] == 0))
        {

            i_0 += 1;

        }

        i_1 = (*n).length_of_num - 1;

        if (i_0 > i_1)
        {

            i_0 -= 1;


        }

        // i_0 = (*n).length_of_num;

        int64_t len = i_Number_of_digits_max * ((*n).length_of_num), i = 0, j = 0;

        char *s = malloc(i_Number_of_digits_max + 2), *all_s = malloc(len + 2), *s_1 = malloc(i_Number_of_digits_max + 2), *i_int_str = NULL;

        while (j < (*n).length_of_num)
        {
        


            i_int_str = int_ND_to_str(my_abs_(((*n).num)[j]));

            strcpy(s_1, i_int_str);

            strcpy(all_s + i, s_1);

            if (i_int_str != NULL)
            {

                free(i_int_str);

                i_int_str = NULL;

            }

            // printf("all_s = %s . (*n).number_of_digite_maximum_after_the_floating_point = %ld . len = %ld .\n", all_s, (*n).number_of_digite_maximum_after_the_floating_point, len);

            
            
            i += i_Number_of_digits_max;
            
            j += 1;


            
        }
        
        
        // print_string(&t_s);


        // printf("all_s = %s . (*n).number_of_digite_maximum_after_the_floating_point = %ld . len = %ld .\n", all_s, (*n).number_of_digite_maximum_after_the_floating_point, len);


        if (((*n).number_of_digite_maximum_after_the_floating_point >= len))
        {

            // printf("hello .\n");

            // printf("2 .all_s = %s . n.number_of_digite_maximum_after_the_floating_point = %ld . len = %ld . _ = %ld .\n", all_s, n.number_of_digite_maximum_after_the_floating_point, len, n.number_of_digite_maximum_after_the_floating_point - len);


            char *res = malloc((*n).number_of_digite_maximum_after_the_floating_point + 5);

            uint64_t n_m = (*n).number_of_digite_maximum_after_the_floating_point;
            
            i = 0;

            
            
            if (((*n).signe) < 0)
            {
                
                strcpy(res, "-0.");
                
                i += 3;
                
            }
            else
            {
                
                strcpy(res, "0.");
                
                i += 2;
                
            }
            
            
            while (0 < n_m)
            {
                
                if (n_m > len)
                {
                    
                    res[i] = '0';
                    
                }
                else
                {
                    
                    res[i] = all_s[len - n_m];
                    
                }
                
                n_m -= 1;
                
                i += 1;
                
            }
            
            res[i] = '\0';
            
            // printf("1 . res = %s .\n", res);
            
            //(*result) = malloc(strlen(res) + 1);
            
            

            strcpy(result, res);


            if (((*n).number_of_digite_maximum_after_the_floating_point + 5 > 0))
            {
    
                free(res);
    
            }
        
    
        }
        else
        {

            char *res = malloc(len + 5);

            uint64_t n_m = len, k;

            i = 0;
            
            if (((*n).signe) < 0)
            {

                res[i] = '-';
                
                i += 1;


            }


            
            k = 0;
            
            while (all_s[k] == '0')
            {
                
                k += 1;
                
            }

            if (k == strlen(all_s))
            {

                k -= 1;

            }
            
            
            
            if (k < (len - (*n).number_of_digite_maximum_after_the_floating_point))
            {
                
                n_m -= k;
                
            }
            else
            {
                n_m -= (len - (*n).number_of_digite_maximum_after_the_floating_point) - 1;
                
            }
            
            
            
            while (k < (*n).length_of_num * i_Number_of_digits_max)//0 < n_m)
            {
                
                
                if (n_m == (*n).number_of_digite_maximum_after_the_floating_point)
                {
                    
                    res[i] = '.';
                    
                    i += 1;
                    
                    // res[i] = all_s[len - n_m];
                    
                    
                    res[i] = all_s[k];

                }
                else
                {
                    
                    // res[i] = all_s[len - n_m];

                    res[i] = all_s[k];

                    
                }
                
                // printf("n_m = %ld . res[%ld] = %c .\n", n_m, i, res[i]);
                
                n_m -= 1;

                k += 1;
                
                i += 1;
                
            }
            
            res[i] = '\0';

            
            // printf("2 . res = %s .\n", res);

            //(*result) = malloc(strlen(res) + 1);

            strcpy(result, res);
            
    
            if ((len + 5 > 0))
            {
    
                free(res);
    
            }
        
    

        }



        if ((i_Number_of_digits_max + 2 > 0))
        {

            free(s);

        }


        if ((len + 2 > 0))
        {

            free(all_s);

        }
    
    
        if ((i_Number_of_digits_max + 2 > 0))
        {

            free(s_1);

        }
    

    }
    else
    {

        char *res = "NULL";

        //(*result) = malloc(strlen(res) + 1);

        strcpy(result, res);
        

    }




}








void number_str(int64_t number_of_digite_maximum_after_the_floating_point, struct number *n, char *s)
{


    // transforme str to number



    // vider le numero n


    if (n->length_of_num > 0)
    {

        free(n->num);

    }

    n->length_of_num = 0;


    n->number_of_digite_maximum_after_the_floating_point = number_of_digite_maximum_after_the_floating_point;






    int64_t sing = 1;

    int64_t i = 0, j;

    if (s[i] == '-')
    {

        sing = -1;

        i += 1;

    }

    size_t length = strlen(s);

    while ((i < length) && (s[i] != '.'))
    {

        i += 1;

    }

    bool b = false;

    if (i == length)
    {

        b = true;

    }



    int64_t n_m = 0;

    while ((n_m < number_of_digite_maximum_after_the_floating_point) && (i < length))
    {

        n_m += 1;

        i += 1;

    }

    if (i == length)
    {

        i -= 1;

        if (b == false)
        {

            n_m -= 1;

        }


    }


    int64_t o = 0, q = 1;
    
    if (n_m < number_of_digite_maximum_after_the_floating_point)
    {

        o = (number_of_digite_maximum_after_the_floating_point - n_m) / i_Number_of_digits_max;

        j = 0;

        while (j < o)
        {

            add_ele_int(n, 0, 0);

            // (*n).num[0] = 0;

            j += 1;

        }

        o = number_of_digite_maximum_after_the_floating_point - (n_m + (o * i_Number_of_digits_max));

    }

    
    j = 0;

    while (j < o)
    {

        q *= 10;

        j += 1;

    }


    int64_t g = 0;


    if (i == length)
    {

        i -= 1;

    }

    // printf("o = %ld . n_m = %ld .\n", o, n_m);

    
    while (0 <= i)
    {


        
        j = 0;
        

        while ((j < (i_Number_of_digits_max - o)) && (0 <= i))
        {

            if ((s[i] != '.') && (s[i] != '-'))
            {
            
                // printf("i = %ld . s[i] = %c\n", i, s[i]);

                g += c_to_int(s[i]) * q;
                
                q *= 10;
                
                j += 1;

            }

            i -= 1;
            

        }

        // printf("g = %ld . i = %ld .\n", g, i);

        add_ele_int(n, g, 0);

        


        // if (t != NULL)
        // {

        //     printf("t->ele = %ld .\n", t->ele);

        // }


        g = 0;

        q = 1;

        o = 0;

    }
    

    while ((1 < n->length_of_num) && ((n->num)[0] == 0))
    {

        remove_ele_int(n, 0);

    }

    if (n->length_of_num > 0)
    {

        (n->num)[0] *= sing;

    }


}









void number_str_1(int64_t number_of_digite_maximum_after_the_floating_point, struct number *n, char *s)
{


    // transforme str to number



    // vider le numero n



    n->number_of_digite_maximum_after_the_floating_point = number_of_digite_maximum_after_the_floating_point;






    int64_t sing = 1;

    int64_t i = 0, j;

    if (s[i] == '-')
    {

        sing = -1;

        i += 1;

    }

    size_t length = strlen(s);

    while ((i < length) && (s[i] != '.'))
    {

        i += 1;

    }

    bool b = false;

    if (i == length)
    {

        b = true;

    }



    int64_t n_m = 0;

    while ((n_m < number_of_digite_maximum_after_the_floating_point) && (i < length))
    {

        n_m += 1;

        i += 1;

    }

    if (i == length)
    {

        i -= 1;

        if (b == false)
        {

            n_m -= 1;

        }


    }


    int64_t o = 0, q = 1;
    
    if (n_m < number_of_digite_maximum_after_the_floating_point)
    {

        o = (number_of_digite_maximum_after_the_floating_point - n_m) / i_Number_of_digits_max;

        j = 0;

        while (j < o)
        {

            add_ele_int(n, 0, 0);

            // (*n).num[0] = 0;

            j += 1;

        }

        o = number_of_digite_maximum_after_the_floating_point - (n_m + (o * i_Number_of_digits_max));

    }

    
    j = 0;

    while (j < o)
    {

        q *= 10;

        j += 1;

    }


    int64_t g = 0;


    if (i == length)
    {

        i -= 1;

    }

    // printf("o = %ld . n_m = %ld .\n", o, n_m);

    
    while (0 <= i)
    {


        
        j = 0;
        

        while ((j < (i_Number_of_digits_max - o)) && (0 <= i))
        {

            if ((s[i] != '.') && (s[i] != '-'))
            {
            
                // printf("i = %ld . s[i] = %c\n", i, s[i]);

                g += c_to_int(s[i]) * q;
                
                q *= 10;
                
                j += 1;

            }

            i -= 1;
            

        }

        // printf("g = %ld . i = %ld .\n", g, i);

        add_ele_int(n, g, 0);

        


        // if (t != NULL)
        // {

        //     printf("t->ele = %ld .\n", t->ele);

        // }


        g = 0;

        q = 1;

        o = 0;

    }
    

    while ((1 < n->length_of_num) && ((n->num)[0] == 0))
    {

        remove_ele_int(n, 0);

    }

    if (n->length_of_num > 0)
    {

        (n->num)[0] *= sing;

    }


}











// prints










void print_list_of_Accounts_of_Amount(struct list_of_Accounts_of_Amount *t)
{

    struct list_of_Accounts_of_Amount *p = t;

    int64_t i = 0;

    char *s = NULL;

    while (p != NULL)
    {


        str_number(&s, &(p->amount));

        printf("list[%ld] = {(amount:%s), (name_of_unity:", i, s);


        size_t size_that_should_be = wcstombs(NULL, p->unity.name_of_unity, 0) + 1;
        
        char *utf8_text = malloc(size_that_should_be);

        wcstombs(utf8_text, p->unity.name_of_unity, size_that_should_be);

        printf("%s)} .\n", utf8_text);



        i += 1;

        p = p->suiv;

    }

}









void print_fast_list_of_Accounts_of_Amount(struct list_of_Accounts_of_Amount *t)
{

    struct list_of_Accounts_of_Amount *p = t;

    int64_t i = 0;

    // char *s = NULL;

    printf("i = ");

    while (p != NULL)
    {


        // str_number(&s, &(p->amount));


        if ((p->amount.num[124] == 0))
        {

            printf("0");

        }
        else if (p->amount.num[124] == 1)
        {

            printf("1");

        }

        // printf("%s", s);

        i += 1;

        p = p->suiv;

    }

    printf(" . length = %ld .\n", i);


}







char* produce_string_fast_list_of_Accounts_of_Amount(struct list_of_Accounts_of_Amount *t)
{

    struct list_of_Accounts_of_Amount *p = t;

    int64_t i = 0, i_len_1 = 0, i_len_2 = 0;

    char *s = NULL, *i_string_0 = NULL, *i_string_1 = NULL, *i_string_2 = NULL;

    i_string_2 = malloc(2);

    strcpy(i_string_2, "");
    
    
    while (p != NULL)
    {
        
        
        str_number(&s, &(p->amount));

        // s = malloc(2);

        // strcpy(s, "0");


        i_len_1 = strlen(s) + 1;



        i_string_0 = malloc(i_len_1);
        
        strcpy(i_string_0, s);


        if (s != NULL)
        {

            free(s);

            s = NULL;


        }


        if (i_len_1 > 1)
        {

            i_len_2 = strlen(i_string_2) + 1;

            if (i_string_1 != NULL)
            {

                free(i_string_1);

                i_string_1 = NULL;

            }

            i_string_1 = malloc(i_len_1 + i_len_2 - 1);

            strcpy(i_string_1, i_string_2);

            strcat(i_string_1, i_string_0);




            if (i_string_2 != NULL)
            {

                free(i_string_2);

                i_string_2 = NULL;


            }



            if (i_string_0 != NULL)
            {

                free(i_string_0);

                i_string_0 = NULL;


            }

            i_len_1 = strlen(i_string_1) + 1;

            i_string_2 = malloc(i_len_1);

            strcpy(i_string_2, i_string_1);

                    



        }

    
        i += 1;

        p = p->suiv;

    }


    



    if (s != NULL)
    {

        free(s);

        s = NULL;


    }



    if (i_string_0 != NULL)
    {

        free(i_string_0);

        i_string_0 = NULL;


    }




    if (i_string_1 != NULL)
    {

        free(i_string_1);

        i_string_1 = NULL;


    }


    

    return i_string_2;

}






void produce_string_fast_list_of_Accounts_of_Amount_1(struct list_of_Accounts_of_Amount *t, char **i_string_3)
{

    struct list_of_Accounts_of_Amount *p = t;

    int64_t i = 0, i_len_1 = 0, i_len_2 = 0;

    char *i_string_0 = NULL, *i_string_1 = NULL, *i_string_2 = NULL;

    // i_string_2 = malloc(len_list_of_Accounts_of_Amount(t) + 1);

    // strcpy(i_string_2, "");

    // i_string_0 = malloc(2);

    strcpy(*i_string_3, "");

    
    while (p != NULL)
    {
        

        if (((p->amount).num)[i_macro_of_Number_max_of_word_byte - 1] == 0)
        {

            strcat(*i_string_3, "0");

        }
        else if (((p->amount).num)[i_macro_of_Number_max_of_word_byte - 1] == 1)
        {

            strcat(*i_string_3, "1");

        }




        
      
        
        // i_len_2 = i + 1;

        // i_len_1 = i_len_2 + 1;

        // i_string_1 = malloc(i_len_1);

        // strcpy(i_string_1, i_string_2);

        // strcat(i_string_1, i_string_0);





        // free(i_string_2);

        // i_string_2 = NULL;





        // i_string_2 = malloc(i_len_1);

        // strcat(i_string_2, i_string_0);

                


            
        // free(i_string_1);
        
        // i_string_1 = NULL;
        
    
        i += 1;

        p = p->suiv;

    }




    // free(i_string_0);

    // i_string_0 = NULL;



    // if (i_string_1 != NULL)
    // {

    //     free(i_string_1);

    //     i_string_1 = NULL;


    // }


    

    // return i_string_2;

}




void print_list_of_Accounts_of_Amount_index(struct list_of_Accounts_of_Amount *t, int64_t index)
{

    struct list_of_Accounts_of_Amount *p = t;

    int64_t i = 0;

    char *s = NULL;

    while ((p != NULL) && (i != index))
    {

        i += 1;

        p = p->suiv;

    }


    if ((p != NULL) && (i == index))
    {

        str_number(&s, &(p->amount));

        printf("list[%ld] = {(amount:%s), (name_of_unity:", i, s);


        size_t size_that_should_be = wcstombs(NULL, p->unity.name_of_unity, 0) + 1;
        
        char *utf8_text = malloc(size_that_should_be);

        wcstombs(utf8_text, p->unity.name_of_unity, size_that_should_be);

        printf("%s)} .\n", utf8_text);


    }

}











void print_list_of_personal_accounts(struct list_of_personal_accounts *t)
{

    struct list_of_personal_accounts *p = t;

    int64_t i = 0;

    char *s = NULL;

    while (p != NULL)
    {
    

        str_number(&s, &(p->identificator));

        printf("list[%ld] = {(id:%s), (name:%s), (pre_name:%s), (phone_number:%s), (e_mail:%s), (pass_word:%s)} .\n", i, s, p->name, p->pre_name, p->phone_number, p->e_mail, p->pass_word);

        i += 1;

        p = p->suiv;

    }

}










bool int_equal(struct number *a, struct number *b)
{
    
    
    if ((*a).length_of_num == (*b).length_of_num)
    {
        
        
        int64_t i = 0;
        
        while ((i < (*a).length_of_num) && (((*a).num)[i] == ((*b).num)[i]))
        {
            
            i += 1;
            
        }

        
        if ((i == (*a).length_of_num) && ((*a).signe == ((*b).signe)) && ((*a).number_of_digite_maximum_after_the_floating_point == ((*b).number_of_digite_maximum_after_the_floating_point)))
        {
            
            return true;
            
            
        }
        else
        {

            return false;
            
        }
        
    }
    else
    {

        return false;

    }

}


bool ints_superieur_equal(struct number *a, struct number *b)
{



    if ((*a).length_of_num == 0)
    {

        if ((*b).length_of_num > 0)
        {

            return false;

        }
        else
        {

            return true;

        }


    }
    else if ((*b).length_of_num == 0)
    {

        return true;

    }
    else
    {
        
        bool m = ((((((*a).signe)) < 0) && (((*b).signe)) > 0) || (((((*a).signe)) > 0) && (((*b).signe)) < 0));

        if (m)
        {

            if (((*a).signe) < 0)
            {

                return false;

            }
            else
            {

                return true;

            }

        }
        else
        {


            if ((((*a).signe) < 0) && ((*a).length_of_num > (*b).length_of_num))
            {

                return false;

            }
            else if ((((*a).signe) < 0) && ((*a).length_of_num < (*b).length_of_num))
            {

                return true;

            }
            else if ((((*a).signe) > 0) && ((*a).length_of_num < (*b).length_of_num))
            {

                return false;

            }
            else if ((((*a).signe) > 0) && ((*a).length_of_num > (*b).length_of_num))
            {

                return true;

            }
            else if (((*a).length_of_num == (*b).length_of_num) && ((*a).number_of_digite_maximum_after_the_floating_point == (*b).number_of_digite_maximum_after_the_floating_point))
            {

                int64_t i = 0;

                while ((i < (*a).length_of_num) && (((*a).num)[i] == ((*b).num)[i]))
                {

                    i += 1;

                }

                if ((i == (*a).length_of_num))
                {

                    return true;

                }
                else if (((*a).num)[i] >= ((*b).num)[i])
                {

                    return true;

                }
                else
                {

                    return false;

                }

            }

        }

    }

}






bool ints_superieur_equal_1(struct number *a, struct number *b)
{



    if ((*a).length_of_num == 0)
    {

        if ((*b).length_of_num > 0)
        {

            return false;

        }
        else
        {

            return true;

        }


    }
    else if ((*b).length_of_num == 0)
    {

        return true;

    }
    else
    {
        
        bool m = ((((((*a).signe)) < 0) && (((*b).signe)) > 0) || (((((*a).signe)) > 0) && (((*b).signe)) < 0));

        if (m)
        {

            if (((*a).signe) < 0)
            {

                return false;

            }
            else
            {

                return true;

            }

        }
        else
        {


        


            int64_t i = (*a).length_of_num - 1 , choice = 0;


            if (i > (*b).length_of_num - 1)
            {
            
                i = (*b).length_of_num - 1;
                
                choice = 1;
            
            }
            



            while ((i >= 0) && (((*a).num)[i] == ((*b).num)[i]))
            {

                i -= 1;

            }


            
            if (i >= 0)
            {
            
                if (((*a).num)[i] > ((*b).num)[i])
                {
                
                    if (((*a).signe) < 0)
                    {
                        
                        return false;
                    
                    }
                    else
                    {
                        
                        return true;
                
                    
                    }
                    
                    
                }
                else
                {
                
                                        
                    if (((*a).signe) < 0)
                    {
                        
                        return true;
                    
                    }
                    else
                    {
                        
                        return false;
                    
                    
                    }
                    
                    
                
                }
            
            }
            else
            {
            
                if ((*a).length_of_num > (*b).length_of_num)
                {
                
                    int64_t counter_0 = (*a).length_of_num - (*b).length_of_num - 1;
                
                    while ((i + counter_0 >= 0) && ((*a).num[i + counter_0] == 0))
                    {
                    
                        counter_0 -= 1;
                    
                    }
                    
                    if (i + counter_0 >= 0)
                    {
                    
                    
                    
                    
                                                
                                            
                        if (((*a).signe) < 0)
                        {
                            
                            return false;
                        
                        }
                        else
                        {
                            
                            return true;
                        
                        
                        }
                        
                        
                    }
                    else
                    {
                        
                        
                                                  
                                            
                        if (((*a).signe) < 0)
                        {
                            
                            return true;
                        
                        }
                        else
                        {
                            
                            return false;
                        
                        
                        }
                        
                    }
                
                }
                else
                {
                
                                        
                    int64_t counter_0 = (*b).length_of_num - (*a).length_of_num - 1;
                    
                    while ((i + counter_0 >= 0) && ((*b).num[i + counter_0] == 0))
                    {
                    
                        counter_0 -= 1;
                    
                    }
                    
                    if (i + counter_0 >= 0)
                    {
                    
                    
                                                   
                        if (((*a).signe) < 0)
                        {
                            
                            return true;
                        
                        }
                        else
                        {
                            
                            return false;
                        
                        
                        }
                        
                    
                    }
                    else
                    {
                    
                                                
                                                   
                        if (((*a).signe) < 0)
                        {
                            
                            return false;
                        
                        }
                        else
                        {
                            
                            return true;
                        
                        
                        }
                        
                        
                        
                    }
                    
                    
                
                }
            
            }


        }

    }

}










struct operation_int add_int(int64_t a, int64_t b)
{



    struct operation_int n;

    int64_t i, q = 1;

    uint64_t h = a + b, k, d;

    i = 0;

    while (i < i_Number_of_digits_max)
    {

        q *= 10;

        i += 1;

    }

    

    k = h / q;

    // d = h - (k * q);

    d = h % q;



    n.ele = d;

    n.reminder = k;


    return n;

}






void add_number_positive(int64_t number_of_digite_maximum_after_the_floating_point, struct number *result, struct number *a, struct number *b)
{

    // adding 2 positive numbers with number_of_digite_maximum_after_the_floating_point
    
    //  --->  res = a + b




    int64_t i, j;



    // if (result->length_of_num > 0)
    // {

    //     free(result->num);

    // }


    result->number_of_digite_maximum_after_the_floating_point = number_of_digite_maximum_after_the_floating_point;

    result->length_of_num = i_macro_of_Number_max_of_word_byte;

    result->signe = 1;


    struct operation_int n;




    int64_t g = 0, a0, b0;
    
    i = (*a).length_of_num - 1;

    j = (*b).length_of_num - 1;


    while ((0 <= i) || (0 <= j))
    {



        if (i < 0)
        {

            a0 = 0;

        }
        else
        {

            a0 = ((*a).num)[i];

            i -= 1;


        }

        if (j < 0)
        {

            b0 = 0;

        }
        else
        {

            b0 = ((*b).num)[j];

            j -= 1;

        }


        n = add_int(a0, b0);

        // add_ele_int(result, n.ele + g, 0);

        (result->num)[i + 1] = n.ele + g;

        // printf("n.ele = %ld . g = %ld . (result->num)[i + 1] = %ld .\n", n.ele, g, (result->num)[i + 1]);

        g = n.reminder;




    }


    if (g != 0)
    {

        (result->num)[i + 1] = g;

        // add_ele_int(result, g, 0);


    }


    // print_number("result = ", result);

    

}











struct operation_int sub_int(int64_t a, int64_t b)
{



    struct operation_int n;

    int64_t i, q = 0, d = 0;

    if (a < b)
    {


        i = 0;

        q = 1;

        while (i < i_Number_of_digits_max)
        {

            q *= 10;

            i += 1;

        }

        d = 1;

    }    


    n.ele = (a + q) - b;

    n.reminder = d;


    return n;

}




void sub_int_number(struct number *result, struct number *a, struct number *b)
{


    int64_t i, j;


    // if (result->length_of_num > 0)
    // {

    //     free(result->num);

    // }


    result->length_of_num = i_macro_of_Number_max_of_word_byte;




    struct operation_int n;

    int64_t q = 1;

    i = 0;

    while (i < i_Number_of_digits_max)
    {

        q *= 10;

        i += 1;

    }


    int64_t g = 0, a0, b0;

    i = (*a).length_of_num - 1;

    j = (*b).length_of_num - 1;



    while ((0 <= i) || (0 <= j))
    {
        
        a0 = ((*a).num)[i];
            

        if (j < 0)
        {

            b0 = 0;

        }
        else
        {

            b0 = ((*b).num)[j];
            
            j -= 1;

        }

        if (i == 0)
        {

            n.ele = ((*a).num)[i] - (b0 + g);

        }
        else
        {

            n = sub_int(a0, b0 + g);

        }



        // add_ele_int(result, n.ele, 0);


        if (n.ele < 0)
        {

            result->signe = -1;

        }

        (result->num)[i] = n.ele;

        g = n.reminder;

        i -= 1;

    }




}






void sub_number(int64_t number_of_digite_maximum_after_the_floating_point, struct number *result, struct number *a, struct number *b)
{

    // substraction 2 numbers with number_of_digite_maximum_after_the_floating_point
    
    //  --->  res = a + b


    result->number_of_digite_maximum_after_the_floating_point = number_of_digite_maximum_after_the_floating_point;


    bool m = ints_superieur_equal(a, b);
    
    if (m)
    {

        sub_int_number(result, a, b);
   
        result->signe = 1;

    }
    else
    {


        sub_int_number(result, b, a);

        result->signe = -1;

    }



    // while ((1 < result->length_of_num) && (((result->num)[0] == 0)))
    // {

    //     remove_ele_int(result, 0);

    // // }

    // if (m == false)
    // {



    // }
    // else
    // {



    // }



}




void add_number(int64_t number_of_digite_maximum_after_the_floating_point, struct number *result, struct number *a, struct number *b)
{

    // adding 2 numbers with number_of_digite_maximum_after_the_floating_point
    
    //  --->  res = a + b





    if ((0 < (*a).length_of_num) && (0 < (*b).length_of_num))
    {

        
        bool m = ((((((*a).signe)) < 0) && ((((*b).signe)) > 0)) || (((((*a).signe)) > 0) && ((((*b).signe)) < 0)));


        
        
        if (m)
        {





            // struct number n;

            // n.length_of_num = 0;


            if (((*b).signe) < 0)
            {

                
                // int_copy_(&n, b);

                // (n.num)[0] *= -1;

                ((*b).signe) = 1;
          
                sub_number(number_of_digite_maximum_after_the_floating_point, result, a, b);

                ((*b).signe) = -1;



            }
            else
            {

                
                // int_copy_(&n, a);

                // (n.num)[0] *= -1;

                ((*a).signe) = 1;


                sub_number(number_of_digite_maximum_after_the_floating_point, result, b, a);

                ((*a).signe) = -1;



            }



            // if (n.length_of_num > 0)
            // {

            //     free(n.num);

            // }





        }
        else
        {

        
        
        
        
            if (((((*a).signe)) < 0) || ((((*b).signe)) < 0))
            {

                // struct number n, n_;

                // n.length_of_num = 0;

                // n_.length_of_num = 0;




                // int_copy_(&n, a);

                // (n.num)[0] *= -1;


                // int_copy_(&n_, b);

                // (n_.num)[0] *= -1;


                ((*a).signe) = 1;

                ((*b).signe) = 1;
                

                add_number_positive(number_of_digite_maximum_after_the_floating_point, result, a, b);



                ((*a).signe) = -1;

                ((*b).signe) = -1;
                

                // while ((1 < result->length_of_num) && ((result->num)[0] == 0))
                // {

                //     remove_ele_int(result, 0);

                // }

                (result->signe) = -1;


                // if (n.length_of_num > 0)
                // {

                //     free(n.num);

                // }



                // if (n_.length_of_num > 0)
                // {

                //     free(n_.num);

                // }


            }
            else
            {



                add_number_positive(number_of_digite_maximum_after_the_floating_point, result, a, b);


                // print_number("result = ", result);
                

                // while ((1 < result->length_of_num) && ((result->num)[0] == 0))
                // {

                //     remove_ele_int(result, 0);

                // }




            }

        }

    }

}





void print_virtual_amount(struct list_of_personal_accounts **tete, struct number *identificator_, struct Unity_of_Number unity_, struct number *amount_)
{



    struct list_of_personal_accounts *q = *tete;


    while ((q != NULL) && (int_equal(&(q->identificator), identificator_) == false))
    {

        q = q->suiv;

    }


    if (q != NULL)
    {
        


        struct number result;

        result.length_of_num = 0;

        int64_t i = 0;

        struct list_of_Accounts_of_Amount *p = (q)->red_pocket.head_of_amount_accounts;

        while ((p != NULL) && (char_equal((p->unity.name_of_unity), (unity_.name_of_unity)) == false))
        {
            

            p = p->suiv;


        }


        if (p != NULL)
        {


            
            add_number(i_macro_of_number_of_digite_maximum_after_the_floating_point, &result, &(p->amount), amount_);

            
            int_copy_(&(p->amount), &result);

            
        }

    }

}







void print_virtual_amount_with_copy_1(struct list_of_Accounts_of_Amount **p_head, struct Unity_of_Number unity_, struct number *amount_)
{



    
    struct list_of_Accounts_of_Amount *p = *p_head;


    if (p != NULL)
    {

        int_copy(&(p->amount), amount_);
        
    }


}








void printing_personal_account_on_file_for_the_show_1(struct list_of_personal_accounts *tete, struct number identificator_, char *output_file, int64_t counter, struct number n6)
{


/*

identificator : "str_number"

    name : "name"

    pre_name : "pre_name"

    phone_number : "phone_number"

    e_mail : "e_mail"

    date : "2025-2-10 16:30:18 : 000000000"

    counter : "1"

    green_pocket : 

        name_of_unity : "name_of_unity"

            amount : "amount"

    red_pocket : 

        name_of_unity : "name_of_unity"

            amount : "amount"





*/



    setlocale(LC_ALL, "");


    



    char cw[PATH_MAX];

    bool semaphore = false;

    if (getcwd(cw, sizeof(cw)) != NULL)
    {

        semaphore = true;

    }


    int64_t i = 0, q = strlen(cw) - 1;

    while (cw[q] != '/')
    {

        q -= 1;

    }

    char *DB_cw = malloc(q + 2);

    while (i < q)
    {

        DB_cw[i] = cw[i];

        i += 1;

    }

    DB_cw[i] = '\0';



    char *file_path = malloc(255 + PATH_MAX);


    // sprintf(thing, "%ld", i);

    strcpy(file_path, DB_cw);

    strcat(file_path, "/Data_Base/");

    strcat(file_path, output_file); 

    //"printing_personal_account.info"

    FILE *file = fopen(file_path, "w");

 

    double t1, t2;

    t1 = time_();
   

    t1 = time_();

    semaphore = false;

    if (file == NULL)
    {

        semaphore = true;

        // printf("Error opening the file .\n");

    }
    else
    {





        


        struct list_of_personal_accounts *q = tete;

        int64_t i_size = 0;
        
        while ((q != NULL) && (int_equal(&(q->identificator), &identificator_) == false))
        {
            
            q = q->suiv;
            
        }
        
        
        if (q != NULL)
        {
            
            
            
            int64_t n = 0;
            
            n += strlen(q->name);

            n += strlen(q->pre_name);

            n += strlen(q->phone_number);

            n += strlen(q->e_mail);

            char *s = NULL, *tab = "    ";

            struct list_of_Accounts_of_Amount *p = (q)->red_pocket.head_of_amount_accounts;

            while (p != NULL)
            {
                
                n += wcslen(p->unity.name_of_unity);

                //str_number(&s, p->amount);

                // n += len_big_number;

                n += (((p->amount).length_of_num) * 18);

                p = p->suiv;

            }


            p = q->green_pocket.head_of_amount_accounts;

            while (p != NULL)
            {
                
                n += wcslen(p->unity.name_of_unity);

                //str_number(&s, p->amount);

                //n += len_big_number;

                n += (((p->amount).length_of_num) * 18);

                p = p->suiv;

            }



            n += 100;

            char *result = malloc(n * 2 + 320 + 2), *p_inc;

            
            p_inc = stpcpy(result, "\nidentificator : \"");

            
            str_number(&s, &(q->identificator));
            
            p_inc = stpcpy(p_inc, s);
            
            
            p_inc = stpcpy(p_inc, "\"\n\n");
            
            p_inc = stpcpy(p_inc, tab);
            
            p_inc = stpcpy(p_inc, "name : \"");
            
            p_inc = stpcpy(p_inc, q->name);
            
            p_inc = stpcpy(p_inc, "\"\n\n");
            
            p_inc = stpcpy(p_inc, tab);
            
            p_inc = stpcpy(p_inc, "pre_name : \"");
            
            p_inc = stpcpy(p_inc, q->pre_name);
            
            p_inc = stpcpy(p_inc, "\"\n\n");
            
            p_inc = stpcpy(p_inc, tab);
            
            p_inc = stpcpy(p_inc, "phone_number : \"");
            
            p_inc = stpcpy(p_inc, q->phone_number);
            
            p_inc = stpcpy(p_inc, "\"\n\n");
            
            p_inc = stpcpy(p_inc, tab);
            
            p_inc = stpcpy(p_inc, "e_mail : \"");
            
            p_inc = stpcpy(p_inc, q->e_mail);
            
            p_inc = stpcpy(p_inc, "\"\n\n");
            
            p_inc = stpcpy(p_inc, tab);
            

            struct timespec tv;

            struct tm* current_time;
        
            // الحصول على الوقت بدقة microseconds
        
            clock_gettime(CLOCK_REALTIME, &tv);
        


            // t = time(NULL);
            
            // current_time = localtime(&t);

            current_time = localtime(&tv.tv_sec);


            // طباعة التاريخ والوقت بالشكل المطلوب
            

            char *thing = malloc(1000), *things = malloc(1000);

            // sprintf(something, "date : %02d-%02d-%d %02d:%02d:%02d\n",
            //     current_time->tm_mday,        // اليوم
            //     current_time->tm_mon + 1,    // الشهر (نضيف 1 لأن الأشهر تبدأ من 0)
            //     current_time->tm_year + 1900,// السنة
            //     current_time->tm_hour,       // الساعات
            //     current_time->tm_min,        // الدقائق
            //     current_time->tm_sec);       // الثواني

            sprintf(thing, "%d", current_time->tm_year + 1900);
            
            strcpy(things, thing);

            sprintf(thing, "-%02d-", current_time->tm_mon + 1);

            strcat(things, thing);

            sprintf(thing, "%02d", current_time->tm_mday);

            strcat(things, thing);

            sprintf(thing, " %02d:", current_time->tm_hour);

            strcat(things, thing);

            sprintf(thing, "%02d:", current_time->tm_min);
            
            strcat(things, thing);

            sprintf(thing, "%02d", current_time->tm_sec);
            
            strcat(things, thing);

            // tv.tv_usec


            sprintf(thing, ": %ld", tv.tv_nsec);
            
            strcat(things, thing);

            p_inc = stpcpy(p_inc, "date : \"");

            p_inc = stpcpy(p_inc, things);

            p_inc = stpcpy(p_inc, "\"\n\n");
            
            p_inc = stpcpy(p_inc, tab);

            
            sprintf(thing, "%ld", counter);

            p_inc = stpcpy(p_inc, "counter : \"");
            
            p_inc = stpcpy(p_inc, thing);

            p_inc = stpcpy(p_inc, "\"\n\n");

            p_inc = stpcpy(p_inc, tab);


            p_inc = stpcpy(p_inc, "pass_word : \"");

            p_inc = stpcpy(p_inc, q->pass_word);

            p_inc = stpcpy(p_inc, "\"\n\n");
            
            p_inc = stpcpy(p_inc, tab);
            
            p_inc = stpcpy(p_inc, "green_pocket : \n\n");
            
            str_number(&s, &n6);


            int64_t i_2 = 0, i_3 = 0;

            p = (q)->green_pocket.head_of_amount_accounts;
            
            while (p != NULL)
            {
            

                
                if (i_3 > 0)
                {

                    result = malloc((n6.length_of_num * 18) + 1000);

                    p_inc = stpcpy(result, tab);


                }
                else
                {

                    p_inc = stpcpy(p_inc, tab);

                }


                p_inc = stpcpy(p_inc, tab);
                
                p_inc = stpcpy(p_inc, "name_of_unity : \"");

                p_inc = stpcpy(p_inc, str_from_UTF_8(p->unity.name_of_unity));

                p_inc = stpcpy(p_inc, "\"\n\n");
                
                p_inc = stpcpy(p_inc, tab);

                p_inc = stpcpy(p_inc, tab);
                
                p_inc = stpcpy(p_inc, tab);

                p_inc = stpcpy(p_inc, "amount : \"");
                

                
                p_inc = stpcpy(p_inc, s);
                
                p_inc = stpcpy(p_inc, "\"\n\n");
                
                
                fprintf(file, "%s", result);
                
                i_size = i_size + strlen(result);
                
                
                printf("strlen(result) = %ld . i_2 = %ld . name_of_unity = %s . i_size = %ld .\n", strlen(result), i_2, str_from_UTF_8(p->unity.name_of_unity), i_size);


                free(result);
        
                // free(s);

                // s = NULL;

                i_2 += 1;

                i_3 = i_3 + 1;
                
                
                p = p->suiv;
                
            }
            
            


            p_inc = stpcpy(p_inc, "\n\n");
            
            p_inc = stpcpy(p_inc, tab);
        
            p_inc = stpcpy(p_inc, "red_pocket : \n\n");


            i_3 = 0;

            p = (q)->red_pocket.head_of_amount_accounts;
            
            while (p != NULL)
            {

            
                
                
                if (i_3 > 0)
                {
                    
                    result = malloc((n6.length_of_num * 18) + 1000);

                    p_inc = stpcpy(result, tab);


                }
                else
                {

                    p_inc = stpcpy(p_inc, tab);

                }


        
                
                p_inc = stpcpy(p_inc, tab);

                p_inc = stpcpy(p_inc, "name_of_unity : \"");

                p_inc = stpcpy(p_inc, str_from_UTF_8(p->unity.name_of_unity));

                p_inc = stpcpy(p_inc, "\"\n\n");
                
                p_inc = stpcpy(p_inc, tab);

                p_inc = stpcpy(p_inc, tab);
                
                p_inc = stpcpy(p_inc, tab);

                p_inc = stpcpy(p_inc, "amount : \"");
                
                // str_number(&s, p->amount);

                p_inc = stpcpy(p_inc, s);

                p_inc = stpcpy(p_inc, "\"\n\n");

                
                
                
                fprintf(file, "%s", result);
                
                i_size = i_size + strlen(result);
                
                printf("strlen(result) = %ld . i_2 = %ld . name_of_unity = %s . i_size = %ld .\n", strlen(result), i_2, str_from_UTF_8(p->unity.name_of_unity), i_size);

                
                free(result);


                // free(s);

                // s = NULL;


                i_2 += 1;

                i_3 = i_3 + 1;


                p = p->suiv;

            }




        }


        t2 = time_();


        printf("\n\n\n\n\ntime of fprintf = %.10f .\n\n\n\n\n\n", t2 - t1);


        fclose(file);

    }
    

}








// void printing_personal_account_on_file_for_the_show(struct list_of_personal_accounts *tete, struct number identificator_, char *output_file)
// {


// /*

// identificator : "str_number"

//     name : "name"

//     pre_name : "pre_name"

//     phone_number : "phone_number"

//     e_mail : "e_mail"

//     green_pocket : 

//         name_of_unity : "name_of_unity"

//             amount : "amount"

//     red_pocket : 

//         name_of_unity : "name_of_unity"

//             amount : "amount"

// */



//     struct list_of_personal_accounts *q = tete;


//     while ((q != NULL) && (int_equal(q->identificator, identificator_) == false))
//     {

//         q = q->suiv;

//     }

//     if (q != NULL)
//     {

//         int64_t n = 0;

//         n += strlen(q->name);

//         n += strlen(q->pre_name);

//         n += strlen(q->phone_number);

//         n += strlen(q->e_mail);

//         char *s = NULL, *tab = "    ";

//         struct list_of_Accounts_of_Amount *p = (q)->red_pocket.head_of_amount_accounts;

//         while (p != NULL)
//         {
            
//             n += strlen(p->unity.name_of_unity);

//             str_number(&s, p->amount);

//             n += strlen(s);

//             p = p->suiv;

//         }


//         p = q->green_pocket.head_of_amount_accounts;

//         while (p != NULL)
//         {
            
//             n += strlen(p->unity.name_of_unity);

//             str_number(&s, p->amount);

//             n += strlen(s);

//             p = p->suiv;

//         }



//         char *result = malloc(n * 2 + 320 + 2);

        
//         strcpy(result, "\nidentificator : \"");

//         str_number(&s, q->identificator);

//         strcat(result, s);

//         strcat(result, "\"\n\n");

//         strcat(result, tab);

//         strcat(result, "name : \"");

//         strcat(result, q->name);

//         strcat(result, "\"\n\n");

//         strcat(result, tab);

//         strcat(result, "pre_name : \"");

//         strcat(result, q->pre_name);

//         strcat(result, "\"\n\n");

//         strcat(result, tab);

//         strcat(result, "phone_number : \"");

//         strcat(result, q->phone_number);

//         strcat(result, "\"\n\n");

//         strcat(result, tab);

//         strcat(result, "e_mail : \"");

//         strcat(result, q->e_mail);

//         strcat(result, "\"\n\n");

//         strcat(result, tab);

//         strcat(result, "pass_word : \"");

//         strcat(result, q->pass_word);

//         strcat(result, "\"\n\n");

//         strcat(result, tab);


//         strcat(result, "green_pocket : \n\n");



//         p = (q)->green_pocket.head_of_amount_accounts;
        
//         while (p != NULL)
//         {
        
            
//             strcat(result, tab);

//             strcat(result, tab);

//             strcat(result, "name_of_unity : \"");

//             strcat(result, p->unity.name_of_unity);

//             strcat(result, "\"\n\n");
            
//             strcat(result, tab);

//             strcat(result, tab);
            
//             strcat(result, tab);

//             strcat(result, "amount : \"");
            
//             str_number(&s, p->amount);

//             strcat(result, s);

//             strcat(result, "\"\n\n");


//             p = p->suiv;

//         }




//         strcat(result, "\n\n");
        
//         strcat(result, tab);
    
//         strcat(result, "red_pocket : \n\n");



//         p = (q)->red_pocket.head_of_amount_accounts;
        
//         while (p != NULL)
//         {
        
    
            
//             strcat(result, tab);

//             strcat(result, tab);

//             strcat(result, "name_of_unity : \"");

//             strcat(result, p->unity.name_of_unity);

//             strcat(result, "\"\n\n");
            
//             strcat(result, tab);

//             strcat(result, tab);
            
//             strcat(result, tab);

//             strcat(result, "amount : \"");
            
//             str_number(&s, p->amount);

//             strcat(result, s);

//             strcat(result, "\"\n\n");

//             p = p->suiv;

//         }

//         char cw[PATH_MAX];

//         bool semaphore = false;

//         if (getcwd(cw, sizeof(cw)) != NULL)
//         {

//             semaphore = true;

//         }


//         int64_t i = 0, q = strlen(cw) - 1;

//         while (cw[q] != '/')
//         {

//             q -= 1;

//         }

//         char *DB_cw = malloc(q + 2);

//         while (i < q)
//         {

//             DB_cw[i] = cw[i];

//             i += 1;

//         }

//         DB_cw[i] = '\0';



//         char *file_path = malloc(255 + PATH_MAX);


//         strcpy(file_path, DB_cw);

//         strcat(file_path, "/Data_Base/");

//         strcat(file_path, output_file); 

//         //"printing_personal_account.info"

//         FILE *file = fopen(file_path, "w");


//         semaphore = false;

//         if (file == NULL)
//         {

//             semaphore = true;

//             // printf("Error opening the file .\n");

//         }
//         else
//         {


//             fprintf(file, "%s", result);

//             fclose(file);


//             // printf("the file is printed succefuly .");

//         }







//     }


    

// }




// void printing_personal_account_on_file_for_the_DataBase(struct list_of_personal_accounts *tete, struct number identificator_, char *output_file)
// {



//     struct list_of_personal_accounts *q = tete;


//     while ((q != NULL) && (int_equal(q->identificator, identificator_) == false))
//     {

//         q = q->suiv;

//     }

//     if (q != NULL)
//     {

//         int64_t n = 0;

//         n += strlen(q->name);

//         n += strlen(q->pre_name);

//         n += strlen(q->phone_number);

//         n += strlen(q->e_mail);

//         char *s = NULL, *tab = "    ";

//         struct list_of_Accounts_of_Amount *p = (q)->red_pocket.head_of_amount_accounts;

//         while (p != NULL)
//         {
            
//             n += strlen(p->unity.name_of_unity);

//             str_number(&s, p->amount);

//             n += strlen(s);

//             p = p->suiv;

//         }


//         p = q->green_pocket.head_of_amount_accounts;

//         while (p != NULL)
//         {
            
//             n += strlen(p->unity.name_of_unity);

//             str_number(&s, p->amount);

//             n += strlen(s);

//             p = p->suiv;

//         }



//         char *result = malloc(n * 2 + 320 + 2);

//         str_number(&s, q->identificator);

//         strcat(result, s);

//         strcat(result, "\n");

//         strcat(result, q->name);

//         strcat(result, "\n");

//         strcat(result, q->pre_name);

//         strcat(result, "\n");

//         strcat(result, q->phone_number);

//         strcat(result, "\n");

//         strcat(result, q->e_mail);

//         strcat(result, "\n");

//         strcat(result, q->pass_word);

//         strcat(result, "\n");

//         sprintf(s, "%ld", len_list_of_Accounts_of_Amount((q)->green_pocket.head_of_amount_accounts));

//         strcat(result, s);

//         strcat(result, "\n");


//         p = (q)->green_pocket.head_of_amount_accounts;
        
//         while (p != NULL)
//         {
        
            
//             strcat(result, p->unity.name_of_unity);

//             strcat(result, "\n");
            
//             str_number(&s, p->amount);

//             strcat(result, s);

//             strcat(result, "\n");


//             p = p->suiv;

//         }



//         sprintf(s, "%ld", len_list_of_Accounts_of_Amount((q)->red_pocket.head_of_amount_accounts));

//         strcat(result, s);

//         strcat(result, "\n");


//         p = (q)->red_pocket.head_of_amount_accounts;
        
//         while (p != NULL)
//         {
        
            
//             strcat(result, p->unity.name_of_unity);

//             strcat(result, "\n");
            
//             str_number(&s, p->amount);

//             strcat(result, s);

//             strcat(result, "\n");


//             p = p->suiv;

//         }

//         char cw[PATH_MAX];

//         bool semaphore = false;

//         if (getcwd(cw, sizeof(cw)) != NULL)
//         {

//             semaphore = true;

//         }

//         int64_t i = 0, q = strlen(cw) - 1;

//         while (cw[q] != '/')
//         {

//             q -= 1;

//         }

//         char *DB_cw = malloc(q + 2);

//         while (i < q)
//         {

//             DB_cw[i] = cw[i];

//             i += 1;

//         }

//         DB_cw[i] = '\0';



//         char *file_path = malloc(255 + PATH_MAX);


//         strcpy(file_path, DB_cw);

//         strcat(file_path, "/Data_Base/");

//         strcat(file_path, output_file); 

//         //"printing_personal_account.info"

//         FILE *file = fopen(file_path, "w");


//         semaphore = false;

//         if (file == NULL)
//         {

//             semaphore = true;

//             // printf("Error opening the file .\n");

//         }
//         else
//         {


//             fprintf(file, "%s", result);

//             // printf("the file is printed succefuly .");
            
//             fclose(file);

//         }





//     }


// }




// void extract_personal_account_from_DataBaseFile(struct list_of_personal_accounts **tete, char *file_path)
// {


//     FILE *file = fopen(file_path, "r");

//     bool semaphore = false;

//     if (file == NULL)
//     {

//         semaphore = true;

//     }
//     else
//     {




//         fseek(file, 0, SEEK_END);

//         long file_size = ftell(file);

//         rewind(file);

//         char *content = (char *)malloc(file_size + 1);

//         semaphore = false;

//         if (content == NULL)
//         {

//             semaphore = true;

//         }
//         else
//         {

//             size_t read_size = fread(content, 1, file_size, file);

//             content[file_size] = '\0';

//             fclose(file);



//             struct number n;

//             int64_t i = 0, j, y;

//             while ((i < strlen(content)) && (content[i] != '\n'))
//             {

//                 i += 1;

//             }
            
//             char *s = (char *)malloc(i);

//             j = 0;

//             while (j < i)
//             {

//                 s[j] = content[j];
                
//                 j += 1;

//             }

//             s[j] = '\0';


//             n.length_of_num = 0;

//             number_str(i_macro_of_number_of_digite_maximum_after_the_floating_point, &n, s);


//             free(s);



//             struct list_of_personal_accounts *q = *tete;



//             while ((q != NULL) && (int_equal(q->identificator, n) == false))
//             {

//                 q = q->suiv;

//             }
            

//             if (q != NULL)
//             {
                


//                 i += 1;

//                 y = i;
                

//                 while ((i < strlen(content)) && (content[i] != '\n'))
//                 {

//                     i += 1;

//                 }



//                 s = (char *)malloc(i - y);

//                 j = 0;

//                 while (j < i - y)
//                 {

//                     s[j] = content[j + y];
                    
//                     j += 1;

//                 }

//                 s[j] = '\0';


//                 strcpy(q->name, s);

//                 free(s);



//                 i += 1;


//                 y = i;
                

//                 while ((i < strlen(content)) && (content[i] != '\n'))
//                 {

//                     i += 1;

//                 }



//                 s = (char *)malloc(i - y);

//                 j = 0;

//                 while (j < i - y)
//                 {

//                     s[j] = content[j + y];
                    
//                     j += 1;

//                 }

//                 s[j] = '\0';


//                 strcpy(q->pre_name, s);

//                 free(s);


//                 i += 1;

//                 y = i;
                

//                 while ((i < strlen(content)) && (content[i] != '\n'))
//                 {

//                     i += 1;

//                 }



//                 s = (char *)malloc(i - y);

//                 j = 0;

//                 while (j < i - y)
//                 {

//                     s[j] = content[j + y];
                    
//                     j += 1;

//                 }

//                 s[j] = '\0';


//                 strcpy(q->phone_number, s);

//                 free(s);


//                 i += 1;

//                 y = i;
                

//                 while ((i < strlen(content)) && (content[i] != '\n'))
//                 {

//                     i += 1;

//                 }



//                 s = (char *)malloc(i - y);

//                 j = 0;

//                 while (j < i - y)
//                 {

//                     s[j] = content[j + y];
                    
//                     j += 1;

//                 }

//                 s[j] = '\0';


//                 strcpy(q->e_mail, s);

//                 free(s);


//                 i += 1;

//                 y = i;
                

//                 while ((i < strlen(content)) && (content[i] != '\n'))
//                 {

//                     i += 1;

//                 }



//                 s = (char *)malloc(i - y);

//                 j = 0;

//                 while (j < i - y)
//                 {

//                     s[j] = content[j + y];
                    
//                     j += 1;

//                 }

//                 s[j] = '\0';


//                 strcpy(q->pass_word, s);

//                 free(s);



//                 i += 1;

//                 y = i;
                

//                 while ((i < strlen(content)) && (content[i] != '\n'))
//                 {

//                     i += 1;

//                 }



//                 s = (char *)malloc(i - y);

//                 j = 0;

//                 while (j < i - y)
//                 {

//                     s[j] = content[j + y];
                    
//                     j += 1;

//                 }

//                 s[j] = '\0';





//                 // green_pocket

                
//                 while (q->green_pocket.head_of_amount_accounts != NULL)
//                 {

//                     remove_ele_list_of_Accounts_of_Amount(&(q->green_pocket.head_of_amount_accounts), 0);

//                 }


//                 int64_t len_, i_;

//                 sscanf(s, "%ld", &len_);

//                 free(s);

//                 char *s_;

//                 struct Unity_of_Number u;

//                 i_ = 0;

//                 while (i_ < len_)
//                 {




//                     i += 1;

//                     y = i;
                    

//                     while ((i < strlen(content)) && (content[i] != '\n'))
//                     {

//                         i += 1;

//                     }



//                     s = (char *)malloc(i - y);

//                     j = 0;

//                     while (j < i - y)
//                     {

//                         s[j] = content[j + y];
                        
//                         j += 1;

//                     }

//                     s[j] = '\0';


//                     u.name_of_unity = s;





//                     i += 1;

//                     y = i;
                    

//                     while ((i < strlen(content)) && (content[i] != '\n'))
//                     {

//                         i += 1;

//                     }



//                     s_ = (char *)malloc(i - y);

//                     j = 0;

//                     while (j < i - y)
//                     {

//                         s_[j] = content[j + y];
                        
//                         j += 1;

//                     }

//                     s_[j] = '\0';

//                     number_str(i_macro_of_number_of_digite_maximum_after_the_floating_point, &n, s);


//                     add_ele_list_of_Accounts_of_Amount(&(q->green_pocket.head_of_amount_accounts), u, n, len_list_of_Accounts_of_Amount(q->green_pocket.head_of_amount_accounts));


//                     free(s_);

//                     free(s);

//                     i_ += 1;

//                 }





//                 i += 1;

//                 y = i;
                

//                 while ((i < strlen(content)) && (content[i] != '\n'))
//                 {

//                     i += 1;

//                 }



//                 s = (char *)malloc(i - y);

//                 j = 0;

//                 while (j < i - y)
//                 {

//                     s[j] = content[j + y];
                    
//                     j += 1;

//                 }

//                 s[j] = '\0';


//                 // red_pocket

                
//                 while (q->red_pocket.head_of_amount_accounts != NULL)
//                 {

//                     remove_ele_list_of_Accounts_of_Amount(&(q->red_pocket.head_of_amount_accounts), 0);

//                 }


//                 sscanf(s, "%ld", &len_);

//                 free(s);


//                 i_ = 0;

//                 while (i_ < len_)
//                 {




//                     i += 1;

//                     y = i;
                    

//                     while ((i < strlen(content)) && (content[i] != '\n'))
//                     {

//                         i += 1;

//                     }



//                     s = (char *)malloc(i - y);

//                     j = 0;

//                     while (j < i - y)
//                     {

//                         s[j] = content[j + y];
                        
//                         j += 1;

//                     }

//                     s[j] = '\0';


//                     u.name_of_unity = s;





//                     i += 1;

//                     y = i;
                    

//                     while ((i < strlen(content)) && (content[i] != '\n'))
//                     {

//                         i += 1;

//                     }



//                     s_ = (char *)malloc(i - y);

//                     j = 0;

//                     while (j < i - y)
//                     {

//                         s_[j] = content[j + y];
                        
//                         j += 1;

//                     }

//                     s_[j] = '\0';

//                     number_str(i_macro_of_number_of_digite_maximum_after_the_floating_point, &n, s);


//                     add_ele_list_of_Accounts_of_Amount(&(q->red_pocket.head_of_amount_accounts), u, n, len_list_of_Accounts_of_Amount(q->red_pocket.head_of_amount_accounts));


//                     free(s_);

//                     free(s);

//                     i_ += 1;

//                 }



//             }
//             else
//             {





//                 i += 1;

//                 y = i;
                

//                 while ((i < strlen(content)) && (content[i] != '\n'))
//                 {

//                     i += 1;

//                 }



//                 char *s_name = (char *)malloc(i - y);

//                 j = 0;

//                 while (j < i - y)
//                 {

//                     s_name[j] = content[j + y];
                    
//                     j += 1;

//                 }

//                 s_name[j] = '\0';




//                 i += 1;

//                 y = i;
                

//                 while ((i < strlen(content)) && (content[i] != '\n'))
//                 {

//                     i += 1;

//                 }



//                 char *s_pre_name = (char *)malloc(i - y);

//                 j = 0;

//                 while (j < i - y)
//                 {

//                     s_pre_name[j] = content[j + y];
                    
//                     j += 1;

//                 }

//                 s_pre_name[j] = '\0';


//                 i += 1;

//                 y = i;
                

//                 while ((i < strlen(content)) && (content[i] != '\n'))
//                 {

//                     i += 1;

//                 }



//                 char *s_phone_number = (char *)malloc(i - y);

//                 j = 0;

//                 while (j < i - y)
//                 {

//                     s_phone_number[j] = content[j + y];
                    
//                     j += 1;

//                 }

//                 s_phone_number[j] = '\0';



//                 i += 1;

//                 y = i;
                

//                 while ((i < strlen(content)) && (content[i] != '\n'))
//                 {

//                     i += 1;

//                 }



//                 char *s_e_mail = (char *)malloc(i - y);

//                 j = 0;

//                 while (j < i - y)
//                 {

//                     s_e_mail[j] = content[j + y];
                    
//                     j += 1;

//                 }

//                 s_e_mail[j] = '\0';



//                 i += 1;

//                 y = i;
                

//                 while ((i < strlen(content)) && (content[i] != '\n'))
//                 {

//                     i += 1;

//                 }



//                 char *s_pass_word = (char *)malloc(i - y);

//                 j = 0;

//                 while (j < i - y)
//                 {

//                     s_pass_word[j] = content[j + y];
                    
//                     j += 1;

//                 }

//                 s_pass_word[j] = '\0';





//                 add_ele_list_of_personal_accounts(tete, n, s_name, s_pre_name, s_phone_number, s_e_mail, s_pass_word, len_list_of_personal_accounts(*tete));

                
//                 struct list_of_personal_accounts *q_ = *tete;

//                 q = q_;

//                 while (q_ != NULL)
//                 {

                    
//                     q = q_;

//                     q_ = q_->suiv;

//                 }
                

//                 i += 1;

//                 y = i;
                

//                 while ((i < strlen(content)) && (content[i] != '\n'))
//                 {

//                     i += 1;

//                 }
                



//                 s = (char *)malloc(i - y);

//                 j = 0;

//                 while (j < i - y)
//                 {

//                     s[j] = content[j + y];
                    
//                     j += 1;

//                 }

//                 s[j] = '\0';



//                 int64_t len_, i_;

//                 sscanf(s, "%ld", &len_);

                
//                 free(s);

//                 char *s_;

//                 struct Unity_of_Number u;

//                 i_ = 0;

//                 while (i_ < len_)
//                 {




//                     i += 1;

//                     y = i;
                    

//                     while ((i < strlen(content)) && (content[i] != '\n'))
//                     {

//                         i += 1;

//                     }



//                     s = (char *)malloc(i - y);

//                     j = 0;

//                     while (j < i - y)
//                     {

//                         s[j] = content[j + y];
                        
//                         j += 1;

//                     }

//                     s[j] = '\0';


//                     i += 1;

//                     y = i;
                    

//                     while ((i < strlen(content)) && (content[i] != '\n'))
//                     {

//                         i += 1;

//                     }



//                     s_ = (char *)malloc(i - y);

//                     j = 0;

//                     while (j < i - y)
//                     {

//                         s_[j] = content[j + y];
                        
//                         j += 1;

//                     }

//                     s_[j] = '\0';

//                     number_str(i_macro_of_number_of_digite_maximum_after_the_floating_point, &n, s_);

                    

//                     u.name_of_unity = s;


//                     add_ele_list_of_Accounts_of_Amount(&(q->green_pocket.head_of_amount_accounts), u, n, len_list_of_Accounts_of_Amount(q->green_pocket.head_of_amount_accounts));





//                     free(s);

//                     free(s_);



//                     i_ += 1;

//                 }




//                 i += 1;

//                 y = i;
                

//                 while ((i < strlen(content)) && (content[i] != '\n'))
//                 {

//                     i += 1;

//                 }



//                 s = (char *)malloc(i - y);

//                 j = 0;

//                 while (j < i - y)
//                 {

//                     s[j] = content[j + y];
                    
//                     j += 1;

//                 }

//                 s[j] = '\0';

             

//                 sscanf(s, "%ld", &len_);



//                 free(s);

                

//                 i_ = 0;

//                 while (i_ < len_)
//                 {




//                     i += 1;

//                     y = i;
                    

//                     while ((i < strlen(content)) && (content[i] != '\n'))
//                     {

//                         i += 1;

//                     }



//                     s = (char *)malloc(i - y);

//                     j = 0;

//                     while (j < i - y)
//                     {

//                         s[j] = content[j + y];
                        
//                         j += 1;

//                     }

//                     s[j] = '\0';


//                     i += 1;

//                     y = i;
                    

//                     while ((i < strlen(content)) && (content[i] != '\n'))
//                     {

//                         i += 1;

//                     }



//                     s_ = (char *)malloc(i - y);

//                     j = 0;

//                     while (j < i - y)
//                     {

//                         s_[j] = content[j + y];
                        
//                         j += 1;

//                     }

//                     s_[j] = '\0';


//                     number_str(i_macro_of_number_of_digite_maximum_after_the_floating_point, &n, s_);


//                     u.name_of_unity = s;



//                     add_ele_list_of_Accounts_of_Amount(&(q->red_pocket.head_of_amount_accounts), u, n, len_list_of_Accounts_of_Amount(q->red_pocket.head_of_amount_accounts));


//                     free(s);

//                     free(s_);



//                     i_ += 1;


//                 }



//             }




//             free(content);

//         }

//     }

// }





void extract_gain(struct number *result, struct number *number_)
{


    // if (0 < result->length_of_num)
    // {

    //     free(result->num);

    // }

    result->number_of_digite_maximum_after_the_floating_point = (*number_).number_of_digite_maximum_after_the_floating_point;

    result->length_of_num = i_macro_of_Number_max_of_word_byte;

    result->signe = 1;


    if (0 < (*number_).length_of_num)
    {
        


        int64_t i_0 = 0;


        while ((i_0 < i_macro_of_Number_max_of_word_byte) && ((*number_).num[i_0] == 0))
        {

            i_0 += 1;

        }


        int64_t q = 1, i = 0;

        while ((i < i_Number_of_digits_max) && (q < (*number_).num[i_0]))
        {

            q *= 10;

            i += 1;

        }

        i -= 4;
        
        int64_t j;

        if (i < 0)
        {

            int64_t i_ = i_Number_of_digits_max + i;
    
            j = 0;

            q = 1;

            while (j < i_)
            {

                q *= 10;

                j += 1;

            }

        }
        else if (i >= 0)
        {

            j = 0;

            q = 1;

            while (j < i)
            {

                q *= 10;

                j += 1;

            }

        }

        int64_t i_ = 0;

        while (i_ < result->length_of_num)
        {

            // add_ele_int(result, 0, 0);

            result->num[i_] = 0;

            i_ += 1;

        }

        if (i >= 0)
        {

            // add_ele_int(result, 0, 0);

            // add_ele_int(result, q, 0);

            result->num[i_0] = q;            


        }
        else if (i_0 + 1 < i_macro_of_Number_max_of_word_byte)
        {

            // add_ele_int(result, q, 0);

            result->num[i_0 + 1] = q;

        }


    }

}



enum Errors_ {

    non_error,

    the_account_of_gain_do_not_exist,

    the_extracted_amount_is_begger_than_the_contity_of_the_amount_in_the_account,

    the_Unity_of_amount_do_not_exist,

    the_account_do_not_exist,

    there_is_no_gain_in_trensfer

};



enum Errors_ transfer(struct list_of_personal_accounts **i_head, struct number *identificator_of_gainer, struct number *identificator_1, struct number *identificator_2, struct Unity_of_Number unity_, struct number *amount_, struct number *gain, struct number *extracted_amount, struct number *n, bool red_)
{


    bool semaphore_of_success = true;

    enum Errors_ error_meesage = non_error;


    /*
    
    comment:

        all of those should be initialize-ed to 0 :

            struct number *gain ,
            
            struct number *extracted_amount , 
            
            struct number *n

    */



    extract_gain(gain, amount_);
    

    int64_t i = 0;


    while ((i < (*gain).length_of_num) && (gain->num[i] == 0))
    {

        i += 1;

    }


    if (i < gain->length_of_num)
    {
        
        add_number(i_macro_of_number_of_digite_maximum_after_the_floating_point, extracted_amount, amount_, gain);


        // print_number("extracted_amount = ", extracted_amount);

        // print_number("gain = ", gain);

        // print_number("amount_ = ", amount_);

        // print_number("identificator_1 = ", identificator_1);

        // print_number("identificator_2 = ", identificator_2);

        // print_number("identificator_of_gainer = ", identificator_of_gainer);


        struct list_of_personal_accounts *q = *i_head;







        // extracting extracted_amount from identificator_1


        if (semaphore_of_success)
        {


            

            q = *i_head;


            while ((q != NULL) && (int_equal(&(q->identificator), identificator_1) == false))
            {

                q = q->suiv;


            }

            if (q != NULL)
            {
                
        
                if (red_)
                {


                    struct list_of_Accounts_of_Amount *p = (q)->red_pocket.head_of_amount_accounts;

                    while ((p != NULL) && (char_equal((p->unity.name_of_unity), (unity_.name_of_unity)) == false))
                    {
                        

                        p = p->suiv;


                    }


                    if (p != NULL)
                    {
                    
                    
                        if (ints_superieur_equal(&(p->amount), extracted_amount))
                        {


                            // printf("\n\n\n\nfrom before .\n\n");

                            // print_number("(p->amount) = ", &(p->amount));


                            int_copy_(n, &(p->amount));

                            (*extracted_amount).signe = -1;
 
                            add_number(i_macro_of_number_of_digite_maximum_after_the_floating_point, &(p->amount), n, extracted_amount);
                         
                            (*extracted_amount).signe = 1;

                            // printf("\n\n\n\nn - extracted_amount .\n\n");

                            // print_number("(p->amount) = ", &(p->amount));


                        }
                        else
                        {
                            

                            semaphore_of_success = false;

                            error_meesage = the_extracted_amount_is_begger_than_the_contity_of_the_amount_in_the_account;

                        }


                    }
                    else
                    {

                        semaphore_of_success = false;

                        error_meesage = the_Unity_of_amount_do_not_exist;

                    }

                }
                else
                {


                    struct list_of_Accounts_of_Amount *p = (q)->green_pocket.head_of_amount_accounts;

                    while ((p != NULL) && (char_equal((p->unity.name_of_unity), (unity_.name_of_unity)) == false))
                    {
                        

                        p = p->suiv;


                    }


                    if (p != NULL)
                    {


                        if (ints_superieur_equal(&(p->amount), extracted_amount))
                        {

                            int_copy_(n, &(p->amount));
                            
                            (*extracted_amount).signe = -1;

                            add_number(i_macro_of_number_of_digite_maximum_after_the_floating_point, &(p->amount), n, extracted_amount);

                            (*extracted_amount).signe = 1;

                        }
                        else
                        {

                            semaphore_of_success = false;

                            error_meesage = the_extracted_amount_is_begger_than_the_contity_of_the_amount_in_the_account;


                        }

                    }
                    else
                    {

                        semaphore_of_success = false;

                        error_meesage = the_Unity_of_amount_do_not_exist;

                    }


                }

            }
            else
            {

                semaphore_of_success = false;

                error_meesage = the_account_do_not_exist;

            }

        }
        



        // giving amount to identificator_2


        if (semaphore_of_success)
        {


            

            q = *i_head;


            while ((q != NULL) && (int_equal(&(q->identificator), identificator_2) == false))
            {

                q = q->suiv;


            }

            if (q != NULL)
            {
        
                if (red_)
                {


                    struct list_of_Accounts_of_Amount *p = (q)->red_pocket.head_of_amount_accounts;

                    while ((p != NULL) && (char_equal((p->unity.name_of_unity), (unity_.name_of_unity)) == false))
                    {
                        

                        p = p->suiv;


                    }


                    if (p != NULL)
                    {


                        // printf("\n\n\n\nfrom before .\n\n");

                        // print_number("(p->amount) = ", &(p->amount));


                        int_copy_(n, &(p->amount));

    
                        add_number(i_macro_of_number_of_digite_maximum_after_the_floating_point, &(p->amount), n, amount_);


                        // printf("\n\n\n\nn + amount_ .\n\n");

                        // print_number("(p->amount) = ", &(p->amount));

                    }
                    else
                    {

                        semaphore_of_success = false;

                        error_meesage = the_Unity_of_amount_do_not_exist;

                    }

                }
                else
                {


                    struct list_of_Accounts_of_Amount *p = (q)->green_pocket.head_of_amount_accounts;

                    while ((p != NULL) && (char_equal((p->unity.name_of_unity), (unity_.name_of_unity)) == false))
                    {
                        

                        p = p->suiv;


                    }


                    if (p != NULL)
                    {
                        
                        int_copy_(n, &(p->amount));


                        add_number(i_macro_of_number_of_digite_maximum_after_the_floating_point, &(p->amount), n, amount_);

                    }
                    else
                    {

                        semaphore_of_success = false;

                        error_meesage = the_Unity_of_amount_do_not_exist;

                    }


                }

            }
            else
            {

                semaphore_of_success = false;

                error_meesage = the_account_do_not_exist;

            }

        }





        // teking my rights


        if (semaphore_of_success)
        {



            q = *i_head;


            while ((q != NULL) && (int_equal(&(q->identificator), identificator_of_gainer) == false))
            {

                q = q->suiv;

            }

            if (q != NULL)
            {
        
                if (red_)
                {


                    struct list_of_Accounts_of_Amount *p = (q)->red_pocket.head_of_amount_accounts;

                    while ((p != NULL) && (char_equal((p->unity.name_of_unity), (unity_.name_of_unity)) == false))
                    {
                        

                        p = p->suiv;


                    }


                    if (p != NULL)
                    {



                        // printf("\n\n\n\nfrom before .\n\n");

                        // print_number("(p->amount) = ", &(p->amount));


                        int_copy_(n, &(p->amount));


                        add_number(i_macro_of_number_of_digite_maximum_after_the_floating_point, &(p->amount), n, gain);


                        // printf("\n\n\n\nn + gain .\n\n");

                        // print_number("(p->amount) = ", &(p->amount));

                    }
                    else
                    {

                        semaphore_of_success = false;

                        error_meesage = the_Unity_of_amount_do_not_exist;


                    }

                }
                else
                {


                    struct list_of_Accounts_of_Amount *p = (q)->green_pocket.head_of_amount_accounts;

                    while ((p != NULL) && (char_equal((p->unity.name_of_unity), (unity_.name_of_unity)) == false))
                    {
                        

                        p = p->suiv;


                    }


                    if (p != NULL)
                    {


                        int_copy_(n, &(p->amount));


                        add_number(i_macro_of_number_of_digite_maximum_after_the_floating_point, &(p->amount), n, gain);

                    }
                    else
                    {

                        semaphore_of_success = false;

                        error_meesage = the_Unity_of_amount_do_not_exist;

                    }



                }

            }
            else
            {

                semaphore_of_success = false;

                error_meesage = the_account_of_gain_do_not_exist;

            }

        }


    }
    else
    {

        semaphore_of_success = false;

        error_meesage = there_is_no_gain_in_trensfer;

    }
    

    return error_meesage;

}




// void making_2(struct list_of_personal_accounts **head, struct number identificator_0, struct number identificator_1, wchar_t *name_of_unity_, char *big_number)
// {




//     struct Unity_of_Number u;

//     u.name_of_unity = malloc(10000);

//     enum add_ele_amount_account_errors errors = non_add_ele_amount_account_error;


//     struct number n3, n4, n5, n6;



//     n6.length_of_num = 0;


//     n5.length_of_num = 0;


//     n4.length_of_num = 0;



//     n3.number_of_digite_maximum_after_the_floating_point = 0;

//     n3.length_of_num = 1;

//     n3.num = malloc(sizeof(int64_t));

//     (n3.num)[0] = 0;




//     number_str(i_macro_of_number_of_digite_maximum_after_the_floating_point, &n5, "1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000");

//     number_str(i_macro_of_number_of_digite_maximum_after_the_floating_point, &n6, big_number);


//     wcscpy(u.name_of_unity, name_of_unity_);

//     errors = add_ele_list_of_Accounts_of_Amount(&((*head)->red_pocket.head_of_amount_accounts), u, &n3, len_list_of_Accounts_of_Amount(((*head)->red_pocket.head_of_amount_accounts)));

//     print_virtual_amount(head, &identificator_0, u, &n6);


//     struct list_of_personal_accounts *p = *head;

//     p = p->suiv;


//     errors = add_ele_list_of_Accounts_of_Amount(&((p)->red_pocket.head_of_amount_accounts), u, &n3, len_list_of_Accounts_of_Amount(((p)->red_pocket.head_of_amount_accounts)));

//     print_virtual_amount(head, &identificator_1, u, &n5);



//     p = p->suiv;


//     errors = add_ele_list_of_Accounts_of_Amount(&((p)->red_pocket.head_of_amount_accounts), u, &n3, len_list_of_Accounts_of_Amount(((p)->red_pocket.head_of_amount_accounts)));






//     p = p->suiv;

//     (identificator_1.num)[0] = 3;

//     errors = add_ele_list_of_Accounts_of_Amount(&((p)->red_pocket.head_of_amount_accounts), u, &n3, len_list_of_Accounts_of_Amount(((p)->red_pocket.head_of_amount_accounts)));

//     print_virtual_amount(head, &identificator_1, u, &n5);



// }










void next_step_in_mix(struct list_of_Accounts_of_Amount **head)
{



    int64_t n = 0, length = len_list_of_Accounts_of_Amount(*head);

    struct list_of_Accounts_of_Amount *p = *head;

    struct number n_1, n_0, length_on_number;

    n_1.length_of_num = 0;

    n_0.length_of_num = 0;

    length_on_number.length_of_num = 0;



    number_str(i_macro_of_number_of_digite_maximum_after_the_floating_point, &n_1, "1");

    number_str(i_macro_of_number_of_digite_maximum_after_the_floating_point, &length_on_number, i_macro_of_length_of_encoding);


    bool run = true, plus_account = false;

    while (run == true)
    {




        if (ints_superieur_equal(&(p->amount), &length_on_number) == true)
        {

        
            number_str(i_macro_of_number_of_digite_maximum_after_the_floating_point, &(p->amount), "0");

            if (p->suiv != NULL)
            {

                p = p->suiv;

            }
            else
            {

                plus_account = true;

                run = false;

            }

        }
        else
        {

            add_number(i_macro_of_number_of_digite_maximum_after_the_floating_point, &n_0, &(p->amount), &n_1);
            
            int_copy_(&(p->amount), &n_0);
            
            run = false;

        }

        n += 1;


        if (n == length)
        {

            run = false;

        }

    }



    if (plus_account == true)
    {

        number_str(i_macro_of_number_of_digite_maximum_after_the_floating_point, &(n_1), "0");

        enum add_ele_amount_account_errors errors = non_add_ele_amount_account_error;

        add_ele_list_of_Accounts_of_Amount(head, p->unity, &n_1, len_list_of_Accounts_of_Amount(*head));
        
    }


}









void initialize_number(struct number *n)
{


    (*n).length_of_num = i_macro_of_Number_max_of_word_byte;

    (*n).number_of_digite_maximum_after_the_floating_point = i_macro_of_number_of_digite_maximum_after_the_floating_point;

    (*n).signe = 1;

    (*n).num = malloc(sizeof(int64_t) * i_macro_of_Number_max_of_word_byte);


    int64_t i = 0;



    while (i < i_macro_of_Number_max_of_word_byte)
    {

        (*n).num[i] = 0;

        i = i + 1;

    }



}











void next_step_in_mix_1(struct list_of_Accounts_of_Amount **head, struct number *n_1, struct number *i_n_2, struct number *length_on_number, struct number *n_0)
{



    int64_t n = 0, length = len_list_of_Accounts_of_Amount(*head);

    struct list_of_Accounts_of_Amount *p = *head;



    bool run = true, plus_account = false;

    while (run == true)
    {




        if (ints_superieur_equal(&(p->amount), length_on_number) == true)
        {

        
            // number_str(i_macro_of_number_of_digite_maximum_after_the_floating_point, &(p->amount), "0");

            int_copy_(&(p->amount), i_n_2);

            if (p->suiv != NULL)
            {

                p = p->suiv;

            }
            else
            {

                plus_account = true;

                run = false;

            }

        }
        else
        {

            add_number(i_macro_of_number_of_digite_maximum_after_the_floating_point, n_0, &(p->amount), n_1);
            
            int_copy_(&(p->amount), n_0);
            
            run = false;

        }

        n += 1;


        if (n == length)
        {

            run = false;

        }

    }



    if (plus_account == true)
    {

        // number_str(i_macro_of_number_of_digite_maximum_after_the_floating_point, &(n_1), "1");

        // enum add_ele_amount_account_errors errors = non_add_ele_amount_account_error;

        add_ele_list_of_Accounts_of_Amount(head, p->unity, i_n_2, len_list_of_Accounts_of_Amount(*head));
        
    }


}











void save_ing_in_file(char *content, char *file_path)
{




    // char i_cwd[PATH_MAX];

    // bool semaphore = false;

    // if (getcwd(i_cwd, sizeof(i_cwd)) != NULL)
    // {

    //     semaphore = true;

    // }


    // int64_t i = 0, q = strlen(cw) - 1;

    // while (cw[q] != '/')
    // {

    //     q -= 1;

    // }

    // char *DB_cw = malloc(q + 2);

    // while (i < q)
    // {

    //     DB_cw[i] = cw[i];

    //     i += 1;

    // }

    // DB_cw[i] = '\0';



    // char *file_path = malloc(255 + PATH_MAX);


    // strcpy(file_path, DB_cw);

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





void read_ing_in_file(char *i_string_0, char *file_path)
{




    FILE *file = fopen(file_path, "r");


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


        char i_word[10000];


        while (fscanf(file, "%s", i_word) != EOF)
        {
            
         
        }
        
        i_word[strlen(i_word)] = '\0';



        strcpy(i_string_0, i_word);
        
        

        fclose(file);

     
     

    }




}







void* make_in_to_a_folder(char *name_of_folder, struct list_of_Accounts_of_Amount *i_head_amount)
{




    struct list_of_Accounts_of_Amount *p = i_head_amount;

    int64_t len_ = len_list_of_Accounts_of_Amount(i_head_amount);
    
    char *s_number = NULL;


    char content[i_macro_of_Number_max_of_word_byte * i_Number_of_digits_max], content_1[i_macro_of_Number_max_of_word_byte * i_Number_of_digits_max];
    
    
    
    
    int64_t counter_1 = 0;
    
    
    //printf("\n\n\n\n\n----------------------------------------\n\n\n\n\n");
    
    
    while (p != NULL)
    {
    
                        
        
        str_number_1(content, &(p->amount));
        
        
        //printf("\n content =  %s .\n", content);
        
        
        
                        
        
                
        char i_cwd[PATH_MAX];
        
        bool semaphore = false;
        
        if (getcwd(i_cwd, sizeof(i_cwd)) != NULL)
        {
        
            semaphore = true;
        
        }
        
        char number_in_file[100];
        
        strcat(i_cwd, "/");
        
        
        strcat(i_cwd, name_of_folder);
        
        
        strcat(i_cwd, "/file_part_");
        
        
        strcat(i_cwd, int_ND_to_str_1(counter_1, number_in_file));
        
        
        strcat(i_cwd, ".mixer");
        
        
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
            
        
        }
        
        
        p = p->suiv;
        
        counter_1 += 1;
    
    }
    
    
    
        
    //printf("\n\n\n\n\n----------------------------------------\n\n\n\n\n");
        
        
        
        
        
        
        









}






void* read_from_a_folder(char *name_of_folder, struct list_of_Accounts_of_Amount **i_head_amount)
{


    struct number n_0, maximum_, n_1, n_2;
    
    
    n_0.length_of_num = 0;
    
    
    n_1.length_of_num = 0;
    
    
    n_2.length_of_num = 0;
    
    
    
    maximum_.length_of_num = 0;
    
    
    initialize_number(&n_2);
    
    
    number_str(i_macro_of_number_of_digite_maximum_after_the_floating_point, &maximum_, i_macro_of_length_of_encoding);
    
    


    number_str(i_macro_of_number_of_digite_maximum_after_the_floating_point, &n_0, "0");

    
    
    
    
    int64_t counter_0 = 0, counter_1;



    bool run_ = true, continue_ = true;


    // this is for check-ing if the number-s inside the file-s are less or equal than the i_macro_of_length_of_encoding
    
    
    while (run_ == true)
    {
    
        
                
                
        char i_cwd[PATH_MAX];
        
        bool semaphore = false;
        
        if (getcwd(i_cwd, sizeof(i_cwd)) != NULL)
        {
        
            semaphore = true;
        
        }
        
        char number_in_file[100];
        
        strcat(i_cwd, "/");
        
        
        strcat(i_cwd, name_of_folder);
        
        
        strcat(i_cwd, "/file_part_");
        
        
        strcat(i_cwd, int_ND_to_str_1(counter_0, number_in_file));
        
        
        strcat(i_cwd, ".mixer");
        
        
        
    
        
        FILE *file = fopen(i_cwd, "r");
        
        if (file) 
        {
    
            
                        
            

            
            char i_word[i_macro_of_Number_max_of_word_byte * 18 + 10];
            
            
            while (fscanf(file, "%s", i_word) != EOF)
            {
                
             
            }
            
            i_word[strlen(i_word)] = '\0';
            
                        
            printf("i_word = %s .\n", i_word);
            
            
            if (strlen(i_word) > 0)
            {
                
                //strcpy(i_string_0, i_word);
                
                
                number_str(i_macro_of_number_of_digite_maximum_after_the_floating_point, &n_1, i_word);
                
        
                if (ints_superieur_equal(&maximum_, &n_1) == false)
                {
                
                    //printf("(ints_superieur_equal(&maximum_, &n_1) == false) .\n");
                
                }
                
                            
                if (ints_superieur_equal(&n_1, &n_0) == false)
                {
                
                    //printf("(ints_superieur_equal(&n_1, &n_0) == false) .\n");
                
                }
                
                
                if ((ints_superieur_equal(&maximum_, &n_1) == false) || (ints_superieur_equal(&n_1, &n_0) == false))
                {
                    
                    //printf("i_hello . continue_ == false .\n");
                
                    
                    continue_ = false;
                    
                    
                    run_ = false;
                    
                
                }
                
                
                    
        
                //printf("الملف موجود.\n");
    
    
    
            }
            else
            {
            
            
                                
                continue_ = false;
                
                
                run_ = false;
                
                
            
            
            }
    
            fclose(file);  
            
            // لا تنسَ إغلاقه
    
        } 
        else 
        {
    
            run_ = false;
    
            //printf("الملف غير موجود.\n");
    
        }
        
        
        //printf("i_hello . counter_0 = %ld .\n", counter_0);
        
        
        counter_0 += 1;
        
    
    }



    // upload-ing


    if (continue_ == true)
    {
    
        counter_0 -= 1;
    
        run_ = true;

        counter_1 = 0;
                
        
        while ((counter_1 < counter_0) && (run_ == true))
        {
        
            
                    
                    
            char i_cwd[PATH_MAX];
            
            bool semaphore = false;
            
            if (getcwd(i_cwd, sizeof(i_cwd)) != NULL)
            {
            
                semaphore = true;
            
            }
            
            char number_in_file[100];
            
            strcat(i_cwd, "/");
            
            
            strcat(i_cwd, name_of_folder);
            
            
            strcat(i_cwd, "/file_part_");
            
            
            strcat(i_cwd, int_ND_to_str_1(counter_1, number_in_file));
            
            
            strcat(i_cwd, ".mixer");
            
            
            
            //printf("i_cwd = %s .\n", i_cwd);
            
            
        
            
            FILE *file = fopen(i_cwd, "r");
            
            if (file) 
            {
        
                
                            
                
        
                
                char i_word[i_macro_of_Number_max_of_word_byte * 18 + 10];
                
                
                while (fscanf(file, "%s", i_word) != EOF)
                {
                    
                 
                }
                
                i_word[strlen(i_word)] = '\0';
                
                
                //strcpy(i_string_0, i_word);
                
                
                number_str(i_macro_of_number_of_digite_maximum_after_the_floating_point, &n_1, i_word);
                
                
                int64_t counter_2 = n_1.length_of_num - 1;
                
                
                while (counter_2 >= 0)
                {
                
                    
                    n_2.num[i_macro_of_Number_max_of_word_byte - 1 + counter_2] = n_1.num[counter_2];
                
                    counter_2 -= 1;
                
                }
                
                
        
                if (counter_1 == 0)
                {
                
                    
                
                
                    int_copy(&((*i_head_amount)->amount), &n_2);

                }
                else
                {
                
                    
                    add_ele_list_of_Accounts_of_Amount(i_head_amount, (*i_head_amount)->unity, &n_2, len_list_of_Accounts_of_Amount(*i_head_amount));
                    
                
                }   
        
                //printf("الملف موجود.\n");
        
                fclose(file);  
                
                // لا تنسَ إغلاقه
        
            } 
            else 
            {
        
        
                run_ = false;
        

                //printf("الملف غير موجود.\n");
        
            }
            
            
            //printf("i_hello . counter_1 = %ld .\n", counter_1);
            
            counter_1 += 1;
            
        
        
        }
        
    
    }
    else
    {
    
    
    
    

        

        run_ = true;
        
        counter_1 = 0;
                
        
        while ((run_ == true))
        {
        
            
                    
                    
            char i_cwd[PATH_MAX];
            
            bool semaphore = false;
            
            if (getcwd(i_cwd, sizeof(i_cwd)) != NULL)
            {
            
                semaphore = true;
            
            }
            
            char number_in_file[100];
            
            strcat(i_cwd, "/");
            
            
            strcat(i_cwd, name_of_folder);
            
            
            strcat(i_cwd, "/file_part_");
            
            
            strcat(i_cwd, int_ND_to_str_1(counter_1, number_in_file));
            
            
            strcat(i_cwd, ".mixer");
            
            
            
            //printf("i_cwd = %s .\n", i_cwd);
            
            
        
            
            FILE *file = fopen(i_cwd, "r");
            
            if (file) 
            {
        
                
                            
                

                fclose(file);  
                
                // لا تنسَ إغلاقه
        
                                
                const char *filename = i_cwd ;
                
                if (remove(filename) == 0) {
                
                
                    printf("file delete-ed : %s .\n", filename);
                
        
        const char *filename = "اسم_الملف.txt";
    
        if (remove(filename) == 0) {
    
            //printf("تم حذف الملف بنجاح.\n");
    
        } else {
    
            //perror("فشل في حذف الملف");
    
        }
    
    
    
                    //printf("تم حذف الملف بنجاح.\n");
                
                } else {
                
                    //perror("فشل في حذف الملف");
                
                }
                
                
                
        
        
        
            } 
            else 
            {
        
        
                run_ = false;
        
        
                //printf("الملف غير موجود.\n");
        
            }
            
            
            //printf("i_hello . counter_1 = %ld .\n", counter_1);
            
            counter_1 += 1;
            
        
        
        }
        
        
    
    
    }



}











bool filter_0(char *operation)
{



    return true;

}





bool filter(char *operation)
{

    bool result = false;


    result = filter_0(operation);


    return result;

}




void calculator(char *operation, char *result)
{



    strcpy(result, "i_hello");


}





int main()
{


    // enter the operation :

    char *operation = "1+1";

    char result[length_of_the_result];
    
    bool pass_from_filter = false;
    

    // filter 
    
    pass_from_filter = filter(operation);



    // calculate :

    calculator(operation, result);
    
    
    
    
    
    // display the result :
    
    
    
    printf("\n\n\n operation = '%s' .\n\n\n", operation);
    
    
    
    if (strlen(result) > 0)
    {
    
        if (pass_from_filter == true)
        {
        
            printf("\n\n\n pass_from_filter = true .\n");
        
        }
        else
        {
        
        
            printf("\n\n\n pass_from_filter = false .\n");
        
        }
        
        
        printf("\n\n\n result = '%s' .\n\n\n\n\n", result);
    
    
    }
    else
    {
    
        printf("\n\n\n (strlen(result) <= 0) .\n\n\n\n\n");
    
    
    }
    
    
    
    return 0;

}


































