class grandpa:
    def __init__(self, grandpa_name):
        self.grandpa_name = grandpaName
class father(grandpa):
    def __init__(self, grandpaName, fathername):
        grandpa.__init__(self, grandpaName)
        self.fathername = fathername
class child(father):
    def __init__(self, grandpaName, fathername, childname):
        father.__init__(self, grandpaName, fathername)
        self.childname = childname
class child1(child):
    def __init__(self, grandpaName, fathername, childname, child1name):
        child.__init__(self, grandpaName, fathername, childname)
        self.child1name = child1name