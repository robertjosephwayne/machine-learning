# Example of Gaussian Naive Bayes
from sklearn.datasets import make_blobs
from sklearn.naive_bayes import GaussianNB

# Generate 2D classification dataset
X, y = make_blobs(n_samples=100, centers=2, n_features=2, random_state=1)

# Define the model
model = GaussianNB()

# Fit the model
model.fit(X, y)

# Select a single sample
Xsample, ysample = [X[0]], y[0]

# Make a probabilistic prediction
yhat_prob = model.predict_proba(Xsample)
print('Predicted Probabilities: ', yhat_prob)

# Make a classification prediction
yhat_class = model.predict(Xsample)
print('Predicted Class: ', yhat_class)
print('Truth: y=%d' % ysample)
