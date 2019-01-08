# /usr/bin/env python
# -*- coding:utf-8-*-

def Add():

    newWindow = Tk()

    newWindow.geometry("600x250")

    newWindow.title("Ajouter")
    label = Label(newWindow, text="Ajouter une adresse mail:")
    label.place(x=75, y=50)
    global newAdress
    newAdress = Entry(newWindow, width=30, justify='right')
    newAdress.place(x=75, y=75)
    car = "@"
    com = ".com"
    fr = ".fr"

    buttonPrint = Button(newWindow, text="ok", command=Ajouter)

    buttonPrint.place(x=75, y=105)

    print("adress mail incorrect !")


def Ajouter():
    car = "@"
    com = ".com"
    fr = ".fr"
    Adresslist = newAdress.get()
    if car in Adresslist:
        if com in Adresslist:
            Adress = open("listeAdress.csv", "a")
            Adress.write(Adresslist)
            Adress.write("\n")
            Adress.close()

            print("Ajouter !")



        elif fr in Adresslist:
            Adress = open("listeAdress.csv", "a")
            Adress.write(Adresslist)
            Adress.write("\n")
            Adress.close()

            print("Ajouter !")

    print("adress mail incorrect !")


def double():
    lines = open('listeAdress.csv', 'r').readlines()

    lines_set = set(lines)

    out = open('listeAdress.csv', 'w')

    for line in lines_set:
        out.write(line)


def ouverture():
    newWindow = Toplevel()

    newWindow.focus_set()
    newWindow.geometry("500x250")
    newWindow.title("Ajouter")
    importer = Button(newWindow, text="Ouvrir fichier", command=ouverture)
    importer.grid(row=0, column=0)
    texte = Text(newWindow, width=80, height=30)
    texte.grid(row=1, column=0)

    filepath = filedialog.askopenfilename(filetypes=[('Adresselist.csv', '.csv')])

    with open("listeAdress.csv", 'r') as FILE:
        content = FILE.read()

    texte.insert("end", content)


import tkinter
from tkinter import *
from tkinter import filedialog

main = Tk()
main.configure(width="680", height="550")
Add = Button(main, text="Ajouter", command=Add)
Add.place(x=150, y=75)
Printcsv = Button(main, text="import csv", command=ouverture)
Printcsv.place(x=300, y=75)
double = Button(main, text="Dédoubloner", command=double)
double.place(x=150, y=150)
main.mainloop()