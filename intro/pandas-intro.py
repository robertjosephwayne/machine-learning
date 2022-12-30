import numpy
import pandas

# series
my_array = numpy.array([1, 2, 3])
row_names = ['a', 'b', 'c']
my_series = pandas.Series(my_array, index=row_names)
print(my_series)
print(my_series[0])
print(my_series['a'])
