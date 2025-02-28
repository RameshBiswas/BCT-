class parent:
    def __init__(self,n,r):
        self.n=n
        self.r=r

    def showname(self):
        print("student name is :",self.n)

    def showroll(self):
        print("student roll is :",self.r)

class child(parent):
    def __init__(self,s, n, r):
        super().__init__(n, r)
        self.s=s
    def showstream(self):
        print("student stream is :",self.s)
object1=child("cse","ramesh",23)
object1.showname()
object1.showstream()
object1.showroll()

