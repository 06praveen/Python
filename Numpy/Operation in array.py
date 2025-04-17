
import numpy as np

array1 = np.array([[1, 2, 3], [4, 5, 6]])
array2 = np.array([[7, 8, 9], [10, 11, 12]])

addition = array1 + array2
subtraction = array1 - array2
multiplication = array1 * array2
division = array1 / array2

print("Array 1:\n", array1)
print("Array 2:\n", array2)
print("Element-wise Addition:\n", addition)
print("Element-wise Subtraction:\n", subtraction)
print("Element-wise Multiplication:\n", multiplication)
print("Element-wise Division:\n", division)

vector1 = np.array([1, 2, 3])
vector2 = np.array([4, 5, 6])

# Calculate dot product and cross product
dot_product = np.dot(vector1, vector2)
cross_product = np.cross(vector1, vector2)

print("Vector 1:", vector1)
print("Vector 2:", vector2)
print("Dot Product:", dot_product)
print("Cross Product:", cross_product)
