// paretofront returns the logical Pareto membership of a set of points
// synopsis:  frontFlag = paretofront(objMat)
// Created by Yi Cao: y.cao@cranfield.ac.uk
// for compiling type:
//   mex paretofront.c

#include <stdio.h>
#include <stdlib.h>  // memory, e.g. malloc
#include <stdbool.h> // to use the bool datatype, required C99
#include <math.h>

void paretofront_cao(bool *frontFlag, double *obj, unsigned nrow, unsigned ncol) {
    unsigned t, s, i, j, j1, j2;
    bool *checklist, colDominatedFlag;
    
    checklist = (bool*)malloc(nrow*sizeof(bool));
    
    for(t=0; t<nrow; t++)
        checklist[t] = true;
    for(s=0; s<nrow; s++) {
        t = s;
        if (!checklist[t])
            continue;
        checklist[t] = false;
        colDominatedFlag = true;
        for(i=t+1; i<nrow; i++) {
            if (!checklist[i])
                continue;
            checklist[i] = false;
            for (j=0,j1=i,j2=t; j<ncol; j++,j1+=nrow,j2+=nrow) {
                if (obj[j1] < obj[j2]) {
                    checklist[i] = true;
                    break;
                }
            }
            if (!checklist[i])
                continue;
            colDominatedFlag = false;
            for (j=0,j1=i,j2=t; j<ncol; j++,j1+=nrow,j2+=nrow) {
                if (obj[j1] > obj[j2]) {
                    colDominatedFlag = true;
                    break;
                }
            }
            if (!colDominatedFlag) { //swap active index continue checking
                frontFlag[t] = false;
                checklist[i] = false;
                colDominatedFlag = true;
                t = i;
            }
        }
        frontFlag[t] = colDominatedFlag;
        if (t>s) {
            for (i=s+1; i<t; i++) {
                if (!checklist[i])
                    continue;
                checklist[i] = false;
                for (j=0,j1=i,j2=t; j<ncol; j++,j1+=nrow,j2+=nrow) {
                    if (obj[j1] < obj[j2]) {
                        checklist[i] = true;
                        break;
                    }
                }
            }
        }
    }
    free(checklist); 
}