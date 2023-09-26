class Expression:
    def evaluer(self):
        print('err')


class OperateurBinaire(Expression):
    def __init__(self, expGauche, expDroit):
        self.expGauche = expGauche
        self.expDroit = expDroit


class Plus(OperateurBinaire):
    def __init__(self, expGauche, expDroit):
        super().__init__(expGauche, expDroit)

    def evaluer(self):
        return self.expGauche.evaluer() + self.expDroit.evaluer()


class Moins(OperateurBinaire):
    def __init__(self, expGauche, expDroit):
        super().__init__(expGauche, expDroit)

    def evaluer(self):
        return self.expGauche.evaluer() - self.expDroit.evaluer()


class Multiply(OperateurBinaire):
    def __init__(self, expGauche, expDroit):
        super().__init__(expGauche, expDroit)

    def evaluer(self):
        return self.expGauche.evaluer() * self.expDroit.evaluer()


class Divid(OperateurBinaire):
    def __init__(self, expGauche, expDroit):
        super().__init__(expGauche, expDroit)

    def evaluer(self):
        return self.expGauche.evaluer() / self.expDroit.evaluer()


class Constante(Expression):
    def __init__(self, value):
        self.value = value

    def evaluer(self):
        return self.value


test = Multiply(Plus(Divid(Constante(9), Constante(3)), Multiply(Constante(7), Constante(7))), Constante(2))
print(test.evaluer())

print('Done !')
