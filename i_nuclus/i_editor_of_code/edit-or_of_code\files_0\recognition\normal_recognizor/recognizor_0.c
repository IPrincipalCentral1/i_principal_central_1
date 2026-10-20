













#define STB_IMAGE_IMPLEMENTATION

#include "stb_image.h"

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







#define i_Number_of_digits_max 18







struct list_of_pixel
{

    int64_t red;
    
    int64_t green;
    
    int64_t blue;
    
    int64_t alpha;

    struct list_of_pixel *suiv;


};









struct type_of_image
{

    int64_t width;
    
    int64_t height;
    
    int64_t channels;
    
    
    struct list_of_pixel *head;
    



};















void date_()
{

    struct timespec tv;

    struct tm* current_time;

    // الحصول على الوقت بدقة microseconds

    clock_gettime(CLOCK_REALTIME, &tv);

    // تحويل الوقت إلى struct tm

    current_time = localtime(&tv.tv_sec);

    // طباعة التاريخ + الوقت + الميلي ثانية

    printf("date : %d-%02d-%02d %02d:%02d:%02d: %ld\n",
           current_time->tm_year + 1900, // السنة
           current_time->tm_mon + 1,      // الشهر
           current_time->tm_mday,         // اليوم
           current_time->tm_hour,         // الساعات
           current_time->tm_min,          // الدقائق
           current_time->tm_sec,          // الثواني
           tv.tv_nsec);             // الميلي ثانية

}











char* str_from_UTF_8(wchar_t *wtext)
{


    size_t size = wcstombs(NULL, wtext, 0) + 1;



    char *utf8_text = malloc(size);

    if (!utf8_text) 
    {

        perror("malloc");

    }


    wcstombs(utf8_text, wtext, size);


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


char* int_N_to_str(int64_t n)
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








void add_element_list_of_pixel(struct list_of_pixel **head, int64_t red, int64_t green, int64_t blue, int64_t alpha, int64_t index)
{

    struct list_of_pixel *p = *head;

    struct list_of_pixel *q = p;

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


            q = (struct list_of_pixel *) malloc(sizeof(struct list_of_pixel));


            q->red = red;
            
            q->green = green;
            
            q->blue = blue;
            
            q->alpha = alpha;


            q->suiv = *head;

            *head = q;





        }
        else
        {


            struct list_of_pixel *k;

            k = (struct list_of_pixel *) malloc(sizeof(struct list_of_pixel));


            
            k->red = red;
            
            k->green = green;
            
            k->blue = blue;
            
            k->alpha = alpha;
            

            k->suiv = q->suiv;

            q->suiv = k;

            
        }

    }


}








void delete_element_list_of_pixel(struct list_of_pixel **head, int64_t index)
{

    struct list_of_pixel *p = *head;

    struct list_of_pixel *q = p;

    struct list_of_pixel *g = q;


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






int64_t len_list_of_pixel(struct list_of_pixel *head)
{

    int64_t counter_0 = 0;

    struct list_of_pixel *p = head;

    while (p != NULL)
    {

        counter_0 += 1;

        p = p->suiv;

    }

    return counter_0;

}




struct list_of_pixel* get_pixel(struct type_of_image image, int64_t x, int64_t y)
{


    if ((x < image.width) && (y < image.height))
    
    int64_t x_1 = 0, y_1 = 0;
    
    while (y_1 < image.height)
    {
    
        x_1 = 0;
        
        
        while (x_1 < image.width)
        {
        
            
        
            x_1 += 1;
        
        }
    
        
        y_1 += 1;
    
    }


} 




void print_list_of_pixel(struct list_of_pixel *head, int64_t width)
{

    int64_t x = 0, y = 0;

    struct list_of_pixel *p = head;

    while (p != NULL)
    {


        printf("pixel (%ld, %ld) : [red = %ld, green = %ld, blue = %ld] .\n", x, y, p->red, p->green, p->blue);

        x += 1;
        

        if (x >= width)
        {
        
            x = 0;
           
            y += 1;
        
        }

        p = p->suiv;

    }


}





void print_image(struct type_of_image image)
{



    printf("image : (width = %ld, height = %ld) .\n", image.width, image.height);

    print_list_of_pixel(image.head, image.width);
    
    printf("\n\n\n\n");


}










void resize_image(struct type_of_image image, int64_t width, int64_t height)
{


    


    if ((width > 0) && (height > 0))
    {

        int64_t x, y, n;
        
        struct list_of_pixel p = NULL;
        
        y = 0;
        
        
        while (y height)
        {
        
            
        
            y += 1;
        
        }
        
        
    
    
    }
    else
    {
    
        printf("error width = %ld . height = %ld .\n", width, height);
    
    }


}















int main() {









 
    int width, height, channels;

    
            
    char i_cwd[PATH_MAX];
    
    bool semaphore = false;
    
    if (getcwd(i_cwd, sizeof(i_cwd)) != NULL)
    {
    
        semaphore = true;
    
    }
    
    

    
    strcat(i_cwd, "/");
    
    
    strcat(i_cwd, "image_0.png");
    
    
    
    
    



    unsigned char *img = stbi_load(i_cwd, &width, &height, &channels, 0);
    if (!img) {
        printf("fail in load-ing the image .\n");
        return 1;
    }

    printf("dimenssion-s of image : width = %d، height = %d، channels = %d\n", width, height, channels);




    struct type_of_image image_0;

    image_0.head = NULL;

    image_0.width = width;
    
    image_0.height = height;
    
    image_0.channels = channels;    
        
    
    
    // المرور على كل بكسل

    for (int y = 0; y < height; y++) {
        for (int x = 0; x < width; x++) {
            int i = (y * width + x) * channels;


            unsigned char r = img[i + 0];

            unsigned char g = (channels > 1) ? img[i + 1] : 0;
            
            unsigned char b = (channels > 2) ? img[i + 2] : 0;

            unsigned char a = (channels > 3) ? img[i + 3] : 255;



            add_element_list_of_pixel(&image_0.head, r, g, b, a, len_list_of_pixel(image_0.head));


            printf("pixel (%d, %d): R=%d, G=%d, B=%d, A=%d\n", x, y, r, g, b, a);


        }

    }

    stbi_image_free(img);

    
    
    printf("\n\n\n\n\n");

    print_image(image_0);





    return 0;
}








































