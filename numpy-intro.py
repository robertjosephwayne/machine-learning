import numpy

# define an array
my_list = [1, 2, 3]
my_array = numpy.array(my_list)
print(my_array)
print(my_array.shape)

# access values
my_list = [[1, 2, 3], [3, 4, 5]]
my_array = numpy.array(my_list)
print(my_array)
print(my_array.shape)
print("First row: %s" % my_array[0])
print("Last row: %s" % my_array[-1])
print("Specific row and column: %s" % my_array[0, 2])
print("Whole column: %s" % my_array[:, 2])
