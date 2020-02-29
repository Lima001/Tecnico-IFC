import numpy as np

A = np.array([[1,2,1],[1,-3,5],[2,-1,3]])
B = np.array([[12],[1],[10]])


X = np.linalg.solve(A,B)

print("x = ", X[0])
print("y = ", X[1])
print("z = ", X[2])