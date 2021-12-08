list_name = []
dict_name = {}
stop_it = ''

def  thesaurus():
    while True:
        x = input('Введите имя сотрудника: ')
        if x != stop_it:
            list_name.append(x)
        else:
            break

    for i, e in enumerate(list_name):
        key = e[0]
        val = e
        dict_name.setdefault(key, []).append(val)
    print(dict_name)


thesaurus()