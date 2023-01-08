# Sample a normal distribution
from numpy.random import normal as numpy_normal
from scipy.stats import norm as scipy_normal
from matplotlib import pyplot

# Define the distribution
mu = 50
sigma = 5
n = 10

# Generate the sample
sample = numpy_normal(mu, sigma, n)
print(sample)

# PDF and CDF for a normal distribution

# Create distribution
dist = scipy_normal(mu, sigma)

# Plot PDF
values = [value for value in range(30, 70)]
probabilities = [dist.pdf(value) for value in values]
pyplot.plot(values, probabilities)
pyplot.show()

# Plot CDF
cumulative_probabilities = [dist.cdf(value) for value in values]
pyplot.plot(values, cumulative_probabilities)
pyplot.show()

# Calculate the values that define the middle 95%
low_end = dist.ppf(0.025)
high_end = dist.ppf(0.975)
print('Middle 95%% between %.1f and %.1f' % (low_end, high_end))
