
def odd_to_n(start, end):
    for num in range(start, end+1, 2):
        yield num
print(*(odd_to_n(1, 15)), sep='\n')
