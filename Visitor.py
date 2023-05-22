class ParteCalculator:
    def accepta(self, vizitatorParteCalculator):
        pass


class Tastatura(ParteCalculator):
    def accepta(self, vizitatorParteCalculator):
        vizitatorParteCalculator.viziteaza_tastatura(self)


class Monitor(ParteCalculator):
    def accepta(self, vizitatorParteCalculator):
        vizitatorParteCalculator.viziteaza_monitorul(self)


class Mouse(ParteCalculator):
    def accepta(self, vizitatorParteCalculator):
        vizitatorParteCalculator.viziteaza_mouse(self)


class Calculator(ParteCalculator):
    def __init__(self):
        self.piese = [Mouse(), Tastatura(), Monitor()]

    def accepta(self, vizitatorParteCalculator):
        for parte in self.piese:
            parte.accepta(vizitatorParteCalculator)
        vizitatorParteCalculator.viziteaza_calculatorul(self)


class VizitatorParteCalculator:
    def viziteaza_calculatorul(self, calculator):
        pass

    def viziteaza_mouse(self, mouse):
        pass

    def viziteaza_tastatura(self, tastatura):
        pass

    def viziteaza_monitorul(self, monitor):
        pass


class VizitatorAfisareParteCalculator(VizitatorParteCalculator):
    def viziteaza_calculatorul(self, calculator):
        print("Afișare Calculator.")

    def viziteaza_mouse(self, mouse):
        print("Afișare Mouse.")

    def viziteaza_tastatura(self, tastatura):
        print("Afișare Tastatură.")

    def viziteaza_monitorul(self, monitor):
        print("Afișare Monitor.")


if __name__ == "__main__":
    calculator = Calculator()
    vizitator = VizitatorAfisareParteCalculator()
    calculator.accepta(vizitator)
