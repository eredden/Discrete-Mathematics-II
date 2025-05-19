### DEFINITION OF MODULO CONGRUENCE:
Let n be an integer greater than 1. Let x and y be any two integers. **Then x is congruent to y modulo n if x mod n = y mod n.** The fact that x is congruent to y modulo n is denoted x ≡ y (mod n).

### IMPORTANCE OF MODULO CONGRUENCE:
A good example here would be coterminal angles from trigonometry. A 40 degree angle is coterminal with a 400 degree angle as their measures are the same when they are visualized on a circle. This is because both dividends modulo 360 degrees are equal to 40 degrees. The same congruence applies to converting 24-hour times to 12-hour times. Hours 0 and 12 are the same on an analog clock because both dividends modulo 12 are equal to 0.

Modulo congruence is especially useful in cryptography, as it is used to determine the divisibility of integers by very large prime numbers.

### ALTERNATIVE NOTATION FOR MODULAR ARITHMETIC:
If we want to perform modulo operations on a set of integers, we can declare that by saying all operations are in Z sub n. Z is the set of integers along with the usual arithmetic operations, i.e. (+, -, *, /). Z sub n is the set of integers {0, 1, 2, . . ., n-1} and arithmetic operations mod n (+ mod n, - mod n, * mod n). There is no (/ mod n) operation.

Let n be an integer larger than 1. Let x and y be integers. Then addition in Z is compatible with addition in Z sub n, as seen below:

**[(x mod n) + (y mod n)] mod n = [x + y] mod n**

**[(x mod n)(y mod n)] mod n = [x * y] mod n**

This means that you can reduce first and then do the operation, or you can do the operation and then reduce. It is generally simpler to reduce as much as possible as a first step. See an example below:

- (43<sup>17</sup> + 32 * 139) mod 7
- = [(43 mod 7)<sup>17</sup> + (32 mod 7)(139 mod 7)] mod 7
- = [1<sup>17</sup> + (4)(6)] mod 7 
- = [1 + 24] mod 7 
- = 25 mod 7 
- = 4