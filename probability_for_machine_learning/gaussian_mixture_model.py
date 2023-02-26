# Example of fitting a gaussian mixture model with expectation maximization
from numpy import hstack
from numpy.random import normal
from sklearn.mixture import GaussianMixture

# Generate a sample
X1 = normal(loc=20, scale=5, size=3000)
X2 = normal(loc=40, scale=5, size=7000)
X = hstack((X1, X2))

# Reshape into a table with one column
X = X.reshape((len(X), 1))

# Fit model
model = GaussianMixture(n_components=2, init_params='random')
model.fit(X)

# Predict latent values
yhat = model.predict(X)

# Check latent value for first few points
print(yhat[:100])

# Check latent value for last few points
print(yhat[-100:])
