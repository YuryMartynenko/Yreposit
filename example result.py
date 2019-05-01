s = '1,2,34,5,67,8,9'
s = s.split(',')
s = list(s)
zex = []
res = 0
for i in range(len(s)):
    if i in (0, 1, 2, 4, 6):
        res += int(s[i])
    if i in (3, 5):
        res -= int(s[i])

print(f'{s[0]} + {s[1]} + {s[2]} - {s[3]} + {s[4]} - {s[5]} + {s[6]} = {res}')

        
    