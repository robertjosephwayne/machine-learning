# Calculate the probability of an email in the spam folder being spam

# Consider the case where we receive an email and the spam detector puts it in the spam folder
# What is the probability it was spam?

# Assumptions
# P(A) - 2% of the email we receive is spam
# P(B|A) - When an email is spam it is detected with an accuracy of 99%
# P(B|not A) - When an email is not spam, it is marked as spam with a rate of 0.1%

# Calculate P(A|B) given P(A), P(B|A), P(B|not A)
def bayes_theorem(p_a, p_b_given_a, p_b_given_not_a):
    # Calculate P(not A)
    not_a = 1 - p_a

    # Calculate P(B)
    p_b = p_b_given_a * p_a + p_b_given_not_a * not_a

    # Calculate P(A|B)
    p_a_given_b = (p_b_given_a * p_a) / p_b
    return p_a_given_b


# P(A)
p_a = 0.02

# P(B|A)
p_b_given_a = 0.99

# P(B|not A)
p_b_given_not_a = 0.001

# Calculate P(A|B)
result = bayes_theorem(p_a, p_b_given_a, p_b_given_not_a)

# Summarize
print('P(A|B) = %.3f%%' % (result * 100))

