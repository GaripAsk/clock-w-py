from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("200x200")

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
vars = []
dayss = None


def open_days_window():
    global dayss
    dayss = Toplevel(root)
    dayss.geometry("200x200")
    for day in days:
        var = IntVar()
        vars.append(var)
        check_button = Checkbutton(dayss, text=day, variable=var)
        check_button.pack(anchor="w")

def check_days():
    selected_days = [day for i, day in enumerate(days) if vars[i].get()]
    messagebox.showinfo("Seçilen Günler", ", ".join(selected_days) if selected_days else "Hiçbir gün seçilmedi")


# A new Button that will call the open_days_window function
button1 = Button(root, text="Günleri Seçmek İçin Tıkla", command=open_days_window)
button1.pack()

# A new Button that will call the check_days function
button2 = Button(root, text="Seçilen Günleri Kontrol Et", command=check_days)
button2.pack()

root.mainloop()
