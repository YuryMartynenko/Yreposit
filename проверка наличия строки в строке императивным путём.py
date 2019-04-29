s1 = 'aaa111bbb'
s2 = '111'
answer = False

for i in range(len(s1)):
    if s1[i] == s2[0]:
        sum = 0
        for j in range(len(s2)):
            if s1[i + j] == s2[j]:
                sum += 1
                if sum == len(s2):
                    answer = True

if answer is True:
    print(f'строка {s2} присутствует в строке {s1}')
else:
    print('None')
                    
                