# 1 - Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр. Учтите, что числа могут быть отрицательными
# Пример:
# 67.82 -> 23
# (-0.56) -> 11

def summa(number):
    return sum(map(int, number.replace('.','').replace('-','')))

number = input('Введите любое вещественное число: ')
print(f'Сумма цифр в этом числе равна {summa(number)}')
