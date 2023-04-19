from PIL import Image

data = []
txt = ""

for i in range(135):
	#print(i)
	for y in range(81):
		#print(y)


		im = Image.open("8.png")
		px = im.load()
		#print(px[y,i])
		pixel = px[y,i]
		
		if str(pixel) == "(0, 0, 0, 255)" or pixel == "(1, 0, 0, 255)" or pixel == "(0, 0, 2, 255)":
			dat = "00"
			data.append(dat)
			txt = txt + dat
			#print("cerna")
		else:
			dat = "7F"
			data.append(dat)
			txt = txt + dat
			
#print(data)
print(txt)			


