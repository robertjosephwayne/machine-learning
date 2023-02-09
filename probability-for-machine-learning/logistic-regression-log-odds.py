# Example of converting between probability and odds

# Define probability of success
prob = 0.8
print('Probability %.1f' % prob)

# Convert probability to odds
odds = prob / (1 - prob)
print('Odds %.1f' % odds)

# Convert back to probability
prob = odds / (odds + 1)
print('Probability %.1f' % prob)
