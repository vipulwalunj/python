#Fibonacci
# Program to print Fibonacci numbers


def fib(n):
    a=0
    b=1
    if n==1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            n=a+b
            a=b
            b=n

            print(b)

num=int(input())
fib(num)
