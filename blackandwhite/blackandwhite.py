from PIL import Image

log = print


def grayscale(image):
    # Gray =（R + G + B） / 3
    log('img', image.width)
    log('img', image.height)
    for x in range(image.width):
        for y in range(image.height):
            position = (x, y)
            r, g, b, a = image.getpixel(position)
            gray = int((r + g + b) / 3)
            image.putpixel(position, (gray, gray, gray, a))


def main():
    # 打开图像文件
    img = Image.open("xx.png")
    # 注意由于不是每个图像都有 a 所以这里强制转换成 RGBA 格式
    img = img.convert('RGBA')

    # # 读取座标 (1, 2) 处的像素点的像素值
    # position = (1, 2)
    # r, g, b, a = img.getpixel(position)
    # log('get pixel', r, g, b, a)
    #
    # # 把座标 position 的像素值改写为 白色（全发光就是白色，0 0 0 0 是黑色）
    # img.putpixel(position, (255, 255, 255, 255))

    grayscale(img)

    # 保存图像文件
    img.save('yy.png')


if __name__ == '__main__':
    main()
