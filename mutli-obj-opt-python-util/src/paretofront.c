#include <math.h>
#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>


void paretofront(bool *frontFlag, double *obj, size_t nPoints, size_t nObjs) {
    
    //bool *checklist, colDominatedFlag;
    size_t nPosDiff;
    size_t nNegDiff;
	double delta = 0.0;
    //checklist = (bool*)malloc(nrow*sizeof(bool));
    // initialize
    //for (size_t p = 0; p < nPoints; p++) frontFlag[p] = true;
    
    for (size_t p = 0; p < nPoints - 1; p++) {
      if (!frontFlag[p]) continue; // skip this point if not of interest
      // loop over other points
      for (size_t q = p + 1; q < nPoints; q++) {
        // skip this point if it is dominated or of no interest
        if (!frontFlag[q]) continue;
        // otherwise compare their objective-differences
        nPosDiff = 0;
        nNegDiff = 0;
        for (size_t j = 0; j < nObjs; j++) {
			    delta = obj[p * nObjs + j] - obj[q * nObjs + j];
			    if (delta > 0) nNegDiff = nNegDiff + 1;
          else //if (delta < 0)commenting this to filter out identical items similar to cao's method
            nPosDiff = nPosDiff + 1;
		      // speed up step
		      if (nNegDiff > 0 && nPosDiff > 0) break; // incomparable
        }
        if (nNegDiff > 0 && nPosDiff > 0) continue; // incomparable
        else if (nNegDiff > 0) { // p is dominated
          frontFlag[p] = false;
          break; 
        }
        else if (nPosDiff > 0) frontFlag[q] = false; // q is dominated
        
      }
    }
    
    //free(checklist); 
}
