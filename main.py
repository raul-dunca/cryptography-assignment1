import math
import time
import timeit
from datetime import datetime


def substraction(a,b):
    if a==0:                # if a is 0 we return b
        return b
    if b==0:                # if b is 0 we return a
        return a

    while a!=b:            # loop until a and b are different
        if a>b:            # if a is bigger than b, we subtract b from a
            a-=b
        else:              # if b is bigger than a, we subtract a from b
            b-=a

    return a

def euclidian(a,b):
    while b:                # loop until b is 0
        rest= a%b
        a=b
        b=rest
    return a

def stein(a,b):
    if a == 0:          # if a is 0 we return b
        return b
    if b == 0:          # if b is 0 we return a
        return a

    k=0
    while a%2==0 and b%2==0:        # if both numbers are even we divide them by 2 and keep the power of 2
        a=a // 2                    # we stop when one of the numbers becomes odd
        b=b // 2
        k+=1

    while a%2==0:
        a=a // 2
                                   # a is odd now

    while b:                       # loop until b is 0
        while b % 2 == 0:          # if b is even we divide by 2 until it becomes odd
            b = b // 2
        if a>b:                    # if a>b we swap a and b
            b,a=a,b
        b=b-a

    return a * (2 ** k)           # return a * 2 to the power of k, k being the number of times a and b were both divisble by 2

inputs=[[12,16],
        [13,121],
        [15,0],
        [0,23],
        [51,1],
        [2468135790,8642097530],
        [123456789012345678901234567890,246913578024691357802469135780],
        [4137524, 1227244],
        [83 ** 17, 41 ** 17],
        [131 * 200, 131 * 89],
        #[239810420482048219048291084209148214923232212, 42984109481948902840912849021412]
            ]



for input in inputs:
    a=input[0]
    b=input[1]

    print("//////////////////////////")
    print("a = "+ str(a) +" b = "+ str(b) +'\n')

    print("Euclidean Division GCD")
    #start = time.time_ns()
    time = timeit.timeit(lambda: euclidian(a, b), number=1000)
    rez = euclidian(a, b)
    #end = time.time_ns()
    print(f"Time elapsed: {time:.7f} ")
    print("Gcd is: "+ str(rez) + '\n')

    print("Stein’s GCD")
    #start = time.time_ns()
    time = timeit.timeit(lambda: stein(a, b), number=1000)
    rez = stein(a, b)
    #end = time.time_ns()
    print(f"Time elapsed: {time:.7f} ")
    print("Gcd is: "+ str(rez) + '\n')

    print("Euclidean Subtraction GCD")
    #start = time.time_ns()
    time = timeit.timeit(lambda: stein(a, b), number=1000)
    rez = substraction(a, b)
    #end = time.time_ns()
    print(f"Time elapsed: {time:.7f} ")
    print("Gcd is: "+ str(rez) + '\n')



