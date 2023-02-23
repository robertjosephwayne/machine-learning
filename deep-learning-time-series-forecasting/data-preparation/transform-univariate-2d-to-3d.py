# Transform univariate 2D to 3D
from numpy import array


# Split a univariate sequence into samples
def split_sequence(sequence, n_steps):
    X, y = list(), list()
    for i in range(len(sequence)):
        # Find the end of this pattern
        end_ix = i + n_steps
        # Check if we are beyond the sequence
        if end_ix > len(sequence) - 1:
            break
        # Gather input and output parts of the pattern
        seq_x, seq_y = sequence[i:end_ix], sequence[end_ix]
        X.append(seq_x)
        y.append(seq_y)
    return array(X), array(y)


# Define univariate time series
series = array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(series.shape)

# Transform to a supervised learning problem
X, y = split_sequence(series, 3)
print(X.shape, y.shape)

# Transform input from [samples, features] to [samples, timesteps, features]
X = X.reshape(X.shape[0], X.shape[1], 1)
print(X.shape)