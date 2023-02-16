# Example of generating a small classification dataset
from sklearn.datasets import make_blobs
from scipy.stats import norm
from numpy import mean, std


# Fit a probability distribution to a univariate data sample
def fit_distribution(data):
    # Estimate distribution
    mu = mean(data)
    sigma = std(data)
    print(mu, sigma)

    # Fit distribution
    dist = norm(mu, sigma)
    return dist


# Calculate the independent conditional probability
def probability(X, prior, dist1, dist2):
    return prior * dist1.pdf(X[0]) * dist2.pdf(X[1])


# Generate 2D classification dataset
X, y = make_blobs(n_samples=100, centers=2, n_features=2, random_state=1)

# Sort data into classes
Xy0 = X[y == 0]
Xy1 = X[y == 1]
print(Xy0.shape, Xy1.shape)

# Calculate priors
priory0 = len(Xy0) / len(X)
priory1 = len(Xy1) / len(X)
print(priory0, priory1)

# Create PDFs for y==0
distX1y0 = fit_distribution(Xy0[:, 0])
distX2y0 = fit_distribution(Xy0[:, 1])

# Create PDFs for y==1
distX1y1 = fit_distribution(Xy1[:, 0])
distX2y1 = fit_distribution(Xy1[:, 1])

# Classify one example
Xsample, ysample = X[0], y[0]
py0 = probability(Xsample, priory0, distX1y0, distX2y0)
py1 = probability(Xsample, priory1, distX1y1, distX2y1)
print('P(y=0 | %s) = %.3f' % (Xsample, py0*100))
print('P(y=1 | %s) = %.3f' % (Xsample, py1*100))
print('Truth: y=%d' % ysample)
