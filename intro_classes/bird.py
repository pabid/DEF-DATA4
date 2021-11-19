from abc import ABC, abstractmethod

#super class
class Bird(ABC):
    fly = True
    babies = 0

    def noise(self):
        return "Squawk"

    def reproduce(self):
        self.babies += 1

    @abstractmethod
    def eat(self):
        pass

    extinct = False

#sub class
#Polymorphism to override the reproduce method
#Abstraction with the eat method and 
# Inheritance in this child class.
class Owl(Bird):

    def reproduce(self):
        self.babies += 6

    def eat(self):
        return "Peck peck"  


#For this subclass we have used 
# Polymorphism to override the reproduce method and Fly and extinct variables, 
# Encapsulation to keep the babies variable from being directly accessed as well as 
# Inheritance again to create a child class of Bird.
class Dodo(Bird):
    Fly = False
    extinct = True

    def eat(self):
        return "Nom nom"

    def reproduce(self):
        if not self.extinct:
            self.babies += 1


#Can't instantiate abstract class Bird with abstract method eat
#so have to use the owl subclass beause the abstract method has been
#implement
#use bird class
# chicken = Bird()
# chicken.noise = "cluck"
# chicken.reproduce()
# chicken.fly =False
# chicken.extinct =False
# eat = chicken.eat("grains")

# print(f"Chickens make the {chicken.noise} sound./n Produces {chicken.reproduce} chicks, fly ={chicken.fly} and ")


#use owl class

barn=Owl()
barn.fly =True
barn.noise ="hoot"
barn.eat = "worms"
barn.reproduce =6
barn.extinct =False
print(f"Barn owls eat {barn.eat} and make the {barn.noise} sound.\nProduces {barn.reproduce} owlings, fly ={barn.fly} and extinct = {barn.extinct}")



#use dodo class

pigeons =Dodo()
pigeons.noise ="sqwalking"
food = pigeons.eat()
pigeons.reproduce =0
if pigeons.extinct:
    extinct = "extinct"

if pigeons.fly:
    fly = "fly"


print(f"The Dodo bird is {extinct}, could not {fly}, ate {food} and known to made the {pigeons.noise} sound.")


