
numbers = input('Введите число от 0 до 10 на английском языке ')

function = {
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
num_translate = function.get(numbers)
print(num_translate)
