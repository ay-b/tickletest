import math


# divide
def div(m,n):
    if n <= 0:
        return False
    else:
        a = m / n
        return a


# add
def add(m,n):
    a = m + n
    return a

# mul
def mul(m,n):
    a = m * n
    return a

# Fibonacci
def fib(n):
    a, b = 1, 1
    for i in range(n - 1):
        a, b = b, a + b
    return a


# square
def sqr(n):
    a = n * n
    return a



# sub
def sub(m, n):
    a = m - n
    return a


# cube
def cube(n):
    a = n * n * n
    return a


# sqrt
def sqr_r(n):
    a = math.sqrt(n)
    return a

# def calc():
#     if choice == 1:
#         a = int(raw_input("enter first number : "))
#         b = int(raw_input("enter second number : "))
#         c = add(a,b)
#         print c
#
#     elif choice == 2:
#         a = int(raw_input("enter first number : "))
#         b = int(raw_input("enter second number : "))
#         c = sub(a,b)
#         print c
#
#     elif choice == 3:
#         a = int(raw_input("enter first number : "))
#         b = int(raw_input("enter second number : "))
#         c = mul(a,b)
#         print c
#
#     elif choice == 4:
#         a = int(raw_input("enter first number : "))
#         b = int(raw_input("enter second number : "))
#         c = div(a,b)
#         print c
#
#     elif choice == 5:
#         a = int(raw_input("enter number : "))
#         b = sqr(a)
#         print b
#
#     elif choice == 6:
#         a = int(raw_input("enter number : "))
#         b = sqr_r(a)
#         print b
#
#     elif choice == 7:
#         a = int(raw_input("enter number : "))
#         b = cube(a)
#         print b
#
#     elif choice == 8:
#         a = int(raw_input("enter number : "))
#         b = fib(a)
#         print b
#
#     elif choice == 9:
#         exit()
#
# while True:
#     choice = int(raw_input("enter the option : \n1.addition \n2.subtraction \n3.multiplication \n4.divide"
#                        "\n5.square"
#                        "\n6.square root"
#                        "\n7.cube"
#                        "\n8.fibonacci"
#                        "\n9.exit \n"))
#     calc()
