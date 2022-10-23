from PIL import Image, ImageFont, ImageDraw
import os

def stitekf(firma,AKZ):

    my_image = Image.open("tisk-stitku/podklad.png")
    title_font = ImageFont.truetype("tisk-stitku/Roboto-Medium.ttf", 50)

    box = ((25, 25, 389, 177))
    font_size = 50
    size = None
    draw = ImageDraw.Draw(my_image)
    

    while (size is None or size[0] > box[2] - box[0] or size[1] > box[3] - box[1]) and font_size > 0:
        font = ImageFont.truetype("tisk-stitku/Roboto-Medium.ttf", font_size)
        size = font.getsize_multiline(firma)
        font_size -= 1
    draw.multiline_text((25,25), firma, "#000", font)
    draw.multiline_text((25,127), AKZ, "#000", ImageFont.truetype("tisk-stitku/Roboto-Medium.ttf", 50))

    width = my_image.size[0] 
    height = my_image.size[1] 
    for i in range(0,width):# process all pixels
        for j in range(0,height):
            data = my_image.getpixel((i,j))
            #print(data) #(255, 255, 255)
            if (data[0]>=150 and data[1]>=150 and data[2]>=150):
                my_image.putpixel((i,j),(255, 255, 255))
                
    for i in range(0,width):# process all pixels
        for j in range(0,height):
            data = my_image.getpixel((i,j))
            #print(data) #(255, 255, 255)
            if (data[0]<150 and data[1]<150 and data[2]<150):
                my_image.putpixel((i,j),(0, 0, 0))

    my_image.save("static/pillow_paste.png", quality=95)

    print("OK")
    os.system("lp -o media=1*2 /home/nic/WebAPP/static/pillow_paste.png")
    return()
