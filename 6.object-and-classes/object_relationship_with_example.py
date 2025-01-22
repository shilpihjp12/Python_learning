# has a relationship like company has an employee. This is a has-a relationship.
# is-a class is inheritance relationship. robot can be dog or cat or any other animal. This is a is-a relationship.

# like robot can walk and manage battery and their name can be common functions and their speaking and eating behaviour can be different

class Robot:

  def __init__(self, name_val):
    self.name = name_val
    self.position = [0,0]
    print("Robot is created with name: ", self.name)

  def walk(self, x):
    self.position[0] += x
    print(f'Robot is walking to position {self.position}')
  
  def eat(self):
    print("I am Hungry")


class RobotDog(Robot): #inheritence
  def make_noise(self):
    print("Woof Woof!")

  def eat(self):
    super().eat() #calling parent class method in child class
    print("I like Becon!")

class RobotCat(Robot): #inheritence
  def make_noise(self):
    print("Meow Meow!")

def main():
  my_dog = RobotDog("Tommy")
  my_dog.walk(10)
  my_dog.make_noise()
  my_dog.eat()

  print("-------------------")

  my_cat = RobotCat("Kitty")
  my_cat.walk(20)
  my_cat.make_noise()

main()