class Parent:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        print(">> Parent Constructor Executed")

    def showDetails(self):
        print("Hello, ",self.fname, self.lname)


class Child(Parent):   # Realtionship -> IS-A
    def __init__(self, fname, lname, vehicles, salary):
        Parent.__init__(self, fname, lname)
        self.vehicles = vehicles
        self.salary = salary
        print(">> Child Constructor Executed")

    #def show(self):
        #print("Hello, ",self.fname, self.lname, self.vehicles, self.salary)

    # Overriding
    #def showDetails(self):
        #print("Hello in Child, ", self.fname, self.lname, self.vehicles, self.salary)

    def showDetails(self):
        #Parent.showDetails(self)
        print("Hello in Child, ", self.vehicles, self.salary)

print("Parent Class Dictionary: ",Parent.__dict__)
print("Child Class Dictionary: ",Child.__dict__)

ch = Child("John", "Watson", 2, 3000)
#ch.fname = "George"
#ch.lname = "Klin"
print(ch.__dict__)
ch.showDetails()  # Child.showDetails(ch)
#ch.show()
Parent.showDetails(ch)

# Parent.showDetails(ch)

# Rule 2 : In Child to have customizations, we shall access Parent's Properties :)
# Funda : If same function with the same name is also available in Child -> OVERRIDING