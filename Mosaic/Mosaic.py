from PIL import Image

log = print


def chang(image, i, j):
    if (i % 10 == 0) and (j % 10 == 0):
        for m in range(10):
            for n in range(10):
                temp = (i, j)

                position = (i + m, j + n)
                r, g, b, a = image.getpixel(temp)
                image.putpixel(position, (r, g, b, a))


# 马赛克算法
def masaike(image):
    log('img', image.width)
    log('img', image.height)
    mm = 8
    w = image.width - mm
    h = image.height - mm
    for i in range(1, w):
        for j in range(1, h):
            chang(image, i, j)
    # return image


def main():
    img = Image.open("xx.png")
    img = img.convert('RGBA')
    masaike(img)
    img.save('yy.png')


if __name__ == '__main__':
    main()
