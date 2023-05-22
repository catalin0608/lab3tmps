class Strategie:
    def executeaza_operatie(self, num1, num2):
        pass

class OperatieAdunare(Strategie):
    def executeaza_operatie(self, num1, num2):
        return num1 + num2

class OperatieScadere(Strategie):
    def executeaza_operatie(self, num1, num2):
        return num1 - num2

class OperatieInmultire(Strategie):
    def executeaza_operatie(self, num1, num2):
        return num1 * num2

class Context:
    def __init__(self, strategie):
        self.strategie = strategie

    def executa_strategie(self, num1, num2):
        return self.strategie.executeaza_operatie(num1, num2)

# Exemplu de utilizare
context = Context(OperatieAdunare())
print("10 + 5 =", context.executa_strategie(10, 5))

context = Context(OperatieScadere())
print("10 - 5 =", context.executa_strategie(10, 5))

context = Context(OperatieInmultire())
print("10 * 5 =", context.executa_strategie(10, 5))
