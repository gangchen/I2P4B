name: inverse
layout: true
class: middle, inverse

---
.title[Getting Started Python]

.author[Gang Chen]

.author[chengangcs@gmail.com]

---
# Outline

* Overview
* Installation: Python, Editors and Git
* Hello Python
* Manage your source codes using git and github
---

# Introduction to Python
---

## Overview
.cite[
Python is an easy to learn, powerful programming language. It has efficient high-level data structures and a simple but effective approach to object-oriented programming. Python's elegant syntax and dynamic typing, together with its interpreted nature, make it an ideal language for scripting and rapid application development in many areas on most platforms.
]
---

### Features
* Simple
* Easy to Learn
* Free and Open Source
* High-level Language
* Portable
* Interpreted
* Object Oriented
* Extensible
* Embeddable
* Extensive Libraries
---

### Applications
* Google
* YouTube
* Quora
* Instagram
* Reddit
* Civilization V
* BioPython
* PyMol
* Scikit-learn, NumPy,
* Caffe, Theano, TensorFlow, mxnet and so on

---
### Implementations

* CPython: CPython is the reference implementation of Python, written in C.
* PyPy: PyPy is a Python interpreter implemented in a restricted statically-typed subset of the Python language called RPython. The interpreter features a just-in-time compiler and supports multiple back-ends (C, CLI, JVM).
* JPython: Jython is a Python implementation that compiles Python code to Java bytecode which is then executed by the JVM (Java Virtual Machine). Additionally, it is able to import and use any Java class like a Python module.
* IronPython: IronPython is an implementation of Python for the .NET framework.

---

### Python 3 or 2
* Python 3.0 was released in 2008.
* The final 2.x version 2.7 release came out in mid-2010, with a statement of extended support for this end-of-life release.
* The 2.x branch will see no new major releases after that. 3.x is under active development and has already seen over five years of stable releases, including version 3.3 in 2012, 3.4 in 2014, and 3.5 in 2015.
* [What's new in Python 3](https://docs.python.org/3.0/whatsnew/3.0.html)
---

## Installation

---
### Installation of Python 3

* Windows
    * [Python Releases for Windows](https://www.python.org/downloads/windows/)
* Ubuntu
    * apt-get:
````
    sudo apt-get install python3
````
* MacOS
    * [Python Releases for Mac OS](https://www.python.org/downloads/mac-osx/)
    * Homebrew:
````
brew install python3
````

---

### Installation of IDE or Editor

* PyCharm
* Pydev with Eclipse
* VIM, Emacs
* Notepad++ for Windows
* ATOM from Github (recommended in this course)
* Visual Studio Codes

---
### Installation of Git

Git is the most popular source codes management system.

* Git: https://git-scm.com
* GUI: SourceTree from BitBuckets (Recommended in this course)
* Hosted Git service:
    * Github.com
    * BitBucket.com
    * Coding.net


---
## References
* [A IPython Notebook for Introduction to Python](http://nbviewer.jupyter.org/github/jdwittenauer/ipython-notebooks/blob/master/notebooks/language/Intro.ipynb) also can be used as a reference for 3rd week.
* [Python Courses on codecademy](https://www.codecademy.com/learn/python) an interactive courses of Python for people who don't have any programming experiences.
* [A byte of Python](http://python.swaroopch.com/)
* [The Hitchhiker’s Guide to Python](https://github.com/kennethreitz/python-guide)


---
# Hello Python

```python
print("Hello Python!")
```
---

Interactive Shell
```bash
> python3
> print("Hello Python!")
Hello Python!
```

---
Script
````bash
> python3 hellp.py
Hello Python!
````
---
# Using Git

---

## Create a local repository (GUI)

1. File -> New
2. Copy the hello.py to the directory
3. Add hello.py to track
4. Commit
5. Modify the codes, and commit again.

---
## Create a local repository (Command Line)
````bash
git init
git add hello.py
git commit -m "first commit"
````
---

## Push to remote repository (GUI)
1. Sign up on github or BitBucket or coding.net.
2. Create a new repository on the hosted git service.
3. repository -> add remote repository.
2. Push local repository to remote.

---
## Push to remote repository (Command Line)
````bash
git remote add origin https://github.com/gangchen/hello.git
git push -u origin master
````
