# 5. (МОДУЛЬ 2) создать модуль 2seq.py. Задание:
# Пользователь вводит любые цифры через запятую
# Сохранить цифры в список
# Получить новый список в котором будут только уникальные элементы исходного (уникальным считается символ, который встречается в исходном списке только 1 раз)
# Вывести новый список на экран
# Порядок цифр в новом списке не важен
# Пример работы: Введите элементы списка через запятую: 2,3,4,5,5,6,5,3,9
# Результат: 2, 4, 6, 9

lst = list(input('Введите любые цифры через запятую без пробела: '))
lst = lst[::2]
lst = [int(x) for x in lst]
lst = list(set(lst))
print('Список уникальных значений: ', lst)