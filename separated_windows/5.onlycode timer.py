from tkinter import *


def cleaner(event, entry):
    if event.char.isdigit() and entry.get() == "00":
        entry.delete(0, END)

def starter1():
    timer()
    starter()

def starter():
    global time_remaining, timer_active
    if not timer_active:
        s = int(second_taker.get())
        m = int(minute_taker.get())
        h = int(hour_taker.get())
        time_remaining = (h * 3600) + (m * 60) + s
    forget()
    start()

    """fixed the bug, still kinda messy thou"""

def start():
    global is_on, timer_active
    is_on = True
    timer_active = True
    submit.config(text="pause", command=pause)
    resett.config(state=NORMAL)
    shower.place(anchor="center", relx=0.5, rely=0.33)
    update_time_display()
    

def update_time_display():
    shower.config(text=f"{time_remaining // 3600:02}:{time_remaining // 60 % 60:02}:{time_remaining % 60:02}")
    shower.place(anchor="center", relx=0.5, rely=0.33)


def pause():
    global is_on, time_remaining
    is_on = False
    submit.config(text="start", command=start)
    update_time_display()


def reset():
    global is_on, time_remaining
    time_remaining = 0
    is_on = False
    submit.config(text="start", command=starter)
    resett.config(state=DISABLED)
    remember()
    shower.place_forget()


def timer():
    global time_remaining, timer_active
    timer_active = True
    if is_on and time_remaining > 0:
        time_remaining -= 1
        update_time_display()
    else:
        timer_active = False
    window.after(1000, timer)


def forget():
    second_taker.place_forget()
    minute_taker.place_forget()
    hour_taker.place_forget()


def remember():
    second_taker.place(anchor="center", relx=0.75, rely=0.33)
    minute_taker.place(anchor="center", relx=0.50, rely=0.33)
    hour_taker.place(anchor="center", relx=0.25, rely=0.33)


window = Tk()
time_remaining = 0
is_on = False
timer_active = False
window.geometry("400x680")
window.resizable(False, False)
vcmd = window.register(lambda P: (len(P) <= 2 and P.isdigit()) or P == "")

hour_taker = Entry(window, width=2, validate='key', validatecommand=(vcmd, '%P'), font=("Arial", 20))
hour_taker.insert(0, "00")
hour_taker.place(anchor="center", relx=0.25, rely=0.33)

minute_taker = Entry(window, width=2, validate='key', validatecommand=(vcmd, '%P'), font=("Arial", 20))
minute_taker.insert(0, "00")
minute_taker.place(anchor="center", relx=0.50, rely=0.33)

second_taker = Entry(window, width=2, validate='key', validatecommand=(vcmd, '%P'), font=("Arial", 20))
second_taker.insert(0, "00")
second_taker.place(anchor="center", relx=0.75, rely=0.33)

shower = Label(window, font=("Arial", 25))
shower.place_forget()

hour_taker.bind("<KeyPress>", lambda event: cleaner(event, hour_taker))
minute_taker.bind("<KeyPress>", lambda event: cleaner(event, minute_taker))
second_taker.bind("<KeyPress>", lambda event: cleaner(event, second_taker))

submit = Button(text="start", command=starter1)
submit.place(anchor="center", rely=0.50, relx=0.50)

resett = Button(text="reset", command=reset, state=DISABLED)
resett.place(anchor="center", rely=0.50, relx=0.25)

window.mainloop()
