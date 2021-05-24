"""
Solutions to module 4
Student: Oskar Ekstrand 
Mail: oskar.ekstrand.1905@student.uu.se
Reviewed by: 
Reviewed date: 
"""

import random
import matplotlib.pyplot as plt
from math import pi

for n in [1000, 10000, 100000]:
    n_c = 0
    n_k = 0
    x_koord = []
    y_koord = []
    x_koord_c = []
    y_koord_c = []

    for k in range(n):
    
        x_koord.append(random.uniform(-1, 1))
        y_koord.append(random.uniform(-1, 1))

        if x_koord[k]**2 + y_koord[k]**2 <= 1:
            n_c += 1
            x_koord_c.append(x_koord[k])
            y_koord_c.append(y_koord[k])
    
        n_k += 1
        pi_est = 4*n_c/n_k

    plt.plot(x_koord, y_koord,'bo',x_koord_c, y_koord_c,'ro')
    plt.show()
    
    print("Estimation of pi =", pi_est)   
    #print("True value of pi =", pi)