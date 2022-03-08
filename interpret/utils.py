from sklearn.linear_model import LogisticRegression


class clf():
    def __init__(self, X, y):
        self.model = LogisticRegression(random_state=0).fit(X, y)

    def get_weights(self):
        b = self.model.intercept_[0]
        weights = self.model.coef_.T
        return weights

    # def



if __name__ == '__main__':
    from toy_data import sample_data
    X, y = sample_data()
    c1 = clf(X, y)
    print(c1.get_weights())
