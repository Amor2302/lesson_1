price = [34.45, 12.99, 96.44, 78.97, 75.12, 13.76, 119.06, 45.56, 673.78, 89.09, 122.2]
i = 0
#A.

for i, n in enumerate(price):
    price_str = str(f'{n :.2f}').split('.')
    print(f'{price_str[0]} руб {price_str[1]} коп,')

# for i in price:
#     rub = i // 10
#     print(i)

#B.
s_price = sorted(price)
print(id(price))
print(s_price)
print(id(s_price))

#C.
new_price = price
s_new_price = sorted(new_price)[::-1]
print(s_new_price)
#D.
print(s_new_price[:5])