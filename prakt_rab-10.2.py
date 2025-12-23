num1 = int(input("Введите первое число: "))
while True:
    num2 = int(input("Введите второе число: "))
    if num2 > num1:
     break
    print("Ошибка")

while True:
    num3 = int(input("Введите третье число: "))
    if num3 > num2:
        break
    print("Ошибка")

print("Последовательность принята")