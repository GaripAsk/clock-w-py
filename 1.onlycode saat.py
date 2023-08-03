from tkinter import *
from tkinter import ttk
import math
import time
from math import cos, sin, pi


def digital_saat():
    zaman_yenileme = time.strftime("saat şu an: %H:%M:%S \n Tarih: %d-%m-%Y")
    saat.config(text=zaman_yenileme)
    pencere.after(1000, digital_saat)


def saniye():
    global saniye1_id1
    zamanz = time.localtime()
    saniye12 = zamanz.tm_sec
    saniye_aci_degiskeni = saniye12 * 6
    merkez_x = genislik // 2
    merkez_y = yukseklik // 2
    yelkovan_uzunluk = min(genislik, yukseklik) // 2 - 45  # Canvas kenarlarından biraz içeride başlat
    aci_radyan = math.radians(saniye_aci_degiskeni)
    uclu_x = merkez_x + yelkovan_uzunluk * math.sin(aci_radyan)
    uclu_y = merkez_y - yelkovan_uzunluk * math.cos(aci_radyan)

    # Yelkovanı güncelle
    canvas.coords(saniye1_id1, merkez_x, merkez_y, uclu_x, uclu_y)
    # Animasyonu güncellemek için kendini çağır
    pencere.after(1000, saniye)  # Her 1 saniyede bir çağır


def dakika_yelkovan():
    global yelkovan_id2

    zamanz = time.localtime()
    dakika12 = zamanz.tm_min
    dakika_aci_degiskeni = dakika12 * 6
    merkez_x = genislik // 2
    merkez_y = yukseklik // 2
    yelkovan_uzunluk = min(genislik, yukseklik) // 2 - 65
    aci_radyan = math.radians(dakika_aci_degiskeni)
    uclu_x = merkez_x + yelkovan_uzunluk * math.sin(aci_radyan)
    uclu_y = merkez_y - yelkovan_uzunluk * math.cos(aci_radyan)

    # Yelkovanı güncelle
    canvas.coords(yelkovan_id2, merkez_x, merkez_y, uclu_x, uclu_y)

    # Animasyonu güncellemek için kendini çağır
    pencere.after(1000, dakika_yelkovan)  # Her 1 saniyede bir çağır


def saat_akrep():
    global akrep_id3
    zamanz = time.localtime()
    saat12 = zamanz.tm_hour

    saat_aci_degiskeni = pi / 2 - (saat12 % 12) * (2 * pi / 12)
    merkez_x = genislik // 2
    merkez_y = yukseklik // 2
    yelkovan_uzunluk = min(genislik, yukseklik) // 2 - 85  # Canvas kenarlarından biraz içeride başlat
    hour_x = merkez_x + yelkovan_uzunluk * cos(saat_aci_degiskeni) * 0.6
    hour_y = merkez_y - yelkovan_uzunluk * sin(saat_aci_degiskeni) * 0.6

    canvas.coords(akrep_id3, merkez_x, merkez_y, hour_x, hour_y)

    pencere.after(1000, saat_akrep)


# Tkinter penceresini oluştur
pencere = Tk()
zaman = time.localtime()
sekmeler = ttk.Notebook(pencere)
pencere.resizable(False, False)
# Canvas örneğini oluştur
sekme1 = Frame(sekmeler)
sekme2 = Frame(sekmeler)
sekme3 = Frame(sekmeler)
sekme4 = Frame(sekmeler)
sekmeler.add(sekme1, text="Saat&Tarih")
sekmeler.add(sekme2, text="Alarm")
sekmeler.add(sekme3, text="Kronometre")
sekmeler.add(sekme4, text="Zamanlayici")
genislik = 400
yukseklik = 400
pencere.geometry("400x680")
canvas = Canvas(sekme1, width=400, height=680)
canvas.pack()
sekmeler.pack()

# Saat işaretlerini (ağları) çiz
for saat in range(13):
    aci = math.radians(saat * 30)  # Her saat için 30 derece
    x1 = genislik // 2 + (genislik // 2 - 40) * math.sin(aci)
    y1 = yukseklik // 2 - (yukseklik // 2 - 40) * math.cos(aci)
    x2 = genislik // 2 + (genislik // 2) * math.sin(aci)
    y2 = yukseklik // 2 - (yukseklik // 2) * math.cos(aci)
    canvas.create_line(x1, y1, x2, y2, width=3)
    # Altındaki sayıyı belirleyin
    if saat >= 1:
        sayi = saat  # İlgili saati temsil eden sayıyı belirleyin

        # Sayıyı ekrana yazdırın
        x_sayi = genislik // 2 + (genislik // 2 - 70) * math.sin(aci)  # Sayının x koordinatını belirleyin
        y_sayi = yukseklik // 2 - (yukseklik // 2 + -70) * math.cos(aci)  # Sayının y koordinatını belirleyin
        canvas.create_text(x_sayi, y_sayi, text=str(sayi),)

for saat in range(60):
    aci = math.radians(saat * 6)  # Her saat için 30 derece
    x1 = genislik // 2 + (genislik // 2 - 20) * math.sin(aci)
    y1 = yukseklik // 2 - (yukseklik // 2 - 20) * math.cos(aci)
    x2 = genislik // 2 + (genislik // 2 - 10) * math.sin(aci)
    y2 = yukseklik // 2 - (yukseklik // 2 - 10) * math.cos(aci)
    canvas.create_line(x1, y1, x2, y2)

# saniye, yelkovanı ,akrebi çizer

saat1 = zaman.tm_hour
dakika1 = zaman.tm_min
saniye1 = zaman.tm_sec

saniye_aci_degiskeni = pi / 2 - saniye1 * (2 * pi / 60)
dakika_aci_degiskeni = pi / 2 - (dakika1 + saniye1 / 60) * (2 * pi / 60)
saat_aci_degiskeni = pi / 2 - (saat1 % 12 + dakika1 / 60 + saniye1 / 3600) * (2 * pi / 12)


merkez_x = genislik // 2
merkez_y = yukseklik // 2
yelkovan_uzunluk = min(genislik, yukseklik) // 2 - 20  # Canvas kenarlarından biraz içeride başlat

aci_radyan_saniye = math.radians(saniye_aci_degiskeni)
uclu_x_s = merkez_x + yelkovan_uzunluk * math.sin(aci_radyan_saniye)
uclu_y_s = merkez_y - yelkovan_uzunluk * math.cos(aci_radyan_saniye)


aci_radyan_dakika = math.radians(dakika_aci_degiskeni)
uclu_x_m = merkez_x + yelkovan_uzunluk * math.sin(aci_radyan_saniye)
uclu_y_m = merkez_y - yelkovan_uzunluk * math.cos(aci_radyan_saniye)

aci_radyan_saat = math.radians(saat_aci_degiskeni)
uclu_x_h = merkez_x + yelkovan_uzunluk * math.sin(aci_radyan_saniye)
uclu_y_h = merkez_y - yelkovan_uzunluk * math.cos(aci_radyan_saniye)

saniye1_id1 = canvas.create_line(merkez_x, merkez_y, uclu_x_s, uclu_y_s, width=2)
yelkovan_id2 = canvas.create_line(merkez_x, merkez_y, uclu_x_m, uclu_y_m, width=4)
akrep_id3 = canvas.create_line(merkez_x, merkez_y, uclu_x_h, uclu_y_h, width=6)

saat = Label(sekme1, font=('Arial', 20, 'bold'), width=20, height=7)
saat.place(anchor="center", relx=0.5, rely=0.8)

digital_saat()
# saati başlat
saniye()
dakika_yelkovan()
saat_akrep()

# Pencereyi aç
pencere.mainloop()
