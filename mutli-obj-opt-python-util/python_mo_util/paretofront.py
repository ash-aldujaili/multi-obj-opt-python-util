""" 
	wrapper for paretofront.c that accepts a C double array as input
	using the numpy.ctypeslib

	Abdullah Al-Dujaili adapted from:
	http://www.scipy-lectures.org/advanced/interfacing_with_c/interfacing_with_c.html#id1
"""

import numpy as np
import numpy.ctypeslib as npct
from ctypes import c_int
import os

from sys import platform as platform

# input type for the pareto front function
array_1d_double = npct.ndpointer(dtype=np.double, flags='C_CONTIGUOUS')
#array_1d_double_c = npct.ndpointer(dtype=np.double, flags='C_CONTIGUOUS')
array_1d_bool = npct.ndpointer(dtype=np.bool,  flags='C_CONTIGUOUS')


# load the library, using numpy mechanisms
if platform == "darwin":
	libpf = npct.load_library("libparetofront", ".")
	#libpf_cao = npct.load_library("libparetofront_cao.so", ".")
else:
  libpf = npct.load_library("libparetofront.so", ".")
	#libpf_cao = npct.load_library("libparetofront_cao", ".")

# setup the return types and argument types
libpf.paretofront.restype = None
libpf.paretofront.argtypes = [array_1d_bool, array_1d_double, c_int, c_int]

libpf.paretofront_cao.restype = None
libpf.paretofront_cao.argtypes = [array_1d_bool, array_1d_double, c_int, c_int]

def paretofront_cao(in_array):
	"""
	Returns the logical Pareto membership of a set of points.
	Takes a numpy array of nrows x ncols and returns a boolean vector of nrows x 1
	where 1 denotes a non-dominated vector, according to cao's method
	Yi Cao: y.cao@cranfield.ac.uk
	"""
	bool_array = np.array([False] * in_array.shape[0], dtype= np.bool)
	libpf.paretofront_cao(bool_array, np.ascontiguousarray(in_array.T), in_array.shape[0], in_array.shape[1])
	return bool_array


def paretofront(in_array):
	"""
	Returns the logical Pareto membership of a set of points
	Takes a numpy array of nrows x ncols and returns a boolean vector of nrows x 1
	where 1 denotes a non-dominated vector.
	"""
	bool_array = np.array([True] * in_array.shape[0], dtype= np.bool)
	libpf.paretofront(bool_array, np.ascontiguousarray(in_array), in_array.shape[0], in_array.shape[1])
	return bool_array
