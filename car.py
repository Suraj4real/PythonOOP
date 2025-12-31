class Car:
    def __init__(self,brand,model,year):
        self.brand =brand
        self.model =model
        self.year =year
    def age(self):
         age=2025-self.year
         return age
    def display(self):
        print(self.brand,self.model,self.year)
c1=Car("Ferrari","SF90 Stradale",2000)
c1.display()
print(f"The age of car is {c1.age()}")

