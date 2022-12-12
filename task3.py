# Дан массив размера N. После каждого отрицательного элемента массива 
# вставьте элемент с нулевым значением.
# пусть N = 4, тогда [28, -46, 14, -14] => [28, -46, 0, 14, -14, 0]

# array = list(input ('введите массив:'))
# for i in array:
#    if array[i]<0:
#         array.insert(i+1, 0)
# print(array)

arr=list(map(int,input("Вводи список, разделяя числа пробелом ").split()))
i=0
while i < len(arr):
        if arr[i]<0:
         arr.insert(i+1,0)
        print(arr[i], end=' ')
        i+=1