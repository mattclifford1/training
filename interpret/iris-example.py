from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt

X, y = load_iris(return_X_y=True)
clf = LogisticRegression(random_state=0).fit(X, y)
clf.predict(X[:2, :])


plot_colours = {0:'red', 1:'blue', 2:'green'}

for features, label in zip(X, y):
    print(features)
    plt.scatter(features[0], features[1], 1, color=plot_colours[label])

plt.axis('equal')
plt.show()
