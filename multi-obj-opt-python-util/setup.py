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
system("gcc" + LDFLAGS + " src/pf.c -o python_mo_util/libpf.so")
system("gcc" + LDFLAGS + " src/eps.c -o python_mo_util/libeps.so")
system("gcc" + LDFLAGS + " src/hypervol.c -o python_mo_util/libhv.so")

print "Testing .."
os.chdir("./python_mo_util/")
system("python test_mo_c2python_util.py")
