"""
structure variabbles

etud = {Nom, prénom, [(note, coef)]}
promo = [Nom, [etud]]
"""


# fonctions
def addNote(etud, note, coef):  # Ajouter une note à un étudiant
    etud['Notes'].append((note, coef))


def createEtud(n, p):
    tmp = {
        "Nom": n,
        "Prénom": p,
        "Notes": []
    }
    return tmp


def moyNote(etud):
    moy, divid, notes = 0, 0, etud['Notes']
    if (len(notes) == 0):
        return None
    else:
        i = 0
        while i < len(notes):
            note, coef = (notes[i])
            j = 0
            while j < coef:
                moy += note
                divid += 1
                j += 1
            i += 1
    return moy / divid


def addEtud(promo, etud):
    promo.append(etud)


def sizePromo(promo):
    return len(promo)


def moyPromo(promo):
    i = 0
    moy, divid = 0, 0
    while i < sizePromo(promo):
        tmp = moyNote(promo[i])
        if (tmp != None):
            moy += tmp
            divid += 1
        i += 1
    return moy / divid


# Exemple d'étudiants
etud1 = createEtud('Martin', "Baptiste")
etud2 = createEtud('Zela', "Xhulio")

promo1 = [etud1, etud2]

# print(promo1)

addNote(etud1, 10, 1)
addNote(etud2, 10, 4)
print(etud1)
print(moyNote(etud1))
print(sizePromo(promo1))
print(moyPromo(promo1))

print('end')
