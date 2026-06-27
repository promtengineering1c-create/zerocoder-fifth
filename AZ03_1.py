import matplotlib.pyplot as plt
import numpy as np  

data = np.random.normal(0, 1, 1000)

plt.hist(data)
plt.ylabel('Ось  Y')
plt.xlabel('Ось  X')
plt.title('Гистограмма')

plt.show()

