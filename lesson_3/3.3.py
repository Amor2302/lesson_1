
def thesaurus(*names):
    res = {}
    for name in names:
        res.setdefault(name[0], []).append(name)
    print(res)
thesaurus('Иван', 'Мария', 'Илья', 'Роман')
