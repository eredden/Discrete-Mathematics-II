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

### CREATING A WEAK INDUCTIVE PROOF

You can create an inductive proof for an equation by substituting variables for constant values, ex. 3, and proving that both sides yield the same value. This is predicate P(n). Then you can try out the induction step by checking if the theorem holds true with those same constants plus one. This is predicate P(k + 1).

Ex. formal outline of a proof for P(n).
```md
# Theorem: For every positive integer n,
  n
  Σ j  = n(n + 1) / 2
j=1

# Proof: By induction on n.
# Base case: n = 1.

# When n = 1, the left side of the equation is equal to 1.
  1
  Σ j = 1
j=1

# When n = 1, the right side of the equation is equal to 1.
= 1(1 + 1) / 2
= 1(2) / 2
= 2 / 2
= 1

# Therefore, the base case n = 1 is proven.
  1
  Σ j  = 1(1 + 1) / 2
j=1
```

Ex. formal proof for P(k + 1), same equation as last time.
```md
# Inductive step: Suppose that for positive integer k,
  k
  Σ j  = k(k + 1) / 2
j=1

# then we will prove P(k + 1):
k+1
  Σ j  = (k + 1)(k + 2) / 2
j=1

# Starting with the left side of the equation to be proven:
# We separate the last term from the summation.
k+1        k
  Σ j  =   Σ j + (k + 1)
j=1      j=1

# By the inductive hypothesis:
       =  (k(k + 1) / 2) + (k + 1)

# By algebra:
       = k(k + 1) + 2(k + 1) / 2

# This seems confusing, but we are just factoring out (k + 1) 
# as it gets us closer to the equation than doing 2k(k + 1 ).
       = (k + 2)(k + 1) / 2

# Therefore, P(k + 1) has been proven.

k+1
  Σ j  = (k + 1)(k + 2) / 2
j=1
```

**Sometimes the smallest n for which S(n) holds is some constant c other than 1. Then the base case must show that S(c) is true.** The inductive step will establish that S(k)→S(k+1) for any k ≥ c. An inductive proof assumes that S(k) and k ≥ c are true and uses those two facts to establish that S(k+1) is true. 

### CREATING A STRONG INDUCTIVE PROOF

The proof shown above is called weak induction - weak as in little was assumed. You only needed the n<sup>th</sup> case for the (n+1)<sup>th</sup> case to exist. However, sometimes you may need to assume more. For example, many recurrences have more than one initial case. So what is the difference between weak and strong induction? The difference is only in the induction hypothesis.

The principle of strong mathematical induction is as follows. **Let S(n) be a statement parameterized by n, a positive integer. Let a ≤ b be integers. Then S(n) is true for all n ≥ a, if the following two conditions hold:**
1. S(a), S(a+1), ..., S(b) are true.
    - Base case.
2. For all k ≥ b, if (S(a) ∧ S(a+1) ∧ .... ∧ S(k)) is true, then S(k+1) is also true.
    - Inductive step.

In strong induction the inductive hypothesis is S(0) ∧ S(1) ∧ .... ∧ S(k). In regular (or weak) induction, the inductive hypothesis is just S(k). Sometimes the inductive hypothesis is expressed using a universal quantifier. The following two ways to express the inductive hypothesis are equivalent:

S(0) ∧ S(1) ∧ .... ∧ S(k) is true.   ↔   For every j in the range 0 through k, S(j) is true. 
Note how ^ is used as a logical **AND** rather than for exponentiation, and the usage of the **IF AND ONLY IF** operator. **For generalized strong induction, you do not need to prove every single base case, only enough to allow assumption that the rest are good.**

**There is no simple rule to determine when strong induction is required instead of the standard form of induction, nor how many base cases must be proven.** The best method is to try proving the inductive step using only the preceding value (i.e., try and prove the statement for k + 1 using only the statement for k).