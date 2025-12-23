start_balance = 1000
print('---Меню банкомата---:')
print()
print('1.   Посмотреть баланс')
print('2.   Снять 100 руб')
print('3.   Положить 100 руб')
print('4.   Выход')
print ()

while True:
    select = int(input('Выберите номер операцию(1-4): '))

    if select == 1:
        print()
        print('*' * 25)
        print (f'Текущий баланс: {start_balance}')
        print('*' * 25)
        print ()


    if select == 2:
        if start_balance >= 100:
            print ('')
            print('*' * 25)
            print ('Вы сняли 100 рублей со своего счета.')
            print('*' * 25)
            start_balance -= 100
            print(f'Ваш текущий баланс: {start_balance}')
            print('*' * 25)
            print('')
        else:
            print('')
            print ('Произошла ошибка. Действие не выполнено!')
            print('Недостаточно средств на счете')
            print('')
            print('*' * 25)
            print (f'Текущий баланс: {start_balance}')
            print('*' * 25)
            print('')

    if select == 3:
        print()
        print('*' * 25)
        print ('Вы положили 100 рублей на свой баланс')
        start_balance += 100
        print('*' * 25)
        print(f'Текущий баланс: {start_balance}')
        print('*' * 25)
        print()

    if select == 4:
        print ('- - - До свидания! - - -')
        break

    if select not in range(1, 5):
        print('')
        print('Выберие действие из указанных')
        print('')