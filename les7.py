# Практическое задание
# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
#
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.
#
# import random
#
# my_list = []
# my_matrix2= []
#
# matrix_size = [random.randint(2,5), random.randint(2,5)]
# print(matrix_size)
#
# def matrix_generation(size):
#     my_temp_list = []
#     for el in range(size[0]):
#         temp_list = []
#         for el in range(size[1]):
#             temp_list.append(random.randint(1, 25))
#         my_temp_list.append(temp_list)
#     return my_temp_list
#
# my_list = matrix_generation(matrix_size)
# my_matrix2 = matrix_generation(matrix_size)
#
# class Matrix():
#     def __init__(self, matr_list=None):
#         self.matrix = matr_list
#         self.size = [len(matr_list),len(matr_list[0])]
#
#     def __str__(self):
#         super.__str__(self)
#         temp_list = []
#         max_lengt = 0
#         for el in range(len(self.matrix)):
#             for el2 in self.matrix[el]:
#                 if max_lengt<=len(str(el2)): max_lengt = len(str(el2))
#         for el in range(len(self.matrix)):
#             temp = ""
#             str_space = ""
#             for el2 in self.matrix[el]:
#                 if len(str(el2))<max_lengt: str_space = " "
#                 else: str_space =""
#                 temp += str_space + str(el2) + " "
#             temp += " \n"
#             temp_list.append(''.join(temp))
#         return ''.join(temp_list)4
#
#     def __add__(self, other):
#         if self.size == other.size:
#             for el in range(self.size[0]):
#                 temp_list =list(self.matrix[el])
#                 temp_list2=list(other.matrix[el])
#                 for el2 in range(len(temp_list)):
#                     temp_list[el2] += temp_list2[el2]
#                 self.matrix[el] = temp_list
#         else:
#             print('Матрицы разного размеры, нельзя складывать!')
#         return self
#
# my_matrix = Matrix(my_list)
# my_matrix2 = Matrix(my_matrix2)
# print(my_matrix)
# print(my_matrix2)
# print(my_matrix + my_matrix2)
#
#

# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
# проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные
# числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
#
# from abc import ABC, abstractmethod
# class Clothes:
#     def __init__(self, clothes_title):
#         self.clothes_type = ""
#         self.clothes_title = clothes_title
#         self.coat_size = 0
#         self.suit_height = 0
#         self.material_quantity = 0
#
#
#     def material_consumption(self):
#         pass
#         # if self.clothes_type == "Coat":
#         #     return (self.coat_size/6.5 + 0.5)
#         # else:
#         #     return
#
# class Coat(Clothes):
#     def __init__(self, coat_title, coat_size):
#         Clothes.__init__(self, coat_title)
#         self.coat_size = coat_size
#         self.clothes_type = "Coat"
#     def material_consumption(self):
#         self.material_quantity = (self.coat_size / 6.5 + 0.5)
#         return self.material_quantity
#
# class Suit(Clothes):
#     def __init__(self, suit_title,suit_height):
#         Clothes.__init__(self, suit_title)
#         self.suit_height = suit_height
#         self.clothes_type = "Suit"
#
#     def material_consumption(self):
#        return (2*self.suit_height + 0.3)
#
#
# my_first_coat = Coat("Размер L",56)
# my_first_suit = Suit("Рост 176", 176)
#
# print(f"Тип изделия {my_first_coat.clothes_type}, размер - {my_first_coat.coat_size}, название - {my_first_coat.clothes_title}, "
#       f"необходимо материала - {my_first_coat.material_consumption()}")
#
# print(f"Тип изделия {my_first_suit.clothes_type}, размер - {my_first_suit.suit_height}, название - {my_first_suit.clothes_title}, "
#       f"необходимо материала - {my_first_suit.material_consumption()}")
#

# Реализовать программу работы с органическими клетками, состоящими из ячеек. Необходимо создать класс Клетка.
# В его конструкторе инициализировать параметр, соответствующий количеству ячеек клетки (целое число).
# В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()),
# умножение (__mul__()), деление (__truediv__()). Данные методы должны применяться только к клеткам и выполнять увеличение,
# уменьшение, умножение и целочисленное (с округлением до целого) деление клеток, соответственно.

# больше нуля, иначе выводить соответствующее сообщение.

## В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
# *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n*****.
# Подсказка: подробный список операторов для перегрузки доступен по ссылке.

class OrganicCell:
    def __init__(self, cell_count):
        self.cell_count = cell_count
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
    def __add__(self, other):
        if type(other)== type(self):
           self.cell_count+=other.cell_count
           print("Сложение клеток!")
        return self.cell_count
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток
    def __sub__(self, other):
        if (type(other) == type(self)) and ((self.cell_count - other.cell_count) >0 ):
            self.cell_count -= other.cell_count
        else: print("В исходной клетке недостаточно ячеек!")
        return self.cell_count
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества
# ячеек этих двух клеток.
    def __mul__(self, other):
       if type(other) == type(self):
            self.cell_count *= other.cell_count
            print("Сложение клеток!")
       return self.cell_count
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление
# количества ячеек этих двух клеток.
    def __truediv__(self, other):
       if type(other) == type(self):
            self.cell_count //= other.cell_count
            print("Деление клеток!")
       return self.cell_count
    def make_order(self,row_cells_cout):
        rows_quantity = self.cell_count // row_cells_cout
        rows_temp = self.cell_count % row_cells_cout
        row_str =""
        for el in range(row_cells_cout): row_str+="*"
        for el in range(rows_quantity):
            print(row_str)
        for el in range(rows_temp):
            print("*", end="")
first_organic_cell = OrganicCell(10)
second_organic_cell = OrganicCell(5)
num = 10
с = OrganicCell(10)
print(type(first_organic_cell))
c = OrganicCell(first_organic_cell + second_organic_cell)
print(OrganicCell(first_organic_cell + second_organic_cell).cell_count)
c.make_order(4)
