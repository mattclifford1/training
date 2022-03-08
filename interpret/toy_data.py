from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import numpy as np
import matplotlib.pyplot as plt
from IPython import embed


def get_normal_dist_data(mean, cov, samples=1000):
    return np.random.multivariate_normal(mean, cov, samples)

def plot_classifier(clf):
    b = clf.intercept_[0]
    w1, w2 = clf.coef_.T
    # Calculate the intercept and gradient of the decision boundary.
    c = -b/w2
    m = -w1/w2

    # Plot the data and the classification with the decision boundary.
    axes = plt.gca()
    xmin, xmax = axes.get_xlim()
    ymin, ymax = axes.get_ylim()
    xd = np.array([xmin, xmax])
    yd = m*xd + c
    plt.plot(xd, yd, 'k', lw=1, ls='--')
    plt.fill_between(xd, yd, ymin, color='tab:blue', alpha=0.2)
    plt.fill_between(xd, yd, ymax, color='tab:orange', alpha=0.2)
    # plt.xlim(xmin, xmax)
    # plt.ylim(ymin, ymax)
    return [xmin, xmax, ymin, ymax]

def plot_surrogate(b, w1, w2, lims):
    c = -b/w2
    m = -w1/w2
    axes = plt.gca()
    xmin, xmax, ymin, ymax = lims
    xd = np.array([xmin, xmax])
    yd = m*xd + c
    plt.plot(xd, yd, 'k', lw=1, ls=':')

def sample_data():

    means = [[10, 2],
             [5, 6],
             [2, 3]]

    covs = [[[1, 0],
             [0, 4]],

            [[3, 1],
             [2, 2]],

            [[1, 0],
             [0, 4]]]

    labels = [0, 1, 1]

    X = np.array(np.array([means[0]]))
    y = np.array(labels[0])
    for mean, cov, label in zip(means, covs, labels):
        features = get_normal_dist_data(mean, cov)
        X = np.concatenate((X, features), axis=0)
        for sample in range(features.shape[0]):
            y = np.append(y, label)
        # plot
    return X, y


if __name__ == '__main__':
    X, y = sample_data()

    plot_colours = {0:'red', 1:'blue'}
    plt.scatter(X[:,0], X[:,1], 1, color=np.vectorize(plot_colours.get)(y))

    clf = LogisticRegression(random_state=0).fit(X, y)
    clf.predict(X[:2, :])
    lims = plot_classifier(clf)


    import lime.lime_tabular
    explainer = lime.lime_tabular.LimeTabularExplainer(X, discretize_continuous=True)
    i = np.random.randint(0, X.shape[0])
    exp = explainer.explain_instance(X[i], clf.predict_proba, num_features=2, top_labels=1)
    plt.plot(X[i, 0], X[i, 1], 'x')
    plot_surrogate(exp.intercept[1], exp.local_exp[1][0][1],exp.local_exp[1][1][1], lims)
    plt.axis('equal')
    plt.show()
