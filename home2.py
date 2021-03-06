import random
import itertools as count
import pandas as pd
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

x_val = []#1, 2, 3, 4, 5]
y_val = []#1, 4, 9, 16, 25]

#plt.plot(x_val, y_val)

index = count.count()

def animate(i):
    x_val.append(next(index))
    y_val.append(random.randint(0, 5))
    plt.cla()
    plt.plot(x_val, y_val)

ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()