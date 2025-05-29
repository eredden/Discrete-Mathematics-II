## RECURSIVELY DEFINED SETS INTRODUCTION

Think of the expression 4(5 - 2)<sup>2</sup> as a line of code. It is clear from the order of operations how this expression should be computed: . Using the rule of operations you know to calculate it. Each parenthesis or bracket is properly matched with a pair, so there is no confusion about how to perform the tasks.

By taking this expression, and adding expressions according to some simple rules, you can create a more complex expression. For example,
4(5 - 2)<sup>2</sup> -> 4(5(2 + x) - 2)<sup>2</sup>(7 - y). The new expression can also be computed without confusion because it is recursively created with computable parts.

You can apply recursive rules to sets rather than expressions using a similar process. To develop a recursive set, you start with a base set and develop the recursive rule(s).

## FORMAL OUTLINE OF A RECURSIVE SET

#### Components of a recursive definition of a set:
- A basis explicitly states that one or more specific elements are in the set.
- A recursive rule shows how to construct larger elements in the set from elements already known to be in the set. (There is often more than one recursive rule).
- An exclusion statement (A.K.A. escape clause) states that an element is in the set only if it is given in the basis or can be constructed by applying the recursive rules repeatedly to elements given in the basis.

#### Ex. validating properly nested parentheses:
- Basis: The sequence () is properly nested.
- Recursive rules: If u and v are properly-nested sequences of parentheses then:
    1. (u) is properly nested.
    2.  uv is properly nested.
- Exclusion statement: a string is properly nested only if it is given in the basis or can be constructed by applying the recursive rules to strings in the basis.

Since the exclusion statement is essentially the same for every recursively defined set, it is often excluded (but implied) in a recursive definition of a set. 

#### Ex. validating proper binary strings:
The set B<sup>k</sup>, where B = {0, 1}, is defined to be the set of all binary strings of length k. The set of all binary strings without any restriction on length (denoted by B<sup>\*</sup>) is an infinite set. The empty string (denoted by the symbol λ) is the unique string whose length is 0. Since B<sup>0</sup> is the set of all binary strings of length 0, B<sup>0</sup> = {λ}. B<sup>\*</sup> includes all of B<sup>k</sup> for any k ≥ 0. One way to define B<sup>\*</sup> is by an infinite union

- Base case: λ ∈ B*
- Recursive rule: if x ∈ B* then,
    1. x0 ∈ B*
    2. x1 ∈ B*

#### Ex. validating that As always come before Bs:

**VERY IMPORTANT NOTE:** x represents the string, so x0 is equivalent to concatenating 0 to the end of string x. Vice versa for other values. It is also important to note that you can concatenate at the beginning of a string as well, like so:

Let S be the set of all strings from A* in which there is no b before an a. For example, the strings λ, aa, bbb, and aabbbb all belong to S, but aabab ∉ S. Give a recursive definition for the set S.
- Base case: λ ∈ S
- Recursive rule: if x ∈ S then,
    1. ax ∈ S
    2. xb ∈ S

#### Ex. validating a proper binary tree.

- Base case: A single vertex with no edges is a full binary tree. The root is the only vertex in the tree.
- Recursive rule: If T1 and T2 are full binary trees, then a new tree T' can be constructed by first placing T1 to the left of T2, adding a new vertex v at the top and then adding an edge between v and the root of T1 and an edge between v and the root of T2. The new vertex v is the root of T'.
    - Note that this does not require the tree to be balanced, just that every vertex must have either zero or two nodes below it.