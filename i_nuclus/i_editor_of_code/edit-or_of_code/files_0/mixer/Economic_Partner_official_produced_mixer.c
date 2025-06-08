











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




#define Number_of_digits_max 18


#define number_of_digite_maximum_after_the_floating_point_macro 0


#define macro_of_length_of_encoding "1"

#define name_of_unity_of_encoding L"ASCII"


/*  

    obligation (0) : number_of_digite_maximum_after_the_floating_point_macro >= 0

    obligation (1) : char *s = NULL; --> str_number(&s, number_var);

    obligation (2) : the account of Billal 'identificator == "0"' should exist

    obligation (3) : macro_of_length_of_encoding == (length of encoding) - 1

*/





struct number
{

    int64_t *num;

    int64_t nombre_de_digite_maximale_apres_la_vergule;

    int64_t length_of_num;

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

    char *res = malloc(Number_of_digits_max + 1);

    d1 = n;

    d2 = n;

    while (i < Number_of_digits_max)
    {

        d1 = d1 / 10;

        d2 = d2 - (d1 * 10);

        res[Number_of_digits_max - i - 1] = int_to_c(d2);

        d2 = d1;
     
        i += 1;

    }

    res[Number_of_digits_max] = '\0';

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

        int64_t *q = malloc(((p->length_of_num) * sizeof(int64_t))  - sizeof(int64_t));


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




void int_copy(struct number *result, struct number a)
{



    if (0 < result->length_of_num)
    {
        
        free(result->num);

    }

    result->nombre_de_digite_maximale_apres_la_vergule = a.nombre_de_digite_maximale_apres_la_vergule;

    result->length_of_num = a.length_of_num;


    int64_t i = 0;

    result->num = malloc(sizeof(int64_t) * a.length_of_num);

    while (i < a.length_of_num)
    {

        (result->num)[i] = (a.num)[i];

        i += 1;

    }


}



enum add_ele_amount_account_errors 
{

    non_add_ele_amount_account_error,

    repetition_add_ele_amount_account_error

};



enum add_ele_amount_account_errors add_ele_list_of_Accounts_of_Amount(struct list_of_Accounts_of_Amount **t, struct Unity_of_Number unity_, struct number amount_, int64_t index)
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

        return non_add_ele_amount_account_error;

    // }

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

        add_ele_list_of_Accounts_of_Amount(&t, p->unity, p->amount, len_list_of_Accounts_of_Amount(t));

        p = p->suiv;

    }


    return t;

}







void add_ele_list_of_personal_accounts(struct list_of_personal_accounts **t, struct number n, char *name_, char *pre_name_, char *phone_number_, char *e_mail_, char *pass_word_, int64_t index)
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


        add_ele_list_of_personal_accounts(&t, p->identificator, p->name, p->pre_name, p->phone_number, p->e_mail, p->pass_word, len_list_of_personal_accounts(t));

        p = p->suiv;

    }


    return t;

}









// prints






void print_number(char *s, struct number t)
{

    int64_t *p = t.num, i = 0;

    printf("%snumber : (num, nombre_de_digite_maximale_apres_la_vergule, length_of_num) = ((", s);

    while (i < t.length_of_num)
    {

        printf("%ld, ", p[i]);

        i += 1;

    }

    printf("), (%ld), (%ld)) .\n", t.nombre_de_digite_maximale_apres_la_vergule, t.length_of_num);


}















char* str_number(char **result, struct number n)
{

    // from number to str


    if (n.length_of_num > 0)
    {


    

        if (*result != NULL)
        {
        
            free(*result);

        }


        int64_t len = Number_of_digits_max * n.length_of_num, i = 0, j = 0; 

        char *s = malloc(Number_of_digits_max + 2), *all_s = malloc(len), *s_1 = malloc(Number_of_digits_max + 2);

        while (j < n.length_of_num)
        {
        
            strcpy(s_1, int_ND_to_str(my_abs_((n.num)[j])));

            strcpy(all_s + i, s_1);

            i += Number_of_digits_max;

            j += 1;
        
        }

        // print_string(&t_s);


        // printf("all_s = %s . n.nombre_de_digite_maximale_apres_la_vergule = %ld . len = %ld .\n", all_s, n.nombre_de_digite_maximale_apres_la_vergule, len);


        if ((n.nombre_de_digite_maximale_apres_la_vergule >= len))
        {

            // printf("hello .\n");

            // printf("2 .all_s = %s . n.nombre_de_digite_maximale_apres_la_vergule = %ld . len = %ld . _ = %ld .\n", all_s, n.nombre_de_digite_maximale_apres_la_vergule, len, n.nombre_de_digite_maximale_apres_la_vergule - len);


            char *res = malloc(n.nombre_de_digite_maximale_apres_la_vergule + 5);

            uint64_t n_m = n.nombre_de_digite_maximale_apres_la_vergule;
            
            i = 0;

            if ((n.num)[0] < 0)
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


            *result = res;


        }
        else
        {

            char *res = malloc(len + 5);

            uint64_t n_m = len, k;

            i = 0;
            
            if ((n.num)[0] < 0)
            {

                res[i] = '-';
                
                i += 1;


            }



            k = 0;

            while (all_s[k] == '0')
            {

                k += 1;

            }



            if (k < (len - n.nombre_de_digite_maximale_apres_la_vergule))
            {

                n_m -= k;

            }
            else
            {
                n_m -= (len - n.nombre_de_digite_maximale_apres_la_vergule) - 1;

            }

    
    
            while (0 < n_m)
            {


                if (n_m == n.nombre_de_digite_maximale_apres_la_vergule)
                {

                    res[i] = '.';

                    i += 1;

                    res[i] = all_s[len - n_m];

                        
                }
                else
                {

                    res[i] = all_s[len - n_m];

                }

                // printf("n_m = %ld . res[%ld] = %c .\n", n_m, i, res[i]);

                n_m -= 1;

                i += 1;

            }

            res[i] = '\0';

            // printf("2 . res = %s .\n", res);

            *result = res;
            

        }

    }
    else
    {

        char *res = "NULL";

        *result = res;
        

    }

}





void number_str(int64_t nombre_de_digite_maximale_apres_la_vergule, struct number *n, char *s)
{


    // transforme str to number



    // vider le numero n


    if (n->length_of_num > 0)
    {

        free(n->num);

    }

    n->length_of_num = 0;


    n->nombre_de_digite_maximale_apres_la_vergule = nombre_de_digite_maximale_apres_la_vergule;






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

    while ((n_m < nombre_de_digite_maximale_apres_la_vergule) && (i < length))
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
    
    if (n_m < nombre_de_digite_maximale_apres_la_vergule)
    {

        o = (nombre_de_digite_maximale_apres_la_vergule - n_m) / Number_of_digits_max;

        j = 0;

        while (j < o)
        {

            add_ele_int(n, 0, 0);

            j += 1;

        }

        o = nombre_de_digite_maximale_apres_la_vergule - (n_m + (o * Number_of_digits_max));

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
        

        while ((j < (Number_of_digits_max - o)) && (0 <= i))
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


        str_number(&s, p->amount);

        printf("list[%ld] = {(amount:%s), (name_of_unity:", i, s);


        size_t size_needed = wcstombs(NULL, p->unity.name_of_unity, 0) + 1;
        
        char *utf8_text = malloc(size_needed);

        wcstombs(utf8_text, p->unity.name_of_unity, size_needed);

        printf("%s)} .\n", utf8_text);



        i += 1;

        p = p->suiv;

    }

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

        str_number(&s, p->amount);

        printf("list[%ld] = {(amount:%s), (name_of_unity:", i, s);


        size_t size_needed = wcstombs(NULL, p->unity.name_of_unity, 0) + 1;
        
        char *utf8_text = malloc(size_needed);

        wcstombs(utf8_text, p->unity.name_of_unity, size_needed);

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
    

        str_number(&s, p->identificator);

        printf("list[%ld] = {(id:%s), (name:%s), (pre_name:%s), (phone_number:%s), (e_mail:%s), (pass_word:%s)} .\n", i, s, p->name, p->pre_name, p->phone_number, p->e_mail, p->pass_word);

        i += 1;

        p = p->suiv;

    }

}










bool ints_egale(struct number a, struct number b)
{

    if (a.length_of_num == b.length_of_num)
    {

            
        int64_t i = 0;

        while ((i < a.length_of_num) && (i < b.length_of_num) && ((a.num)[i] == (b.num)[i]))
        {

            i += 1;

        }

        if (i == a.length_of_num)
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


bool ints_superieur_egale(struct number a, struct number b)
{



    if (a.length_of_num == 0)
    {

        if (b.length_of_num > 0)
        {

            return false;

        }
        else
        {

            return true;

        }


    }
    else if (b.length_of_num == 0)
    {

        return true;

    }
    else
    {
        
        bool m = (((((a.num)[0]) < 0) && ((b.num)[0]) > 0) || ((((a.num)[0]) > 0) && ((b.num)[0]) < 0));

        if (m)
        {

            if ((a.num)[0] < 0)
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


            if (((a.num)[0] < 0) && (a.length_of_num > b.length_of_num))
            {

                return false;

            }
            else if (((a.num)[0] < 0) && (a.length_of_num < b.length_of_num))
            {

                return true;

            }
            else if (((a.num)[0] > 0) && (a.length_of_num < b.length_of_num))
            {

                return false;

            }
            else if (((a.num)[0] > 0) && (a.length_of_num > b.length_of_num))
            {

                return true;

            }
            else if (a.length_of_num == b.length_of_num)
            {

                int64_t i = 0;

                while ((i < a.length_of_num) && ((a.num)[i] == (b.num)[i]))
                {

                    i += 1;

                }

                if (i == a.length_of_num)
                {

                    return true;

                }
                else if ((a.num)[i] > (b.num)[i])
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












struct operation_int add_int(int64_t a, int64_t b)
{



    struct operation_int n;

    int64_t i, q = 1;

    uint64_t h = a + b, k, d;

    i = 0;

    while (i < Number_of_digits_max)
    {

        q *= 10;

        i += 1;

    }

    

    k = h / q;

    d = h - (k * q);


    n.ele = d;

    n.reminder = k;


    return n;

}






void add_number_positive(int64_t nombre_de_digite_maximale_apres_la_vergule, struct number *result, struct number a, struct number b)
{

    // adding 2 positive numbers with nombre_de_digite_maximale_apres_la_vergule
    
    //  --->  res = a + b




    int64_t i, j;



    if (result->length_of_num > 0)
    {

        free(result->num);

    }


    result->nombre_de_digite_maximale_apres_la_vergule = nombre_de_digite_maximale_apres_la_vergule;

    result->length_of_num = 0;


    struct operation_int n;




    int64_t g = 0, a0, b0;
    
    i = a.length_of_num - 1;

    j = b.length_of_num - 1;


    while ((0 <= i) || (0 <= j))
    {



        if (i < 0)
        {

            a0 = 0;

        }
        else
        {

            a0 = (a.num)[i];

            i -= 1;


        }

        if (j < 0)
        {

            b0 = 0;

        }
        else
        {

            b0 = (b.num)[j];

            j -= 1;

        }


        n = add_int(a0, b0);

        add_ele_int(result, n.ele + g, 0);

        g = n.reminder;




    }


    if (g != 0)
    {

        add_ele_int(result, g, 0);


    }

}











struct operation_int sub_int(int64_t a, int64_t b)
{



    struct operation_int n;

    int64_t i, q = 0, d = 0;

    if (a < b)
    {


        i = 0;

        q = 1;

        while (i < Number_of_digits_max)
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




void sub_int_number(struct number *result, struct number a, struct number b)
{


    int64_t i, j;


    if (result->length_of_num > 0)
    {

        free(result->num);

    }


    result->length_of_num = 0;




    struct operation_int n;

    int64_t q = 1;

    i = 0;

    while (i < Number_of_digits_max)
    {

        q *= 10;

        i += 1;

    }


    int64_t g = 0, a0, b0;

    i = a.length_of_num - 1;

    j = b.length_of_num - 1;



    while ((0 <= i) || (0 <= j))
    {
        
        a0 = (a.num)[i];
            

        if (j < 0)
        {

            b0 = 0;

        }
        else
        {

            b0 = (b.num)[j];
            
            j -= 1;

        }

        if (i == 0)
        {

            n.ele = (a.num)[i] - (b0 + g);

        }
        else
        {

            n = sub_int(a0, b0 + g);

        }



        add_ele_int(result, n.ele, 0);

        g = n.reminder;

        i -= 1;

    }




}






void sub_number(int64_t nombre_de_digite_maximale_apres_la_vergule, struct number *result, struct number a, struct number b)
{

    // substraction 2 numbers with nombre_de_digite_maximale_apres_la_vergule
    
    //  --->  res = a + b


    result->nombre_de_digite_maximale_apres_la_vergule = nombre_de_digite_maximale_apres_la_vergule;


    bool m = ints_superieur_egale(a, b);
    
    if (m)
    {

        sub_int_number(result, a, b);
   

    }
    else
    {


        sub_int_number(result, b, a);


    }



    while ((1 < result->length_of_num) && (((result->num)[0] == 0)))
    {

        remove_ele_int(result, 0);

    }

    if (m == false)
    {

        (result->num)[0] *= -1;


    }



}




void add_number(int64_t nombre_de_digite_maximale_apres_la_vergule, struct number *result, struct number a, struct number b)
{

    // adding 2 numbers with nombre_de_digite_maximale_apres_la_vergule
    
    //  --->  res = a + b





    if ((0 < a.length_of_num) && (0 < b.length_of_num))
    {

        
        bool m = (((((a.num)[0]) < 0) && (((b.num)[0]) > 0)) || ((((a.num)[0]) > 0) && (((b.num)[0]) < 0)));


        
        
        if (m)
        {





            struct number n;

            n.length_of_num = 0;


            if ((b.num)[0] < 0)
            {

                
                int_copy(&n, b);

                (n.num)[0] *= -1;
          
                sub_number(nombre_de_digite_maximale_apres_la_vergule, result, a, n);

            }
            else
            {

                
                int_copy(&n, a);

                (n.num)[0] *= -1;

                sub_number(nombre_de_digite_maximale_apres_la_vergule, result, b, n);

            }

        }
        else
        {

        
        
        
        
            if ((((a.num)[0]) < 0) || (((b.num)[0]) < 0))
            {

                struct number n, n_;

                n.length_of_num = 0;

                n_.length_of_num = 0;




                int_copy(&n, a);

                (n.num)[0] *= -1;


                int_copy(&n_, b);

                (n_.num)[0] *= -1;


                add_number_positive(nombre_de_digite_maximale_apres_la_vergule, result, n, n_);


                while ((1 < result->length_of_num) && ((result->num)[0] == 0))
                {

                    remove_ele_int(result, 0);

                }

                (result->num)[0] *= -1;


            }
            else
            {



                add_number_positive(nombre_de_digite_maximale_apres_la_vergule, result, a, b);


                while ((1 < result->length_of_num) && ((result->num)[0] == 0))
                {

                    remove_ele_int(result, 0);

                }




            }

        }

    }

}





void print_virtual_amount(struct list_of_personal_accounts **tete, struct number identificator_, struct Unity_of_Number unity_, struct number amount_)
{



    struct list_of_personal_accounts *q = *tete;


    while ((q != NULL) && (ints_egale(q->identificator, identificator_) == false))
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


            
            add_number(number_of_digite_maximum_after_the_floating_point_macro, &result, p->amount, amount_);

            
            int_copy(&(p->amount), result);

            
        }

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


//     while ((q != NULL) && (ints_egale(q->identificator, identificator_) == false))
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


//     while ((q != NULL) && (ints_egale(q->identificator, identificator_) == false))
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

//             number_str(number_of_digite_maximum_after_the_floating_point_macro, &n, s);


//             free(s);



//             struct list_of_personal_accounts *q = *tete;



//             while ((q != NULL) && (ints_egale(q->identificator, n) == false))
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

//                     number_str(number_of_digite_maximum_after_the_floating_point_macro, &n, s);


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

//                     number_str(number_of_digite_maximum_after_the_floating_point_macro, &n, s);


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

//                     number_str(number_of_digite_maximum_after_the_floating_point_macro, &n, s_);

                    

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


//                     number_str(number_of_digite_maximum_after_the_floating_point_macro, &n, s_);


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





void extract_gain(struct number *result, struct number number_)
{


    if (0 < result->length_of_num)
    {

        free(result->num);

    }

    result->nombre_de_digite_maximale_apres_la_vergule = number_.nombre_de_digite_maximale_apres_la_vergule;

    result->length_of_num = 0;


    if (0 < number_.length_of_num)
    {
        
        int64_t q = 1, i = 0;

        while ((i < Number_of_digits_max) && (q < number_.num[0]))
        {

            q *= 10;

            i += 1;

        }

        i -= 4;
        
        int64_t j;

        if (i < 0)
        {

            int64_t i_ = Number_of_digits_max + i;
    
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

        while (i_ < number_.length_of_num - 2)
        {

            add_ele_int(result, 0, 0);

            i_ += 1;

        }

        if (i >= 0)
        {

            add_ele_int(result, 0, 0);

            add_ele_int(result, q, 0);

        }
        else if (number_.length_of_num > 1)
        {

            add_ele_int(result, q, 0);

        }


    }

}



enum Errors_ {

    non_error,

    the_account_of_gain_do_not_exist,

    the_extracted_amount_is_begger_than_the_contity_of_the_amount_in_the_account,

    the_Unity_of_amount_do_not_exist,

    the_account_do_not_exist,

    there_is_no_value_to_trensfer

};



enum Errors_ trensfer(struct list_of_personal_accounts **tete, struct number identificator_of_gainer, struct number identificator_1, struct number identificator_2, struct Unity_of_Number unity_, struct number amount_, bool red_)
{


    bool semaphore_of_success = true;

    enum Errors_ error_meesage = non_error;

    struct number gain;

    gain.length_of_num = 0;




    extract_gain(&gain, amount_);
    

    if (0 < gain.length_of_num)
    {
        

        struct number extracted_amount;

        extracted_amount.length_of_num = 0;

        add_number(number_of_digite_maximum_after_the_floating_point_macro, &extracted_amount, amount_, gain);




        struct list_of_personal_accounts *q = *tete;







        // extracting extracted_amount from identificator_1


        if (semaphore_of_success)
        {


            

            q = *tete;


            while ((q != NULL) && (ints_egale(q->identificator, identificator_1) == false))
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
                    
                    
                        if (ints_superieur_egale(p->amount, extracted_amount))
                        {


                            struct number n;

                            n.length_of_num = 0;

                            int_copy(&(n), p->amount);

                            extracted_amount.num[0] *= -1;
 
                            add_number(number_of_digite_maximum_after_the_floating_point_macro, &(p->amount), n, extracted_amount);
                         


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


                        if (ints_superieur_egale(p->amount, extracted_amount))
                        {

                            struct number n;

                            n.length_of_num = 0;

                            int_copy(&(n), p->amount);
                            
                            extracted_amount.num[0] *= -1;

                            add_number(number_of_digite_maximum_after_the_floating_point_macro, &(p->amount), n, extracted_amount);


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


            

            q = *tete;


            while ((q != NULL) && (ints_egale(q->identificator, identificator_2) == false))
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


                        struct number n;

                        n.length_of_num = 0;

                        int_copy(&(n), p->amount);

    
                        add_number(number_of_digite_maximum_after_the_floating_point_macro, &(p->amount), n, amount_);

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
                        
                        struct number n;

                        n.length_of_num = 0;

                        int_copy(&(n), p->amount);


                        add_number(number_of_digite_maximum_after_the_floating_point_macro, &(p->amount), n, amount_);

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



            q = *tete;


            while ((q != NULL) && (ints_egale(q->identificator, identificator_of_gainer) == false))
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


                        struct number n;

                        n.length_of_num = 0;

                        int_copy(&(n), p->amount);


                        add_number(number_of_digite_maximum_after_the_floating_point_macro, &(p->amount), n, gain);

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


                        struct number n;

                        n.length_of_num = 0;

                        int_copy(&(n), p->amount);


                        add_number(number_of_digite_maximum_after_the_floating_point_macro, &(p->amount), n, gain);

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

        error_meesage = there_is_no_value_to_trensfer;

    }
    

    return error_meesage;

}




void making_2(struct list_of_personal_accounts **head, struct number identificator_0, struct number identificator_1, wchar_t *name_of_unity_, char *big_number)
{




    struct Unity_of_Number u;

    u.name_of_unity = malloc(10000);

    enum add_ele_amount_account_errors errors = non_add_ele_amount_account_error;


    struct number n3, n4, n5, n6;



    n6.length_of_num = 0;


    n5.length_of_num = 0;


    n4.length_of_num = 0;



    n3.nombre_de_digite_maximale_apres_la_vergule = 0;

    n3.length_of_num = 1;

    n3.num = malloc(sizeof(int64_t));

    (n3.num)[0] = 0;




    number_str(number_of_digite_maximum_after_the_floating_point_macro, &n5, "1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000");

    number_str(number_of_digite_maximum_after_the_floating_point_macro, &n6, big_number);


    wcscpy(u.name_of_unity, name_of_unity_);

    errors = add_ele_list_of_Accounts_of_Amount(&((*head)->red_pocket.head_of_amount_accounts), u, n3, len_list_of_Accounts_of_Amount(((*head)->red_pocket.head_of_amount_accounts)));

    print_virtual_amount(head, identificator_0, u, n6);


    struct list_of_personal_accounts *p = *head;

    p = p->suiv;


    errors = add_ele_list_of_Accounts_of_Amount(&((p)->red_pocket.head_of_amount_accounts), u, n3, len_list_of_Accounts_of_Amount(((p)->red_pocket.head_of_amount_accounts)));

    print_virtual_amount(head, identificator_1, u, n5);



    p = p->suiv;


    errors = add_ele_list_of_Accounts_of_Amount(&((p)->red_pocket.head_of_amount_accounts), u, n3, len_list_of_Accounts_of_Amount(((p)->red_pocket.head_of_amount_accounts)));






    p = p->suiv;

    (identificator_1.num)[0] = 3;

    errors = add_ele_list_of_Accounts_of_Amount(&((p)->red_pocket.head_of_amount_accounts), u, n3, len_list_of_Accounts_of_Amount(((p)->red_pocket.head_of_amount_accounts)));

    print_virtual_amount(head, identificator_1, u, n5);



}










void next_step_in_mix(struct list_of_Accounts_of_Amount **head)
{



    int64_t n = 0, length = len_list_of_Accounts_of_Amount(*head);

    struct list_of_Accounts_of_Amount *p = *head;

    struct number n_1, n_0, length_on_number;

    n_1.length_of_num = 0;

    n_0.length_of_num = 0;

    length_on_number.length_of_num = 0;



    number_str(number_of_digite_maximum_after_the_floating_point_macro, &n_1, "1");

    number_str(number_of_digite_maximum_after_the_floating_point_macro, &length_on_number, macro_of_length_of_encoding);


    bool run = true, plus_account = false;

    while (run == true)
    {




        if (ints_superieur_egale(p->amount, length_on_number) == true)
        {

        
            number_str(number_of_digite_maximum_after_the_floating_point_macro, &(p->amount), "0");

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

            add_number(number_of_digite_maximum_after_the_floating_point_macro, &n_0, p->amount, n_1);
            
            int_copy(&(p->amount), n_0);
            
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

        number_str(number_of_digite_maximum_after_the_floating_point_macro, &(n_1), "0");

        enum add_ele_amount_account_errors errors = non_add_ele_amount_account_error;

        errors = add_ele_list_of_Accounts_of_Amount(head, p->unity, n_1, len_list_of_Accounts_of_Amount(*head));
        
    }


}










void next_step_in_mix_1(struct list_of_Accounts_of_Amount **head)
{



    int64_t n = 0, length = len_list_of_Accounts_of_Amount(*head);

    struct list_of_Accounts_of_Amount *p = *head;

    struct number n_1, n_0, length_on_number;

    n_1.length_of_num = 0;

    n_0.length_of_num = 0;

    length_on_number.length_of_num = 0;



    number_str(number_of_digite_maximum_after_the_floating_point_macro, &n_1, "1");

    number_str(number_of_digite_maximum_after_the_floating_point_macro, &length_on_number, macro_of_length_of_encoding);


    bool run = true, plus_account = false;

    while (run == true)
    {




        if (ints_superieur_egale(p->amount, length_on_number) == true)
        {

        
            number_str(number_of_digite_maximum_after_the_floating_point_macro, &(p->amount), "0");

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

            add_number(number_of_digite_maximum_after_the_floating_point_macro, &n_0, p->amount, n_1);
            
            int_copy(&(p->amount), n_0);
            
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

        number_str(number_of_digite_maximum_after_the_floating_point_macro, &(n_1), "1");

        enum add_ele_amount_account_errors errors = non_add_ele_amount_account_error;

        errors = add_ele_list_of_Accounts_of_Amount(head, p->unity, n_1, len_list_of_Accounts_of_Amount(*head));
        
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







int main()
{


    

    struct number n, n1, n2;

    int64_t nombre_de_digite_maximale_apres_la_vergule = 6;

    n.length_of_num = 0;

    n.nombre_de_digite_maximale_apres_la_vergule = nombre_de_digite_maximale_apres_la_vergule;

    n1.length_of_num = 0;

    n1.nombre_de_digite_maximale_apres_la_vergule = nombre_de_digite_maximale_apres_la_vergule;

    n2.length_of_num = 0;

    n2.nombre_de_digite_maximale_apres_la_vergule = nombre_de_digite_maximale_apres_la_vergule;


    add_ele_int(&n, 999999999999999999, n.length_of_num);

    add_ele_int(&n, 999999999999999999, n.length_of_num);

    // add_ele_int(&n, 999999999999999999, n.length_of_num);

    // add_ele_int(&n, 999999999999999999, n.length_of_num);




    add_ele_int(&n1, -999999999999999999, n1.length_of_num);

    add_ele_int(&n1, 999999999999999999, n1.length_of_num);

    // add_ele_int(&n1, 999999999999999999, n1.length_of_num);

    // add_ele_int(&n1, 999999999999999999, n1.length_of_num);




    print_number("n = ", n);

    print_number("n1 = ", n1);


    bool b = ints_superieur_egale(n, n1);

    if (b)
    {

        printf("b = true .\n");

    }
    else
    {

        printf("b = false .\n");


    }


    char *s = NULL, *s1 = NULL;

    
    str_number(&s, n);
    
    str_number(&s1, n1);

    str_number(&s1, n1);


    printf("s = %s .\n", s);

    
    printf("s1 = %s .\n", s1);



    number_str(nombre_de_digite_maximale_apres_la_vergule, &n, s);

    
    print_number("n = ", n);




    number_str(nombre_de_digite_maximale_apres_la_vergule, &n1, s1);

    
    print_number("n1 = ", n1);





    printf("----------------------------------------\n");



    double t1, t2;


    t1 = time_();


    number_str(nombre_de_digite_maximale_apres_la_vergule, &n, s);
   

    number_str(nombre_de_digite_maximale_apres_la_vergule, &n1, s1);


    add_number(nombre_de_digite_maximale_apres_la_vergule, &n2, n, n1);



    t2 = time_();

    print_number("n2 = ", n2);

    printf("time = %.10f .\n\n", t2 - t1);




    t1 = time_();



    struct list_of_personal_accounts *tete = NULL, *tete_1 = NULL, *p = NULL;

    struct number n3, n4, n5, n6, n7;

    enum Errors_ message;


    n7.length_of_num = 0;


    n6.nombre_de_digite_maximale_apres_la_vergule = 0;

    n6.length_of_num = 1;

    n6.num = malloc(sizeof(int64_t));

    (n6.num)[0] = 1;


    n5.length_of_num = 0;


    n4.nombre_de_digite_maximale_apres_la_vergule = 0;

    n4.length_of_num = 1;

    n4.num = malloc(sizeof(int64_t));

    (n4.num)[0] = 0;


    n3.nombre_de_digite_maximale_apres_la_vergule = 0;

    n3.length_of_num = 1;

    n3.num = malloc(sizeof(int64_t));

    (n3.num)[0] = 0;



   
    add_ele_list_of_personal_accounts(&tete, n3, "Billal", "Debouci", "+213561577437", "deboubil4@outlook.com", "male_principal-central_official_pass_word_0", len_list_of_personal_accounts(tete));


    (n3.num)[0] = 1;

    add_ele_list_of_personal_accounts(&tete, n3, "me_1", "pre_name_1", "+0000000000001", "deboubil4@outlook.com", "male_principal-central_official_pass_word_1", len_list_of_personal_accounts(tete));

    (n3.num)[0] = 2;


    add_ele_list_of_personal_accounts(&tete, n3, "Billal", "Debouci", "+213561577437", "deboubil4@outlook.com", "male_principal-central_official_pass_word_1", len_list_of_personal_accounts(tete));


    (n3.num)[0] = 3;


    add_ele_list_of_personal_accounts(&tete, n3, "imparallel", "Debouci", "+213561577437", "deboubil4@outlook.com", "male_central_official_pass_word_1", len_list_of_personal_accounts(tete));




    (n3.num)[0] = 0;



    add_ele_list_of_personal_accounts(&tete_1, n3, "Billal", "Debouci", "+213561577437", "deboubil4@outlook.com", "pass_official_word_0", len_list_of_personal_accounts(tete_1));


    (n3.num)[0] = 1;


    add_ele_list_of_personal_accounts(&tete_1, n3, "simulated_name_1", "simulated_pre_name_1", "simulated_phone_number_1", "simulated_e_mail_1", "simulated_pass_word_1", len_list_of_personal_accounts(tete_1));
    

    (n3.num)[0] = 0;


    printf("tete -> \n");

    print_list_of_personal_accounts(tete);


    printf("tete_1 -> \n");

    print_list_of_personal_accounts(tete_1);



    struct Unity_of_Number u;

    u.name_of_unity = malloc(10000);

    number_str(number_of_digite_maximum_after_the_floating_point_macro, &n3, "0");

    print_number("n3 = ", n3);


    number_str(number_of_digite_maximum_after_the_floating_point_macro, &n5, "1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000");

    print_number("n5 = ", n5);




    enum add_ele_amount_account_errors errors = non_add_ele_amount_account_error;


    // strcpy(u.name_of_unity, "money");

    // errors = add_ele_list_of_Accounts_of_Amount(&(tete->red_pocket.head_of_amount_accounts), u, n3, len_list_of_Accounts_of_Amount((tete->red_pocket.head_of_amount_accounts)));

    // print_virtual_amount(&tete, n4, u, n5);


    // strcpy(u.name_of_unity, "money");

    // errors = add_ele_list_of_Accounts_of_Amount(&(tete_1->red_pocket.head_of_amount_accounts), u, n3, len_list_of_Accounts_of_Amount((tete_1->red_pocket.head_of_amount_accounts)));
    

    // print_virtual_amount(&tete_1, n4, u, n5);


    // p = tete_1->suiv;


    // strcpy(u.name_of_unity, "money");

    // errors = add_ele_list_of_Accounts_of_Amount(&(p->red_pocket.head_of_amount_accounts), u, n3, len_list_of_Accounts_of_Amount((p->red_pocket.head_of_amount_accounts)));


    (n6.num)[0] = 1;


    number_str(number_of_digite_maximum_after_the_floating_point_macro, &n7, "100");

    print_number("n7 = ", n7);




    // printf("tete_1 : ele[0] -> \n");

    // print_list_of_Accounts_of_Amount(tete_1->red_pocket.head_of_amount_accounts);




    message = trensfer(&(tete_1), n4, n4, n6, u, n7, true);


    printf("message = %d .\n", message);




    // printf("tete_1 : ele[1] -> \n");

    // print_list_of_Accounts_of_Amount(p->red_pocket.head_of_amount_accounts);



    // printf("tete_1 : ele[0] -> \n");

    // print_list_of_Accounts_of_Amount(tete_1->red_pocket.head_of_amount_accounts);



    int64_t number_of_unitys = 1;

    t1 = time_();




    circle I;

    I.pointer = (void *)tete;

    I.name_of_circle = malloc(10);

    strcpy(I.name_of_circle, "I\0");

    I.type_of_reference = malloc(30);

    strcpy(I.type_of_reference, "reference\0");




    struct list_of_Accounts_of_Amount *head_amout = NULL;


    number_str(number_of_digite_maximum_after_the_floating_point_macro, &n3, "0");

    print_number("n3 = ", n3);


    wcscpy(u.name_of_unity, name_of_unity_of_encoding);

    errors = add_ele_list_of_Accounts_of_Amount(&(head_amout), u, n3, len_list_of_Accounts_of_Amount(head_amout));


    // wcscpy(u.name_of_unity, name_of_unity_of_encoding);

    // errors = add_ele_list_of_Accounts_of_Amount(&(head_amout), u, n3, len_list_of_Accounts_of_Amount(head_amout));

    
    printf("\n\n\n\n\n");
    

    printf("list before : \n");

    print_list_of_Accounts_of_Amount(head_amout);


    next_step_in_mix_1(&(head_amout));



    printf("list after : \n");

    print_list_of_Accounts_of_Amount(head_amout);



    next_step_in_mix_1(&(head_amout));



    printf("list after : \n");

    print_list_of_Accounts_of_Amount(head_amout);



    next_step_in_mix_1(&(head_amout));



    printf("list after : \n");

    print_list_of_Accounts_of_Amount(head_amout);



    next_step_in_mix_1(&(head_amout));



    printf("list after : \n");

    print_list_of_Accounts_of_Amount(head_amout);



    printf("\n\n\n\n\n");


    int64_t i = 0;


    printf("list from first to last : \n");


    while (i < len_list_of_Accounts_of_Amount(head_amout))
    {

        print_list_of_Accounts_of_Amount_index(head_amout, i);

        i += 1;

    }



    printf("list from last to first : \n");


    i = len_list_of_Accounts_of_Amount(head_amout) - 1;

    while (i >= 0)
    {

        print_list_of_Accounts_of_Amount_index(head_amout, i);

        i -= 1;

    }



    t2 = time_();







    printf("\n\n\ntime = %.10f seconde-s .\n\n\n", t2 - t1);

    //printf("\n\n\nbig_number = %ld .\n\n\n", strlen(big_number));

    date_();

    printf("\nfinished .\n");


    printf("\nnumber of unitys = %ld .\n", len_list_of_Accounts_of_Amount(tete->red_pocket.head_of_amount_accounts));


    // printing_personal_account_on_file_for_the_show(tete, n4, "printed_personal_account_for_smallest_for_the_show_part(0).economic_partner");



    // printing_personal_account_on_file_for_the_DataBase(tete, n4, "printed_personal_account_for_smallest_for_the_DataBase_part(0).economic_partner");





    // p = tete;

    // p = p->suiv;

    // p = p->suiv;


    // (n4.num)[0] = 2;

    // printing_personal_account_on_file_for_the_show(p, n4, "printed_personal_account_for_smallest_for_the_show_part(1).economic_partner");


    printf("\n\nmixer .\n");




    // bool run = true;

    // char *end_message = malloc(255);

    // while (run == true)
    // {

    //     scanf("%s", end_message);

    //     printf("end_message = %s .\n", end_message);

    //     if (char_equal_(end_message, "exit") == true)
    //     {

    //         run = false;

    //     }

    // }










    // removing all elements



    while (0 < len_list_of_personal_accounts(tete))
    {
        
        remove_ele_list_of_personal_accounts(&tete, 0);

    }


    while (0 < len_list_of_personal_accounts(tete_1))
    {
        
        remove_ele_list_of_personal_accounts(&tete_1, 0);

    }


    print_list_of_personal_accounts(tete);

    printf("All elements removed succesfuly .\n");



    t2 = time_();


    printf("time = %.10f .\n", t2 - t1);



    return 0;

}



















