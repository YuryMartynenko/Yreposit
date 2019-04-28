#ANAGRAMM  
def anagram(s1, s2):
    alias1 = list(s1)
    alias2 = list(s2)
    alias1.sort()
    alias2.sort()
    zex = 0
    for i in range(len(alias1)):
        if alias2[i] == alias1[i]:
            zex += 1
            if zex == len(alias2):
                return f'Строка {st1} является анаграммой строки {st2}.'
    else:
        return f'Строки {st1} и {st2} не являются анаграммой.'
  
  
st1 = 'abcaac'
st2 = 'cbacaa'
hex = anagram(st1, st2)
print(hex)

