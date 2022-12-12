# Составьте алгоритм нахождения случайного числа без использования библиотеки random.
import datetime 

def get_rand():
    return datetime.datetime.now().microsecond%10
n = get_rand()
print(n)