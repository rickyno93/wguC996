import numpy as np

# slow version.  dynamic typing causes type-checking on each iteration of the
# loop.
def compute_reciprocals(values):
    output = np.empty(len(values))
    for i in range(len(values)):
        output[i] = 1.0 / values[i]
    return output

values = np.random.randint(1, 100, size=1000000)
#print(compute_reciprocals(values))

# vectorized operation that uses numpy's compiled layer

print (1.0 / values)

# more vectorized operations between arrays

print (np.arange(5) / np.arange(1, 6))

x = np.arange(9).reshape(3,3)
print (2**x)

# anytime a loop is used on an array, a vectorized expression should be
# considered instead
