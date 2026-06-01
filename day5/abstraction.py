class student:
    def __init__(self,name,number):
        self.name=name
        self.__number=number
    def demo(self):
        self.__number=123
std=student("senaa",123)
print(std.name)
print(std.number)
