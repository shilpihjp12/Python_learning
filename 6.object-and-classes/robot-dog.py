#class Robot_Dog:
class Robot_Dog:
  # self is a reference to the current instance of the class and mendatory to be there in the init function
  def __init__(self, name_val, breed_val):
    self.name = name_val
    self.breed = breed_val
  
  # self we have to use always in the class methods for getting refrence of clas
  def bark(self):
    print("Woof Woof!")
  
my_dog = Robot_Dog("Tommy", "German Shepherd")
print(my_dog.name)
my_dog.bark()