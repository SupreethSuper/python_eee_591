###############################################################################
# hw1_591.py
#
# EEE 419/591 - Homework 1 (591 additional problem)
# Problem 4: Manual Discrete Cosine Transform (DCT-II) Calculations
#
# Computes the type-II DCT of a 1D signal two different ways -- nested for
# loops and an N x N matrix-vector product -- and compares both against
# scipy.fftpack.dct(x, type=2, norm=None).
#
# The DCT-II used here is the unnormalized definition:
#
#     X[k] = 2 * sum_{n=0}^{N-1} x[n] * cos( (pi/N) * (n + 1/2) * k )
#
#     for k = 0, 1, ..., N-1
#
# which is the same convention SciPy uses for type=2, norm=None.
#
# Author: <your name>
# ASU ID: <your id>
#
# CITATIONS (required per syllabus, page 4):
#   <fill in per the syllabus citation format>
###############################################################################

import numpy as np                      # arrays and vectorized math
from scipy.fftpack import dct           # reference implementation

N = 512                                 # signal length, problem requires N > 256


def dct2_loops(x):
    """DCT-II computed with nested for loops (the direct O(N^2) definition).

    x       : 1D array of length N
    returns : 1D array of length N holding the DCT-II coefficients
    """
    n_samples = len(x)
    x_freq = np.zeros(n_samples)         # output array, one coefficient per k

    for k in range(n_samples):           # outer loop over frequency index k
        total = 0.0                      # running sum for this k
        for n in range(n_samples):       # inner loop over time index n
            angle = np.pi / n_samples * (n + 0.5) * k
            total += x[n] * np.cos(angle)
        x_freq[k] = 2.0 * total          # factor of 2 from the definition

    return x_freq


def dct2_matrix(x):
    """DCT-II computed as a matrix-vector product X = C @ x.

    Builds the N x N transformation matrix C whose entries are

        C[k, n] = 2 * cos( (pi/N) * (n + 1/2) * k )

    so that row k of C, dotted with x, gives coefficient X[k].

    x       : 1D array of length N
    returns : 1D array of length N holding the DCT-II coefficients
    """
    n_samples = len(x)

    k = np.arange(n_samples).reshape(-1, 1)   # column vector of k, shape (N,1)
    n = np.arange(n_samples).reshape(1, -1)   # row vector of n,    shape (1,N)

    # Broadcasting the column against the row builds the full N x N matrix.
    C = 2.0 * np.cos(np.pi / n_samples * (n + 0.5) * k)

    return C @ x                              # matrix-vector multiply


def main():
    # Build a test signal. A fixed seed keeps the run repeatable, and mixing
    # a couple of tones with noise avoids any accidentally trivial input.
    rng = np.random.default_rng(591)
    t = np.arange(N)
    x_time = (np.sin(2.0 * np.pi * 5.0 * t / N)
              + 0.5 * np.cos(2.0 * np.pi * 37.0 * t / N)
              + 0.1 * rng.standard_normal(N))

    # Reference result from SciPy, plus the two manual implementations.
    x_freq_ref = dct(x_time, type=2, norm=None)
    x_freq_loop = dct2_loops(x_time)
    x_freq_matrix = dct2_matrix(x_time)

    # Maximum absolute error across all N coefficients.
    err_loop = np.max(np.abs(x_freq_loop - x_freq_ref))
    err_matrix = np.max(np.abs(x_freq_matrix - x_freq_ref))

    print("N = %d" % N)
    print("Max error (loop vs SciPy DCT):   %.2e" % err_loop)
    print("Max error (matrix vs SciPy DCT): %.2e" % err_matrix)


if __name__ == "__main__":
    main()
