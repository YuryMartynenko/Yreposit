mas1 = [ [[1,2], [3,4]],
         [[1,2], [3,4]],
         [[1,2], [3,4]] ]

mas2 = [ [[1,2], [3,4]],
         [[1,2], [3,4]],
         [[1,2], [3,4]] ]

answer = False

if len(mas1) == len(mas2):
    for i in range(len(mas1)):
        for j in range(len(mas1[i])):
            for k in range(len(mas1[i][j])):
                if mas1[i][j][k] != mas2[i][j][k]:
                    answer = True
                    break
else:
    print('размер массивов разный')

if answer is False:
    print(f'значения массивов {mas1} и {mas2} одинаковы')
    
else:
    print('значения массивов разные')
    
         