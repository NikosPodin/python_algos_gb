"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""

from random import randint
print('Нужно угадать число в диапазоне от 1 до 100. У вас будет 10 попыток')

def riddle(numb, count=9):
    if count==0:
        print(f'ты НЕ_угадал! Верное число {numb}')
        return
    else:
        number = user_numb()
        if number==riddle_numb:
            print(f'Ты угадал! это цифра {numb}... поздравления!')
            return numb
        elif number>numb:
            print(f'Число {number} БОЛЬШЕ загаданного числа\nУ тебя осталось {count} попыток')
        else:
            print(f'Число {number} МЕНЬШЕ загаданного числа\nУ тебя осталось {count} попыток')
    return riddle(numb, count-1)

def user_numb():
    try:
        user_numb = int(input('Введите цисло: '))
    except ValueError:
        print('Нужно ввести число, а не цифру')
        user_numb = int(input('Введите цисло: '))
    return user_numb

riddle_numb= randint(1,10)

riddle(riddle_numb)
