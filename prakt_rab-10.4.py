total = 0
print(("0 - прекращение ввода данных"))
while True:
    price = int(input("Введите цену товара: "))

    if price == 0:
        break

    if price < 0:
        print("Ошибка цены")
        continue

    total += price  # Суммируем положительные цены

if total > 1000:
    total = total * 0.9  # Скидка 10%
    print("Применена скидка 10%")

print(f"Итоговая сумма к оплате: {total:.2f} руб.")