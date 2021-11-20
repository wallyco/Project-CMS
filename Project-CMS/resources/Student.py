from data.StudentData import StudentData, ListSet


class Student:

    def __init__(self, name=None, id=None, course=None):
        self.name = name
        self.id = id
        self.data = ListSet(course)

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def setID(self, id):
        self.id = id

    def addCourse(self, course):
        self.data.add(course)

    def removeCourse(self, course):
        self.data.remove(course)

    def showCourses(self):
        return print(self.data.__str__())