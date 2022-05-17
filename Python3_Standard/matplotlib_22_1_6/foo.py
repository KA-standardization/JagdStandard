import numpy as np
import matplotlib.pyplot as plt

x = np.array(np.arange(-5, 5.2, 0.2))
y = x ** 2
plt.figure(figsize=(5, 5))
plt.plot(x, y)
plt.show()

