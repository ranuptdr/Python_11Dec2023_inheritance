class MyParent(): #Base class
    #1.1  Property
    bloodGroup = '+Ove'

    #1.2  Constructor

    #1.3  Method
    pass

class MyChild(MyParent): # derived class
    #1.1  Property

    #1.2  Constructor

    #1.3  Method
    def getMyBloodGroup(self):
        print(f"My Blood Group is {self.bloodGroup}")
    pass

# Create Class Object
# We always Create object of child class
co = MyChild()
co.getMyBloodGroup() # classObject.method