"""
A setup script for multi-objective c-2-python related functionalities

Abdullah Al-Dujaili, 2016

"""

import os
from os import system

from sys import platform as platform



# Define the compilation flags
if platform == "darwin": # mac os
	LDFLAGS = " -fPIC -std=c99 -dynamiclib "
else: # other systems tested so far
	LDFLAGS = " -fPIC -std=c99 -shared "



print "Cleaning files"
system("rm -vf *.so *.o *~")

print "Compiling libs"
system("gcc" + LDFLAGS + " src/paretofront.c src/paretofront_cao.c -o python_mo_util/libparetofront.so")
system("gcc" + LDFLAGS + " src/incremental_epsilonindicator.c src/fast_eps_ind.c src/epsilonindicator.c -o python_mo_util/libepsilonindicator.so")

print "Testing .."
os.chdir("./python_mo_util/")
system("python test_mo_c2python_util.py")
