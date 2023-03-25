import numpy as np
from numba import cuda, jit
from timeit import default_timer as timer


def fill_array_cpu(array):
    for i in range(len(array)):
        array[i] += 1

@jit(target_backend='cuda')
def fill_array_gpu(array):
    for i in range(len(array)):
        array[i] += 1

size = 10_000_000
array = np.ones(size, dtype=np.float64)

start = timer()
fill_array_cpu(array)
print("On a CPU: ", timer() - start)
start = timer()
fill_array_gpu(array)
print("On a GPU: ", timer() - start)
