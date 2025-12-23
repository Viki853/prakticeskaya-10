print ('Введите последовательность чисел (0 - прекращение ввода данных): ')
max_num = 0

while True:
    num=int(input())
    if num == 0:
        break
    if num>max_num:
        max_num=num

if max_num == 0:
    print ('Не было введедено ни одного числа. ')
else:
    print(f'Максимальное из введеных чисел: {max_num}')