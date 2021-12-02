class StudentData(object):

    def __init__(self, sourceCollection=None):
        self.collection = set()
        if sourceCollection:
            self.collection = set(sourceCollection)

    def isEmpty(self):
        return len(self.collection) == 0

    def __len__(self):
        return len(self.collection)

    def __str__(self):
        if len(self.collection) == 0:
            return "You have no courses to display"
        else:
            return "{" + ", ".join(map(str, self)) + "}"

    def __iter__(self):
        return iter(self.collection)

    def __add__(self, other):
        result = StudentData(self.collection)
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
            self.collection.add(item)
            print(f"Course '{item}' added.")

    def remove(self, item):
        if item not in self:
            print(f"Course '{item}' not found in registered courses.")
        else:
            self.collection.remove(item)
            print(f"Course '{item}' dropped.")
