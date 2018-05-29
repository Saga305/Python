def fib(n):
    a, b = 0, 1
    while n:
       a, b = b, a+b
       print (b)
       n = n-1

fib(9)