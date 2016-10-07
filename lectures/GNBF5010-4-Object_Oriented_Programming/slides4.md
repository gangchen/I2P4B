name: inverse
layout: true
class: middle, inverse

---
.title[Object Oriented Programming]

.author[Gang Chen]

.author[chengangcs@gmail.com]

---
# Outline

OOP = Object Oriented Programming
* OOP Basics
* OOP in Python
* Design Pattern in Python
* Examples
---

# OOP Basics
---
## OOP
---
## Classes and Instances
* Objects Combine state (data) and behavior (algorithms).
Encapsulation
* Classes Define what is common for a whole class of objects
---
<img src="imgs/classes_instances.png" width="800">
---

<img src="imgs/dog.gif" width="800">
---

### Encapsulation
Dividing the code into a public interface, and a private implementation of that interface.

In an object oriented python program, you can restrict access to methods and variables.
This can prevent the data from being modified by accident and is known as *encapsulation*.
---

Encapsulation of Methods and Variables

|Type |	Description|
|-----|------------|
|public methods	| Accessible from anywhere|
|private methods|	Accessible only in their own class. starts with two underscores|
|public variables |Accessible from anywhere|
|private variables|	Accessible only in their own class or by a method if defined. starts with two underscores|
---



### Polymorphism
The ability to overload standard operators so that they have appropriate behavior based on their context
Inheritance.
````python
class Bear(object):
    def sound(self):
        print("Groarrr")

class Dog(object):
    def sound(self):
        print("Woof woof!")

def makeSound(animalType):
    animalType.sound()


bearObj = Bear()
dogObj = Dog()

makeSound(bearObj)
makeSound(dogObj)
````

---
### Inheritance
The ability to create subclasses that contain specializations of their parents.

````python
class User:
    name = ""

    def __init__(self, name):
        self.name = name

    def printName(self):
        print("Name  = " + self.name)

class Programmer(User):
    def __init__(self, name):
        self.name = name

    def doPython(self):
        print("Programming Python")

brian = User("brian")
brian.printName()

diana = Programmer("Diana")
diana.printName()
diana.doPython()
````
---

# OOP in Python
---
## Defining Class
````python
class ClassName:
  Class Body
````

````python
class dog:
  def __init__(self):
    self.color = "yellow"
    self.size = "big"
    self.age = 4
````

---
## Defining Method

````python
class ClassName:
  def MethodName(self, paramters):
    method body
````

---

Encapsulation in Python

`Any identifier of the form \_\_spam (at least two leading underscores, at most one trailing underscore) is textually replaced with \_classname\_\_spam, where classname is the current class name with leading underscore(s) stripped. This mangling is done without regard to the syntactic position of the identifier, so it can be used to define class-private instance and class variables, methods, variables stored in globals, and even variables stored in instances. private to this class on instances of other classes.

Name mangling is intended to give classes an easy way to define “private” instance variables and methods, without having to worry about instance variables defined by derived classes, or mucking with instance variables by code outside the class. Note that the mangling rules are designed mostly to avoid accidents; it still is possible for a determined soul to access or modify a variable that is considered private.`

---
Private methods
````python
class Car:

    def __init__(self):
        self.__updateSoftware()

    def drive(self):
        print('driving')

    def __updateSoftware(self):
        print('updating software')

redcar = Car()
redcar.drive()
#redcar.__updateSoftware()  not accesible from object.
````

---

Encapsulation

Private variables

````python
class Car:

    __maxspeed = 0
    __name = ""

    def __init__(self):
        self.__maxspeed = 200
        self.__name = "Supercar"

    def drive(self):
        print('driving. maxspeed ' + str(self.__maxspeed))

redcar = Car()
redcar.drive()
redcar.__maxspeed = 10  # will not change variable because its private
redcar.drive()
````
---

---
## Creating Object
---
## Calling Method
---
## Designing a class for FASTA sequence
---


# Design Pattern in Python
---

## Design Pattern
In software engineering, a software design pattern is a general reusable solution
to a commonly occurring problem within a given context in software design.

Best reference is “Design Patterns. Elements of Reusable Object-Oriented
Software.” (1995), written by the “Gang of Four” (GoF).
---

## Iterator Pattern

---

## Decorator Pattern
---
## Strategy Pattern

---
# Examples

---
## BioPython
SeqIO in BioPython:
* [Tutorial](http://biopython.org/DIST/docs/tutorial/Tutorial.html)
* [Source Codes](https://github.com/biopython/biopython/tree/master/Bio/SeqIO)
---
## TADtool
[TADtool: visual parameter identification for TAD-calling algorithms](http://bioinformatics.oxfordjournals.org/content/32/20/3190.full)
