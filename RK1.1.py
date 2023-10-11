import matplotlib.pyplot as plt
from PIL import Image, ImageDraw

def draw_line_bresenham(x0, y0, x1, y1, n=10):
    img = Image.new('RGB', (400, 400), color='white')
    draw = ImageDraw.Draw(img)
    
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    
    if x0 < x1:
        sx = 1
    else:
        sx = -1
    if y0 < y1:
        sy = 1
    else:
        sy = -1

    err = dx - dy
    count = 0
    
    while True:
        draw.point((x0, y0), fill='black')
        e2 = 2 * err
        if e2 >= -dy:
            if count < n:
                count += 1
                yield (x0, y0)
            if x0 == x1:
                break
            err -= dy
            x0 += sx
        if e2 <= dx:
            if count < n:
                count += 1
                yield (x0, y0)
            if y0 == y1:
                break
            err += dx
            y0 += sy

    plt.imshow(img)
    plt.show()

# ”казываем координаты начала и конца отрезка, а также количество точек (n)
x0, y0 = 50, 50
x1, y1 = 250, 250
n = 10

for point in draw_line_bresenham(x0, y0, x1, y1, n):
    print(point)
