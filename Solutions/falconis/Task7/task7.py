from PIL import Image, ImageFont, ImageDraw


x = int(input("Enter x-coordinate:"))
y = int(input("Enter y-coordinate:"))

f = open("names.txt", "r")
i = 1
for name in f:
    image = Image.open('certi.jpg')
    img_draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("font.ttf", 60)
    img_draw.text((x, y), name.strip(), fill='black', font=font)
    image.save('certi' + str(i) + '.jpg')
    i += 1

