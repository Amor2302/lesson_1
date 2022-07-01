src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

def new_lst(any_lst):
    sum_lst = list(zip(any_lst[1:], any_lst))
    result = []

    for i in sum_lst:
        if i[1] < i[0]:
            result.append(i[0])
    return result

print(new_lst(src))