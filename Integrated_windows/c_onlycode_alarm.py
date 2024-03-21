from tkinter import *
from tkinter import filedialog
import pygame
import time
import os
from tkinter import messagebox
from pygame import mixer

def alarmm(window):

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
        resetter()

    def resetter():
        tag_label_name.config(text="")
        repeat_label_days.config(text="")
        alarm_sound_name.config(text="")

    def day_new_window():
        global daywindow
        days_b.config(state=DISABLED)
        x = window.winfo_x() + 100
        y = window.winfo_y() + 100
        daywindow = Toplevel(window)
        daywindow.geometry(f"150x240+{x}+{y}")
        dayss = Frame(daywindow, bg="white", bd=10)
        dayss.pack()
        vars.clear()
        for day in days:
            var = IntVar()
            vars.append(var)
            check_button = Checkbutton(dayss, text=day, variable=var)
            check_button.pack(anchor="w")
        day_new_window_confirm = Button(daywindow, text="Confirm", command=day_window_confirm)
        day_new_window_confirm.place(anchor="center", relx=0.5, rely=0.9)
        dayw_controller(daywindow)


    def day_window_confirm():
        selected_days.clear()
        for i, var in enumerate(vars):
            if var.get():
                selected_days.append(short_days[i])
        repeat_label_days.config(text=f"{selected_days}") #gonna add some changes
        daywindow.destroy()
        

    def tag_new_window():
        global tage, tag_window
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
        global taglabelvar
        taglabelvar = tage.get()
        tag_label_name.config(text=f"{taglabelvar}")
        tag_window.destroy()


    def alarm_window():
        global music_path, new_name_of_music_file
        music_path = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3") ])
        new_name_of_music_file = os.path.basename(music_path)
        alarm_sound_name.config(text=f"{new_name_of_music_file}")


    def confirms():
        hour_value = spin_hour.get()
        if len(hour_value) == 1:
            messagebox.showwarning("Uyarı", "SAAT Parametresi sağlanmadı.")
            return
        minute_value = spin_minute.get()
        if len(minute_value) == 1:
            messagebox.showwarning("Uyarı", "DAKİKA Parametresi sağlanmadı.")
            return

        with open(dosya_yolu, "r", encoding="utf-8") as f:
            lines = f.readlines()
        if len(hour_value) == 3:
            hour_value = str(hour_value)
            hour_value = hour_value[1:]
        if len(minute_value) == 3:
            minute_value = str(minute_value)
            minute_value = minute_value[1:]

        for index, line in enumerate(lines):
            if line.isspace(): 
                print("satır boş, alarm bilgileri kaydediliyor, bu mesaj test içindir")
                lines[index] = f"{hour_value}:{minute_value}|{taglabelvar}|{selected_days}|{music_path}\n"
                break
            else:
                print("Boş bir satır bulunamadı, yeni satır ekleniyor.")
                lines.append(f"{hour_value}:{minute_value}|{taglabelvar}|{selected_days}|{music_path}\n")
                break
        with open(dosya_yolu, 'w', encoding="utf-8") as f:
            f.writelines(lines)
        forget_spinboxes()
        other_remembers()
        add_forgeter()
        alarm_settings.place_forget()
        resetter()
        alarm_save_checker()


    def alarm_save_checker():
        alarmslistbox.delete(0, 'end')
        with open(dosya_yolu, "r", encoding="utf-8") as f:
            lines = f.readlines()
        for index, line in enumerate(lines):
            if not line.strip() == "":
                all_except_last = line.split("|")[:-1]
                joined = "|".join(all_except_last)
                last_part = line.split("|")[-1]
                last_part = os.path.basename(last_part)
                line = joined + "|" + last_part
                alarmslistbox.insert(index, line)
    
    def alarm_checker():
        with open(dosya_yolu, "r", encoding="utf-8") as f:
            lines = f.readlines()
        for line in lines:
            if not line.strip() == "":
                time_in_line = line.split("|")[0]
                if time_in_line == time.strftime("%H:%M"):
                    day_in_line = line.split("|")[1]
                    if time.strftime("%a") in day_in_line:
                        alarm_path = line.split("|")[-1]
                        alarm_path = alarm_path.replace("/","\\")
                        alarm_path = alarm_path.replace("\n"," ")
                        music_player.load(alarm_path)
                        music_player.play()
        window.after(1000, alarm_checker)


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
            
    music_player = mixer.music
    dosya_yolu = "alarm_saves.txt"
    if os.path.exists(dosya_yolu):
        pass
    else:
        print("No Alarm save detected, creating one...")
        with open (dosya_yolu, "w") as f:
            f.write("")
        print("Alarm save have been created.")

    mixer.init()
    window.configure(bg='white')
    vcmd_h = window.register(lambda P: P.isdigit() and int(P) <= 24)
    vcmd_m = window.register(lambda P: P.isdigit() and int(P) <= 60)
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    short_days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    vars = []
    selected_days = []

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

    alarm_adder = Button(window, text="+", font=('Arial', 20, 'bold'), width=3, command=add_alarm, state=NORMAL)
    alarm_adder.place(anchor="center", relx=0.50, rely=0.85)

    confirm = Button(window, text="+", font=('Arial', 20, 'bold'), width=3, command=confirms, state=NORMAL)
    reject = Button(window, text="-", font=('Arial', 20, 'bold'), width=3, command=rejects, state=NORMAL)

    repeat_label = Label(alarm_settings, text="Repeat:", font=("Arial", 10, "bold"), width=30, anchor='w', height=3)
    repeat_label_days = Label(alarm_settings, text="", font=("Arial", 8), width=40, anchor='w', height=1)
    repeat_label.place(anchor='center', relx=0.5, rely=0.2)
    repeat_label_days.place(anchor='center', relx=0.5, rely=0.3)

    tag_label = Label(alarm_settings, text="Tag: ", font=("Arial", 10, "bold"), width=30, anchor='w', height=3)
    tag_label_name = Label(alarm_settings, text="", font=("Arial", 8), width=40, anchor='w', height=1)
    tag_label.place(anchor='center', relx=0.5, rely=0.5)
    tag_label_name.place(anchor='center', relx=0.5, rely=0.6)

    alarm_sound_label = Label(alarm_settings, text="Alarm sound: ", font=("Arial", 10, "bold"), width=30, anchor='w', height=3)
    alarm_sound_name = Label(alarm_settings, text="", font=("Arial", 8), width=40, anchor='w', height=1)
    alarm_sound_label.place(anchor='center', relx=0.5, rely=0.8)
    alarm_sound_name.place(anchor='center', relx=0.5, rely=0.9)

    days_b = Button(alarm_settings, text="+", height=1, width=3, font=("Arial", 16), command=day_new_window)
    days_b.place(anchor='center', relx=0.8, rely=0.2)

    tag_b = Button(alarm_settings, text="+", height=1, width=3, font=("Arial", 16), command=tag_new_window)
    tag_b.place(anchor='center', relx=0.8, rely=0.5)

    alarm_sound_b = Button(alarm_settings, text="+", height=1, width=3, font=("Arial", 16), command=alarm_window)
    alarm_sound_b.place(anchor='center', relx=0.8, rely=0.8)

    alarmslistbox = Listbox(window, bg='white', highlightcolor='white', highlightbackground='white', width=50, height=20)
    alarmslistbox.place(anchor="center", relx=0.50, rely=0.55)
    alarm_save_checker()
    alarm_checker()
    #wip = Label(window, font=("Arial", 50), text="WIP", bg="red", fg="white", width=20)
    #wip.place(anchor="center", relx=0.5, rely=0.5)

