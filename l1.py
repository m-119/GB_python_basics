"""
Урок 1. Знакомство с Python
1. Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и сохраните в переменные, выведите на экран.
"""
a, b, c = None, 1, "Три"
print(f"a=\"{a}\", b=\"{b}\", c=\"{c}\"")

a = input("Введите a:")
b = input("Введите b:")
c = input("Введите c:")

print(f"a=\"{a}\", b=\"{b}\", c=\"{c}\"")

"""
2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
"""
t = int(input("Введите секунды:"))
print(f"{int(t / 3600) if t / 3600 < 99 else 99}:{int(t / 60 % 60)}:{int(t % 60)}")

"""
3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""
a = input("Введите число:")
print(int(a) + int(a * 2) + int(a * 3))

"""
4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе. Для решения используйте цикл while и арифметические операции.
"""
intstr = input("Введите целое положительное число:")
indx = 0
reslt = None
if indx == 0 and len(intstr):
    reslt = int(intstr[0])
while indx < len(intstr):
    if int(intstr[indx]) > reslt:
        reslt = int(intstr[indx])
    indx += 1

print(reslt)

"""
5. Запросите у пользователя значения выручки и издержек фирмы. Определите, с каким финансовым результатом работает фирма (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.
"""
a = int(input("Выручка:"))
b = int(input("Издержки:"))
reslt = int(a - b);
reslt
if reslt:
    if reslt > 0:
        print(f"прибыль: {reslt}")
        reslt = int(reslt / int(input("Число сотрудников:")))
        print(f"прибыль на одного сотрудника:{reslt}")
    else:
        print(f"убыток: {abs(reslt)}")
else:
    print("-")

"""
6. Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров. Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров. Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.
Например: a = 2, b = 3.
Результат:

1-й день: 2
2-й день: 2,2
3-й день: 2,42
4-й день: 2,66
5-й день: 2,93
6-й день: 3,22
Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.
"""
a: int = int(input("В первый день его результат составил (километров):"))
b: int = int(input("Результат спортсмена составить не менее (километров):"))
day: int = 1
up: int = 1.1


def prnt() -> None:
    print(f"{day}-й день: {str('%.2f' % a).replace('.', ',')}")


prnt()
while a <= b:
    day += 1
    a *= up
    prnt()
print(f"Ответ: на {day}-й день спортсмен достиг результата — не менее {b} км.")

