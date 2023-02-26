from numpy import array

# Define the dataset
data = list()
n = 5000
for i in range(n):
    data.append([i + 1, (i + 1) * 10])
data = array(data)

# If the time series data is uniform over time and there are no missing values, we can drop the time column.
# Otherwise, need to look at imputing the missing values, resampling the data to a new time scale,
# or developing a model that can handle missing values

# Drop time column
data = data[:, 1]

# LSTMs work best with 200 to 400 time steps. Therefore, we need to split the 5,000 time steps
# into multiple shorter sub-sequences.

# Split into samples (e.g. 5000/200 = 25)
samples = list()
length = 200

# Step over the 5,000 in jumps of 200
for i in range(0, n, length):
    # Grab from i to i + 200
    sample = data[i:i+length]
    samples.append(sample)

# Convert list of arrays into 2D array
data = array(samples)

# Reshape into [samples, timesteps, features]
data = data.reshape((len(samples), length, 1))
print(data.shape)