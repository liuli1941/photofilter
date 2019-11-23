from PIL import Image
import math


log = print


# 剪裁
def crop(image, frame):
    x = frame[0]
    y = frame[1]
    w = frame[2]
    h = frame[3]
    new_image = Image.new('RGBA', (w, h))
    for i in range(x, w + x):
        for j in range(y, h + y):

            position_get = (i, j)
            log(image.getpixel(position_get))
            r, g, b = image.getpixel(position_get)

            position_put = (i - x, j - y)
            new_image.putpixel(position_put, (r, g, b, 255))
    # new_image.save('剪裁.png')
    return new_image


def pixel(image):
    # 这个数值是指， 取 s * s 个像素做一个色块， 可取任意值
    # 每 s * s 个像素组成一个色块
    s = 15
    # 这是每一个色块的中心点
    cx = math.floor(s / 2)
    cy = math.floor(s / 2)
    # 整个图片的宽高
    w = image.width
    h = image.height
    # 这是用图片的宽高， 对 s 除余
    # 如果除余不等于0， 就减去除余的余数
    # 此意为自动处理超出边界的问题， 但方法是不好的——有一些像素行列被粗暴减去了
    # 初始化 n ， 预防图片刚好除余为0， n 不被赋值的情况
    n = 0
    if w % s != 0:
        n = w % s
        image = crop(image, (0, 0, w - n, h))
        w = w - n
    if h % s != 0:
        n = h % s
        image = crop(image, (0, 0, w, h - n))
    # 更新宽高数据
    w = image.width
    h = image.height
    for i in range(w):
        for j in range(h):
            # 判定每一个色块的左上角起点
            if i % s == 0 and j % s == 0:
                # 初始化3个放入最终结果的变量
                R = 0
                G = 0
                B = 0
                # 开始处理每一个色块
                for m in range(s):
                    for n in range(s):
                        # temp是定位， 本色块像素在全图中的坐标
                        temp = (i + m, j + n)
                        r, g, b, a = image.getpixel(temp)
                        R += r
                        G += g
                        B += b
                # 一共加了 s * s 个值， 要取平均数， 除以 s * s
                r = int(R / s / s)
                g = int(G / s / s)
                b = int(B / s / s)
                for p in range(s):
                    for q in range(s):
                        # 这里很乱对不起
                        # abs(((cx - p) ** 2 + (cy - q) ** 2) ** 0.5)
                        # 这是勾股定理，求每一个像素点距离色块中心的距离
                        # 如果此距离短于此色块的边长一半， 则填上面所求的rgb
                        # 如果此距离长于此色块的边长一半， 则填黑色
                        if abs(((cx - p) ** 2 + (cy - q) ** 2) ** 0.5) < int(s / 2):
                            position = (i + p, j + q)
                            image.putpixel(position, (r, g, b, a))
                        else:
                            position = (i + p, j + q)
                            image.putpixel(position, (0, 0, 0, 251))
    return image


def main():
    img = Image.open('xx.png')
    i = pixel(img)
    i.save('yy.png')


if __name__ == '__main__':
    main()