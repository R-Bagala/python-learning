import numpy as np

#print numpy version
print("nmpuy:", np.__version__)

python_list = [4, 66, 77, 12, 3]
list_to_numpy = np.array(python_list)
list_to_floatnp = np.array(python_list, dtype=float)
print(list_to_floatnp)
print(type(list_to_numpy))

#we can do the same for multi dimensional arrays
two_dimensional_array = [[6, 12, 3], [66, 88, 90], [66, 98, 120]]
numpy_2d = np.array(two_dimensional_array)

#convert back to list
two_dimensional_array = numpy_2d.tolist()

#creatiung numpy array from tuple
norm_tuple = (55, 78, 12, 33)
numpy_tuple = np.array(norm_tuple) # the exact same way as lists

#we can print the shapes which are the number of rows and columns. 
#if the array is 1d it returns the length

three_x_three = np.array([[3, 6, 7], [9, 8, 7], [6, 7, 1]])
print(three_x_three.shape)

#datatypes ane size
print(three_x_three.dtype)
print(three_x_three.size)

#operations\


random_np = np.array([6, 8, 9, 10, 12], dtype=float)
ten_plus = random_np + 10
minus_6 = random_np - 6
divide_2 = random_np / 2
multiply_by_5 = random_np * 5
#print(f"{ten_plus}\n {minus_6}\n {divide_2}\n {multiply_by_5}\n")
#caries out the operation on every number: for EG add_10 increases all the value sizes by 10

#multi dimensional: 2d array with numpy_2d
first_row = numpy_2d[0]
second_row = numpy_2d[1]
#print(f"{first_row}\n {second_row}")

print(f"First 2 rows and columns: {numpy_2d[0:2, 0:2]}")
print(f"Second value from first row: {numpy_2d[0,1]}")

#zero and 1 matrices
numpy_0s = np.zeros((3,3),dtype=int,order="C")
numpy_1s = np.ones((3,3),dtype=int,order="C")
print(f"{numpy_0s}\n {numpy_1s}")

#flattened
flattened_0s = numpy_0s.flatten()
#print(flattened_0s)

#random numbers
random_floats = np.random.random(5) # creates a numpy array of many random values
print(random_floats)
random_int = np.random.randint(2, 10, size=4) # creates an array of size 4 with numbers between 2 and 10
random_nt = np.random.randint(7, 12, size = (3,3)) # multidimensional array