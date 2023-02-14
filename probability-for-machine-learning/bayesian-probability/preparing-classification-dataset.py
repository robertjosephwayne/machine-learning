# Example of generating a small classification dataset
from sklearn.datasets import make_blobs

# Generate 2D classification dataset
X, y = make_blobs(n_samples=100, centers=2, n_features=2, random_state=1)

# Summarize
print(X.shape, y.shape)
print(X[:5])
print(y[:5])

