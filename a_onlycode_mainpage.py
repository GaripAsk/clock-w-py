from tkinter import *
from tkinter import ttk
import b_onlycode_clock
import c_onlycode_alarm
import d_onlycode_stopwatch
import e_onlycode_timer

window = Tk()
tabs = ttk.Notebook(window)
tab1 = Frame(tabs)
tab2 = Frame(tabs)
tab3 = Frame(tabs)
tab4 = Frame(tabs)
tabs.add(tab1, text="Clock")
tabs.add(tab2, text="Alarm")
tabs.add(tab3, text="Stopwatch")
tabs.add(tab4, text="Timer")
width = 400
height = 400
tabs.pack()
e_onlycode_timer.timerr(tab4)
d_onlycode_stopwatch.stopwatchh(tab3)
c_onlycode_alarm.alarmm(tab2)
b_onlycode_clock.clockk(tab1, height, width)

window.mainloop()