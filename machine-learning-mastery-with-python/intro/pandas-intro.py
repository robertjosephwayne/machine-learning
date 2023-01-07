import numpy
import pandas

# series
my_array = numpy.array([1, 2, 3])
row_names = ['a', 'b', 'c']
my_series = pandas.Series(my_array, index=row_names)
print(my_series)
print(my_series[0])
print(my_series['a'])

# data frame
my_array = numpy.array([[1, 2, 3], [4, 5, 6]])
row_names = ['a', 'b']
column_names = ['one', 'two', 'three']
my_data_frame = pandas.DataFrame(my_array, index=row_names, columns=column_names)
print(my_data_frame)

print("one column: \n%s" % my_data_frame['one'])
print("one column: \n%s" % my_data_frame.one)
