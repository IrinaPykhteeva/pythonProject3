# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

a=1
d=2
print(a+d)

# запрос у пользователя нескольких чисел:
dig_1 = int(input('Введите целое число: '))
dig_2 = int(input('Введите целое число: '))
dig_3 = int(input('Введите целое число: '))

# запрос у пользователя нескольких строк:
str_1 = input('Введите строку: ')
str_2 = input('Введите строку: ')
str_3 = input('Введите строку: ')

# вывод сохраненных данных:
print("Вы ввели числа:", dig_1, dig_2, dig_3)
print("Вы ввели строки:", str_1, str_2, str_3)

# 2. Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате
# чч:мм:сс. Используйте форматирование строк.

time_sec = int(input('Введите число: '))
hours = time_sec//3600
hours_res = (hours) if hours > 10 else ('0' + str(hours))
minutes = (time_sec % 3600)//60
minutes_res = (minutes) if minutes > 10 else ('0' + str(minutes))
seconds = (time_sec % 3600) % 60
seconds_res = (seconds) if seconds > 10 else ('0' + str(seconds))
if hours > 24:
    print('Количество полученных часов превышает количество часов в сутка, скоректируйте ввод.')
else:
    print(f'Московское время: {hours_res}:{minutes_res}:{seconds_res}')

    n = input('Введите число: ')
    nn = int(n+n)
    nnn = int(n+n+n)
    n = int(n)
    result = n+nn+nnn
    print(result)

  # 4.Пользователь вводит целое положительное число.Найдите самую большую цифру в числе.

 number = int(input(''))

# 5. Запросите у пользователя значения выручки и издержек фирмы. Определите,
# с каким финансовым результатом работает фирма (прибыль — выручка больше
# издержек, или убыток — издержки больше выручки). Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

plus = int(input('Введите значение прибыли: '))

 minus = int(input('Введите значение издержек: '))
 people = int(input('Ввдите количество работников: '))
 if plus > minus:
    print('Выручка больше издержек')
    clear_plus = plus - minus
    rent = clear_plus/plus
    print('Рентабельность {} выручки {}: {:.2f}' .format('нашей','составила',rent))
    clear_for_person = float(clear_plus/people)
    print('Прибыль фирмы в расчете на одного сотрудника: %s'%clear_for_person)
    else:
    print('Фирма работает в убыток')
