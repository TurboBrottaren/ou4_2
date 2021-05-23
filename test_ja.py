"""
Solutions to module 4
Student: Oskar Ekstrand
Mail: oskar.ekstrand.1905@student.uu.se
Reviewed by:
Reviewed date: 
"""

from heltal import Heltal
from time import perf_counter as pc
import matplotlib.pyplot as plt


def fib_py(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib_py(n-1) + fib_py(n-2)


py_time = []
cpp_time = []
n_low = 30
n_high = 45
n_list = [[i for i in range(n_low, n_high)]]

for i in range(n_low, n_high):
	
	print('Python code running fib(n) for n =', i)
	py_start_time = pc()
	print(Heltal(i).fib())
	py_end_time = pc()
	print(f'Time in seconds {py_end_time - py_start_time}')
	py_time.append({py_end_time - py_start_time})	

	print('C++ code running fib(n) for n =', i)
	cpp_start_time = pc()
	print(Heltal(i).fib())
	cpp_end_time = pc()
	print(f'Time in seconds {cpp_end_time - cpp_start_time}')
	cpp_time.append({cpp_end_time - cpp_start_time})


print('C++ code running fib(n) for n = 47')
cpp_start_time = pc()
print(Heltal(47).fib())
cpp_end_time = pc()
print(f'Time in seconds {cpp_end_time - cpp_start_time}')


plt.plot(n_list, py_time, 'bo',n_list, cpp_time, 'ro')
plt.title('fib(n) n vs time')
plt.xlabel('n')
plt.ylabel('Time [s]')
plt.savefig('fib_plot.png')