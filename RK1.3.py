import matplotlib.pyplot as plt
from PIL import Image, ImageDraw

def bresenham_line(x0, y0, x1, y1):
    points = []
    
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
    
    while True:
        points.append((x0, y0))
        
        if x0 == x1 and y0 == y1:
            break
        
        e2 = 2 * err
        if e2 >= -dy:
            err -= dy
            x0 += sx
        if e2 <= dx:
            err += dx
            y0 += sy

    return points

def draw_segments_with_intersection(x0, y0, x1, y1, x2, y2, x3, y3):
    img = Image.new('RGB', (400, 400), color='white')
    draw = ImageDraw.Draw(img)
    
    # Рисуем первый отрезок
    points1 = bresenham_line(x0, y0, x1, y1)
    for point in points1:
        draw.point(point, fill='black')
    
    # Рисуем второй отрезок
    points2 = bresenham_line(x2, y2, x3, y3)
    for point in points2:
        draw.point(point, fill='black')

    # Находим точку пересечения
    intersection = set(points1) & set(points2)
    
    if intersection:
        for point in intersection:
            draw.point(point, fill='red')
        print("Отрезки пересекаются в точке:", intersection)
    else:
        print("Отрезки не пересекаются.")
    
    plt.imshow(img)
    plt.show()

# Указываем координаты четырех точек, задающих два отрезка
x0, y0 = 100, 100
x1, y1 = 300, 100
x2, y2 = 200, 50
x3, y3 = 200, 200

draw_segments_with_intersection(x0, y0, x1, y1, x2, y2, x3, y3)

