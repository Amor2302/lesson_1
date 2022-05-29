num = 0

for num in range(1, 101):
    if 9 < num < 21:
        print(num, 'процентов')
    elif 1 < num % 10 < 5:
        print(num, 'процента')
    elif num % 10 == 0:
        print(num, 'процентов')
    elif num % 10 == 1:
        print(num, 'процент')
    else:
        print(num, 'процентов')
