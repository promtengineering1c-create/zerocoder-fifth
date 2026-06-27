import matplotlib.pyplot as plt
import numpy as np  

x1 = np.random.rand(5)
y1 = np.random.rand(5)
plt.scatter(x1, y1, color='r', label='Точки 1')

x2 = np.random.rand(5)
y2 = np.random.rand(5)
plt.scatter(x2, y2, color='b', label='Точки 2')

plt.ylabel('Ось  Y')
plt.xlabel('Ось  X')
plt.title('Диаграмму рассеяния')
plt.legend()

plt.show()
