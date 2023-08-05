from tkinter import *
import time


def on_spinbox_click(event):
    if spin_hour.get() == "0":
        spin_hour.delete(0, 'end')


def timeee():
    zaman_yenileme = time.strftime("%H:%M:%S \n %A %B %d")
    time_of_day.config(text=zaman_yenileme)
    window.after(1000, timeee)


def add_alarm():
    remember_spinboxes()
    other_forgethers()
    add_placer()
    alarm_settings.place(anchor="center", relx=0.5, rely=0.6, width=300, height=275)


def other_forgethers():
    alarmslistbox.place_forget()
    alarm_adder.place_forget()
    time_of_day.place_forget()


def other_remembers():
    alarmslistbox.place(anchor="center", relx=0.50, rely=0.55)
    alarm_adder.place(anchor="center", relx=0.50, rely=0.85)
    time_of_day.place(anchor="center", relx=0.50, rely=0.20)


def forget_spinboxes():
    spin_hour.place_forget()
    spin_minute.place_forget()


def add_placer():
    confirm.place(anchor="center", relx=0.85, rely=0.85)
    reject.place(anchor="center", relx=0.15, rely=0.85)


def add_forgeter():
    confirm.place_forget()
    reject.place_forget()


def remember_spinboxes():
    spin_hour.place(anchor="center", relx=0.35, rely=0.20)
    spin_minute.place(anchor="center", relx=0.65, rely=0.20)


def rejects():
    add_forgeter()
    forget_spinboxes()
    other_remembers()
    alarm_settings.place_forget()


def day_new_window():
    days_b.config(state=DISABLED)
    x = window.winfo_x() + 100
    y = window.winfo_y() + 100
    daywindow = Toplevel(window)
    daywindow.geometry(f"150x213+{x}+{y}")
    dayss = Frame(daywindow, bg="white", bd=10)
    dayss.pack()
    for day in days:
        var = IntVar()
        vars.append(var)
        check_button = Checkbutton(dayss, text=day, variable=var)
        check_button.pack(anchor="w")
    dayw_controller(daywindow)


def tag_new_window():
    global tage
    tag_b.config(state=DISABLED)
    x = window.winfo_x() + 100
    y = window.winfo_y() + 385
    tag_window = Toplevel(window)
    tag_window.geometry(f"200x40+{x}+{y}")
    tags = Frame(tag_window, bg="white", bd=10)
    tags.pack()
    tagw_controller(tag_window)
    tage = Entry(tag_window, width=10, font=("Arial", 16))
    tage.pack(side="left")
    tag_s_b = Button(tag_window, text="Confirm", width=10, font=("Arial", 10), command=tag_confirm_b)
    tag_s_b.pack(side="right")


def tag_confirm_b():
    taglabelvar = tage.get()
    

def alarm_window():
    pass


def confirms():
    pass


def dayw_controller(windows):
    if not windows.winfo_exists():
        days_b.config(state=NORMAL)
    else:
        window.after(100, dayw_controller, windows)


def tagw_controller(windows):
    if not windows.winfo_exists():
        tag_b.config(state=NORMAL)
    else:
        window.after(100, tagw_controller, windows)


def soundw_controller(windows):
    if not windows.winfo_exists():
        alarm_sound_b.config(state=NORMAL)
    else:
        window.after(100, soundw_controller, windows)


window = Tk()
window.geometry("400x680")
window.resizable(False, False)
loca_time = time.localtime()
window.configure(bg='white')
vcmd_h = window.register(lambda P: P.isdigit() and int(P) <= 24)
vcmd_m = window.register(lambda P: P.isdigit() and int(P) <= 60)
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
vars = []

spin_hour = Spinbox(window, from_=0, to=24, width=2, validate='key', validatecommand=(vcmd_h, '%P'), font=("Arial", 20))
spin_hour.place(anchor="center", relx=0.25, rely=0.20)
spin_hour.place_forget()

spin_minute = Spinbox(window, from_=0, to=60, width=2, validate='key', validatecommand=(vcmd_m, '%P'),
                      font=("Arial", 20))

spin_minute.place(anchor="center", relx=0.50, rely=0.20)
spin_minute.place_forget()

spin_hour.bind('<KeyPress>', on_spinbox_click)
spin_minute.bind('<KeyPress>', on_spinbox_click)

alarm_settings = Frame(window, width=300, height=275, bg="#808080")
alarm_settings.place_forget()

time_of_day = Label(window, font=('Arial', 20, 'bold'), width=20, height=7, bg='white')
time_of_day.place(anchor="center", relx=0.50, rely=0.20)
timeee()

alarm_adder = Button(window, text="+", font=('Arial', 20, 'bold'), width=3, command=add_alarm)
alarm_adder.place(anchor="center", relx=0.50, rely=0.85)

confirm = Button(window, text="+", font=('Arial', 20, 'bold'), width=3, command=confirms)
reject = Button(window, text="-", font=('Arial', 20, 'bold'), width=3, command=rejects)

repeat_label = Label(alarm_settings, text="Repeat", font=("Arial", 16), width=20, anchor='w', height=2)
repeat_label.place(anchor='center', relx=0.5, rely=0.2)

tag_label = Label(alarm_settings, text="Tag", width=20, anchor='w', height=2, font=("Arial", 16))
tag_label.place(anchor='center', relx=0.5, rely=0.5)

alarm_sound_label = Label(alarm_settings, text="Alarm sound", width=20, anchor='w', height=2, font=("Arial", 16))
alarm_sound_label.place(anchor='center', relx=0.5, rely=0.8)

days_b = Button(alarm_settings, text="+", height=1, width=3, font=("Arial", 16), command=day_new_window)
days_b.place(anchor='center', relx=0.8, rely=0.2)

tag_b = Button(alarm_settings, text="+", height=1, width=3, font=("Arial", 16), command=tag_new_window)
tag_b.place(anchor='center', relx=0.8, rely=0.5)

alarm_sound_b = Button(alarm_settings, text="+", height=1, width=3, font=("Arial", 16))
alarm_sound_b.place(anchor='center', relx=0.8, rely=0.8)

alarmslistbox = Listbox(window, bg='white', highlightcolor='white', highlightbackground='white', width=50, height=20)
alarmslistbox.place(anchor="center", relx=0.50, rely=0.55)


window.mainloop()