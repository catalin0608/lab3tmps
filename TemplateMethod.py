class Joc:
    def initialize(self):
        pass

    def start_joc(self):
        pass

    def end_joc(self):
        pass

    def joaca(self):
        self.initialize()
        self.start_joc()
        self.end_joc()


class Cricket(Joc):
    def end_joc(self):
        print("Jocul de Cricket s-a încheiat!")

    def initialize(self):
        print("Jocul de Cricket a fost inițializat! Începeți jocul.")

    def start_joc(self):
        print("Jocul de Cricket a început. Bucurați-vă de joc!")


class Football(Joc):
    def end_joc(self):
        print("Jocul de Fotbal s-a încheiat!")

    def initialize(self):
        print("Jocul de Fotbal a fost inițializat! Începeți jocul.")

    def start_joc(self):
        print("Jocul de Fotbal a început. Bucurați-vă de joc!")


if __name__ == "__main__":
    joc = Cricket()
    joc.joaca()
    print()
    joc = Football()
    joc.joaca()
