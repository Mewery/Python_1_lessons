# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math

"""
class Triangle:

    def __init__(self, a_x, a_y, b_x, b_y, c_x, c_y):
        self.a_x = a_x
        self.a_y = a_y
        self.b_x = b_x
        self.b_y = b_y
        self.c_x = c_x
        self.c_y = c_y

    def side1_length(self):
        side1 = math.sqrt((self.b_y - self.a_y) ** 2 + (self.b_x - self.a_x) ** 2)
        return side1

    def side2_length(self):
        side2 = math.sqrt((self.c_y - self.b_y) ** 2 + (self.c_x - self.b_x) ** 2)
        return side2

    def side3_length(self):
        side3 = math.sqrt((self.a_y - self.c_y) ** 2 + (self.a_x - self.c_x) ** 2)
        return side3

    def perimeter(self):
        perimeter_of_the_figure = triangle.side1_length() \
        + triangle.side2_length() + triangle.side3_length()
        return perimeter_of_the_figure

    def area(self):
        p = triangle.perimeter() / 2
        figure_area = math.sqrt(p * (p - triangle.side1_length()) \
        * (p - triangle.side2_length()) * (p -
        triangle.side3_length()))
        return figure_area

    def height(self):
        triangle_height = (2 * triangle.area()) / triangle.side1_length()
        return triangle_height

triangle = Triangle(4, 2, 5, 9, 6, 1)
print("Площадь треугольника: ", triangle.area())
print("Высота треугольника: ", triangle.height())
print("Периметр треугольника: ", triangle.perimeter())

"""

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.

"""
class Trapezium:

    def __init__(self, p_1, p_2,p_3, p_4):
        self.p_1 = p_1
        self.p_2 = p_2
        self.p_3 = p_3
        self.p_4 = p_4

        self.length1 = (((self.p_2[0] - self.p_1[0])**2 + (self.p_2[1] - self.p_1[1])**2)** (1/2))
        self.length2 = (((self.p_3[0] - self.p_2[0])**2 + (self.p_3[1] - self.p_2[1])**2)** (1/2))
        self.length3 = (((self.p_3[0] - self.p_4[0])**2 + (self.p_3[1] - self.p_4[1])**2)** (1/2))
        self.length4 = (((self.p_1[0] - self.p_4[0])**2 + (self.p_1[1] - self.p_4[1])**2)** (1/2))

        self.diagonal1 = (((self.p_3[0] - self.p_1[0])**2 + (self.p_3[1] - self.p_1[1])**2)** (1/2))
        self.diagonal2 = (((self.p_4[0] - self.p_2[0])**2 + (self.p_4[1] - self.p_2[1])**2)** (1/2))

    def check_hips (self):
        if self.length1 == self.length3:
            if self.diagonal1 == self.diagonal2:
                res = "равнобедренная"
        else:
            res = "не равнобедренная"

    def perimeter(self):
        return self.length1 + self.length2 + self.length3 + self.length4

    def area(self):
        if self.length1 == self.length3 and self.length2 != self.length4:
            l = (abs(self.length2 - self.length4))/2
            h = math.sqrt ((self.length1**2) - l**2)
            return h*(self.length2 + self.length4)/2
        else:
            print ("не равнобедренная")

trap1 = Trapezium ([0,0],[1,4],[5,4],[6,0])
print (trap1.check_hips(), 'Периметр: ', trap1.perimeter(), 'Площадь:', trap1.area())
"""