## BIJECTION RULE

#### DESCRIPTION
You can use the sum and product rules to count the number of possible sequences that could be determined from individual sequences.

But what if you want to count one thing by counting another? For example, let's say you see a pile of shoes from a group of children at the front door. You could determine the number of children (assuming each child had two shoes in the pile) by counting the number of shoes and dividing by two. For this situation you would use a method of counting called "bijection."

#### THEOREM
**TL;DR: Let S and T be two finite sets. If there is a bijection from S to T, then |S| = |T|.**

A bijective function or one-to-one correspondence is a function between two sets such that each element of the second set (the codomain) is the image of exactly element of the first set (the domain). Every element from one set is paired with an element from the other set.

A function is bijective if it is invertible, i.e. a function f: X -> Y is bijective if and only if there is a function g: Y -> X, the inverse of f, such that each of the two ways for composing the two functions produces an identity function:
- g(f(x)) = x for each x in X
- f(g(y)) = y for each y in Y

#### EXAMPLE

This example uses the bijection rule to determine the cardinality of the power set of a finite set X. Recall that the power set of X (denoted P(X)) is the set of all subsets of X. Let |X| = n. The information below illustrates a bijection f from P(X) to the set of binary strings of length n: 
- x = {a, b, c}
- P(x) = {∅, {a}, {b}, {c}, {a, b}, {a, c}, {b, c}, {a, b, c}}

We can translate the elements of P(x) into binary strings of length n, with each digit being associated with an element from x, i.e. {a, c} would be 101 since a and c are present but not b. When applied to the other elements of P(x), we get the following:
- {0, 1}<sup>3</sup> = {000, 100, 010, 001, 110, 101, 011, 111}

f defines a bijection between the set {0, 1}<sup>3</sup> and the power set of {a, b, c} (i.e. P(x)). Therefore:
- | P(x) | = | {0, 1}<sup>3</sup> |
    - Note that the || notation is used to get the cardinality (size, i.e. number of elements) of a set.


## THE K-TO-1 RULE

#### DESCRIPTION
A group of kids at a slumber party all leave their shoes in a big pile at the door. One way to count the number of kids at the party is to count the number of shoes and divide by 2. Of course, it is important to establish that each kid has exactly one pair of shoes in the pile. Counting kids by counting shoes and dividing by 2 is an example of the k-to-1 rule with k = 2. Applying the k-to-1 rule requires a well defined function from objects we can count to objects we would like to count. In the example with the shoes, the function maps each shoe to the kid who owns it.

#### THEOREM
Let X and Y be finite sets. The function f: X -> Y is a k-to-1 correspondence if for every y ∈ Y, there are exactly k different x ∈ X such that f(x) = y. 

For the k-to-1 rule itself, suppose there is a k-to-1 correspondence from a finite set A to a finite set B. Then **|B| = |A|/k**.