"""
Урок 6. Объектно-ориентированное программирование
1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.
"""
print(1, end="---------------------------------\n")
import random


class TrafficLight(object):

    def __init__(self):
        self.__color: dict = {
            'current_step': None
            , 'current_timer': 99
            , 'colors': ['красный', 'желтый', 'зеленый']
            , 'timers': [7, 2, 1]
            , 'mode': 1
        }

    def running(self, color: str = None):
        tlc: dict = self._TrafficLight__color
        '''
        если цвет неверный
                выводим ошибку
        ещё не ходили
            текущий цвет не задан
                тогда начинаем с начала
            иначе:
                начинаем с заданног цвета
                если это последний цвет, то направляемся назад
            обновляем таймер
        цвет задан
            не планируется на него перейти
                возврат ошибки
            если планируется
                переход досрочно
                если это последний шаг
                    то направляемся назад
                если это первый шаг
                    то направляемся вперед
            обновляем таймер
        цвет не задан
            таймер истёк
                переходим к следующему цвету
                обновляем таймер
                если это последний шаг
                    то направляемся назад
                если это первый шаг
                    то направляемся вперед
            иначе
                тик таймера
        вывод
                
        '''
        if not (color is None) and color not in tlc['colors']:
            raise ValueError(f'Недопустимый цвет {color}')
        elif tlc['current_step'] is None:
            if color is None:
                tlc['current_step'] = 0
            else:
                tlc['current_step'] = tlc['colors'].index(color)
                if tlc['current_step'] == len(tlc['colors']) - 1:
                    tlc['mode'] = -1
            tlc['current_timer'] = tlc['timers'][tlc['current_step']]
        elif not (color is None):
            if tlc['colors'].index(color) != tlc['current_step'] + tlc['mode']:
                raise ValueError(f'''{color} не идёт за {tlc['colors'][tlc['current_step']]}''')
            else:
                tlc['current_step'] = tlc['colors'].index(color)
                if tlc['current_step'] == len(tlc['colors']) - 1:
                    tlc['mode'] = -1
                elif not tlc['current_step']:
                    tlc['mode'] = 1
            tlc['current_timer'] = tlc['timers'][tlc['colors'].index(color)]
        else:
            if tlc['current_timer'] == 0:
                tlc['current_step'] = tlc['current_step'] + tlc['mode']
                tlc['current_timer'] = tlc['timers'][tlc['current_step']]
                if tlc['current_step'] == len(tlc['colors']) - 1:
                    tlc['mode'] = -1
                elif not tlc['current_step']:
                    tlc['mode'] = 1
            else:
                tlc['current_timer'] -= 1
        print(tlc['colors'][tlc['current_step']], " : ", tlc['current_timer'])


tstl = ['красный', 'желтый', 'зеленый', 'белый']
tl = TrafficLight()
for i in range(32):
    # random light
    r = random.randint(0, 10)
    rl = None if r else tstl[random.randint(0, 3)]
    ##
    try:
        tl.running(rl)
    except ValueError as e:
        print(f">>переключение на {rl}\n>>>>", e)

"""
2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
толщиной в 1 см * число см толщины полотна. Проверить работу метода.
Например: 20м * 5000м * 25кг * 5см = 12500 т
"""
print(2, end="---------------------------------\n")


class Road(object):
    def __init__(self, length: int = 1, width: int = 1):
        self._length = length
        self._width = width

    def get_mass(self, weight: int = 1, depth: int = 1):
        s = " т"
        result = self._length * self._width * weight * depth
        if not result % 1000:
            result = str(result // 1000) + s
        return result


print(Road(20, 500).get_mass(25, 5))

"""
3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income). Проверить работу примера на реальных данных
(создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""
print(3, end="---------------------------------\n")


class Worker:

    def __init__(self, name: str = 'Name', surname: str = 'Surname', position: str = 'worker', wage: int = 1000,
                 bonus: int = 50):
        self.name: str = name
        self.surname: str = surname
        self.position: str = position
        self._income: dict = {'wage': int(wage), 'bonus': float(bonus / 100)}


class Position(Worker):

    def get_full_name(self) -> str:
        return f"{self.name} {self.surname}"

    def get_full_salary(self) -> int:
        return int(self._income['wage'] + (self._income['wage'] * self._income['bonus']))


p1 = Position('Ivanov', 'Ivan', 'worker', 50000, 35)
print(p1.get_full_name())
print(p1.get_full_salary())

"""
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""
print(4, end="---------------------------------\n")


class Car(object):

    def __init__(self, color: str = 'default', name: str = 'default', is_police: bool = False, speed: int = 0):
        self.speed: int = speed
        self.color: str = color
        self.name: str = name
        self.is_police: bool = bool(is_police)

    def go(self):
        print("go:", True if self.speed else False)
        return True if self.speed else False

    def stop(self):
        print(f"{self.name} stop.")
        return not self.go()

    def turn(self, s: str = '') -> str:
        if s in ('left', 'right', 'ahead'):
            print(f"{self.name} moving: {self.speed}")
            if self.speed < 0:
                return 'go back'
            if self.speed == 0:
                return 'stop'
            elif s == 'ahead':
                return 'go ahead'
            else:
                return f'turn {s}'
        else:
            raise ValueError('direction not in (left,right,ahead)')

    def show_speed(self) -> int:
        print(f"{self.name} speed: {self.speed}")
        return self.speed

    def show_name(self) -> str:
        print(f"{self.name}")
        return self.name

    def __speed_alert(self) -> None:
        try:
            if not (self.max_speed is None):
                speed = int(self.max_speed)
                if self.speed > int(self.max_speed):
                    print(f'{self.speed} overspeed!')
        except Exception:
            pass

    def speed_up(self, val: int = 10) -> int:
        self.speed += val
        self.__speed_alert()
        print(f"{self.name} speed: {self.speed}")
        return self.speed

    def speed_down(self, val: int = 10) -> int:
        self.speed -= val
        print(f"{self.name} speed: {self.speed}")
        return self.speed


class TownCar(Car):
    def __init__(self, color: str = 'red', name: str = None, is_police=False, speed=0, max_speed=40):
        super().__init__(color, name, speed)
        self.max_speed = max_speed


class SportCar(Car):
    pass


class WorkCar(Car):
    def __init__(self, color: str = 'red', name: str = None, is_police=False, speed=0, max_speed=60):
        super().__init__(color, name, speed)
        self.max_speed = max_speed


class PoliceCar(Car):
    pass


tc = TownCar(color='red', name='TownCar', is_police=False, speed=60)
sc = SportCar('blue', 'SportCar', False, 60)
wc = WorkCar('green', 'WorkCar', False, 20)
pc = PoliceCar(name='PoliceCar', is_police=True, speed=60)

tc.name
sc.name
wc.name
pc.name

tc.speed_up(60)
sc.speed_up(60)
wc.speed_down(60)
pc.speed_down(60)

tc.go()
sc.go()
wc.go()
pc.go()

tc.show_speed()
sc.show_name()

print(tc.turn('ahead'))
print(sc.turn('left'))
print(wc.turn('ahead'))
print(pc.turn('ahead'))

"""
5. Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод draw (отрисовка).
Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
В каждом из классов реализовать переопределение метода draw. Для каждого из классов методы должен выводить уникальное сообщение.
Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
"""
print(5, end="---------------------------------\n")
from abc import ABS, abstractmethod


class Stationary(ABS):
    def __init__(self, title: str = 'Stationary'):
        self.title = title

    @abstractmethod
    def draw(self):
        print('Запуск отрисовки.')


class Pen(Stationary):

    def draw(self):
        print(f'Запуск отрисовки1: {type(self).__name__}')


class Pencil(Stationary):

    def draw(self):
        print(f'Запуск отрисовки2: {type(self).__name__}')


class Handle(Stationary):

    def draw(self):
        print(f'Запуск отрисовки3: {type(self).__name__}')


pen = Pen()
pencil = Pencil()
handle = Handle()
pen.draw()
pencil.draw()
handle.draw()
