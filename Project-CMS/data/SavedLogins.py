# josh is a sample student, and idlist and studentlist are populated with sample testable entries
from resources.Student import Student

josh = Student("josh", "1", "csc130")
hunter = Student("hunter", "2")
hagar = Student("hagar", "3", ("csc130", "test")) #TODO This fails at StudentData Constructor's sourceCollection


# IDList is a dict with items structured {"ID number": "Password"}
IDList = {josh.id: "1", hunter.id: "2", hagar.id: "3"}

# studentlist is a dict with items structured {"ID number": Student object}
studentlist = {josh.id: josh, hunter.id: hunter, hagar.id: hagar}