# Sample a pareto distribution
from numpy.random import pareto as numpy_pareto
from scipy.stats import pareto as scipy_pareto
from matplotlib import pyplot

# Define the distribution
alpha = 1.1
n = 10

# Generate the sample
sample = numpy_pareto(alpha, n)
print(sample)

# PDF and CDF for a pareto distribution

# Define distribution parameter
alpha = 1.5

# Create distribution
dist = scipy_pareto(alpha)

# Plot PDF
values = [value/10.0 for value in range(10, 100)]
probabilities = [dist.pdf(value) for value in values]
pyplot.plot(values, probabilities)
pyplot.show()

# Plot CDF
cumulative_probabilities = [dist.cdf(value) for value in values]
pyplot.plot(values, cumulative_probabilities)
pyplot.show()

