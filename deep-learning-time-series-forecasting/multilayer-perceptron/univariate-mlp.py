# Univariate MLP example
from numpy import array
from keras.models import Sequential
from keras.layers import Dense

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


# Define input sequence
raw_seq = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# Choose a number of steps
n_steps = 3

# Split into samples
X, y = split_sequence(raw_seq, n_steps)

# Summarize the data
for i in range(len(X)):
    print(X[i], y[i])

# Define model
model = Sequential()
model.add(Dense(100, activation='relu', input_dim=n_steps))
model.add(Dense(1))
model.compile(optimizer='adam', loss='mse')

# Fit model
model.fit(X, y, epochs=2000, verbose=0)

# Demonstrate prediction
x_input = array([70, 80, 90])
x_input = x_input.reshape((1, n_steps))
yhat = model.predict(x_input, verbose=0)
print(yhat)