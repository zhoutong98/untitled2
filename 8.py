import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression

x = np.arange(-10, 10)
y = [-22, -19.2, -14.9, -16, -13, -14, -9, -8,
     -5.5, -3.5, -2, 1.8, 3.3, 5, 9, 9, 11.5, 13, 18, 17]
print(x)
print("---------------")
print(y)
plt.scatter(x, y)
plt.show()
