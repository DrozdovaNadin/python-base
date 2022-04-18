# Реализовать вывод информации о промежутке времени в зависимости от его продолжительности duration в секундах.

minutes_sec = 60
haur_sec = 3600
day_sec = 86400

time = int(input('Введите число в секундах: '))

if time > 0 and time < minutes_sec:
    print(time, "сек")

if time >= minutes_sec and time < haur_sec:
    minutes = time//minutes_sec
    second = time % minutes_sec
    print(minutes, 'мин', second, 'сек')
if time >= haur_sec and time < day_sec:
    haur = time // haur_sec
    second = (time % haur_sec)
    minutes = 0
    if  second  < minutes_sec:
        print(haur, 'час', minutes, 'мин', second, 'сек')
    elif second >= minutes_sec:
        minutes = (time % haur_sec)//minutes_sec
        second =  (time % haur_sec) % minutes_sec
        print(haur, 'час',  minutes, 'мин', second, 'сек')

if time >= day_sec:
    day = time//day_sec
    haur = (time % day_sec)
    if haur < haur_sec and haur >= minutes_sec:
        haur = 0
        minutes = (time % day_sec)//minutes_sec
        second = (time % day_sec) % minutes_sec
        print(day,'дн', haur, 'час', minutes, 'мин', second, 'сек')
    elif haur < haur_sec and haur < minutes_sec:
        haur = 0
        minutes = 0
        second = (time % day_sec)
        print(day, 'дн', haur, 'час', minutes, 'мин', second, 'сек')
    else:
        haur = (time % day_sec)//haur_sec
        minutes = ((time % day_sec) % haur_sec)//minutes_sec
        second = ((time % day_sec) % haur_sec) % minutes_sec
        print(day, 'дн', haur, 'час', minutes, 'мин', second, 'сек')


