class baseclass:
    def __init__(self, name):
        self.name = name

    def data(self):
        print(self.name)
class chilsclass(baseclass):
    def smaple(self):
        print("Hii",self.name)
obj = chilsclass("Senaa")
obj.data()
obj.smaple()