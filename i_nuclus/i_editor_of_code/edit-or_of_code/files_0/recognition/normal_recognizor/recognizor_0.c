













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





int main() {
 
    int width, height, channels;

    // تحميل الصورة


        
    
            
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

    // المرور على كل بكسل
    for (int y = 0; y < height; y++) {
        for (int x = 0; x < width; x++) {
            int i = (y * width + x) * channels;

            unsigned char r = img[i + 0];
            unsigned char g = (channels > 1) ? img[i + 1] : 0;
            unsigned char b = (channels > 2) ? img[i + 2] : 0;
            unsigned char a = (channels > 3) ? img[i + 3] : 255;

            printf("pixel (%d, %d): R=%d, G=%d, B=%d, A=%d\n", x, y, r, g, b, a);
        }
    }

    stbi_image_free(img);
    return 0;
}








































