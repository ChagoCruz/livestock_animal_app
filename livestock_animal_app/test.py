import numpy as np

a = np.ones((2,3))
print('array a:')
print(a)
print()

b = np.zeros_like(a)
print('array b:')
print(b)
print()

print('b shape')
print(b.shape)