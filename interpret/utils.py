from sklearn.linear_model import LogisticRegression
import numpy as np
import matplotlib.pyplot as plt
import random

def sample_rand_points(X, clf, percent=20):
    # get percentage of points and estimate labels using clf
    total_samples = X.shape[0]
    number_to_sample = int(total_samples*percent/100)
    all_indices = range(total_samples)
    random_indices = random.sample(all_indices, number_to_sample)
    X_random = X[random_indices, :]
    y_random = clf.predict(X_random)
    return X_random, y_random


def weight_locally(point, samples):
    # weight samples based on distance from point of interest

    return [1]*samples.shape[0]   # even weighting for now

def clf_difference(c1, c2):
    # compare difference in clfs weights
    return np.sum(np.abs(c1.get_weights() - c2.get_weights()))


class eX_clf():
    def __init__(self, X, y, sample_weight=None):
        self.model = LogisticRegression(random_state=0).fit(X, y, sample_weight)

    def get_weights(self):
        # b = self.model.intercept_[0]
        weights = self.model.coef_.T
        return weights

    def predict(self, X):
        return self.model.predict(X)



if __name__ == '__main__':
    from toy_data import sample_data
    X, y = sample_data()
    clf_original = eX_clf(X, y)

    percents = []
    clf_diffs = []
    for perc in range(1, 101):
        diff = []
        for i in range(10):
            X_local, y_local = sample_rand_points(X, clf_original, perc)
            X_weights = weight_locally(X[1,:], X_local)
            clf_explaination = eX_clf(X_local, y_local, X_weights)
            diff.append(clf_difference(clf_original, clf_explaination))
        percents.append(perc)
        clf_diffs.append(diff)

    clf_diffs = np.array(clf_diffs)
    mean_diffs = np.mean(clf_diffs, axis=1)
    std_diffs = np.std(clf_diffs, axis=1)
    plt.plot(percents, mean_diffs, '-')
    plt.fill_between(percents,
                     mean_diffs - std_diffs,
                     mean_diffs + std_diffs,
                     alpha=0.2)
    plt.show()
