# Example of simulating a multinomial process
from numpy.random import multinomial as numpy_multinomial
from scipy.stats import multinomial as scipy_multinomial

# Define the parameters of the distribution

# Probability of each category
p = [1.0/3.0, 1.0/3.0, 1.0/3.0]

# Number of trials
k = 100

# Run a single simulation
cases = numpy_multinomial(k, p)

# Summarize cases
for i in range(len(cases)):
    print('Case %d: %d' % (i+1, cases[i]))


# Calculate the probability for a given number of events of each type

# Define the distribution
dist = scipy_multinomial(k, p)

# Define a specific number of outcomes from 100 trials
cases = [33, 33, 34]

# Calculate the probability for the scenario
probability = dist.pmf(cases)

# Print as a percentage
print('Case=%s, Probability: %.3f%%' % (cases, probability*100))
