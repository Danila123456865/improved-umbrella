while True:
    numbers=int(input('Введите число'))
    numbers_1 = numbers // 100
    numbers_2 = numbers % 100 // 10
    numbers_3 = numbers % 10
    degree_1=numbers_1**3
    degree_2=numbers_2**3
    degree_3=numbers_3**3
    amount=degree_1+degree_2+degree_3
    if amount==numbers:
        print('это число армстронга')
    else:
        print('это не число армстронга')
