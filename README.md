# multi-obj-opt-python-util
A collection of handy functions for multi-objective optimization written in C with a python wrapper

Currently it has the current utilities:

* identifying the Pareto front (non-dominated solutions) among a set of solutions.
* computing quality indicators such as hypervolume, inverted generational distance, generational distance, and additive epsilon indicator.

# Setup: 

In a system shell, `cd` into the `multi-obj-opt-python-util` folder, and execute the following command:
```
python setup.py
```
This will compile the *.c files and run a test script found in the `python-mo-util` folder.

# Use: 
To use it withnin your code, just copy the *.py and *.so files from the `python-mo-util` folder to your working folder.

Enjoy..
