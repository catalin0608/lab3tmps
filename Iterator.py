class Iterator:
    def are_urmatorul(self):
        pass

    def urmatorul(self):
        pass


class Container:
    def obtine_iterator(self):
        pass


class RepositoryNume(Container):
    nume = ["Robert", "John", "Julie", "Lora"]

    def obtine_iterator(self):
        return self.IteratorNume()

    class IteratorNume(Iterator):
        def __init__(self):
            self.index = 0

        def are_urmatorul(self):
            if self.index < len(RepositoryNume.nume):
                return True
            return False

        def urmatorul(self):
            if self.are_urmatorul():
                nume = RepositoryNume.nume[self.index]
                self.index += 1
                return nume
            raise StopIteration


class IteratorNumeIterable:
    def __init__(self, iterator_nume):
        self.iterator_nume = iterator_nume

    def __iter__(self):
        return self

    def __next__(self):
        return self.iterator_nume.urmatorul()


if __name__ == "__main__":
    repository_nume = RepositoryNume()
    iterator_nume = repository_nume.obtine_iterator()
    iterator_nume_iterabil = IteratorNumeIterable(iterator_nume)

    for nume in iterator_nume_iterabil:
        print("Nume: " + nume)
