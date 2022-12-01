import numpy as np
import matplotlib.pyplot as plt
import math


x = np.linspace(-3, 10, 51)
y = 2*np.sin(x)+np.log2(np.fabs(x))

plt.plot(x, y, 'm--', label='y=3x^3-8')
# декоративна частина
plt.axis([-3, 5, -10, 4])
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.title('Графік функції ')
plt.legend()

plt.show()
plt.savefig('page.svg')