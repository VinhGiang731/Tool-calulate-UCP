# UAW
class Actor:
    def __init__(self, simple=0, average=0, complex=0):
        self.simple = simple
        self.average = average
        self.complex = complex

    def calculate_UAW(self):
        return self.simple * 1 + self.average * 2 + self.complex * 3

    def number_Of_User(self):
        return self.simple + self.average + self.complex

    def input(self):
        print("Enter number actor are simple: ")
        self.simple = int(input())
        print("Enter number actor are average: ")
        self.average = int(input())
        print("Enter number actor are complex: ")
        self.complex = int(input())