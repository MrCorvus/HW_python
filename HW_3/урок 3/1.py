list_en = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
list_ru = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять']

def num_translate():
    v = input('Введите число ')
    for i, e in enumerate(list_en):
        if v == e:
           c = i
           print(list_ru[c])


num_translate()



# list_en = {0 : 'zero', 1 : 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten'}
# list_ru = {0 : 'ноль', 1 : 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять', 10: 'десять'}