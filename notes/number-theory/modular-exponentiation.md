### MODULAR EXPONENTIATION

The variables s and p in the fast exponentiation algorithm could potentially become very large if the exponent y is a large number. In fact, s and p could become so large that their values exceed the maximum value that can be stored in a computer variable. Cryptographic applications require computing x<sup>y</sup> mod n for very large numbers. 

**Fortunately, adding intermediate mod n operations does not change the final result and keeps the intermediate values in the range from 0 through n - 1. To put that another way, all the calculations are going on over Z<sub>n</sub>, rather than over Z.** The figure below gives the algorithm for fast integer exponentiation mod n. 

```
Input: Positive integers x, y, and n.
Output: x^y mod n

p := 1     //p holds the partial result.
s := x     //s holds the current x^2^j.
r := y     //r is used to compute the binary expansion of y

While ( r > 0 )
      If ( r mod 2 = 1 )
            p := p·s mod n
      s := s·s mod n
      r := r div 2
End-while

Return(p) 
```

**NOTE:** Quite literally nothing has changed from the fast exponentiation algorithm aside from the `mod n` operations appended to two of the variable assignments. See the notes on that algorithm for more details here.

Ex. compute 5<sup>35</sup> mod 11:
```
CONSTRAINTS:
x = 5
y = 35
n = 11

p = 1
s = x (5)
r = y (35)


LOOPS:
p = 5 mod 11 = 5
s = 25 mod 11 = 3
r = 17

p = 15 mod 11 = 4
s = 9 mod 11 = 9
r = 8

p = 15
s = 81 mod 11 = 4
r = 4

p = 15
s = 16 mod 11 = 5
r = 2

p = 15
s = 25 mod 11 = 3
r = 1

p = 45 mod 11 = 1
s = 9 mod 11 = 9
r = 0

p = 1 is the answer.
```