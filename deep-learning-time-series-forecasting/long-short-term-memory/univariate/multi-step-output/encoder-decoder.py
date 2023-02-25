# Example of an Encoder-Decoder LSTM for multi-step-output time series forecasting
from numpy import array
from keras.models import Sequential
from keras.layers import Dense, LSTM, RepeatVector, TimeDistributed


# A model specifically developed for forecasting variable length output sequences is called the Encoder-Decoder LSTM.
# The model was designed for prediction problems where there are both input and output sequences,
# so-called sequence-to-sequence, or seq2seq problems,
# such as translating text from one language to another.
# This model can be used for multi-step-output-output time series forecasting.


# Split a univariate sequence into samples
def split_sequence(sequence, n_steps_in, n_steps_out):
    X, y = list(), list()
    for i in range(len(sequence)):
        # Find the end of this pattern
        end_ix = i + n_steps_in
        out_end_ix = end_ix + n_steps_out
        # Check if we are beyond the sequence
        if out_end_ix > len(sequence):
            break
        # Gather input and output parts of the pattern
        seq_x, seq_y = sequence[i:end_ix], sequence[end_ix:out_end_ix]
        X.append(seq_x)
        y.append(seq_y)
    return array(X), array(y)


# Define input sequence
raw_seq = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# Choose a number of time steps
n_steps_in, n_steps_out = 3, 2

# Split into samples
X, y = split_sequence(raw_seq, n_steps_in, n_steps_out)

# Reshape from [samples, timesteps] into [samples, timesteps, features]
n_features = 1
X = X.reshape((X.shape[0], X.shape[1], n_features))
y = y.reshape((y.shape[0], y.shape[1], n_features))

# Define model
model = Sequential()
model.add(LSTM(100, activation='relu', input_shape=(n_steps_in, n_features)))
model.add(RepeatVector(n_steps_out))
model.add(LSTM(100, activation='relu', return_sequences=True))
model.add(TimeDistributed(Dense(1)))
model.compile(optimizer='adam', loss='mse')

# Fit model
model.fit(X, y, epochs=100, verbose=0)

# Demonstrate prediction
x_input = array([70, 80, 90])
x_input = x_input.reshape((1, n_steps_in, n_features))
yhat = model.predict(x_input, verbose=0)
print(yhat)
