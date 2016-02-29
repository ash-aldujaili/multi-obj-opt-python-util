"""
A test script for multi-objective c-2-python related functionalities

Abdullah Al-Dujaili, 2016

"""

import numpy as np
import paretofront 
import epsilonindicator
import time
from paretofront import paretofront
from paretofront import paretofront_cao
from epsilonindicator import compute_eps
from epsilonindicator import compute_incr_eps
from epsilonindicator import compute_fast_incr_eps



# create an input array
nrows = 100
ncols = 10
inArray = np.random.random((nrows,ncols))
refSet = np.random.random((nrows,ncols))
# Arrays
print "Input Array:"
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

print "A speed up of ", time_incr_eps / time_incr_feps 

