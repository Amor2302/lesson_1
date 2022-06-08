def num_translate():
    user_input = str(input('Введите число от 0 до 10 на английском языке '))
    if user_input.istitle():
        return print(dictionary.get(user_input.lower()).title())
    print(dictionary.get(user_input))
dictionary = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'for': 'четыре',
    'five': 'пять',
    'six': 'шесть',
    'seven': 'семь',
    'eight': 'восемь',
    'nine': 'девять',
    'ten': 'десять'}
num_translate()