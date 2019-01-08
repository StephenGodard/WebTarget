import tkinter
import csv
from tkinter import *
from tkinter import filedialog
def refreshList(newWindow):
    liste = Listbox(newWindow)
    liste.configure(width="120", height="29")
    i = 1
    with open("listeAdress.csv", 'r') as FILE:
        for ligne in FILE.readlines():
            liste.insert(i, ligne)
            ++i

    liste.place(x=20, y=300)

def double():
    lines = open('listeAdress.csv', 'r').readlines()

    lines_set = set(lines)

    out = open('listeAdress.csv', 'w')

    for line in lines_set:
        out.write(line)

def Add(*args):

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
def importer():
    Home.destroy()
    main = Tk()
    main.geometry("350x500")
    buttonAdd = Button(main, text="Ajouter", command=lambda *args: Add())
    buttonAdd.configure(width="10", height="3")
    buttonAdd.place(x=75, y=25)
    buttonRefresh=Button(main,text="Rafraichir")
    buttonRefresh.configure(width="10", height="3")
    buttonRefresh.place(x=200,y=25)
    double = Button(main, text="Dédoubloner", command=lambda: double)
    double.configure(width="10", height="3")
    double.place(x=75, y=100)
    liste = Listbox(main)
    liste.configure(width="45", height="15")
    filepath = filedialog.askopenfilename(filetypes=[('Adresselist.csv', '.csv')])
    i = 1
    with open("listeAdress.csv", 'r') as FILE:
        for ligne in FILE.readlines():
            liste.insert(i, ligne)
            ++i

    liste.place(x=20, y=250)





Home = Tk()
Home.configure(width="680", height="550")
label = Label(Home, text="Bienvenue sur WebTarget !",font='Helvetica 18 bold')
label.place(x=180, y=150)
importer = Button(Home, text="importer csv",command=importer)
importer.config( height = 5, width = 10 )
importer.place(x=220,y=300)
nouveau= Button(Home,text="nouveau")
nouveau.config( height = 5, width = 10 )
nouveau.place(x=390,y=300)

Home.mainloop()