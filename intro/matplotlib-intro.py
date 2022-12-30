import matplotlib.pyplot as plt
import numpy

# basic line plot
my_array = numpy.array([1, 2, 3])
plt.plot(my_array)
plt.xlabel('some x axis')
plt.ylabel('some y axis')
plt.show()
