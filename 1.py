how_second = int(input('Введите число: '))
day = 86400
hour = 3600
minute = 60
second = 1
if not (how_second > minute) :
    print(how_second, ' секунд')
elif not (how_second >= hour):
    print(how_second % day % hour % minute, ' минут', how_second, ' секунд');
elif not (how_second >= day) :
    print (how_second % day % hour // minute, ' часов', how_second % day % hour % minute, ' минут', how_second, ' секунд');
else:
    print(how_second // day, " дней", how_second % day // hour, ' часов', how_second % day % hour // minute, ' минут', how_second % day % hour % minute , ' секунд' );




