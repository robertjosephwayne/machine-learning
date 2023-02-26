# Example of plotting a histogram of a random sample
from matplotlib import pyplot
from numpy.random import normal as numpy_normal
from numpy import mean
from numpy import std
from numpy import hstack
from numpy import asarray
from numpy import exp
from scipy.stats import norm as scipy_normal
from sklearn.neighbors import KernelDensity

# Generate a sample
sample = numpy_normal(size=1000)

# Plot a histogram of the sample
pyplot.hist(sample, bins=10)
pyplot.show()

# Example of parametric density estimation

# Generate a sample
sample = numpy_normal(loc=50, scale=5, size=1000)
sample_mean = mean(sample)
sample_std = std(sample)
print('Mean=%.3f, Standard Deviation=%.3f' % (sample_mean, sample_std))

# Define the distribution
dist = scipy_normal(sample_mean, sample_std)

# Sample probabilities for a range of outcomes
values = [value for value in range(30, 70)]
probabilities = [dist.pdf(value) for value in values]

# Plot the histogram and PDF
pyplot.hist(sample, bins=10, density=True)
pyplot.plot(values, probabilities)
pyplot.show()

# Example of a bimodal data sample

# Generate a sample
sample1 = numpy_normal(loc=20, scale=5, size=300)
sample2 = numpy_normal(loc=40, scale=5, size=700)
sample = hstack((sample1, sample2))

# Plot the histogram
pyplot.hist(sample, bins=50)
pyplot.show()

# Example of kernel density estimation for a bimodal data sample

# Fit density
model = KernelDensity(bandwidth=2, kernel='gaussian')
sample = sample.reshape((len(sample), 1))
model.fit(sample)

# Sample probabilities for a range of outcomes
values = asarray([value for value in range(1, 60)])
values = values.reshape((len(values), 1))
probabilities = model.score_samples(values)
probabilities = exp(probabilities)

# Plot the histogram and PDF
pyplot.hist(sample, bins=50, density=True)
pyplot.plot(values[:], probabilities)
pyplot.show()
