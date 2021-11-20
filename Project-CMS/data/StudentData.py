class StudentData:  # TODO  or not to do Pretty sure this isn't working properly

    def __init__(self, id=None, course=None):
        self.data = {
            "StudentId": id,
            "StudentCourse": course
        }
        self.size = 0

    def __iter__(self):
        return iter(self.data)

    def add(self, course):
        if self.size == 0:
            self.data["StudentCourse"] = course
            self.size += 1

        if course not in self.data.get("StudentCourse"):
            self.data.get("StudentCourse").add(course)
            print(f"Course '{course}' added.")
            self.size += 1
        else:
            print(f"Course '{course}' already registered.")

    def remove(self, course):
        if course in self.data.get("StudentCourse"):
            self.data.pop("StudentCourse", course)
            print(f"Course '{course}' dropped.")
            self.size -= 1
        else:
            print(f"Course '{course}' not found in registered courses.")

    def coursesToString(self):
        if self.size == 0:
            return print("You have no courses to display")
        return print(self.data["StudentCourse"])


class ListSet(object):

    def __init__(self, sourceCollection=None):
        self.collection = list()
        if sourceCollection:
            self.collection.append(sourceCollection)

    def isEmpty(self):
        return len(self.collection) == 0

    def __len__(self):
        return len(self.collection)

    def __str__(self):
        if len(self.collection) == 0:
            return print(
                "You have no courses to display")  # TODO None is still displayed, its being called in Students showCourses method
        else:
            return "{" + ", ".join(map(str, self)) + "}"

    def __iter__(self):
        return iter(self.collection)

    def __add__(self, other):
        result = ListSet(self.collection)
        for item in other:
            result.add(item)
        return result

    def __eq__(self, other):
        self.collection.sort()
        other.collection.sort()
        return self.collection == other.collection

    def clear(self):
        self.collection.clear()

    def add(self, item):
        if self.collection.__contains__(item):
            print(f"Course '{item}' already registered.")
        else:
            self.collection.append(item)
            print(f"Course '{item}' added.")

    def remove(self, item):
        if item not in self:
            print(f"Course '{item}' not found in registered courses.")
        else:
            self.collection.remove(item)
            print(f"Course '{item}' dropped.")
