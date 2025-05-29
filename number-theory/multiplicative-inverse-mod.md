### MULTIPLICATIVE INVERSE MODULO

A multiplicative inverse mod n (or just inverse mod n) of an integer x, is an integer s ∈ {1, 2, . . ., n-1} such that **sx mod n = 1.**

Alternatively, we could say that s is the multiplicative inverse of x in Z<sub>n</sub>. For instance, in Z<sub>14</sub>, the multiplicative inverse of 3 is 5, since **3 * 5 = 15** and **15 mod 14 = 1.** Not every number has an inverse mod n.

The Extended Euclidean Algorithm can be used to find the multiplicative inverse of **x mod n** when it exists.
- **If GCD(x, n) ≠ 1, then x does not have a multiplicative inverse mod n.**
- If x and n are relatively prime, then the Extended Euclidean Algorithm finds integers s and t such that 1 = sx + tn.
- **sx - 1 = -tn.** Therefore, **(sx mod n) = (1 mod n) = 1**. It was shown earlier that if A - B is a multiple of n then (A mod n) = (B mod n).
- **(s mod n) is the unique multiplicative inverse of x in {0, 1, …, n - 1}.**

Ex. Find the mulitplicative inverse of 54 mod 61.

1. Apply the Euclidean Algorithm:
    - 61 mod 54 = 7
    - 54 mod 7 = 5
    - 7 mod 5 = 2
    - 5 mod 2 = 1
    - 2 mod 1 = 0

2. Prep for the Extended Euclidean Algorithm by putting the remainders from the GCD upwards into **r = y - (y div x) * x** form:
    - 1 = 5 - 2 * 2
    - 2 = 7 - 1 * 5
    - 5 = 54 - 7 * 7
    - 7 = 61 - 1 * 54

3. Apply the Extended Euclidean Algorithm to get the Bezout coefficients (s, t):
    - 1 = 5 - 2 * 2
    - 1 = 5 - 2 * (7 - 1 * 5)
    - 1 = 5 + (- 2 * 7) + (2 * 5)
    - 1 = (- 2 * 7) + (3 * 5)
    - 1 = 3 * 5 - 2 * 7
    - 1 = 3 * (54 - 7 * 7) - 2 * 7
    - 1 = 3 * 54 - 21 * 7 - 2 * 7
    - 1 = 3 * 54 - 23 * 7
    - 1 = 3 * 54 - 23 * (61 - 1 * 54)
    - 1 = 3 * 54 - 23 * 61 + 23 * 54
    - 1 = -23 * 61 + 26 * 54
    - 1 = **26** * 54 - 23 * 61 
    - **s = 26**

4. Get the inverse of x (54) by getting the value of **s mod n**:
    - **26 mod 61 = 26**.

5. Prove it!
    - **54 * 26 mod 61 = 1**.