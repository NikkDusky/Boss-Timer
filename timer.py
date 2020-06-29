from datetime import datetime
from calendar import weekday
from time import sleep
import os

clear = lambda: os.system('cls') # Если вы хотите запустить этот скрипт на Termux или другой Linux подобной системе, измените 'cls' на 'clear'.

def get_date():

    num_of_notification = True

    while True:
        daylist = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
        year = int(datetime.today().strftime('%Y'))
        month = int(datetime.today().strftime('%m'))
        day = int(datetime.today().strftime('%d'))
        hour = int(datetime.today().strftime('%H'))
        weekday_num = weekday(year, month, day)  # Получаем номер от 0 до 6 текущего дня недели!
        weekday_text = daylist[weekday_num]  # Выбираем из списка по номеру текстовый вариант дня! UDP. Используется просто для удобства!
        if num_of_notification == True:
            print("\n+-+-+-+-+-+-+-+-+-+-+-+-+\n")
            print("Сегодня " + weekday_text + " " + str(year) + "/" + str(month) + "/" + str(day))
            print("\n+-+-+-+-+-+-+-+-+-+-+-+-+\n")
            sleep(1)
            num_of_notification = False

        bosses(weekday_text,hour)

def bosses(day, hour):
    # Понедельник
    if day == "Понедельник":
        if int(hour) < 1:
            timer("Офин", "01")
        elif int(hour) < 2:
            timer("Каранда, Кзарка", "02")
        elif int(hour) < 3:
            timer("Нубэр", "03")
        elif int(hour) < 14:
            timer("Кутум", "14")
        elif int(hour) < 16:
            timer("Нубэр", "16")
        elif int(hour) < 18:
            timer("Каранда", "18")
        elif int(hour) < 20:
            timer("Кутум", "20")
        else:
            timer("Ближайший босс после 12-ночи, ждем перезапуска...", "24")

    # Вторник
    if day == "Вторник":
        if int(hour) < 1:
            timer("Нубэр, Каранда", "01")
        elif int(hour) < 2:
            timer("Кзарка", "02")
        elif int(hour) < 3:
            timer("Каранда", "03")
        elif int(hour) < 14:
            timer("Каранда", "14")
        elif int(hour) < 16:
            timer("Кзарка", "16")
        elif int(hour) < 18:
            timer("Кутум", "18")
        elif int(hour) < 20:
            timer("Каранда", "20")
        else:
            timer("Ближайший босс после 12-ночи, ждем перезапуска...", "24")

    # Среда
    if day == "Среда":
        if int(hour) < 1:
            timer("Квинт, Мурака", "01")
        elif int(hour) < 2:
            timer("Кутум", "02")
        elif int(hour) < 3:
            timer("Нубэр", "03")
        elif int(hour) < 16:
            timer("Каранда", "16")
        elif int(hour) < 18:
            timer("Нубэр", "18")
        elif int(hour) < 20:
            timer("Кзарка", "20")
        else:
            timer("Ближайший босс после 12-ночи, ждем перезапуска...", "24")

    # Четверг
    if day == "Четверг":
        if int(hour) < 1:
            timer("Офин", "01")
        elif int(hour) < 2:
            timer("Каранда", "02")
        elif int(hour) < 3:
            timer("Кутум", "03")
        elif int(hour) < 14:
            timer("Нубэр", "14")
        elif int(hour) < 16:
            timer("Кутум", "16")
        elif int(hour) < 18:
            timer("Нубэр", "18")
        elif int(hour) < 20:
            timer("Кзарка", "20")
        else:
            timer("Ближайший босс после 12-ночи, ждем перезапуска...", "24")

    # Пятница
    if day == "Пятница":
        if int(hour) < 1:
            timer("Камос", "01")
        elif int(hour) < 2:
            timer("Нубэр", "02")
        elif int(hour) < 3:
            timer("Кзарка", "03")
        elif int(hour) < 14:
            timer("Каранда", "14")
        elif int(hour) < 16:
            timer("Кутум", "16")
        elif int(hour) < 18:
            timer("Нубэр", "18")
        elif int(hour) < 20:
            timer("Кзарка", "20")
        else:
            timer("Ближайший босс после 12-ночи, ждем перезапуска...", "24")

    # Суббота
    if day == "Суббота":
        if int(hour) < 1:
            timer("Офин", "01")
        elif int(hour) < 2:
            timer("Кзарка, Нубэр", "02")
        elif int(hour) < 3:
            timer("Кутум", "03")
        elif int(hour) < 10:
            timer("Кзарка", "10")
        elif int(hour) < 12:
            timer("Нубэр", "12")
        elif int(hour) < 14:
            timer("Кутум", "14")
        elif int(hour) < 16:
            timer("Квинт, Мурака", "16")
        elif int(hour) < 18:
            timer("Каранда", "18")
        elif int(hour) < 20:
            timer("Кутум", "20")
        else:
            timer("Ближайший босс после 12-ночи, ждем перезапуска...", "24")

    # Воскресенье
    if day == "Воскресенье":
        if int(hour) < 2:
            timer("Камос", "02")
        elif int(hour) < 3:
            timer("Кзарка", "03")
        elif int(hour) < 10:
            timer("Каранда", "10")
        elif int(hour) < 12:
            timer("Кутум", "12")
        elif int(hour) < 14:
            timer("Камос", "14")
        elif int(hour) < 16:
            timer("Кутум", "16")
        elif int(hour) < 18:
            timer("Велл", "18")
        elif int(hour) < 20:
            timer("Нубэр, Кзарка", "20")
        else:
            timer("Ближайший босс после 12-ночи, ждем перезапуска...", "24")

def timer(boss_name, boss_hour):
    whathourisit = (datetime.today().strftime('%H')) #(%H:%M:%S.%f')[:-5]
    whatminisit = (datetime.today().strftime('%M'))
    whatsecisit = (datetime.today().strftime('%S'))
    whatmillisit = (datetime.today().strftime('%f')[:-5])
    whattimeisit = (whathourisit + ":" + whatminisit + ":" + whatsecisit + "." + whatmillisit)

    if whattimeisit == "00:00:00.5":
        clear()
        print("Глобальный перезапуск, подожди 10 секунд!")
        sleep(9)
        get_date()

    boss_spawned = (str(boss_hour) + ":00:01.0")
    if whattimeisit == boss_spawned:
        clear()
        print("Появился босс, а скрипт уходит на 10 секундный перезапуск!")
        sleep(9)
        get_date()

    sleep(0.1)
    boss_countH = (int(boss_hour)) - (int(whathourisit)+1)
    boss_countM = 59 - int(whatminisit)
    boss_countS = 59 - int(whatsecisit)
    boss_countMill = 9 - int(whatmillisit)
    clear()
    print(boss_name + " " + str(boss_countH) + ":" + str(boss_countM) + ":" + str(boss_countS) + ":" + str(boss_countMill))

get_date()