from tkinter import *
from tkinter.ttk import *
import locale
from screencfg import beallit
import startscreen
from competition import Competition
from dbaccess import createdb

locale.setlocale(locale.LC_ALL, "hu-HU.utf8")
createdb()
root = Tk()
root.title("Table Tennis Competiton Manager")

# feltölti a stílus elemeit a screencfg modulból
s = Style()
beallit(s)

# létrehozza az induló képernyőt
fr_main = Frame(root, style="main.TFrame")
l_title = Label(fr_main, text="A verseny adatainak megadása", style="title.TLabel")

fr_main.grid(column=0, row=0)
l_title.grid(column=0, row=0, padx=10, pady=(10, 5), sticky="EW")

comp = Competition()

startscreen.newcomp(fr_main, comp)
startscreen.loadcomp(fr_main, comp)

root.mainloop()
