name: inverse
layout: true
class: center, middle, inverse

---
.title[Computer Systems and Programming]

.author[Gang Chen]

.author[chengangcs@gmail.com]

---


# Information in Computer

## Hello World
```c
#include<stdio>

int main(){
    print("hello world\n");
    return 0;
}
```

---
```shell
> od -t a src/hello.c
```

```
0000000    #   i   n   c   l   u   d   e   <   s   t   d   i   o   .   h
0000020    >  nl  nl   i   n   t  sp   m   a   i   n   (   )   {  nl  sp
0000040   sp  sp  sp   p   r   i   n   t   f   (   "   H   e   l   l   o
0000060   sp   W   o   r   l   d   \   n   "   )   ;  nl   }  nl
0000076
```

---
```shell
> od -t d1 src/hello.c
```
```
0000000    35 105 110  99 108 117 100 101  60 115 116 100 105 111  46 104
0000020    62  10  10 105 110 116  32 109  97 105 110  40  41 123  10  32
0000040    32  32  32 112 114 105 110 116 102  40  34  72 101 108 108 111
0000060    32  87 111 114 108 100  92 110  34  41  59  10 125  10
0000076
```

---

![ASCII Table](imgs/asciifull.gif)

---

## Binary vs. Text

# How to make the source codes executable?




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
