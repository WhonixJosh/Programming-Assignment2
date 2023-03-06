# Programming Assignment2
 Created by Josh Green

 ## Analysis

 ALGORITHM HayesSort(A[0..n-1])
Description: Sorts an input array A
Input: A[0..n-1] where A is an array of DISTINCT NON-NEGATIVE INTEGERS
Output: B[0..n-1] where B contains all numbers in A, but rearranged in non-decreasing order
index  0
max = A[0]
for i = 1 to n – 1
if A[i] ¿ max
max  A[i]
for j = 0 to max
if j is an element in array A
B[index] = j
index  index + 1
return B

 ### 1. Basic Operation

