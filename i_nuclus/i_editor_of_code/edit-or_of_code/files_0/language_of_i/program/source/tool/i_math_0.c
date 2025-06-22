










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




#define length_of_the_result 1000





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




double time_()
{

    struct timeval u;

    if (gettimeofday(&u, NULL) == 0)
    {


        return u.tv_sec + (u.tv_usec / 1000000.0);


    }


}








int main()
{


    // enter the operation :

    char *operation = "1+1";

    char result[length_of_the_result];
    
    
    

    // calculate :

    calculator(operation, &result);
    
    
    
    
    
    // display the result :
    
    printf("\n\n\n result = %s .\n\n\n", result);
    
    
    return 0;

}


































