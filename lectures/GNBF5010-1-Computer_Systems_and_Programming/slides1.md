name: inverse
layout: true
class: middle, inverse

---
.title[Computer Systems and Programming]

.author[Gang Chen]

.author[chengangcs@gmail.com]

---


# Information in Computer

---
## Hello World
.left-column[
Text File
```c
#include<stdio>

int main(){
    print("hello world\n");
    return 0;
}
```
]
--

.right-column[
ASCII Characters
```bash
> od -t a src/hello.c
```

```bash
0000000    #   i   n   c   l   u   d   e   <   s   t   d   i   o   .   h
0000020    >  nl  nl   i   n   t  sp   m   a   i   n   (   )   {  nl  sp
0000040   sp  sp  sp   p   r   i   n   t   f   (   "   H   e   l   l   o
0000060   sp   W   o   r   l   d   \   n   "   )   ;  nl   }  nl
0000076
```
]

---

.left-column[
ASCII Characters
```bash
> od -t a src/hello.c
```

```bash
0000000    #   i   n   c   l   u   d   e   <   s   t   d   i   o   .   h
0000020    >  nl  nl   i   n   t  sp   m   a   i   n   (   )   {  nl  sp
0000040   sp  sp  sp   p   r   i   n   t   f   (   "   H   e   l   l   o
0000060   sp   W   o   r   l   d   \   n   "   )   ;  nl   }  nl
0000076
```
]

--

.right-column[
ASCII Codes
```bash
> od -t d1 src/hello.c
```

```bash
0000000    35 105 110  99 108 117 100 101  60 115 116 100 105 111  46 104
0000020    62  10  10 105 110 116  32 109  97 105 110  40  41 123  10  32
0000040    32  32  32 112 114 105 110 116 102  40  34  72 101 108 108 111
0000060    32  87 111 114 108 100  92 110  34  41  59  10 125  10
0000076
```
]

---

.left-column[
ASCII Codes
```bash
> od -t d1 src/hello.c
```

```bash
0000000    35 105 110  99 108 117 100 101  60 115 116 100 105 111  46 104
0000020    62  10  10 105 110 116  32 109  97 105 110  40  41 123  10  32
0000040    32  32  32 112 114 105 110 116 102  40  34  72 101 108 108 111
0000060    32  87 111 114 108 100  92 110  34  41  59  10 125  10
0000076
```
]

.right-column[
![ASCII Table](imgs/asciifull.gif)
]

---
Binary

```bash
> xxd -b src/hello.c
0000000: 00100011 01101001 01101110 01100011 01101100 01110101  #inclu
0000006: 01100100 01100101 00111100 01110011 01110100 01100100  de<std
000000c: 01101001 01101111 00101110 01101000 00111110 00001010  io.h>.
0000012: 00001010 01101001 01101110 01110100 00100000 01101101  .int m
0000018: 01100001 01101001 01101110 00101000 00101001 01111011  ain(){
000001e: 00001010 00100000 00100000 00100000 00100000 01110000  .    p
0000024: 01110010 01101001 01101110 01110100 01100110 00101000  rintf(
000002a: 00100010 01001000 01100101 01101100 01101100 01101111  "Hello
0000030: 00100000 01010111 01101111 01110010 01101100 01100100   World
0000036: 01011100 01101110 00100010 00101001 00111011 00001010  \n");.
000003c: 01111101 00001010
```
---

## Non-ASCII Characters?

---

## Floating Numbers?

---

# How to make the source codes executable?

---

## Preprocessing

---

## Compilation

---

## Assembly

---

## Linking


---
# What happened when you run the program?

Content 1.2


---
# Storage

Content 2.1


---
# Operating Systems

Content 3.1

---
# Network

Content 3.2

---
# Advanced Topics
