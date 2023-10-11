import matplotlib.pyplot as plt
from PIL import Image, ImageDraw

def draw_circle_bresenham(x0, y0, radius, n=7):
    img = Image.new('RGB', (400, 400), color='white')
    draw = ImageDraw.Draw(img)
    
    x = radius
    y = 0
    err = 0

    count = 0
    while x >= y:
        if count < n:
            count += 1
            draw.point((x0 + x, y0 + y), fill='black')
            if x != y:
                draw.point((x0 + y, y0 + x), fill='black')
                draw.point((x0 - y, y0 + x), fill='black')
                draw.point((x0 - x, y0 + y), fill='black')
                draw.point((x0 - x, y0 - y), fill='black')
                draw.point((x0 - y, y0 - x), fill='black')
                draw.point((x0 + y, y0 - x), fill='black')
                draw.point((x0 + x, y0 - y), fill='black')
        
        if err <= 0:
            y += 1
            err += 2*y + 1
        
        if err > 0:
            x -= 1
            err -= 2*x + 1

    plt.imshow(img)
    plt.show()

# ”казываем координаты центра окружности, радиус и количество точек (n)
x0, y0 = 200, 200
radius = 100
n = 7

draw_circle_bresenham(x0, y0, radius, n)
