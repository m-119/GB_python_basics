"""
Урок 5. Работа с файлами
1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
f = open("l5-1.txt", "a+", encoding='utf-8')
while True:
    inpt: str = f"{input('записать:')}\n"
    if not inpt.strip():
        print("---end---")
        break
    f.write(inpt)

f.close()

"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.
"""
line_cnt: int = 0
word_cnt: list = []
with open('l5-2.txt', 'r', encoding='utf-8') as f:
    for ln in f:
        line_cnt += 1
        word_cnt.append(len(ln.strip().split()))
    print({line_cnt: word_cnt})

"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
"""
from functools import partial
from statistics import mean


def salary_int(l: list):
    return [l[0], int(l[1])]


def salary_filter(l: list = None, sz: int = 20000):
    if l[1] >= sz:
        return True
    else:
        return False


empl: list = []

with open('l5-3.txt', 'r', encoding='utf-8') as f:
    for ln in f:
        # print(ln.strip())
        empl.append(ln.strip().split())
    empl = list(map(salary_int, empl))
    print(list(i[0] for i in filter(partial(salary_filter, sz=20000), empl)))
    print("средняя ЗП:", mean(list(i[1] for i in filter(partial(salary_filter, sz=20000), empl))))

"""
4. Создать (не программно) текстовый файл со следующим содержимым: One — 1 Two — 2 Three — 3 Four — 4 Необходимо 
написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные 
должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
"""
# from googletrans import Translator
# tr = Translator()
# with open('l5-4en.txt', 'r', encoding='utf-8') as f_en:
#     with open('l5-4ru.txt', 'a+', encoding='utf-8') as f_ru:
#         for ln in f_en:
#             result = tr.translate(ln, src='en', dest='ru')
#             # print(result.text)
#             f_ru.write(ln)

en_ru = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
    'Five': 'Пять'}

with open('l5-4en.txt', 'r', encoding='utf-8') as f_en:
    with open('l5-4ru.txt', 'w+', encoding='utf-8') as f_ru:
        for ln in f_en:
            for w in en_ru.keys():
                ln = ln.replace(w, en_ru[w])
            f_ru.write(ln)

"""f_ru.write
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

import random as rnd

cnt = rnd.randint(0, 100)
with open('l5-5.txt', 'w+', encoding='utf-8') as f:
    for i in range(cnt):
        f.write(str(rnd.randint(0, 100)))
        f.write(" ")

l_result = []
with open('l5-5.txt', 'r', encoding='utf-8') as f:
    for ln in f:
        l_result.extend(list(map(int, ln.split())))
print(l_result)
print(f"сумма цифр в l5-5.txt:", sum(l_result))

"""
6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий.
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:

Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —
Пример словаря:

{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
"""
import re

result = dict()
with open('l5-6.txt', 'r', encoding='utf-8') as f:
    for ln in f:
        result[re.search('^[^:]+', ln)[0].strip()] = sum(map(int, re.findall('\d+', ln)))
print(result)

"""7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: название, 
форма собственности, выручка, издержки. Пример строки файла: firm_1 ООО 10000 5000. Необходимо построчно прочитать 
файл, вычислить прибыль каждой компании, а также среднюю прибыль. Если фирма получила убытки, в расчет средней 
прибыли ее не включать. Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, 
а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков). 
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}]. Итоговый список 
сохранить в виде json-объекта в соответствующий файл. Пример json-объекта: 

[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста.
"""

from statistics import mean
import json


def norm(l: list) -> None:
    for i in range(len(l)):
        if l[i].strip().isdigit():
            l[i] = int(l[i].strip())
        else:
            l[i] = l[i].strip()
    return l


lst = []
result = []
with open('l5-7.txt', 'r', encoding='utf-8') as f:
    for ln in f:
        lst.append(norm(ln.strip().split()))
        pass
result.append({i[0]: i[2] - i[3] for i in lst})
result.append({'average_profit': mean(list(i[2] - i[3] for i in lst))})
print(result)
with open("l5-7.json", "w", encoding="utf-8") as f:
    json.dump(result, f)
