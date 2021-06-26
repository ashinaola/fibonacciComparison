# Recursive Fibonacci 
import timeit

num = int(input('Enter Integer to calculate the Fibonacci number: '))
print('fibo_rec input: {}'.format(num))

start = timeit.default_timer()
def fibo_rec(n):
    if n < 2:
        return n
    else:
        return fibo_rec(n - 1) + fibo_rec(n - 2)

print('fibo_rec output: {}'.format(fibo_rec(num)))
stop = timeit.default_timer()
print('fibo_rec runtime: {}'.format(stop - start))