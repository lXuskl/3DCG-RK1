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

def find_normal_vector(x0, y0, x1, y1):
    # Найдем вектор отрезка
    vector = (x1 - x0, y1 - y0)
    
    # Найдем вектор нормали, повернутый на 90 градусов
    normal_vector = (-vector[1], vector[0])
    
    return normal_vector

def draw_line_with_normal(x0, y0, x1, y1):
    img = Image.new('RGB', (400, 400), color='white')
    draw = ImageDraw.Draw(img)
    
    # Рисуем отрезок
    points = bresenham_line(x0, y0, x1, y1)
    for point in points:
        draw.point(point, fill='black')
    
    # Находим и рисуем вектор нормали
    normal_vector = find_normal_vector(x0, y0, x1, y1)
    x2, y2 = x0 + normal_vector[0], y0 + normal_vector[1]
    draw.line([(x0, y0), (x2, y2)], fill='red', width=2)

    plt.imshow(img)
    plt.show()

# Указываем координаты двух точек, задающих отрезок
x0, y0 = 100, 100
x1, y1 = 300, 200

draw_line_with_normal(x0, y0, x1, y1)

