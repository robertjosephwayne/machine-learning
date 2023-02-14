# Example of converting between probability and odds
from math import log
from math import exp

# Define probability of success
prob = 0.8
print('Probability %.1f' % prob)

# Convert probability to odds
odds = prob / (1 - prob)
print('Odds %.1f' % odds)

# Convert back to probability
prob = odds / (odds + 1)
print('Probability %.1f' % prob)

# Example of converting between probability and log-odds

# Define probability of success
prob = 0.8
print('Probability %.1f' % prob)

# Convert probability to odds
odds = prob / (1 - prob)
print('Odds %.1f' % odds)

# Convert odds to log-odds
logodds = log(odds)
print('Log-Odds %.1f' % logodds)

# Convert log-odds to a probability
prob = 1 / (1 + exp(-logodds))
print('Probability %.1f' % prob)

