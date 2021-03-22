"""
Задание 3.

Для этой задачи:
1) придумайте 1-3 решения (желательно хотя бы два)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.


Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
"""


company = {
    'ПАО НЕФТЯНАЯ КОМПАНИЯ РОСНЕФТЬ': 155.8,
    'ПАО ГАЗПРОМ НЕФТЬ': 162.6,
    'ПАО ГОРНО-МЕТАЛЛУРГИЧЕСКАЯ КОМПАНИЯ НОРИЛЬСКИЙ НИКЕЛЬ': 300.1,
    'ПАО СЕВЕРСТАЛЬ': 114.9,
    'ПАО НОВОЛИПЕЦКИЙ МЕТАЛЛУРГИЧЕСКИЙ КОМБИНАТ': 61.1
}

def sort_1(list_input):  # вариант 1 : O(n)
    input_max = {}
    list_d = dict(list_input)
    for i in range(3):
        maximum = max(list_d.items(), key=lambda k_v: k_v[1])
        del list_d[maximum[0]]
        input_max[maximum[0]] = maximum[1]
    return input_max

print('\nвариант 1\n')
print(sort_1(company))



def sort_2(random_list): # вариант 2: O(n ^ 2)
    for i in range(len(random_list)):
        low_value = i
        for j in range(i + 1, len(random_list)):
            if random_list[j][1] > random_list[low_value][1]:
                low_value = j
        random_list[i], random_list[low_value] = random_list[low_value], random_list[i]
    return random_list[0:3]

print('\nвариант 2\n')

list_dict = list(company.items())
for i in sort_2(list_dict):

    print(i[0], ':', i[1], ' ')


print('\nвариант 3\n')

list_dict = list(company.items())  # Вариант 3: O(n log n)
list_dict.sort(key=lambda i: i[1], reverse=True)
for i in range(3):
    print(list_dict[i][0], ':', list_dict[i][1] )

#Быстрее вариант 1 : O(n) - проще и быстрее в данном примере (объёме).
#Вариант 2 и уступает O(n) на небольших объёмах и при увеличении вводимых данных уступает варианту 3
#Вариант 3 O(n log n) масштабируемый и при бОльших объёмах будет одинакого оперативно выдавать результат
