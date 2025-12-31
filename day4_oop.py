#square = lambda x: x * x #lambda function example(Anonymouse 1-line fn)
#print(square(5))
#x=10 #global variable
#def demo() :
    #x=5 #local variable
    #print("inside",x)
#print("outside",x)
#demo()
"""Object Oriented Programming(DAY4)"""
class User:
    def __init__(self,name,age):  #Creating constructor self=default
        self.name =name
        self.age =age
        
    def display(self):
        print(self.name)
        print(self.age)
u1=User("Suraj",18)
u1.display()
