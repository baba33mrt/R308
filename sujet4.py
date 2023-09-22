class Heure:
    def __init__(self, heure=0, minute=0):  # constructeur

        self.heure = heure
        self.minute = minute

    """
    fonction toString permettant d'afficher l'heure
    """

    def toString(self):
        # print(f"{self.heure}H {self.minute}min")
        return f"{self.heure}H {self.minute}min"

    """
    fonction compareTo permettant de comparer deux heures
    paramètre : checkHeure de type Heure
    """

    def compareTo(self, checkHeure):
        # print("---------- compareto ----------")
        # print(f'{self.heure} {self.minute}')
        # print(f'{checkHeure.heure} {checkHeure.minute}')

        # --- tests de comparaison ---
        if self.heure < checkHeure.heure or (self.heure >= checkHeure.heure and self.minute < checkHeure.minute):
            return -1
        elif self.heure == checkHeure.heure and self.minute == checkHeure.minute:
            return None
        elif self.heure > checkHeure.heure or (self.heure <= checkHeure.heure and self.minute > checkHeure.minute):
            return 1
        else:
            print('err')
            return 2


"""
====================================================================
classes Creneau 
====================================================================
"""


# classe Creneau
class Creneau:
    def __init__(self, startH=0, startM=0, endH=0, endM=0):  # constructeur
        self.type = None
        self.start = Heure(startH, startM)
        self.end = Heure(endH, endM)



    def typeof(self):
        return self.type

    """
    fonction edit permettant de modifier les horaires d'un créneau
    paramètre : startH, startM, endH, endM de type int
    """

    def edit(self, startH=0, startM=0, endH=0, endM=0):
        self.start = Heure(startH, startM)
        self.end = Heure(endH, endM)

    """
    fonction conflitWith
    paramètre : crenneau2 de type Creneau
    """

    def conflitWith(self, crenneau2):
        e1s2check = crenneau2.start.compareTo(self.end)  # -1
        e2s1check = crenneau2.end.compareTo(self.start)  # 1

        """
        si s2 < e1 and e2 > s1 ==> col
        """
        # print('---------------')
        # print(e2s1check)
        # print(e1s2check)
        # print('---------------')

        if (e1s2check == -1 and e2s1check == 1):
            return True
        else:
            return False

    """
    methode dureeInMin permettant de retourner la durée d'un créneau
    """

    def dureeInMin(self):
        return (self.end.heure - self.start.heure) * 60 + (self.end.minute - self.start.minute)




# classe CreneauCours
class CreneauCours(Creneau):
    def __init__(self, startH=0, startM=0, endH=0, endM=0):  # constructeur
        super().__init__(startH, startM, endH, endM)
        self.type = "Cours"


    """
    methode dureeInMin permettant de retourner la durée d'un cours
    """

    def dureeInMin(self):
        return (self.end.heure - self.start.heure) * 60 + (self.end.minute - self.start.minute) + (
                    (self.end.heure - self.start.heure) * 60 + (self.end.minute - self.start.minute)) / 2



class CrenneauTD(Creneau):
    def __init__(self, startH=0, startM=0, endH=0, endM=0):  # constructeur
        super().__init__(startH, startM, endH, endM)
        self.type = "TD"

    """
    methode dureeInMin permettant de retourner la durée d'un TD
    """

    def dureeInMin(self):
        return (self.end.heure - self.start.heure) * 60 + (self.end.minute - self.start.minute)


# classe CrenneauTP
class CrenneauTP(Creneau):
    def __init__(self, startH=0, startM=0, endH=0, endM=0):  # constructeur
        super().__init__(startH, startM, endH, endM)
        self.type = "TP"

    """
    methode dureeInMin permettant de retourner la durée d'un TP
    """

    def dureeInMin(self):
        return 2 * (((self.end.heure - self.start.heure) * 60 + (self.end.minute - self.start.minute)) / 3)


# classe Planning
class Planning:
    def __init__(self):  # constructeur
        self.creneaux = []

    """
    methode ajourerCrenneau permettant d'ajouter un créneau au planning
    paramètre : startH, startM, endH, endM de type int
    """

    def ajourerCrenneau(self, startH=0, startM=0, endH=0, endM=0):
        crenneau = Creneau(startH, startM, endH, endM)
        for i in self.creneaux:
            if crenneau.conflitWith(i):
                return {"error": "conflit de creéneau"}
        self.creneaux.append(crenneau)
        # print('Crénneau ajouté')

    def ajourerCrenneauObj(self, crenneau):
        for i in self.creneaux:
            if crenneau.conflitWith(i):
                return {"error": "conflit de creéneau"}
        self.creneaux.append(crenneau)
        # print('Crénneau ajouté')
    """
    methode dureeTotal permettant de retourner la durée totale du plannin
    """

    def dureeTotal(self):
        duretotal = 0
        for crenneau in self.creneaux:
            duretotal += crenneau.dureeInMin()
        return duretotal


    """
    methode afficher permettant d'afficher le planning dans la console
    """
    def afficher(self):
        print("+-------------------------------+")

        for crenneau in self.creneaux:
            print(f'[{crenneau.start.toString()} - {crenneau.end.toString()}] {crenneau.typeof()}')

        print("+-------------------------------+")





# ------------- main -------------

time = Heure(10, 3)
time.toString()

time2 = Heure(22, 4)
time2.toString()

cren1 = Creneau(10, 0, 16, 0)
cren2 = Creneau(15, 3, 17, 4)

planning = Planning()
planning.ajourerCrenneau(18, 0, 22, 0)

print(planning.dureeTotal())

td = CrenneauTD(10, 0, 16, 0)
print(f"durée TD : {td.dureeInMin()}")
print(td.typeof())
cours = CreneauCours(10, 0, 16, 0)
print(f"durée Cours : {cours.dureeInMin()}")
print(cours.typeof())
tp = CrenneauTP(10, 0, 16, 0)
print(f"durée TP : {tp.dureeInMin()}")
print(tp.typeof())


planning.ajourerCrenneauObj(tp)

# afficher planning
planning.afficher()