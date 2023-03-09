# Programming Assignment 2
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

The basic operation of HayesSort is comparison.

### 2. Input Size

Measuring input size can be done through anaylzing the inputs given from the description.
With a finite of array of non negative distinct non-negative integers we can assume that our input will have no repeats and be less than infinity.

### 3. Efficiency Class

The worst-case efficiency class of HayesSort is in O(n^2). While it may seem that in runs in O(n) in the worst case, the condition of: "if j is an element in array A" runs inside of the second for loop. If every iteration of j is an element in Array A this loop will do at worst n^2 the amounts of basic operations for every iteration of j to ensure it's an element of A.

### 4. Limitations

HayesSort doesn't work on arrays with duplicate elements as the second for loop runs from 0 until the max value in A, assuming we have unique elements this will find all of our integers up until the max of A. However, if we have duplicates this will only sort the first instance of the integer we find. Duplicate values will not be sorted on the first pass through.

### 5. Runtime Comparision

I suspect HayesSort has the same worst case efficiency in the worst case if every element of j i in the array of A the runtime is of O(n^2). This places it in the same worst runtime of bubble and selection sort.