from tkinter import *
from PIL import Image, ImageTk



window = Tk()
x = 0
def saniye():
    global x, tiktak, image

    image_path = "tiktak.png"
    image = Image.open(image_path)
    image = image.rotate(x)
    tiktak = ImageTk.PhotoImage(image)
    canvas.create_image(450, 454, image=tiktak)
    x -= 6
    window.update()
    window.after(1000, saniye)


canvas = Canvas(window, width=900, height=900)
canvas.pack()

arkaplan = PhotoImage(file='saat.png')
canvas.create_image(450, 450, image=arkaplan)

saniye()

window.mainloop()