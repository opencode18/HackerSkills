from PIL import Image, ImageFont, ImageDraw


with open('names.txt', 'r') as fl:
    for name in fl:
        x_cd, y_cd = map(int, input().split())
        img = Image.open('certificate.jpg')
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype('Acme-Regular.ttf', 30)
        draw.text((x_cd, y_cd), name, (24, 72, 136), font = font)
        img.save('output_certificate_' + name + '.jpg')