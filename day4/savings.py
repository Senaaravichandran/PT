class base1:
    def demo1(self):
        self.x=10
        print("say hi!!")
class base2:
    def demo2(self):
        self.y=20
        print("say hello!!")
class child(base1,base2):
    def demo3(self):
        self.z=self.x+self.y
        print(self.x,self.y)
obj=child()
obj.demo1()
obj.demo2() 
obj.demo3()