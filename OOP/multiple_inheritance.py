class Teacher:
    def teach(self):
        print("Teacher teaches students")

class Researcher:
    def research(self):
        print("Researcher performs research")

class Professor(Teacher, Researcher):
    def display(self):
        print("Professor is both Teacher and Researcher")

obj = Professor()

obj.teach()
obj.research()
obj.display()
