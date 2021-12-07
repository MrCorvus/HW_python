# trial_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'в', 'была', '+5', 'градусов']


trial_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'в', 'была', '+5', 'градусов']
for i, e in enumerate(trial_list):
    if e.isdigit():
        trial_list[i] = f'"{int(e):02d}"'
    elif e[1:].isdigit():
        trial_list[i] = f'"{e[0]}{int(e[1:]):02d}"'


print(' '.join(trial_list))
#print(f'{trial_list:" ".join}') # не понял как сделать тоже самое, но новым способом


