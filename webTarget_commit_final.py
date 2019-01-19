import tkinter
import csv
import time
from tkinter import *
from tkinter import filedialog
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import requests
from bs4 import BeautifulSoup
import re
def refreshList(name):
    namefilepath=name
    liste = Listbox()
    liste.configure(width="45", height="15")
    i = 1
    with open(namefilepath, 'r') as FILE:
        for ligne in FILE.readlines():
            liste.insert(i, ligne)
            ++i

    liste.place(x=20, y=250)


def Add(namefilepath):

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
    name=namefilepath
    buttonPrint = Button(newWindow, text="ok", command=lambda: Ajouter(name))

    buttonPrint.place(x=75, y=105)

def crawlToImport(url,namefilepath):
    url1=url.get()
    plainPage = requests.get(url1).text
    beautifulPage = str(BeautifulSoup(plainPage, "html.parser"))
    result = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+', beautifulPage)

    str1 = ''.join(result)
    FILE = open(namefilepath, "a")
    FILE.write(str1)
    FILE.write("\n")
    FILE.close()
    print(list(set(result)))

def crawlformail(name):
    namefilepath=name
    newWindow = Tk()

    newWindow.geometry("600x250")

    newWindow.title("URL")

    labelurl = Label(newWindow, text="Importer un url")
    labelurl.place(x=75, y=50)
    url = Entry(newWindow, width=30, justify='right')
    url.place(x=75,y=75)
    buttonurl = Button(newWindow, text="ok", command=lambda: crawlToImport(url,namefilepath))
    buttonurl.place(x=75, y=105)




def Ajouter(name):
    car = "@"
    com = ".com"
    fr = ".fr"
    namefilepath=name
    Adresslist = newAdress.get()
    if car in Adresslist:
        if com in Adresslist:
            Adress = open(namefilepath, "a")
            Adress.write(Adresslist)
            Adress.write("\n")
            Adress.close()

            print("Ajouter !")



        elif fr in Adresslist:
            Adress = open(namefilepath, "a")
            Adress.write(Adresslist)
            Adress.write("\n")
            Adress.close()

            print("Ajouter !")

    print("adress mail incorrect !")
def importer():
    Home.destroy()
    main = Tk()
    main.geometry("500x500")


    double = Button(main, text="Dédoubloner", command=lambda: double)
    double.configure(width="10", height="3")
    double.place(x=75, y=100)
    liste = Listbox(main)
    liste.configure(width="45", height="15")
    filepath = filedialog.askopenfilename(filetypes=[('csv files', '.csv')])
    i=0
    j=45
    namefilepath = filepath[j]

    lenghtFilepath = len(filepath)
    for j in range(j + 1, lenghtFilepath):
        namefilepath = namefilepath + filepath[j]
    buttonAdd = Button(main, text="Ajouter", command=lambda: Add(namefilepath))
    buttonAdd.configure(width="10", height="3")
    buttonAdd.place(x=75, y=25)
    buttonRefresh = Button(main, text="Rafraichir", command=lambda:refreshList(namefilepath))
    buttonRefresh.configure(width="10", height="3")
    buttonRefresh.place(x=200, y=25)
    buttonURL = Button(main, text="import url", command=lambda: crawlformail(namefilepath))
    buttonURL.configure(width="10", height="3")
    buttonURL.place(x=200, y=100)
    with open(namefilepath, 'r') as FILE:
        for ligne in FILE.readlines():
            liste.insert(i, ligne)
            ++i

    liste.place(x=20, y=250)


def newfile():
    Home.destroy()
    main = Tk()
    main.geometry("500x500")
    double = Button(main, text="Dédoubloner", command=lambda: double)
    double.configure(width="10", height="3")
    double.place(x=75, y=100)
    liste = Listbox(main)
    liste.configure(width="45", height="15")
    filepath = filedialog.asksaveasfilename(initialdir = "/home/stephen/PycharmProjects/untilted1/venv",title = "Select file",filetypes = (("csv files","*.csv"),("all files","*.*")))
    i = 0
    j = 45
    namefilepath = filepath[j]

    lenghtFilepath=len(filepath)
    for j in range(j+1, lenghtFilepath):

        namefilepath = namefilepath + filepath[j]
    print(namefilepath)

    buttonAdd = Button(main, text="Ajouter", command=lambda: Add(namefilepath))
    buttonAdd.configure(width="10", height="3")
    buttonAdd.place(x=75, y=25)
    buttonRefresh = Button(main, text="Rafraichir", command=lambda: refreshList(namefilepath))
    buttonRefresh.configure(width="10", height="3")
    buttonRefresh.place(x=200, y=25)
    with open(namefilepath, 'w+') as FILE:
        FILE.close()
    liste.place(x=20, y=250)






Home = Tk()

Home.configure(width="680", height="550")
label = Label(Home, text="Bienvenue sur WebTarget !",font='Helvetica 18 bold')
label.place(x=180, y=150)
importer = Button(Home, text="importer csv",command=importer)
importer.config( height = 5, width = 10 )
importer.place(x=220,y=300)
nouveau= Button(Home,text="nouveau",command=newfile)
nouveau.config( height = 5, width = 10 )
nouveau.place(x=390,y=300)

Home.mainloop()
