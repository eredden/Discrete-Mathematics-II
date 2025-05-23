### INTRODUCTION TO INDUCTIVE PROOFS

Once the Titanic hit an iceberg and the first bulkhead filled with water, Captain Smith knew the ship would sink. As soon as the first bulkhead filled with the water, he knew the second bulkhead would fill. As soon as the second filled up with water, the third would fill, and like dominos the fourth, fifth, ..., and n<sup>th</sup> bulkhead would eventually fill. It didn't matter whether n=1 or n=100. The Titanic was doomed regardless.

Induction was used to reach this realization. Knowing that the (n + 1)<sup>th</sup> compartment would fill is the inductive step. The first compartment (n=1) filling was the base case.

### FORMAL DEFINITION FOR INDUCTIVE PROOFS

The base case establishes that the theorem is true for the first value in the sequence. The inductive step establishes that if the theorem is true for k, then the theorem also holds for k + 1.

The principle of mathematical induction is as follows. **Let S(n) be a statement parameterized by a positive integer n. Then S(n) is true for all positive integers n, if:**

1. S(1) is true.
    - Base case.
2. For all k ∈ Z<sup>+</sup>, S(k) implies S(k + 1).
    - Inductive step.

### CREATING AN INDUCTIVE PROOF

You can create an inductive proof for an equation by substituting variables for constant values, ex. 3, and proving that both sides yield the same value. This is predicate P(n). Then you can try out the induction step by checking if the theorem holds true with those same constants plus one. This is predicate P(k + 1).

Ex. proving the base case predicate P(n):
```
Predicate P(n):

  n
  Σ j  = n(n + 1) / 2
j=1


Predicate P(3):

  3
  Σ j  = 3(3 + 1) / 2
j=1

  1 + 2 + 3  = 6
  6 = 6


Therefore, predicate P(n) is true.
```

Ex. proving the inductive step predicate P(k + 1):
```
Predicate P(k + 1):

k+1
  Σ j  = (k + 1)(k + 2) / 2
j=1


Predicate P(3):

3+1
  Σ j  = (3 + 1)(3 + 2) / 2
j=1

  4
  Σ j  = (4)(5) / 2
j=1

  1 + 2 + 3 + 4  = 10
  10 = 10


Therefore, predicate P(k + 1) is true.
```

Sometimes the smallest n for which S(n) holds is some constant c other than 1. Then the base case must show that S(c) is true. The inductive step will establish that S(k)→S(k+1) for any k ≥ c. An inductive proof assumes that S(k) and k ≥ c are true and uses those two facts to establish that S(k+1) is true. 