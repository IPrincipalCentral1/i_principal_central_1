



















import os



os.system("pip install pillow")




from PIL import Image

import os





def create_image(path_of_file, width, height, color, flip, border):
    
    
    


    image = Image.new("RGBA", (width, height), color)


    y = 0
    
    while (y < height):
    
        x = 0
        
        while (x < width):
        
            
            if (x == y):
            
                if (border > 0):

                    image.putpixel((x, y), (255, 0, 0, color[3]))
        
            x += 1
    
        y += 1


    if (flip == True):
    
        image = image.transpose(Image.FLIP_LEFT_RIGHT)



    image.save(path_of_file)
        









file_of_image = os.path.join(os.getcwd(), "image_0.png")


create_image(path_of_file=file_of_image, width=10, height=10, color=(0, 255, 255, 255), flip=False, border=1)















