# Iterative Fibonacci 
import timeit

num = int(input('Enter Interger to calculate the Fibonacci number: '))
print('fibo_itr input: {}'.format(num))

start = timeit.default_timer()
def fibo_itr(x):
    a,b = 0,1
    for i in range(x):
        a,b = b,a+b
    return a

print('fibo_itr output: {}'.format(fibo_itr((num))))
stop = timeit.default_timer()
print('fibo_itr runtime: {}'.format(stop - start))