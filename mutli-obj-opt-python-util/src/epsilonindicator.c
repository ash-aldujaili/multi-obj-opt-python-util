#include <math.h>
#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

#define max(x,y) (((x)>(y))? (x) : (y))
#define min(x,y) (((x)<(y))? (x) : (y))

// returns I_{\epsilon+}(A,B)
double epsilonindicator(double* A, double *B, size_t numelA, size_t  numelB, size_t nObjs) {
    
    double eps_i = 0.0;
    // iterate over the reference set
    for(size_t i = 0; i < numelB; i++) {
    	double eps_j = INFINITY;
    	// iterate over the approximation set
    	for(size_t j = 0; j < numelA; j++) {
    	    double eps_k = 0.0;
    		for(size_t k = 0; k < nObjs; k++) eps_k = max(eps_k, A[j * nObjs + k] - B[i * nObjs + k]);
    		eps_j = min(eps_j, eps_k);
    	}
    	eps_i = max(eps_i, eps_j);
    } 
    return eps_i;
}