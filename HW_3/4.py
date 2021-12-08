list_name = []
dict_name = {}
list_name2 = []
dict_name2 = {}
stop_it = ''

def  thesaurus():

    while True:
        x = str(input('Введите имя и фамилию сотрудника: '))
        if x != stop_it:
            list_name.append(x)
            for i, e in enumerate(list_name):
                dict_name3 = {}
                surname = ((x.split(' '))[1])[0].title()
                dict_name2.setdefault(surname, {})
                first_letter_s = surname[0]
                first_letter_n = e[0]
                dict_name3[first_letter_n] = sorted(dict_name3.get(first_letter_n, []) + [e])
                dict_name2[first_letter_s] = dict_name3.get(first_letter_s, dict_name3)



        else:
            break


    print(dict_name2)


thesaurus()

#dict_name3[first_letter_n] = dict_name3.get(first_letter_n, []) + [e]
#                dict_name2[first_letter_s] = dict_name3.get(first_letter_s, dict_name3)