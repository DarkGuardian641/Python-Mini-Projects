# Parent Class
class Employee:
    # Constructor
    def __init__(self,name,occupation,networth) -> None:
        self.name = name
        self.occupation = occupation
        self.networth = networth

    # Decorator
    def greet(fx):
        def mfx(*args, **kwargs):
            print("Welcome to the program.")
            fx(*args, **kwargs)
            print("Byeee \n")
        return mfx

    # Using decorators
    @greet

    # Functions inside the class
    def info(self):
        print(f"{self.name} is a {self.occupation} and his networth is ${self.networth}")

#Inherited Class
class Programmer(Employee) :
    def showlang(self):
        print(f"{self.name} codes in Python")

a = Employee("Harry","Developer",10000)
b = Employee("Riyan","HR",15000)
c = Employee("Shubham","Sales Manager",25000)

a.info()
b.info()
c.info()

d = Programmer("Jake","Developer",60000)
d.info() 
d.showlang()