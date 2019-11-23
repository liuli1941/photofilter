from PIL import Image


log = print

# 选择图片
# 计算图片的rgba的像素， 求平均值
# 把得出的像素平均值赋值给rgba
# def chang(image, i, j):
#     if(i % 10 == 0) and (j % 10 == 0):
#         for m in range(10):
#             for n in range(10):
#                 temp = (i, j)
#                 position = (i + m, j + n)
#                 r, g, b, a = image.getpixel(temp)
#                 image.putpixel(position, (r, g, b, a))


# 浮雕算法
def fudiao(image):
    log('img', image.width)
    log('img', image.height)
    # mm = 8
    w = image.width
    h = image.height
    for i in range(w - 1):
        for j in range(h - 1):
            position1 = (i, j)
            position2 = (i + 1, j + 1)
            r1, g1, b1, a1 = image.getpixel(position1)
            r2, g2, b2, a2 = image.getpixel(position2)
            r = abs(r1 - r2 + 128)
            g = abs(g1 - g2 + 128)
            b = abs(b1 - b2 + 128)
            if r > 255:
                r = 255
            if r < 0:
                r = 0
            if g > 255:
                g = 255
            if g < 0:
                g = 0
            if b > 255:
                b = 255
            if b < 0:
                b = 0
            image.putpixel(position1, (r, g, b, a1))


def main():
    # 打开图像文件
    img = Image.open("xx.jpg")
    # 注意由于不是每个图像都有 a 所以这里强制转换成 RGBA 格式
    img = img.convert('RGBA')

    fudiao(img)

    # 保存图像文件
    img.save('yy.png')


if __name__ == '__main__':
    main()
