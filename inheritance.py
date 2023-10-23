class Animal:
    def speak(self):
        print("Animal speaking")
class Dog(Animal):
    def bark(self):
        print("Dog barks")

class DogChild(Dog):
    def eats(self):
        print("Drinking milk")

dog=Dog()  #this is the object
dog.bark()
dog.speak()

dogmgogo=DogChild() #object2
dogmgogo.bark()
dogmgogo.speak()
dogmgogo.eats()


