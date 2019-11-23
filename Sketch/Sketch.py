from PIL import Image, ImageFilter

# 将彩色图转换成灰度图；
def quse(img):
    w = img.width
    h = img.height
    image = Image.new('RGBA', (w, h))

    for i in range(w):
        for j in range(1, h):
            position = (i, j)
            r, g, b, a = img.getpixel(position)
            rgb = (r * 30 + g * 59 + b * 11) / 100
            rgb = int(rgb)
            image.putpixel(position, (rgb, rgb, rgb, a))
    return image


# 对灰度图进行反色操作，
def fanxiang(img):
    w = img.width
    h = img.height
    # image此刻为灰度图
    image = quse(img)
    for i in range(1, w):
        for j in range(1, h):
            position = (i, j)
            r, g, b, a = image.getpixel(position)
            # 对image各通道进行反色操作，
            r = 255 - r
            g = 255 - g
            b = 255 - b

            image.putpixel(position, (r, g, b, a))
    return image


# 高斯模糊
def gaosi(img):
    image = fanxiang(img)
    gaoimg = image.filter(ImageFilter.GaussianBlur(radius=2))
    return gaoimg


# 4. color dodge
# C =MIN( A +（A×B）/（255-B）,255)，
def sumiao(img):
    w = img.width
    h = img.height
    image = Image.new('RGBA', (w, h))
    im = quse(img)
    gao = gaosi(img)

    for i in range(w):
        for j in range(h):
            position = (i, j)
            r, g, b, a = im.getpixel(position)
            x, y, z, o = gao.getpixel(position)
            #  A +（A×B）/（255-B），
            #  A +（A×B）/（255-B）暂记作 temp
            # 其中 255-B 如果为0，需要特殊考虑
            if (255 - x) == 0:
                r1 = r
            else:
                r1 = r + (r * x) / (255 - x)

            if (255 - y) == 0:
                g1 = g
            else:
                g1 = g + (g * y) / (255 - y)

            if (255 - z) == 0:
                b1 = b
            else:
                b1 = b + (b * z) / (255 - z)
            # min(temp, 255)
            sr = int(min(r1, 255))
            sg = int(min(g1, 255))
            sb = int(min(b1, 255))

            image.putpixel(position, (sr, sg, sb, a))
    return image


def main():
    img = Image.open('xx.png')
    img = img.convert('RGBA')

    i = sumiao(img)
    i.save('yy.png')


if __name__ == '__main__':
    main()
