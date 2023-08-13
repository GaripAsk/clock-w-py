from tkinter import *
from tkinter import ttk
import math
import time
from math import cos, sin, pi

def clockk(window, height, width):
    global second_id1, minute_id2, hour_id3

    canvas = Canvas(window, width=400, height=680)
    canvas.pack()


    def digital_clock():
        time_refresher = time.strftime("Time: %H:%M:%S \n Date: %d-%m-%Y")
        saat.config(text=time_refresher)
        window.after(1000, digital_clock)


    def clock_secondhand():
        global second_id1
        timez = time.localtime()
        second12 = timez.tm_sec
        second_angle_adj = second12 * 6
        core_x = width // 2
        core_y = height // 2
        secondhand_lenght = min(width, height) // 2 - 30
        angle_radian = math.radians(second_angle_adj)
        uclu_x = core_x + secondhand_lenght * math.sin(angle_radian)
        uclu_y = core_y - secondhand_lenght * math.cos(angle_radian)

        canvas.coords(second_id1, core_x, core_y, uclu_x, uclu_y)
        
        window.after(1000, clock_secondhand) 


    def clock_minutehand():
        global minute_id2

        timez = time.localtime()
        minute12 = timez.tm_min
        minute_angle_adj = minute12 * 6
        core_x = width // 2
        core_y = height // 2
        minutehand_lenght = min(width, height) // 2 - 65
        angle_radian = math.radians(minute_angle_adj)
        uclu_x = core_x + minutehand_lenght * math.sin(angle_radian)
        uclu_y = core_y - minutehand_lenght * math.cos(angle_radian)

        canvas.coords(minute_id2, core_x, core_y, uclu_x, uclu_y)

        window.after(1000, clock_minutehand)  


    def clock_hourhand():
        global hour_id3
        timez = time.localtime()
        hour12 = timez.tm_hour

        hour_angle_adj = pi / 2 - (hour12 % 12) * (2 * pi / 12)
        core_x = width // 2
        core_y = height // 2
        hourhand_lenght = min(width, height) // 2 - 85  
        hour_x = core_x + hourhand_lenght * cos(hour_angle_adj) * 0.6
        hour_y = core_y - hourhand_lenght * sin(hour_angle_adj) * 0.6

        canvas.coords(hour_id3, core_x, core_y, hour_x, hour_y)

        window.after(1000, clock_hourhand)


    timee = time.localtime()

    for saat in range(13):
        aci = math.radians(saat * 30) 
        x1 = width // 2 + (width // 2 - 40) * math.sin(aci)
        y1 = height // 2 - (height // 2 - 40) * math.cos(aci)
        x2 = width // 2 + (width // 2) * math.sin(aci)
        y2 = height // 2 - (height // 2) * math.cos(aci)
        canvas.create_line(x1, y1, x2, y2, width=3)

        if saat >= 1:
            sayi = saat  

            x_sayi = width // 2 + (width // 2 - 70) * math.sin(aci)  
            y_sayi = height // 2 - (height // 2 + -70) * math.cos(aci) 
            canvas.create_text(x_sayi, y_sayi, text=str(sayi),)

    for saat in range(60):
        aci = math.radians(saat * 6) 
        x1 = width // 2 + (width // 2 - 20) * math.sin(aci)
        y1 = height // 2 - (height // 2 - 20) * math.cos(aci)
        x2 = width // 2 + (width // 2 - 10) * math.sin(aci)
        y2 = height // 2 - (height // 2 - 10) * math.cos(aci)
        canvas.create_line(x1, y1, x2, y2)


    saat1 = timee.tm_hour
    dakika1 = timee.tm_min
    saniye1 = timee.tm_sec

    second_angle_adj = pi / 2 - saniye1 * (2 * pi / 60)
    minute_angle_adj = pi / 2 - (dakika1 + saniye1 / 60) * (2 * pi / 60)
    hour_angle_adj = pi / 2 - (saat1 % 12 + dakika1 / 60 + saniye1 / 3600) * (2 * pi / 12)


    core_x = width // 2
    core_y = height // 2
    minutehand_lenght = min(width, height) // 2 - 20 

    angle_radian_second = math.radians(second_angle_adj)
    uclu_x_s = core_x + minutehand_lenght * math.sin(angle_radian_second)
    uclu_y_s = core_y - minutehand_lenght * math.cos(angle_radian_second)


    angle_radian_minute = math.radians(minute_angle_adj)
    uclu_x_m = core_x + minutehand_lenght * math.sin(angle_radian_minute)
    uclu_y_m = core_y - minutehand_lenght * math.cos(angle_radian_minute)

    angle_radian_clock = math.radians(hour_angle_adj)
    uclu_x_h = core_x + minutehand_lenght * math.sin(angle_radian_clock)
    uclu_y_h = core_y - minutehand_lenght * math.cos(angle_radian_clock)

    second_id1 = canvas.create_line(core_x, core_y, uclu_x_s, uclu_y_s, width=2)
    minute_id2 = canvas.create_line(core_x, core_y, uclu_x_m, uclu_y_m, width=4)
    hour_id3 = canvas.create_line(core_x, core_y, uclu_x_h, uclu_y_h, width=6)


    saat = Label(window, font=('Arial', 20, 'bold'), width=20, height=7)
    saat.place(anchor="center", relx=0.5, rely=0.8)

    digital_clock()
    clock_secondhand()
    clock_minutehand()
    clock_hourhand()

