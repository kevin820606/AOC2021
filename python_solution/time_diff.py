from timeit import timeit
import numpy as np

a = lambda x: np.arange(0, x + 1).sum()
b = lambda x: ((1 + x) * x) / 2

# print(a(5) == b(5))

ta = timeit("a(5)", "from __main__ import a", number=1000)
tb = timeit("b()", "from __main__ import b", number=1000)
print(ta, tb)
