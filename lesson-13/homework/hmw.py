import numpy as np

# 1. Create a vector with values ranging from 10 to 49
vector = np.arange(10, 50)

# 2. Create a 3x3 matrix with values ranging from 0 to 8
matrix_3x3 = np.arange(9).reshape(3, 3)

# 3. Create a 3x3 identity matrix
identity_matrix = np.eye(3)

# 4. Create a 3x3x3 array with random values
array_3x3x3 = np.random.random((3, 3, 3))

# 5. Create a 10x10 array with random values and find the minimum and maximum values
array_10x10 = np.random.random((10, 10))
min_value = array_10x10.min()
max_value = array_10x10.max()

# 6. Create a random vector of size 30 and find the mean value
vector_30 = np.random.random(30)
mean_value = vector_30.mean()

# 7. Normalize a 5x5 random matrix
matrix_5x5 = np.random.random((5, 5))
normalized_matrix_5x5 = (matrix_5x5 - matrix_5x5.min()) / (matrix_5x5.max() - matrix_5x5.min())

# 8. Multiply a 5x3 matrix by a 3x2 matrix (real matrix product)
matrix_5x3 = np.random.random((5, 3))
matrix_3x2 = np.random.random((3, 2))
product_5x2 = np.dot(matrix_5x3, matrix_3x2)

# 9. Create two 3x3 matrices and compute their dot product
matrix_a = np.random.random((3, 3))
matrix_b = np.random.random((3, 3))
dot_product = np.dot(matrix_a, matrix_b)

# 10. Given a 4x4 matrix, find its transpose
matrix_4x4 = np.random.random((4, 4))
transpose_4x4 = matrix_4x4.T

# 11. Create a 3x3 matrix and calculate its determinant
matrix_3x3_det = np.random.random((3, 3))
determinant = np.linalg.det(matrix_3x3_det)

# 12. Create two matrices A (3x4) and B (4x3), and compute the matrix product A · B
A = np.random.random((3, 4))
B = np.random.random((4, 3))
product_AB = np.dot(A, B)

# 13. Create a 3x3 random matrix and a 3-element column vector. Compute the matrix-vector product.
matrix_3x3_vec = np.random.random((3, 3))
vector_3 = np.random.random((3, 1))
matrix_vector_product = np.dot(matrix_3x3_vec, vector_3)

# 14. Solve the linear system Ax = b where A is a 3x3 matrix, and b is a 3x1 column vector
A_system = np.random.random((3, 3))
b_system = np.random.random((3, 1))
solution = np.linalg.solve(A_system, b_system)

# 15. Given a 5x5 matrix, find the row-wise and column-wise sums
matrix_5x5_sum = np.random.random((5, 5))
row_sums = matrix_5x5_sum.sum(axis=1)
column_sums = matrix_5x5_sum.sum(axis=0)

print("1. Vector:", vector)
print("\n2. 3x3 Matrix:\n", matrix_3x3)
print("\n3. Identity Matrix:\n", identity_matrix)
print("\n4. 3x3x3 Random Array:\n", array_3x3x3)
print("\n5. Min and Max Values:", min_value, max_value)
print("\n6. Mean Value:", mean_value)
print("\n7. Normalized 5x5 Matrix:\n", normalized_matrix_5x5)
print("\n8. Product of 5x3 and 3x2 Matrix:\n", product_5x2)
print("\n9. Dot Product of two 3x3 Matrices:\n", dot_product)
print("\n10. Transpose of 4x4 Matrix:\n", transpose_4x4)
print("\n11. Determinant of 3x3 Matrix:", determinant)
print("\n12. Product of A and B:\n", product_AB)
print("\n13. Matrix-Vector Product:\n", matrix_vector_product)
print("\n14. Solution of Linear System:\n", solution)
print("\n15. Row Sums:\n", row_sums)
print("    Column Sums:\n", column_sums)
