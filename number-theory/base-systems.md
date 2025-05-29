### OTHER NUMBER SYSTEMS TO BASE-10
You already know this stuff fairly well. Converting numbers from any base to base 10 simply requires that you multiply each digit integer d by the base integer b to the power of the digit place p, such as **d * b<sup>p</sup>**.

Fix an integer b > 1. Every non-negative integer n can be expressed uniquely as:

**n = a<sub>k</sub> * b<sup>k</sup> + a<sub>k-1</sub> * b<sup>k-1</sup> + . . . a<sub>1</sub> * b<sup>1</sup> + a<sub>0</sub> * b<sup>0</sup>**

where k is a non-negative integer, each a<sub>i</sub> is an integer in the range from 0 to b - 1, and a<sub>k</sub> ≠ 0.

Ex. **1001<sub>2</sub>** = (1 * 2<sup>3</sup>) + (0 * 2<sup>2</sup>) + (0 * 2<sup>1</sup>) + (1 * 2<sup>0</sup>) = **9<sub>10</sub>**

When a number system has a base number exceeding 10, extra symbols must be used to represent the subsequent digits. For the hexadecimal base-16 system, these are the first six letters of the alphabet. 0123456789ABCDEF is the full range of digit values for the base system, ranging from 0-15<sub>10</sub>. 

Each hexadecimal character represents 4 bits of data in binary (base-2 number system). F<sub>16</sub> = 1111<sub>2</sub>.

### BASE-10 TO OTHER NUMBER SYSTEMS

You actually wrote about this in a paper! 

"A common method for converting decimal numbers into other number system equivalents is to simply divide the decimal number n by desired base b repeatedly until the quotient is 0 (Morelli et al., 2015). The remainders from each operation must be lined up from the least significant digit leftwards. You can convert 291<sub>10</sub> back to 123<sub>16</sub> through this process: 291 mod 16 = 3, 18 mod 16 = 2, and 1 mod 16 = 1. Arranging the remainders from least significant digit leftwards makes 123<sub>16</sub>."

Provided below is an algorithm which carries this out.

```
Input: Integers n and b. b > 1 and n ≥ 1.
Output: Base b expansion of n. Base b digits are output in reverse order.

x := n
while ( x > 0 )
      Output( x mod b )
      x := x div b
End-while 
```
Ex. Find the expansion base 5 of 57<sub>10</sub>:
- 57 mod 5 = 2
- 57 div 5 = 11
- 11 mod 5 = 1
- 11 div 5 = 2
- 2 mod 5 = 2
- 2 div 5 = 0
- 57<sub>10</sub> = (2 * 5<sup>2</sup>) + (1 * 5<sup>1</sup>) + (2 * 5<sup>0</sup>) = **212<sub>5</sub>**


### REQUIRED DIGIT COUNT FOR REPRESENTATION
Many algorithms rely upon knowledge of how many digits a number will take up when represented in another base system. This can be determined using the formula *log*<sub>b</sub>(n + 1), where b is the base number and n is the number we are checking.

Ex. If we want to know how many digits the number 13<sub>10</sub> will take up in binary, you can plug it into *log*<sub>2</sub>(13 + 1) to get 4.