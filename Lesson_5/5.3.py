def gen_from_2_lst(lst_1, lst_2):

    i = 0
    while i < len(lst_1) and i < len(lst_2):
        yield lst_1[i], lst_2[i]
        i += 1
    while i < len(lst_1):
        yield lst_1[i], None
        i += 1

tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', 'Иван', 'Данила']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

for i in gen_from_2_lst(tutors, klasses):
    print(i)



