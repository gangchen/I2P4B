print(type(2))
print(type(1.3))
print(type("Hello"))

print(type(type(1.3)))

message = "Hello"
a = 1.3
b = 0.6
c = 0.7

# the classical question 1.3 - 0.6 == 0.7 ?
a - b == c

# functions and fib sequence
def fib(n):
    a, b = 0, 1
    while a < n:
        print a
        a, b = b, a+b

fib(1000)
