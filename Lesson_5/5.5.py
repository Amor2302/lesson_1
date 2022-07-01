src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

def unc_lst(any_lst):

    result = []

    for i in any_lst:
        if any_lst.count(i) == 1:
            result.append(i)

    return result

print(unc_lst(src))

