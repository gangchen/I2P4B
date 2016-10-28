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
Original *seqstat*

````python
from fqstat import count

seq = """ >chr21
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNCGTGCAGTCAGTG
TCTGCCCTTGCTGTTAGCTCCTGGAGGGCTGCGGACGGCACCTGCTGTGT
TTGTGACTGAAGGGCATGTGTTCAGGCAAGATTGTTGGGTGGCTGTGTTT
TGTCTTCTTCCAGCTCGGCCATGGAATAGCCTGTGGGGACCTACTCTGTG
GTCCCCAGGGAGCTACTCTGTGGGGGCTGTTTCTGTTCAGCAGGGAAGGC
TCTGCCCTTGCTGTTAGCTCCTGGAGGGCTGCGGACGGCACCTGCTGTGT
TCACAGATGACAGTTACTTCCCTAGGTAGTCTGCATGTTGGGCCTCCCAG"""

counts = {'A':0, 'C':0,'G':0,'T':0,'N':0}
for base in seq:
    if base in counts.keys():
        counts[base] += 1

print(counts)
````

---
Procedures
````python
from fqstat import count

seq = """ >chr21
NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNCGTGCAGTCAGTG
TCTGCCCTTGCTGTTAGCTCCTGGAGGGCTGCGGACGGCACCTGCTGTGT
TTGTGACTGAAGGGCATGTGTTCAGGCAAGATTGTTGGGTGGCTGTGTTT
TGTCTTCTTCCAGCTCGGCCATGGAATAGCCTGTGGGGACCTACTCTGTG
GTCCCCAGGGAGCTACTCTGTGGGGGCTGTTTCTGTTCAGCAGGGAAGGC
TCTGCCCTTGCTGTTAGCTCCTGGAGGGCTGCGGACGGCACCTGCTGTGT
TCACAGATGACAGTTACTTCCCTAGGTAGTCTGCATGTTGGGCCTCCCAG"""

def count(seq):
    counts = {'A':0, 'C':0,'G':0,'T':0,'N':0}
    for base in seq:
        if base in counts.keys():
            counts[base] += 1

    return(counts)


print(count(seq))

````
---

* *count* function for DNA sequence, RNA sequence, Amino Acid sequence ...:
    * countDNA
    * countRNA
    * countAA
    * ...
* if different display methods are required:
    * print0, DNA, RNA, AA
    * print1, DNA, RNA, AA
    * print2...
    * print3...

---
## OOP

.cite[Object-oriented programming (OOP) is a programming paradigm based on the concept of "objects", which may contain data, in the form of fields, often known as attributes; and code, in the form of procedures, often known as methods.]

-Wikipedia

--


Important features of OOP:
* Abstraction
* Encapsulation
* Polymorphism
* Inheritance

---
## Abstraction
Classes and Instances
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

Polymorphism
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
seqstat in OOP style:
1. Define a parent class named *seq*:
    * variable: *seq*
    * methods: *count*, *print1* and *print2*
2. Define classes *dnaseq*, *rnaseq* and *aaseq* based on *seq* class
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

.cite[Any identifier of the form \_\_spam (at least two leading underscores, at most one trailing underscore) is textually replaced with \_classname\_\_spam, where classname is the current class name with leading underscore(s) stripped. This mangling is done without regard to the syntactic position of the identifier, so it can be used to define class-private instance and class variables, methods, variables stored in globals, and even variables stored in instances. private to this class on instances of other classes.

Name mangling is intended to give classes an easy way to define “private” instance variables and methods, without having to worry about instance variables defined by derived classes, or mucking with instance variables by code outside the class. Note that the mangling rules are designed mostly to avoid accidents; it still is possible for a determined soul to access or modify a variable that is considered private.]

---

Why?

--
.cite[We are all consenting adults here.]

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
redcar.__updateSoftware() # not accesible from object.
redcar._Car__updateSoftware() # is designed mostly to avoid accidents.
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

Polymorphism

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
Inheritance

````python
class User:
    def __init__(self, name=""):
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
## Creating Object

````python
obj = classname()
````
* A empty object is created by default;
* *__init__* method is used to initial object's attributes;

---
## Designing a class for various sequences

see [src/seqstat.py](src/seqstat.py)
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
The **iterator pattern** is a design pattern in which an iterator is used to traverse a container and access the container's elements.

````python
for i in [1,2,3,4]:
    print(i)
````
---

## Decorator Pattern
The **decorator pattern** is a design pattern that allows behavior to be added to an individual object, either statically or dynamically, without affecting the behavior of other objects from the same class.

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
