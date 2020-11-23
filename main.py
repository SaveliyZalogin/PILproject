from PIL import Image, ImageDraw

a = int(input())
image = Image.open('image.png')
draw = ImageDraw.Draw(image)
width = image.size[0]
height = image.size[1]
pix = image.load()
image.convert("RGBA")
datas = image.getdata()


def gray():
    for x in range(width):
        for y in range(height):
            r = pix[x, y][0]
            g = pix[x, y][1]
            b = pix[x, y][2]
            sr = (r + g + b) // 3
            draw.point((x, y), (sr, sr, sr))
    image.save("result.jpg", "JPEG")


def inverse():
    for x in range(width):
        for y in range(height):
            r = pix[x, y][0]
            g = pix[x, y][1]
            b = pix[x, y][2]
            draw.point((x, y), (255 - r, 255 - g, 255 - b))
    image.save("result.jpg", "JPEG")


def svetlee():
    for x in range(width):
        for y in range(height):
            r = pix[x, y][0]
            g = pix[x, y][1]
            b = pix[x, y][2]
            draw.point((x, y), (r + 20, g + 20, b + 20))
    image.save("result.jpg", "JPEG")


def krasnee():
    for x in range(width):
        for y in range(height):
            r = pix[x, y][0]
            g = pix[x, y][1]
            b = pix[x, y][2]
            draw.point((x, y), (255, g, b))
    image.save("result.jpg", "JPEG")


def to_png():
    # for x in range(width):
    #     for y in range(height):
    #         r = pix[x, y][0]
    #         g = pix[x, y][1]
    #         b = pix[x, y][2]
    #         if r == 255 and g == 255 and b == 255:
    #             draw.point((x, y), (255, 255, 255, 0))
    # image.save("result.png", "PNG")
    newData = []
    for item in datas:
        if item[0] == 255 and item[1] == 255 and item[2] == 255:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    image.putdata(newData)
    image.save("img2.png", "PNG")


def wtf():
    counter = 0
    for x in range(width):
        for y in range(height):
            if counter >= 255:
                counter = 0
            r = pix[x, y][0]
            g = pix[x, y][1]
            b = pix[x, y][2]
            draw.point((x, y), (r + counter, g, b))
            counter += 1
    image.save("result.jpg", "JPEG")


def geniously_thing():
    counter = 0  # отсчитывает 9 итераций по x чтобы поменять color в нужный момент
    counter2 = 1  # определяет координату x, из которой нужно взять цвет для следующего квадрата
    counter3 = 1  # определяет координату y, из которой нужно взять цвет и начать следующий ряд
    color = None  # определяет цвет в формате (r, g, b)
    pixelization_scale = 0
    if width < 500 and height < 500:
        if width > height:
            pixelization_scale = width // 100
        else:
            pixelization_scale = height // 100
    elif 500 < width < 1000 and 500 < height < 1000:
        if width > height:
            pixelization_scale = width // 250
        else:
            pixelization_scale = height // 250
    elif 1000 < width and 1000 < height:
        if width > height:
            pixelization_scale = width // 370
        else:
            pixelization_scale = height // 370
    for y in range(height):
        for x in range(width):
            print(counter, counter2, counter3, sep=' ')
            if counter < pixelization_scale:  # определяем цвет на ближайший квадрат
                r = pix[x - (x - counter2), y - (y - counter3)][0]
                g = pix[x - (x - counter2), y - (y - counter3)][1]
                b = pix[x - (x - counter2), y - (y - counter3)][2]
                color = (r, g, b)
            else:  # если квадрат кончился, то меняем значения переменных
                counter2 += pixelization_scale
                counter = 0
                if counter2 >= width:  # на случай, если мы хотим взять цвет из несуществующего пикселя
                    counter2 = (counter2 - pixelization_scale) + (width - (counter2 - pixelization_scale)) - 1
            for p in range(y - (y - counter3), (y - (y - counter3)) + pixelization_scale):  # рисуем линию 9px вниз
                draw.point((x, p), color)
            counter += 1  # засчитываем линию квадрата
        counter3 += pixelization_scale  # переключаемся на следующий ряд
        counter2 = 0  # в начало ряда
        if counter3 >= height:  # на случай, если мы хотим взять цвет из несуществующего пикселя
            counter3 = (counter3 - pixelization_scale) + (height - (counter3 - pixelization_scale)) - 1
    try:
        image.save("result.jpg", "JPEG")  # сохраняем результат :)
    except:
        image.save("result.png", "PNG")  # сохраняем результат :)


def main():
    if a == 1:
        gray()
    elif a == 2:
        inverse()
    elif a == 3:
        svetlee()
    elif a == 4:
        krasnee()
    elif a == 5:
        to_png()
    elif a == 6:
        wtf()
    elif a == 7:
        geniously_thing()
    elif a == 8:
        print(11 // 3)

main()
