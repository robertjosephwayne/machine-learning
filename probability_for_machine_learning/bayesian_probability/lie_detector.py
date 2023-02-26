# Calculate the probability of a person lying given a positive lie detector result.

# Consider the case where a person is tested with a lie detector
# and gets a positive result suggesting that they are lying.
# What is the probability that the person is actually lying?

# Assumptions
# P(A) - 2% of people that are tested are lying
# P(B|A) - When someone is lying, the test can detect them 72% of the time
# P(not B|not A) - When the machine says someone is not lying, this is true 97% of the time

# Calculate P(A|B) given P(A), P(B|A), P(not B|not A)
def bayes_theorem(p_a, p_b_given_a, p_not_b_given_not_a):
    # Calculate P(not A)
    not_a = 1 - p_a
    # Calculate P(B|not A)
    p_b_given_not_a = 1 - p_not_b_given_not_a
    # Calculate P(B)
    p_b = p_b_given_a * p_a + p_b_given_not_a * not_a
    # Calculate P(A|B)
    p_a_given_b = (p_b_given_a * p_a) / p_b
    return p_a_given_b

# P(A), base rate
p_a = 0.02
# P(B|A)
p_b_given_a = 0.72
# P(not B|not A)
p_not_b_given_not_a = 0.97
# Calculate P(A|B)
result = bayes_theorem(p_a, p_b_given_a, p_not_b_given_not_a)
# Summarize
print('P(A|B) = %.3f%%' % (result * 100))
