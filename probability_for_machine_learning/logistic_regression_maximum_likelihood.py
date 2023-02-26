# Test of Bernoulli likelihood function

# Likelihood function for Bernoulli distribution
def likelihood(y, y_hat):
    return y_hat * y + (1 - y_hat) * (1 - y)

# Test for y=1
y, y_hat = 1, 0.9
print('y=%.1f, yhat=%.1f, likelihood: %.3f' % (y, y_hat, likelihood(y, y_hat)))
y, y_hat = 1, 0.1
print('y=%.1f, yhat=%.1f, likelihood: %.3f' % (y, y_hat, likelihood(y, y_hat)))

# Test for y=0
y, y_hat = 0, 0.1
print('y=%.1f, yhat=%.1f, likelihood: %.3f' % (y, y_hat, likelihood(y, y_hat)))
y, y_hat = 0, 0.9
print('y=%.1f, yhat=%.1f, likelihood: %.3f' % (y, y_hat, likelihood(y, y_hat)))