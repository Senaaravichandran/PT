class student:
    def __init__(self,name,number):
        self.name=name
        self.__number=number
class clg(student):
    def data(self):
        print(self._number)
std=clg("senaa",123)
print(std.name)
print(std._number)
std.data()