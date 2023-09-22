# ------------- Classes / Fonctions -------------

class Etudiant: # classe Etudiant

    # @nom
    def __init__(self, nom, prenom): # method init de la classe Etudiant
        self.nom = nom
        self.prenom = prenom
        self.notes = []

    def ajouterNote(self, note, coef): # method ajouterNote permettant d'ajouter une note à un étudiant
        self.notes.append((note, coef))

    def nbNotes(self): # method nbNotes permettant de retourner le nombre de notes de l'étudiant
        return len(self.notes)

    def moyenne(self): # method moyenne permettant de retourner la moyenne de l'étudiant
        moy, divid, notes, size = 0, 0, self.notes, self.nbNotes()
        if(size == 0):
            return None
        else:
            i = 0
            while i < size:
                note, coef = (notes[i])
                j = 0
                while j < coef:
                    moy += note
                    divid += 1
                    j += 1
                i += 1
        return moy / divid

    # def print(self): # debug
    #    print(self.notes)


class Promotion: # classe Promotion

    def __init__(self, nom): # method init de la classe Promotion
        self.nom = nom
        self.etudiants = []

    def ajouterEdudiant(self, etud): # method ajouterEtudiant permettant d'ajouter un étudiant à une promotion
        self.etudiants.append(etud)

    def nbEtudiants(self): # method nbEtudiants permettant de retourner le nombre d'étudiants de la promotion
        return len(self.etudiants)

    def moyenne(self): # method moyenne permettant de retourner la moyenne de la promotion
        i, moy, divid, etudiants, size = 0, 0, 0, self.etudiants, self.nbEtudiants()
        while i < size:
            tmp = etudiants[i].moyenne()
            if(tmp != None):
                moy += tmp
                divid += 1
            i += 1
        return moy / divid


# ------------- main -------------

etud1 = Etudiant("Dupont", "Jean")
etud1.ajouterNote(20, 1)
etud1.ajouterNote(10, 2)
etud1.ajouterNote(0, 4)
print(f"La moyenne de {etud1.prenom} {etud1.nom} est {etud1.moyenne()}")

etud2 = Etudiant("Martin", "Baptiste")
etud2.ajouterNote(13, 1)
etud2.ajouterNote(15, 2)
etud2.ajouterNote(8, 3)
print(f"La moyenne de {etud2.prenom} {etud1.nom} est {etud2.moyenne()}")


etud3 = Etudiant("Zela", "Xhulio")
etud3.ajouterNote(17, 1)
etud3.ajouterNote(13, 3)
etud3.ajouterNote(9, 0.5)
print(f"La moyenne de {etud2.prenom} {etud1.nom} est {etud3.moyenne()}")


promo1 = Promotion("L3")
promo1.ajouterEdudiant(etud1)
promo1.ajouterEdudiant(etud2)
promo1.ajouterEdudiant(etud3)

print(f'La moyenne de la promotion {promo1.nom} est {promo1.moyenne()}')
print('end')