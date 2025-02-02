"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321
"""


def rev(number,inven=0):
    return inven if (number==0) else rev(number//10, inven*10 + number % 10)
try:
    user_numb = int(input('Введите число: '))
except ValueError:
    print('Вы ввели буквы, а нужно ввести цифры')
    user_numb = int(input('Введите число: '))
print(f'В обратном порядке число получаются: {rev(user_numb)}')
