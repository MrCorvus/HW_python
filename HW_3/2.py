list_en = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
list_ru = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять']

def num_translate():
    v = input('Введите число ')
    v_low = v.lower()
    for i, e in enumerate(list_en):
        if v_low == e:
            c = i
            print(list_ru[c].title())



num_translate()
