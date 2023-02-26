from math import log
from sklearn.datasets import make_regression
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


# Calculate AIC for regression
def calculate_aic(n, mse, num_params):
    aic = n * log(mse) + 2 + num_params
    return aic


# Calculate BIC for regression
def calculate_bic(n, mse, num_params):
    bic = n * log(mse) + num_params * log(n)
    return bic


# Generate a test dataset and fit a linear regression model

# Generate dataset
X, y = make_regression(n_samples=100, n_features=2, noise=0.1)

# Define and fit the model on all data
model = LinearRegression()
model.fit(X, y)

# Number of parameters
num_params = len(model.coef_) + 1
print('Number of parameters: %d' % num_params)

# Predict the training set
yhat = model.predict(X)

# Calculate the error
mse = mean_squared_error(y, yhat)
print('MSE: %.3f' % mse)

# Calculate the AIC
aic = calculate_aic(len(y), mse, num_params)
print('AIC: %.3f' % aic)

# Calculate the BIC
bic = calculate_bic(len(y), mse, num_params)
print('BIC: %.3f' % bic)



