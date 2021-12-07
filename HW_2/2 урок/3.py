list1 = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for i, e in enumerate(list1):
    i = list1[i].split()
    name = i[-1]
    print(f'Привет, {name.title()}')




# i = list1[0].split()
# name1 = i[-1]
# i = list1[1].split()
# name2 = i[-1]
# i = list1[2].split()
# name3 = i[-1]
# i = list1[3].split()
# name4 = i[-1]
# print(f'Привет, {name1.title()}')
# print(f'Привет, {name2.title()}')
# print(f'Привет, {name3.title()}')
# print(f'Привет, {name4.title()}')
