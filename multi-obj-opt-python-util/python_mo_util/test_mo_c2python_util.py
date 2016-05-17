"""
A test script for multi-objective c-2-python related functionalities

Abdullah Al-Dujaili, 2016

"""

import numpy as np
import pymoutils
import time
from pymoutils import *


# create an input array
nrows = 10
ncols = 5
inArray = np.random.random((nrows,ncols))
refSet = np.random.random((nrows,ncols))-1
# Arrays
#rint "Input Array:"
print inArray
print "Reference Array"
print refSet

# Pareto filtering
print "Non-dominated vectors in the input array"
start_time = time.time()
pf_array = paretofront(inArray)
time_pf = time.time() - start_time
print "Non-dominated vectors in the input array: Cao's method"
start_time = time.time()
pf_array_cao =  paretofront_cao(inArray)
time_pf_cao = time.time() - start_time
if np.all(pf_array_cao == pf_array):
	print "test passed"
else:
	print "test failed"

if time_pf == 0.0:
	print "A speed up of ", time_pf_cao / 1e-8, "for paretofront over paretofront_cao" 
else:	
	print "A speed up of ", time_pf_cao / time_pf, "for paretofront over paretofront_cao" 

# Epsilon Indicator
print "Additive Epsilon indicator value:"
start_time = time.time()
print compute_eps(inArray, refSet)
print "Translated reference array:", refSet+compute_eps(inArray, refSet)
print "It took:", time.time()- start_time, "seconds to compute eps."
start_time = time.time()
print compute_fast_incr_eps(inArray, refSet)
time_incr_feps = time.time() - start_time
print "It took:", time_incr_feps, "seconds for fast incremental eps."
start_time = time.time()
print compute_incr_eps(inArray, refSet)
time_incr_eps = time.time() - start_time
print "It took:", time_incr_eps, "seconds to compute incremental eps."

if time_incr_feps == 0.0:
	print "A speed up of ", time_incr_eps / 1e-8
else:
	print "A speed up of ", time_incr_eps / time_incr_feps


# Hypervolume
print "Hypervolume value on python hv code:"
start_time = time.time()
pyhv = compute_pyhv(inArray,[2]* ncols)
time_hvpy = time.time() - start_time
print pyhv

print "Hypervolume value on c hv code:"
start_time = time.time()
chv = compute_incr_hv_c(inArray,[2]* ncols)
time_hvc = time.time() - start_time
print chv

print "Incremental Hypervolume value on python hv code:"
start_time = time.time()
phv = compute_incr_hv(inArray,[2]* ncols)
time_hvp = time.time() - start_time
print phv

# Testing the GD calls
print "GD value:"
start_time = time.time()
print compute_gd(inArray, refSet)
print "It took:", time.time()- start_time, "seconds to compute gd."

print "Incremental GD value:"
start_time = time.time()
print compute_incr_gd(inArray, refSet)
print "It took:", time.time()- start_time, "seconds to compute incremental gd."

print "IGD value:"
start_time = time.time()
print compute_igd(inArray, refSet)
print "It took:", time.time()- start_time, "seconds to compute igd."

print "Incremental IGD value:"
start_time = time.time()
print compute_incr_igd(inArray, refSet)
print "It took:", time.time()- start_time, "seconds to compute incremental igd."