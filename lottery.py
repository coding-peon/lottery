import random

class Lottery:

    contents = []

    def __init__(self, num):
        self.contents.clear()
        max = self.convert_to_int(num)
        for i in range(max):
            self.contents.append(i+1)

    def convert_to_int(self, num):
        try:
            whole = int(float(num))
            return whole
        except:
            print("Error: This variable should be a number. Variable: ", num)
            return 0

    def draw(self, num):
        howmany = self.convert_to_int(num)
        if howmany > len(self.contents):
            return ("No such lottery.")
        else:
            drawn_numbers = []
            for i in range(howmany):
                length = len(self.contents)
                j = random.randrange(length)
                item = self.contents.pop(j)
                drawn_numbers.append(item)
            return drawn_numbers