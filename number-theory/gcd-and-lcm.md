### GCD AND LCM DEFINITIONS:
The **greatest common divisor (GCD)** of non-zero integers x and y is the **largest positive integer that is a factor of both x and y.**
Ex. the GCD of 12 and 18 is 6.

The **least common multiple (LCM)** of non-zero integers x and y is the **smallest positive integer that is divisible both x and y.**
Ex. the LCM of 12 and 15 is 60.

### CALCULATING THE GCD AND LCM:
1. Get the prime factorizations of x and y.
2. For prime factors present in one factorization and not the other, multiply it in and set it to the power of zero. This turns it into 1 so that the product is unchanged.
3. Once both prime factorizations contain the same factors, get the maximum (LCM) or minimum (GCD) exponents from each factorization and combine that into the maximum or minimum factorization. The product will be the LCM or GCD. 

GCD Ex. 
 - The prime factorization for 24 is 2<sup>3</sup> * 3.
 - The prime factorization for 50 is 5<sup>2</sup> * 2.
 - Note that prime factor 3 is unique to 24, and 5 is unique to 50.
 - Multiply the factorization of 24 by 5<sup>0</sup> to get 5<sup>0</sup> * 2<sup>3</sup> * 3<sup>1</sup>.
 - Mulitply the factorization of 50 by 3<sup>0</sup> to get 5<sup>2</sup> * 2<sup>1</sup> * 3<sup>0</sup>.
 - The factorizations share the same prime factors, so we can continue.
 - GCD(24, 50) = 2<sup>min(3,1)</sup> * 3<sup>min(1,0)</sup> * 5<sup>min(0,2)</sup>
 - GCD(24, 50) = 2<sup>1</sup> * 3<sup>0</sup> * 5<sup>0</sup>
 - GCD(24, 50) = 2

LCM Ex. 
 - The prime factorization for 24 is 2<sup>3</sup> * 3.
 - The prime factorization for 50 is 5<sup>2</sup> * 2.
 - Note that prime factor 3 is unique to 24, and 5 is unique to 50.
 - Multiply the factorization of 24 by 5<sup>0</sup> to get 5<sup>0</sup> * 2<sup>3</sup> * 3<sup>1</sup>.
 - Mulitply the factorization of 50 by 3<sup>0</sup> to get 5<sup>2</sup> * 2<sup>1</sup> * 3<sup>0</sup>.
 - The factorizations share the same prime factors, so we can continue.
 - LCM(24, 50) = 2<sup>max(3,1)</sup> * 3<sup>max(1,0)</sup> * 5<sup>max(0,2)</sup>
 - LCM(24, 50) = 2<sup>3</sup> * 3<sup>1</sup> * 5<sup>2</sup>
 - LCM(24, 50) = 8 * 3 * 25
 - LCM(24, 50) = 600

### PRACTICE PROBLEM EXAMPLES:

Given:
- 147 = 3<sup>1</sup> * 7<sup>2</sup>
- 315 = 3<sup>2</sup> * 5<sup>1</sup> * 7<sup>1</sup>
- 550 = 2<sup>1</sup> * 5<sup>2</sup> * 11<sup>1</sup>

Find GCD(147, 315):
- 147 = 3<sup>1</sup> * 5<sup>0</sup> * 7<sup>2</sup>
- 315 = 3<sup>2</sup> * 5<sup>1</sup> * 7<sup>1</sup>
- GCD(147, 315) = 3<sup>1</sup> * 5<sup>0</sup> * 7<sup>1</sup>
- GCD(147, 315) = 21

Find LCM(147, 315):
- 147 = 3<sup>1</sup> * 5<sup>0</sup> * 7<sup>2</sup>
- 315 = 3<sup>2</sup> * 5<sup>1</sup> * 7<sup>1</sup>
- LCM(147, 315) = 3<sup>2</sup> * 5<sup>1</sup> * 7<sup>2</sup>
- LCM(147, 315) = 9 * 5 * 49
- LCM(147, 315) = 45 * 49
- LCM(147, 315) = 2205

Find GCD(315, 550):
- 315 = 2<sup>0</sup> * 3<sup>2</sup> * 5<sup>1</sup> * 7<sup>1</sup> * 11<sup>0</sup>
- 550 = 2<sup>1</sup> * 3<sup>0</sup> * 5<sup>2</sup> * 7<sup>0</sup> * 11<sup>1</sup>
- GCD(315, 550) = 2<sup>0</sup> * 3<sup>0</sup> * 5<sup>1</sup> * 7<sup>0</sup> * 11<sup>0</sup>
- GCD(315, 550) = 5