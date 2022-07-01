
def odd_to_n(start, end):
    for number in range(start, end+1, 2):
        yield number
print(*(odd_to_n(1, 15)), sep='\n')
