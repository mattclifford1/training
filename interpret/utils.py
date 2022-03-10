from sklearn.linear_model import LogisticRegression
import numpy as np
import matplotlib.pyplot as plt
import random
from tqdm import tqdm

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


def plot_with_std(x_axis, y_axis, colour='blue'):
    # y axis is multiple data point we will plot mean and std of
    y_axis = np.array(y_axis)
    mean_diffs = np.mean(y_axis, axis=1)
    std_diffs = np.std(y_axis, axis=1)
    plt.plot(x_axis, mean_diffs, '-', color=colour)
    plt.fill_between(x_axis,
                     mean_diffs - std_diffs,
                     mean_diffs + std_diffs,
                     alpha=0.2,
                     color=colour)

def run_all(clf_original, X, percents, runs=3):
    clf_diffs = []
    for perc in tqdm(percents):
        diff = []
        for i in range(runs):
            X_local, y_local = sample_rand_points(X, clf_original, perc)
            X_weights = weight_locally(X[1,:], X_local)
            clf_explaination = eX_clf(X_local, y_local, X_weights)
            diff.append(clf_difference(clf_original, clf_explaination))
        clf_diffs.append(diff)
    return clf_diffs


if __name__ == '__main__':
    from toy_data import sample_data, plot_data, plot_classifier
    # get data and classifier to explain
    X, y = sample_data()
    clf_original = eX_clf(X, y)
    # plot data and decision boundary
    fig = plt.figure()
    plt.subplot(2, 2, 1)
    plot_data(X, y)
    plot_classifier(clf_original.model)

    # run explaination on different percentages local data
    percents = range(1, 101)
    clf_diffs = run_all(clf_original, X, percents, runs=100)
    # plot results
    plt.subplot(2, 2, 2)
    plot_with_std(percents, clf_diffs)
    plt.show()
