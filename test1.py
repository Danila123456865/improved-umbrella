while True:
    numbers=int(input('Введите число'))
    t=len(str(numbers))
    if t==1:
        print('еденицы всегда число армстронга')
    if t ==2:
        print('десятки немогут быть числом армстронга')
    if t==3:
        number_1 = numbers // 100
        number_2 = numbers % 100 // 10
        number_3 = numbers % 10
        degree_1=number_1**3
        degree_2=number_2**3
        degree_3=number_3**3
        amount1=degree_1+degree_2+degree_3
        if amount1==numbers:
            print('это число армстронга')
        else:
            print('это не число армстронга')
