from PIL import ImageFont, ImageDraw, Image


print("NOTE: Please place the image in the same folder as the one in which the script is running")
print("NOTE: Name the text file to be read as names.txt")

imName = raw_input("Input the name of the image along with its extension type\n")

print("Enter the co-ordinates of the text to be placed")
x = int(raw_input("X co-ordinate:\n"))
y = int(raw_input("Y co-ordinate:\n"))

fontName = raw_input("Enter the name of the font file which is to be used:\n")
fontSize = int(raw_input("Enter the size of font:\n"))

with open("names.txt") as f:
    for line in f:
        text = line.rstrip()


        im = Image.open(imName)
        draw = ImageDraw.Draw(im)

        font = ImageFont.truetype(fontName, fontSize)
        draw.text((x, y), text, font=font)

        im.save(text + '.jpg')
        print("Finished with " + text + ".jpg")
