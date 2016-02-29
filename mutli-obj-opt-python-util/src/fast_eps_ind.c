#include <math.h>
#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>

#define max(x,y) (((x)>(y))? (x) : (y))
#define min(x,y) (((x)<(y))? (x) : (y))

// returns I_{\epsilon+}(A,B) across different timestamps of A
void fast_eps_ind(double* eps_i, double* A, double *B, size_t numelA, size_t  numelB, size_t nObjs) {
    
      double *eps_j = (double*) malloc(numelA*sizeof(double));
      
      // pre-processing
      for (size_t j = 0; j < numelA; j++) eps_i[j] = 0.0;

      // iterate over the reference set
      for(size_t i = 0; i < numelB; i++) {
        for (size_t j = 0; j < numelA; j++) eps_j[j] = INFINITY;
    	  // iterate over the approximation set
      	for(size_t j = 0; j < numelA; j++) {
    	      double eps_k = 0.0;
    		    for(size_t k = 0; k < nObjs; k++) eps_k = max(eps_k, A[j * nObjs + k] - B[i * nObjs + k]);
    		    if (j > 0) 
    		      eps_j[j] = min(eps_j[j-1], eps_k);
    		    else 
    		      eps_j[j] = min(eps_j[j], eps_k);
    	  }
    	  // post-processing
        for (size_t j = 0; j < numelA; j++) eps_i[j] = max(eps_i[j], eps_j[j]);

      } 
      
            // free
      free(eps_j);
}
