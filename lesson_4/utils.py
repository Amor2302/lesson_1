import sys

sys.path.append('C:\Users\ДОМ\Roman_Radzhabov\lesson_4')
from 4.2 import *


chse = ((input(f'Список валют:\n{money_code_lst}\nЧто бы получить курс, введите код валюты из списка выше: ')).upper())
print(currency_rates(chse))