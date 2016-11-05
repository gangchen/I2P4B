name: inverse
layout: true
class: middle, inverse

---
.title[Python in Bioinformatics]

.author[Gang Chen]

.author[chengangcs@gmail.com]

---
# Outline

* BioPython
* scikit-bio
* Orange and Orange-bioinformatics
* FASTA Projects
---

# BioPython

---

## Overview
.cite[
The Biopython Project is an international association of developers of freely available Python tools for computational molecular biology.]

.cite[
The Biopython web site (http://www.biopython.org) provides an online resource for modules, scripts, and web links for developers of Python-based software for bioinformatics use and research.
]
---

## Features

* The ability to parse bioinformatics files into Python utilizable data structures. Files in the supported formats can be iterated over record by record or indexed and accessed via a Dictionary interface.
* Code to deal with popular on-line bioinformatics destinations.
* Interfaces to common bioinformatics programs.
* A standard sequence class that deals with sequences, ids on sequences, and sequence features.
* Tools for performing common operations on sequences, such as translation, transcription and weight calculations.
* Code to perform classification of data using k Nearest Neighbors, Naive Bayes or Support Vector Machines.

---
## Features cont.
* Code for dealing with alignments, including a standard way to create and deal with substitution matrices.
* Code making it easy to split up parallelizable tasks into separate processes.
* GUI-based programs to do basic sequence manipulations, translations, BLASTing, etc.
Extensive documentation and help with using the modules, including this file, on-line wiki documentation, the web site, and the mailing list.
* Integration with BioSQL, a sequence database schema also supported by the BioPerl and BioJava projects.
---

## Installation

* Download and install
* pip
* Package manager of your system
    * apt for Ubuntu
    * brew for MacOS

see doc for details.footnote[see http://biopython.org/DIST/docs/install/Installation.html].
---
## Quick Getting Started

see src/seqio_biopy.py
---

# scikit-bio

---

## Overview

scikit-bio™ is an open-source, BSD-licensed, python package providing data structures, algorithms, and educational resources for bioinformatics.

* Codes: https://github.com/biocore/scikit-bio
* Cookbook: [Jupyrt Notebook]( http://nbviewer.jupyter.org/github/biocore/scikit-bio-cookbook/blob/master/Index.ipynb)
---

## Features

* File I/O (skbio.io)
* Sequences (skbio.sequence)
* Alignments (skbio.alignment)
* Tree representations (skbio.tree)
* Constructing workflows (skbio.workflow)
* Diversity calculations (skbio.diversity)
* Statistics (skbio.stats)
* Utility functionality (skbio.util)

---
## Example

see src/seqio_skbio.py

---
# Orange and Orange-bioinformatics

---

## Orange

.cite[Open source machine learning and data visualization for novice and expert. Interactive data analysis workflows with a large toolbox.]
---
## Orange-Bioinformatics

A Orange Widget for Bioinformatics.

---
# FASTA Projects
