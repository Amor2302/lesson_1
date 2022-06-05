
numbers = input('Введите число от 0 до 10 на английском языке ')

num_translate = {
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
    'ten': 'десять'

}
temp = num_translate.get(numbers)
print(temp)
