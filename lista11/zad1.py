import tkinter as tk
from tkinter import *


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.createInitWidgets()

        self.number = 0
        self.widgets = []

    def createInitWidgets(self):

        szerokość = 38
        wysokość = 2
        kolor_tła="#66b3ff"
        kolor_aktywny_tła="#b3d9ff"
        typ_ramki=GROOVE
        grubość_ramki=2.2

        self.button1 = Button(self, text="Dodaj produkt", width=szerokość, height=wysokość,
                              background=kolor_tła, activebackground=kolor_aktywny_tła, relief=typ_ramki, borderwidth=grubość_ramki,
                              command=self.dodanie)
        self.button1.grid(row=0, column=1, sticky=W, padx=2)

        self.button2 = Button(self, text="Wyjdź", width=szerokość, height=wysokość,
                              background=kolor_tła, activebackground=kolor_aktywny_tła, relief=typ_ramki, borderwidth=grubość_ramki,
                              command=self.wyjście)
        self.button2.grid(row=0, column=2, sticky=W, padx=2, pady=5)

        self.button3 = Button(self, text="Witamy!", width=szerokość, height=wysokość,
                              background=kolor_tła, activebackground=kolor_aktywny_tła, relief=typ_ramki, borderwidth=grubość_ramki,
                              command=self.przywitanie)
        self.button3.grid(row=0, column=0, sticky=W, padx=2, pady=5)

        self.frame = tk.Entry()
        self.frame.pack()
        self.frame.place(x=285, y=50, width=280, height=30)
        # ustawienie jako zmienna
        self.contents = tk.StringVar()
        # nadanie wartości
        self.contents.set("wpisz produkt i naciśnij enter")
        # ustawienie jako zmienna tekstowa
        self.frame["textvariable"] = self.contents

        self.frame.bind('<Key-Return>', self.print_contents)

    def print_contents(self, event):
        print("Wpisywany produkt to:",
              self.contents.get())

    def przywitanie(self):
        print("Dzień dobry!")


    def dodanie(self):
        iterator = self.number + 1
        textForWidget = iterator, "-", self.contents.get()

        widget = Label(self, text=textForWidget)
        widget.grid()
        self.widgets.append(widget)
        self.number += 1
        print("dodano")

    def wyjście(self):
        self.master.destroy()


root = tk.Tk(className='lista zakupów')
root.geometry("870x700")

app = Application(master=root)
app.mainloop()