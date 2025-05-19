### GREATEST COMMON DENOMINATOR THEOREM:
Let x and y be two positive integers. Then **GCD(x, y) = GCD(y mod x, x).**


### EUCLIDEAN ALGORITHM:
The simplification of calculating the GCD for two integers using modulo operations can be repeated. y is set to the value of x, x is set to the remainder, and then the **modulo operations repeat until y mod x = 0**. Once y mod x = 0, the y is a multiple of x and **GCD(x, y) = x**.

```
Input: Two positive integers, x and y.
Output: GCD(x, y).

If ( x > y )
      Swap x and y.
r := y mod x.

While ( r ≠ 0 )
      y := x
      x := r
      r := y mod x.
End-while

Return( x )
``` 


### EXTENDED EUCLIDEAN ALGORITHM:
The GCD of x and y can be expressed as a linear combination of x and y.
Let x and y be integers, then there are integers s and t such that:
**GCD(x, y) = sx + ty**

Ex. GCD(874, 2415) = (s * 874) + (t * 2415)

Recall that the equation used for division and modulo operations is y = qx + r. We can modify this to solve for r, such that r = y - qx. We can eliminate q by substituting it with (y div x), such that:
r = y - (y div x) * x

With this knowledge in hand, you can find the Bezout coefficients (s, t) of the linear combination of x and y by doing the following:

1. Perform the standard Euclidean algorithm and note down each step in the form **y = qx + r**.
2. Now express each remainder as a linear combination of a and b. Start from the second to last step (r = GCD here) by transforming it into the form **r = y - qx**.
3. Substitute 

. . .