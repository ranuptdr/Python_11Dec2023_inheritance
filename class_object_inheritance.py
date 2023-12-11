#1. Class Defination
class Car: # PascleCase
    #1.1  Property = Variable
    brand = "TATA" # Property
    model = '2024' # Property
    color = 'Black' # Property
    
    #1.2  cunstructor

    #1.3  Method = Function
    def getMyBrand(self): # camleCase
        print(f'brand is {self.brand}') #self is internal class object
        print(f"Model Year is {self.model}") #self is internal class object
        print(f'''color is {self.color}''') #self is internal class object
pass

#2. Create Class Object
# classObject = className
co = Car() # co is a external clas object

# Call the method with classObject
# classObject.method(actualargument1,actualArgument2)
co.getMyBrand() 