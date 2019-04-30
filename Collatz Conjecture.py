def Collatz(decimal):
    i = 0
    if decimal < 0:
        return 'введите положительое число'
    else:
        while decimal > 1:
            i += 1
            if decimal % 2 == 0:
                decimal /= 2
            elif decimal % 2 != 0:
                decimal = (decimal * 3) + 1
        return decimal
            
            
in_decimal = 12
result = Collatz(in_decimal)
print(result)

