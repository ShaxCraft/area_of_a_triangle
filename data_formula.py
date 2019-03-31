# Формулы для расчета площади треугольников
# Formula for calculating the area of triangles
from triangle import *


# Расчет площади треугольника и полу-периметра
# Calculate the area of a triangle and the semi-perimeter
def area_tringle():
    s = float((A + B + C)) / 2  # полуперимерт треугольника
    area = (s * (s - A) * (s - B) * (s - C)) ** 0.5  # площадь треугольника
    return area
