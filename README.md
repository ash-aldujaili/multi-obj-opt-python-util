# multi-obj-opt-python-util
A collection of handy functions for multi-objective optimization written in C with a python wrapper

Currently it has the current utilities:
..1. paretfront.py : processes a set of vectors and returns a logical vector indicating which vectors are non-dominated.
..2. epsilonindicator.py: processes a set of vectors (approximation set) with respect to a reference set and returns the additive epsilon indicator value of the entire set as well as a the incremental epsilon indicatior values over the elements of the approximation set.

# Setup: 

In a system shell, `cd` into the `multi-obj-opt-python-util` folder, and execute the following command:
```
python setup.py
```
This will compile the *.c files and run a test script found in the `python-mo-util` folder.

# Use: 
To use it withnin your code, just copy the *.py and *.so files from the `python-mo-util` folder to your working folder.

Enjoy..
