from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA #导入PCA算法
iris = load_iris()
y=iris.target
X=iris.data
pca = PCA(n_components=2) #引用PCA算法，参数的含义是降维后的维度数
reduced_x = pca.fit_transform(X) #运行算法
red_x, red_y = [], []
blue_x, blue_y = [], []
green_x, green_y = [], []
for i in range(len(reduced_x)):
    if y[i] == 0:
        red_x.append(reduced_x[i][0])
        red_y.append(reduced_x[i][1])
    elif y[i] == 1:
        blue_x.append(reduced_x[i][0])
        blue_y.append(reduced_x[i][1])
    else:
        green_x.append(reduced_x[i][0])
        green_y.append(reduced_x[i][1])
        plt.scatter(red_x, red_y, c='r', marker='.')
        plt.scatter(blue_x, blue_y, c='b', marker='.')
        plt.scatter(green_x, green_y, c='g', marker='.')
        plt.show()