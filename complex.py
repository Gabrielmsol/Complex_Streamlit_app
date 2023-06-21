import numpy as np


def make_grid(i, fi, n_x, n_y):
    x = np.linspace(i, fi, n_x)
    y = np.linspace(i, fi, n_y).reshape(n_y, 1)
    return x+y*1j


def make_circ(r_i, r_f, w_i, w_f, n_r, n_w):
    r = np.linspace(r_i, r_f, n_r)
    w = np.linspace(w_i, w_f, n_w).reshape(n_w, 1)
    return r*np.exp(w*1j)


def get_tensor(matrix):
    tensor = np.zeros((matrix.shape[0], matrix.shape[1], 3), dtype=complex)
    tensor[..., 0] = matrix
    tensor[..., 1] = np.abs(matrix)
    return tensor


def get_dimensions(tensor):
    x = np.real(tensor[..., 0].flatten())
    y = np.imag(tensor[..., 0].flatten())
    return x, y


def Z(matrix):
    return matrix
