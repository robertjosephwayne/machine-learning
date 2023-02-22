# Calculate the probability of an elderly person dying from a fall

# Consider the case where an elderly person (over 80 years of age) falls
# What is the probability that they will die from the fall?

# Assumptions
# P(A) - The base rate of someone elderly dying is 10%
# P(B) - The base rate for elderly people falling is 5%
# P(B|A) - 7% of all elderly people that die had a fall

# Calculate P(A|B) given P(B|A), P(A) and P(B)
# P(A|B) = P(B|A) * P(A) / P(B)
def bayes_theorem(p_a, p_b, p_b_given_a):
    p_a_given_b = p_b_given_a * p_a / p_b
    return p_a_given_b


# P(A)
p_a = 0.10

# P(B)
p_b = 0.05

# P(B|A)
p_b_given_a = 0.07

# Calculate P(A|B)
result = bayes_theorem(p_a, p_b, p_b_given_a)

# Summarize
print('P(A|B) = %.3f%%' % (result * 100))

