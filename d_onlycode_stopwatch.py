from tkinter import *

def stopwatchh(window):
    global y, x, continue_

    def start():
        global continue_
        continue_ = True
        counter()
        time_start.config(text="Stop", command=stop)
        resetter.config(state=DISABLED)
        Lap_counter.config(state=NORMAL)
        Lap_counter_label.place(anchor="center", relx=0.5, rely=0.27)
        Lap_counter_list.pack(expand=YES)


    def stop():
        global continue_
        continue_ = False
        time_start.config(text="Start", command=start)
        resetter.config(state=NORMAL)


    def counter():
        global continue_, x, y
        stopwatch()
        if continue_:
            x += 1
            y += 1
            window.after(10, counter)
        else:
            pass


    def stopwatch():
        global x, y
        timer.config(text=f"{x//36000:02}:{x//100:02}:{x % 100:02}")
        Lap_counter_label.config(text=f"{y//36000:02}:{y//100:02}:{y % 100:02}")


    def reset():
        global x, y
        x = 0
        y = 0
        timer.config(text="00:00:00")
        Lap_counter_label.place_forget()
        Lap_counter_list.pack_forget()
        Lap_counter.config(state=DISABLED)


    def lap_button():
        global y
        lap = f"{y//36000:02}:{y//100:02}:{y % 100:02}".center(13)
        if y != 0:
            y = 0
            Lap_counter_list.insert(END, lap)
        Lap_counter_label.config(text="00:00:00")


    y = 0
    x = 0
    continue_ = False

    timer = Label(window, font=("Arial", 40), anchor="center", text="00:00:00")
    timer.place(anchor="center", relx=0.5, rely=0.20)

    stopwatch_text = Label(window, font=("Arial", 20), width=12, anchor="center", text="Stopwatch")
    stopwatch_text.place(anchor="center", relx=0.5, rely=0.1)

    time_start = Button(window, text="Start", command=start)
    time_start.place(anchor="center", relx=0.5, rely=0.8)

    resetter = Button(window, text="Reset", command=reset)
    resetter.place(anchor="center", relx=0.3, rely=0.8)

    Lap_counter = Button(window, text="Lap", command=lap_button, state=DISABLED)
    Lap_counter.place(anchor="center", relx=0.7, rely=0.8)

    scroll_bar = Scrollbar(window, width=20)
    scroll_bar.pack(side=RIGHT, fill=Y)

    Lap_counter_list = Listbox(window, yscrollcommand=scroll_bar.set, width=9, height=7, font=("Arial", 20))
    Lap_counter_list.pack_forget()

    scroll_bar.config(command=Lap_counter_list.yview)

    Lap_counter_label = Label(window, font=("Arial", 20), anchor="center", text="00:00:00")
    Lap_counter_label.pack_forget()

