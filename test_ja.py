#!/usr/bin/env python3


from time import perf_counter as pc
import matplotlib.pyplot as plt
from heltal import Heltal


def fib_py(n):
    if n <= 1:
        return n
    else:
        return(fib_py(n-1) + fib_py(n-2))


n1=30
n2=35
time_cpp=[]
n_cpp=[]
time_py=[]
n_py=[]

for n in range(n1,n2):

    k=Heltal(n)
    print(f'fib(n) for C++ with n={n}' )
    start_cpp = pc()
    print(k.fib())
    end_cpp = pc()
    print(f'Time in seconds {round(end_cpp-start_cpp, 2)}')
    time_cpp.append(round(end_cpp-start_cpp, 2))
    n_cpp.append(n)

    print(f'fib(n) for py with n={n}' )
    start_py = pc()
    print(fib_py(n))
    end_py = pc()
    print(f'Time in seconds {round(end_py-start_py, 2)}')
    time_py.append(round(end_py-start_py, 2))
    n_py.append(n)


print(f'fib(n) for C++ with n=47')
start_cpp = pc()
print(Heltal(35).fib())
end_cpp = pc()
print(f'Time in seconds {round(end_cpp-start_cpp, 2)}')

plt.plot(n_cpp,time_cpp ,'bo',n_py, time_py,'ro')
plt.xlabel('n')
plt.ylabel('time in sedonds')
plt.title('time and n')
plt.savefig('fib_c_new.png')