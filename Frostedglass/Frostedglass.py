from PIL import Image
import random

log = print


# 选择图片
def randindex():
    index = int(random.random() * 8)
    return index


# 毛玻璃算法
def maoboli(image):
    log('img', image.width)
    log('img', image.height)
    mm = 8
    w = image.width - mm
    h = image.height - mm
    for x in range(1, w):
        for y in range(1, h):
            index = randindex()
            position = (x, y)
            temp = (abs(x + index), abs(y - index))
            log('temp', temp)
            r, g, b, a = image.getpixel(temp)
            log('r, g, b, a', r, g, b, a)
            # gray = int((r + g + b) / 3)
            image.putpixel(position, (r, g, b, a))
    # return image


def main():
    # 打开图像文件
    img = Image.open("xx.png")
    # 注意由于不是每个图像都有 a 所以这里强制转换成 RGBA 格式
    img = img.convert('RGBA')

    maoboli(img)

    # 保存图像文件
    img.save('yy.png')


if __name__ == '__main__':
    main()
