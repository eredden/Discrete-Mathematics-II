## RECURSIVE / INDUCTIVE ALGORITHMS

A recursive algorithm is an algorithm that calls itself. Like recursively defined sequences and structures, a recursively defined algorithm has a base case in which the output is computed directly on an input of small size or value. On a larger input, the algorithm calls itself on an input of smaller size and uses the result to construct a solution to the larger input (divide and conquer). An algorithm's calls to itself are known as recursive calls. 

#### Ex. compute n! (n factorial):
Here is an example of a recursive algorithm to compute n!. 

```
Factorial(n)

Input: A non-negative integer n.
Output: n!

If (n = 0)
    Return( 1 )
r := Factorial( n - 1 ) // The recursive call

Return( r*n ) 
```

#### Ex. get the power set P(A) of set A:

The algorithm given below takes in as input a set A and returns the power set of A. Recall that the power set of A (denoted P(A)) is the set of all subsets of A, **i.e. all possible permutations of the values in set A**. The elements of P(A) are subsets of A. 

```
PowerSet(A)

Input: A set A.
Output: The power set of A.

If (A = ∅)
    Return( {∅} )

Select an element a ∈ A
A' := A - {a}
P := PowerSet(A')  //the recursive call
P' := P
For each S ∈ P'
    Add S∪{a} to P
End-for

Return( P ) 
```

The base case for the algorithm is when the input A is the empty set. The power set of the empty set is the set containing the empty set as its only element. Then for the recursive step, the algorithm removes an element x from A to obtain A' whose cardinality is strictly smaller than A. The algorithm is then run recursively on A'. All the elements in the power set of A' are also in the power set of A. In addition, the power set of A contains each set in P(A') with the element x added back in.