num = 0

for num in range(1, 101):
    if 9 < num < 21:
        print(num, 'процентов')
    elif num % 10 == 0:
        print(num, 'процентов')
    elif num % 10 == 1:
        print(num, 'процент')
    elif 1 < num % 10 < 5:
        print(num, 'процента')
    else:
        print(num, 'процентов')
