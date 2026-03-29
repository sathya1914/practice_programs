import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.svm import SVC

# Load the Iris dataset
iris = datasets.load_iris()

# Use only first two features
X = iris.data[:, :2]
y = iris.target

# Train Linear SVM
clf_linear = SVC(kernel='linear')
clf_linear.fit(X, y)

# Create mesh grid
h = 0.02
x_min, x_max = X[:,0].min() - 1, X[:,0].max() + 1
y_min, y_max = X[:,1].min() - 1, X[:,1].max() + 1

xx, yy = np.meshgrid(
    np.arange(x_min, x_max, h),
    np.arange(y_min, y_max, h)
)

# Predict for mesh grid
Z_linear = clf_linear.predict(np.c_[xx.ravel(), yy.ravel()])
Z_linear = Z_linear.reshape(xx.shape)

# Plot decision boundary
plt.contourf(xx, yy, Z_linear, cmap=plt.cm.Paired, alpha=0.8)

# Plot data points
plt.scatter(X[:,0], X[:,1], c=y, cmap=plt.cm.Paired)

plt.title("Linear SVM")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")

plt.xlim(xx.min(), xx.max())
plt.ylim(yy.min(), yy.max())

plt.show()