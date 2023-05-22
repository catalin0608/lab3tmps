class Student:
    def __init__(self):
        self.rollNo = None
        self.name = None

    def getRollNo(self):
        return self.rollNo

    def setRollNo(self, rollNo):
        self.rollNo = rollNo

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name


class StudentView:
    def printStudentDetails(self, studentName, studentRollNo):
        print("Student: ")
        print("Nume: " + studentName)
        print("Număr matricol: " + studentRollNo)


class StudentController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def setStudentName(self, name):
        self.model.setName(name)

    def getStudentName(self):
        return self.model.getName()

    def setStudentRollNo(self, rollNo):
        self.model.setRollNo(rollNo)

    def getStudentRollNo(self):
        return self.model.getRollNo()

    def updateView(self):
        self.view.printStudentDetails(self.model.getName(), self.model.getRollNo())


def retrieveStudentFromDatabase():
    student = Student()
    student.setName("Robert")
    student.setRollNo("10")
    return student


if __name__ == "__main__":
    model = retrieveStudentFromDatabase()
    view = StudentView()
    controller = StudentController(model, view)

    controller.updateView()

    controller.setStudentName("John")

    controller.updateView()
