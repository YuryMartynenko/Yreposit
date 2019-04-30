def coding(text):
    res = []
    score = 0
    for i in range(len(text)):
        score += 1
        if i == len(text)-1 or text[i] != text[i+1]:
            res.extend([text[i], str(score)])
            score = 0
    result = ''.join(res)
    return result
            

def decoding(text):
    res = []
    for i in range(len(text)):
        if i == len(text)-1:
            break
        elif text[i+1].isdigit():
            value = text[i] * int(text[i+1])
            res.append(value)
    result = ''.join(res)
    return result
        



code = input().split()
variant, text = code

if variant.upper() == 'E':
    result = coding(text)
    print(f'зашифровка вашего сообщения {code} будет выглядеть так -', result)
elif variant.upper() == 'D':
    result = decoding(text)
    print(f'расшифровка вашего сообщения {code} будет выглядеть так -', result)
    
    