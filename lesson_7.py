"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д.
"""
print(1, end="---------------------------------\n")
import numpy as np

pass


class Matrix:

    def __init__(self, mx):
        self.value = None
        ln = len(mx[0])
        for i in mx:
            if len(i) == ln:
                continue
            else:
                raise ValueError('Ошибка размерности')
        self.value = mx

    def __str__(self) -> str:
        result = ''
        for i in self.value:
            for j in i:
                result += f'{j:5}'
            result += '\n'
        return result

    def __add__(self, other) -> list:
        result = []
        if len(self.value) != len(other.value) and len(self.value[0]) != len(other.value[0]):
            raise ValueError('Ошибка размерности')
        for i in range(len(self.value)):
            row = []
            for j in range(len(self.value[i])):
                row.append(self.value[i][j] + other.value[i][j])
            result.append(row)
        return Matrix(result)


mx1 = Matrix([list(int(x) for x in row) for row in np.random.randint(0, 100, (5, 5))])
mx2 = Matrix([list(int(x) for x in row) for row in np.random.randint(0, 100, (5, 5))])

print(mx1, "-" * 30)
print(mx2, "-" * 30)
print(mx1 + mx2, "-" * 30)

"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто)
и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), 
для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: реализовать абстрактные
классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
print(2, end="---------------------------------\n")
from abc import ABC, abstractmethod


class Сlothes(ABC):
    def __init__(self, property):
        self.validate(property)

    def validate(self, property):
        if not (isinstance(property, float) or isinstance(property, int)):
            raise ValueError
        else:
            return property

    @abstractmethod
    def get_property(self):
        pass

    def __add__(self, other):
        return self.get_property + self.get_property


class Coat(Сlothes):
    def __init__(self, property):
        self._size = self.validate(property)
        print(f'Пальто(размер): {self._size}')

    @property
    def get_property(self):
        return round(self._size / 6.5 + 0.5, 2)


class Suit(Сlothes):
    def __init__(self, property):
        self._height = self.validate(property)
        print(f'Костюма(рост): {self._height}')

    @property
    def get_property(self):
        return round(2 * self._height + 0.3, 2)


my_coat = Coat(48)
my_suit = Suit(1.78)

print(f'Расход ткани (Пальто): {my_coat.get_property}')
print(f'Расход ткани (Костюм): {my_suit.get_property}')
print(f'Расход ткани (Общий): {my_coat + my_suit}')

"""
3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка.
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число).
В классе должны быть реализованы методы перегрузки арифметических операторов:
сложение (__add__()),
вычитание (__sub__()),
умножение (__mul__()),
деление (__truediv__()).
Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение
и обычное (не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться округление значения
до целого числа.
Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
Вычитание. Участвуют две клетки.
Операцию необходимо выполнять только если разность количества ячеек двух клеток больше нуля, 
иначе выводить соответствующее сообщение.
Умножение. Создается общая клетка из двух.
Число ячеек общей клетки определяется как произведение количества ячеек этих двух клеток.
Деление. Создается общая клетка из двух.
Число ячеек общей клетки определяется как целочисленное деление количества ячеек этих двух клеток.
В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. 
Данный метод позволяет организовать ячейки по рядам.
Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n**.
Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
Тогда метод make_order() вернет строку: *****\n*****\n*****.
Подсказка: подробный список операторов для перегрузки доступен по ссылке:
https://pythonworld.ru/osnovy/peregruzka-operatorov.html
"""
print(3, end="---------------------------------\n")
class Cell:

    @classmethod
    def make_order(self, cls, param: int = 0):
        if int(cls) < 0:
            raise ValueError("неправильная клетка")
        if param < 1:
            raise ValueError("неправильный параметр")
        return (('*' * param) + '\n') * (int(cls) // param) + '*' * (int(cls) % param)

    def __init__(self, amount:int):
        self.c_amount = None

        if int(amount)>0:
            self.c_amount: int = int(amount)
        else:
            raise ValueError ("параметр, соответствующий количеству клеток (целое положительное число)")

    def __int__(self):
        return self.c_amount

    def __str__(self):
        return str(self.c_amount)

    def __add__(self, other):
        return Cell(self.c_amount + other.c_amount)

    def __sub__(self, other):
        result = Cell(self.c_amount - other.c_amount)
        if int(result) > 0:
            return result
        else:
            raise ValueError ("Отрицательное значение")

    def __mul__(self, other):
        return Cell(self.c_amount * other.c_amount)

    def __truediv__(self, other):
        return Cell(self.c_amount // other.c_amount)


cell_1 = Cell(3)
print(cell_1)
cell_2 = Cell(5)
print(cell_2)
cell_1 += cell_2
print(cell_1)   # 3+5=8
cell_1 *= cell_2
print(cell_1)   # 8*5=40
cell_1 -= cell_2
print(cell_1)   # 40-5=35
cell_1 /= cell_2
print(cell_1)   # 35/5=7
print(Cell.make_order(cell_1,3))
