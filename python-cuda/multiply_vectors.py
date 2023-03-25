import numpy as np
from numba import vectorize
from timeit import default_timer as timer


def multiply_vectors(a, b, c):
    for i in range(a.size):
        c[i] = a[i] * b[i]


@vectorize(["float32(float32,float32)"], target='cuda')
def multiply_vectors_faster(a, b):
    return a*b


def run_cpu():
    start = timer()
    multiply_vectors(A, B, C)
    cpu_multiply_vectors_time = timer() - start
    print(f"CPU multiplication took: {cpu_multiply_vectors_time} seconds \n")


def run_gpu():
    start = timer()
    c = multiply_vectors_faster(A, B)
    cpu_multiply_vectors_time = timer() - start
    print(f"GPU multiplication took: {cpu_multiply_vectors_time} seconds \n")


N = 64_000_000

A = np.ones(N, dtype=np.float32)
B = np.ones(N, dtype=np.float32)
C = np.ones(N, dtype=np.float32)

run_cpu()
run_gpu()
