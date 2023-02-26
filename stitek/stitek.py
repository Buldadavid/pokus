from PIL import Image,ImageFont, ImageDraw

img  = Image.open("/home/pidipi/POKUS/stitek/podklad.png")

draw = ImageDraw.Draw(img)

# use a bitmap font
font = ImageFont.load("/home/pidipi/POKUS/stitek/Roboto15.pil")

draw.text((10, 34), "3 ~ Motor 1FT6105-8AC71-1EH1", font=font,fill = (0,0,0))

draw.text((10, 55), "YF M123 1234 12 123   Z:X01 N05", font=font,fill = (0,0,0))
   


#img.show()
img.save("stitek.png")