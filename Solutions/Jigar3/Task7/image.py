from PIL import ImageFont, ImageDraw, Image


print("NOTE: Please place the image in the same folder as the one in which the script is running")
imName = raw_input("Input the name of the image along with its extension type\n")

im = Image.open(imName)
draw = ImageDraw.Draw(im)

text = raw_input("Enter the text to be added:\n")

print("Enter the co-ordinates of the text to be placed")
x = int(raw_input("X co-ordinate:\n"))
y = int(raw_input("Y co-ordinate:\n"))

fontName = raw_input("Enter the name of the font file which is to be used:\n")
fontSize = int(raw_input("Enter the size of font:\n"))

font = ImageFont.truetype(fontName, fontSize)
draw.text((x, y), text, font=font)

im.save('certificate.jpg')
