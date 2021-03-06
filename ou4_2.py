#!/usr/bin/env python3

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
py_n = [i for i in range(n_low, n_high)]
cpp_n = [i for i in range(n_low, n_high)]

for i in range(n_low, n_high):
	
	print('Python code running fib(n) for n =', i)
	py_start_time = pc()
	print(fib_py(i))
	py_end_time = pc()
	print(f'Time in seconds {py_end_time - py_start_time}')
	py_time.append(py_end_time - py_start_time)	

	h = Heltal(i)
	print('C++ code running fib(n) for n =', i)
	cpp_start_time = pc()
	print(h.fib())
	cpp_end_time = pc()
	print(f'Time in seconds {cpp_end_time - cpp_start_time}')
	cpp_time.append(cpp_end_time - cpp_start_time)
	

h_47 = Heltal(47)
print('C++ code running fib(n) for n = 47')
cpp_start_time_47 = pc()
print(h_47.fib())
cpp_end_time_47 = pc()
print(f'Time in seconds {cpp_end_time_47 - cpp_start_time_47}')


plt.plot(py_n, py_time, 'bo', cpp_n, cpp_time, 'ro')
plt.title('fib(n) n vs time')
plt.xlabel('n')
plt.ylabel('Time [s]')
plt.savefig('fib_plot.png')


# def main():
# 	f = Heltal(5)
# 	print(f.get())
# 	f.set(7)
# 	print(f.get())

# if __name__ == '__main__':
# 	main()