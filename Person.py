class Person:
    
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name : {self.name}\tAge : {self.age}")

p1 = Person("Sakshi", 20)
p2 = Person("Pranay", 12)

p1.display()
p2.display()

