mes = 0

l_t = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
message = ''
i = 0

while i < len(l_t):
    if l_t[i].isdigit():
        l_t[i] = l_t[i].zfill(2)
    elif l_t[i].startswith('+'):
        l_t[i] = l_t[i].zfill(3)
    i += 1
    print(l_t)
# n = 1
# while n < len(l_t):
#     if l_t[n].isdigit():
#         l_t.insert(n, '"')
#         l_t.insert(n + 2, '"')
#     n +=2
# f = 0
#
#
# print(l_t)
