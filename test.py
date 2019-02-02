import math, sys, getopt


# divide
def div(m,n):
    if n <= 0:
        return False
    else:
        a = m / n
        print(a)
        return a


# add
def add(m,n):
    a = m + n
    print(a)
    return a

# mul
def mul(m,n):
    a = m * n
    print(a)
    return a

# sub
def sub(m, n):
    a = m - n
    print(a)
    return a


if __name__ == "__main__":
    function = getattr(sys.modules[__name__], sys.argv[1])
    m = int(sys.argv[2])
    n = int(sys.argv[3])
    function(m,n)