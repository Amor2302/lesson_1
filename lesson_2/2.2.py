l_t = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

i = 0

while i < len(l_t):
    if l_t[i].isnumeric():
        l_t[i] = '"' + l_t[i].zfill(2) + '"'
    elif l_t[i].startswith('+'):
        l_t[i] = '"' + l_t[i].zfill(3) + '"'
    i += 1
l_t = ''.join(l_t)

print(l_t)
