duration = int(input('Введите целое положительное число'))

num_s = 1
num_m = 60
num_h = 3600
num_d = 86400

if duration < 60:
    print(duration, 'сек')
elif duration == 60 or duration < 3600:
    print(duration // num_m, 'мин', duration % num_m, 'сек')
elif duration == 3600 or duration < 86400:
    print(duration // num_h, 'час', (duration // num_m) % num_m, 'мин', duration % num_m, 'сек')
elif duration >= 86400:
    print(duration // num_d, 'дн', (duration % num_d) // num_h, 'час', (duration % num_h) // num_m, 'мин', duration % num_m, 'сек')
