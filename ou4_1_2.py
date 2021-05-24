"""
Solutions to module 4
Student: Oskar Ekstrand 
Mail: oskar.ekstrand.1905@student.uu.se
Reviewed by: 
Reviewed date: 
"""

import random
import functools
from math import pi


def HypersphereVolume(n, d):
    inside = 0
    for i in range(n):
        koord = [0]
        for k in range(d):
            koord.append(random.uniform(-1,1))
        coords_inside = functools.reduce(lambda s, i : s + i**2, koord) <=1
        if coords_inside:
            inside +=1
    return 2**d * inside/n

print(f'Volume of an n-ball with n = 10000 d = 11 {HypersphereVolume(10000, 11)}')
print(f'Volume of an n-ball with n = 10000 d = 2 {HypersphereVolume(10000, 2)}')
