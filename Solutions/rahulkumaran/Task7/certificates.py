import os
from PIL import ImageFont, ImageDraw, Image

fileName = raw_input("Enter name of the file from which you want to read the names of participants: ")
imgName = raw_input("Enter the name of image that you want to use as your template along with extension: ")

coOrdinates = raw_input("Enter the x and y co-ordinates of the text to be placed by separating them with a space like \"500 500\"")
coOrdinates_List = coOrdinates.split(" ")
x = int(coOrdinates_List[0])
y = int(coOrdinates_List[1])


with open(filename) as f:
    for line in f:
        name = line.rstrip()


        img = Image.open(imgName)
        draw = ImageDraw.Draw(img)

        font = font = ImageFont.truetype("a.ttf", 60)
        draw.text((x, y), name, font=font)

        img.save(name + '.jpg')

	if not os.path.exists( 'certificates' ) :
            os.makedirs( 'certificates' )

        img.save( 'certificates\\'+ name +'.pdf', "PDF", resolution=100.0)

