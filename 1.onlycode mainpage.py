from tkinter import *
from tkinter import ttk

window = Tk()
tabs = ttk.Notebook(window)
window.resizable(False, False)
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
window.geometry("400x680")
tabs.pack()

window.mainloop()