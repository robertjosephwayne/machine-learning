import matplotlib.pyplot as plt
import numpy

# Basic line plot
my_array = numpy.array([1, 2, 3])
plt.plot(my_array)
plt.xlabel('some x axis')
plt.ylabel('some y axis')
plt.show()

# Basic scatter plot
x = numpy.array([1, 2, 3])
y = numpy.array([2, 4, 6])
plt.scatter(x, y)
plt.xlabel('some x axis')
plt.ylabel('some y axis')
plt.show()
