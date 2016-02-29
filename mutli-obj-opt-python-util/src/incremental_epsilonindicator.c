#include <math.h>
#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

#define max(x,y) (((x)>(y))? (x) : (y))
#define min(x,y) (((x)<(y))? (x) : (y))

// returns I_{\epsilon+}(A,B) across different timestamps of A
void incremental_epsilonindicator(double* eps_i, double* A, double *B, size_t numelA, size_t  numelB, size_t nObjs) {
    
    for (size_t l = 0; l < numelA; l++) {
      eps_i[l] = 0.0;
      // iterate over the reference set
      for(size_t i = 0; i < numelB; i++) {
    	  double eps_j = INFINITY;
    	  // iterate over the approximation set
      	for(size_t j = 0; j < l+1; j++) {
    	      double eps_k = 0.0;
    		  for(size_t k = 0; k < nObjs; k++) eps_k = max(eps_k, A[j * nObjs + k] - B[i * nObjs + k]);
    		  eps_j = min(eps_j, eps_k);
    	  }
    	  eps_i[l] = max(eps_i[l], eps_j);
      } 
    }
}
