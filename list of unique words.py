def clean(string):      # в функцию попадает слово  ****
    result = ''
    for char in string: # для каждой буквы в слове
        if char.isalnum() or char == '-': # состоит буква из цифр или букв ИЛИ буква является пунктиром
            result += char.lower() # добавляем в результирующую строку эту букву в нижнем регистре
    return result # возвращаем результат


def resort(filename):                 # в функцию попадает фаил
    unique_words = set()              # структура множество возвращающее уникальные значения
    with open(filename, 'r', encoding='utf-8') as f: # распаковываем фаил в режиме read
        for line in f:                # для каждой линии в файле
            words = set(line.split()) # в переменную word записываем преобразованную во множество линию файла, делим её по разделителю split-ом
            if len(words) == 0:       # если длиннна переменной word, которая хранит линию разделенную split-ом
                continue              # возвращаемся вначало цикла
            for word in words:        # для слова  в линии
                cleaned = clean(word) # в переменную  ложим результат функции clean ****
                if cleaned != '':     # если результат функции не равен пустой строке то
                    unique_words.add(cleaned) # добавляем в результат уникальных значений.
    return list(unique_words)         # возвращаем результат уникальный значений в виде списка
                    
                
def count(values):
    elements = 0
    for i in range(len(values)):
        elements += 1
    return f'\nВсего уникальных слов в файле - {elements} значений.'
        
        
        

file = 'qwerty.txt' # фаил с текстом
values = resort(file)
count_values = count(values)
print(values)
print(count_values)


