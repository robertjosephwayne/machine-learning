# Sample an exponential distribution
from numpy.random import exponential as numpy_exponential
from scipy.stats import expon as scipy_exponential
from matplotlib import pyplot

# Define the distribution
beta = 50
n = 10

# Generate the sample
sample = numpy_exponential(beta, n)
print(sample)

# PDF and CDF for an exponential distribution
dist = scipy_exponential(beta)

# Plot PDF
values = [value for value in range(50, 70)]
probabilities = [dist.pdf(value) for value in values]
pyplot.plot(values, probabilities)
pyplot.show()

# Plot CDF
cumulative_probabilities = [dist.cdf(value) for value in values]
pyplot.plot(values, cumulative_probabilities)
pyplot.show()
