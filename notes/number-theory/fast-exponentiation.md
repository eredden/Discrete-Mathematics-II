### REPEATED MULTIPLICATION VS SQUARING

When doing standard exponentiation, you multiply a number by itself n - 1 times to get the result. A more efficient way to exponentiate numbers is called ***fast exponentiation*, where you use successive squaring of values rather than repeated multiplication**, greatly speeding up the calculation process. 

**Fast exponentiation uses binary expansions of the exponent to successively square values rather than repeatedly multiplying them.**

Ex. standard exponentiation for x^16:
This takes 15 multiplication operations (16 - 1) which can take an impractical amount of time if the power is a very large number. **O(N) time.**
```
p := x
p := p * x
p = x^2
p := p * x
p = x^3

. . .

p = x^16 
```

Ex. fast exponentiation for x^16:
This tkaes 4 unique multiplication operations (sqrt(16)) which is far more efficient than standard exponentiation. **O(log n) time.**

```
p := x
p := p * p
p = x^2
p := p * p
p = x^4
p := p * p
p = x^8
p := p * p
p = x^16
```

### BINARY EXPANSION OF EXPONENTS

Let there be two integers, x and y. Then,
- Integer y will represent the exponent, which can be subjected to a binary expansion:
    - y = a<sub>k</sub> * 2<sup>k</sup> + a<sub>k-1</sub> * 2<sup>k-1</sup> + . . . a<sub>1</sub> * 2<sup>1</sup> + a<sub>0</sub> * 2<sup>0</sup>
- Integer x will represent the base number which is being exponentiated. It can be represented with y expanded in binary form and split into multiple powers which can be multiplied together.
    - x<sup>y</sup> 
    - = x<sup>a<sub>k</sub> * 2<sup>k</sup> + a<sub>k-1</sub> * 2<sup>k-1</sup> + . . . a<sub>1</sub> * 2<sup>1</sup> + a<sub>0</sub> * 2<sup>0</sup></sup>
    - = x<sup>(a<sub>k</sub> * 2<sup>k</sup>)</sup> * x<sup>(a<sub>k-1</sub> * 2<sup>k-1</sup>)</sup> * . . . * x<sup>(a<sub>1</sub> * 2<sup>1</sup>)</sup> * x<sup>(a<sub>0</sub> * 2<sup>0</sup>)</sup>
- If a<sub>k</sub> is 0 for a given power, then it can be omitted from the calculation as multiplying by x<sup>0</sup> = 1 does not change the product.

### FAST INEGER EXPONENTIATION

With the prerequisites covered above, we can now understand fast integer exponentiation. For the term x<sup>y</sup>, we expand the exponent y into binary form and split x<sup>y</sup> into multiple terms multiplied together. The product is our answer.

An iterative algorithm for doing this is shown below:
```
Input: Positive integers x and y.
Output: xy

p := 1     // p holds the partial result.
s := x     // s holds the current x^2^j.
r := y     // r is used to compute the binary expansion of y

While ( r > 0 )
      If ( r mod 2 = 1 )
            p := p·s
      s := s·s
      r := r div 2
End-while

Return(p) 
```

The initial value of r is y. The results of the (r mod 2) in each iteration are the bits in the binary representation of the exponent y in reverse order. The value of s is x<sup>2<sup>j</sup></sup> during iteration j. The product p is the product of all the x<sup>2<sup>j</sup></sup> terms for those iterations in which (r mod 2) = 1, i.e. odd. Thus, the final result is x<sup>y</sup>.

Ex. compute 7<sup>11</sup>:
- 11<sub>10</sub> = 1011<sub>2</sub>
- 11<sub>10</sub> = (1 * 2<sup>3</sup>) + (0 * 2<sup>2</sup>) + (1 * 2<sup>1</sup>) + (1 * 2<sup>0</sup>)
- 7<sup>11</sup> = 7<sup>(1 * 2<sup>3</sup>) + (0 * 2<sup>2</sup>) + (1 * 2<sup>1</sup>) + (1 * 2<sup>0</sup>)</sup>
- 7<sup>11</sup> = 7<sup>(1 * 2<sup>3</sup>)</sup> *  7<sup>(0 * 2<sup>2</sup>)</sup> * 7<sup>(1 * 2<sup>1</sup>)</sup> * 7<sup>(1 * 2<sup>0</sup>)</sup>
- 7<sup>11</sup> = 7<sup>(1 * 8)</sup> *  7<sup>(0 * 4)</sup> * 7<sup>(1 * 2)</sup> * 7<sup>(1 * 1)</sup>
- 7<sup>11</sup> = 7<sup>8</sup> *  7<sup>0</sup> * 7<sup>2</sup> * 7<sup>1</sup>
- 7<sup>11</sup> = 7<sup>8</sup> * 7<sup>2</sup> * 7<sup>1</sup>
- 7<sup>11</sup> = 5764801 * 49 * 7
- 7<sup>11</sup> = 1977326743