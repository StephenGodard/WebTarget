class ajouter:
    newWindow = Tk()

    def __init__(self):
        self.car="@"
        self.fr="fr"
        self.com="com"
    def add(self,Entry):
        if self.car in Entry:
            if self.com in Entry:
                Adress = open("listeAdress.csv", "a")
                Adress.write(Adresslist)
                Adress.write("\n")
                Adress.close()


            elif self.fr in Entry:
                Adress = open("listeAdress.csv", "a")
                Adress.write(Adresslist)
                Adress.write("\n")
                Adress.close()
        print("adress mail incorrect !")