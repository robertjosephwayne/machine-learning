# Example of simulating a binomial process and counting success
from numpy.random import binomial as numpy_binomial
from scipy.stats import binom as scipy_binomial

# Define the parameters of the distribution

# Probability
p = 0.3

# Number of trials
k = 100

# Run a single simulation
success = numpy_binomial(k, p)

print('Total Success: %d' % success)

# Calculate moments
mean, var, _, _ = scipy_binomial.stats(k, p, moments='mvsk')
print('Mean=%.3f, Variance=%.3f' % (mean, var))

# Define the distribution
dist = scipy_binomial(k, p)

# Calculate the probability of n successes
for n in range(10, 110, 10):
    print('P of %d success: %.3f%%' % (n, dist.pmf(n)*100))

# Calculate the probably of <=n successes
for n in range(10, 110, 10):
    print('P of %d success: %.3f%%' % (n, dist.cdf(n)*100))
