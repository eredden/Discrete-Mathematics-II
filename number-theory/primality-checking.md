### BRUTE FORCE PRIMALITY CHECKING:
If you want to check if an integer x is composite (divisible by some positive integer greater than one) or a prime, you can do so by dividing that integer x by every number in the range 2 to sqrt(x), as **sqrt(x) is the highest possible factor of x.** This would also obviously give you the factors of that composite number. 

Because the speed of this algorithm is bounded by the size of the integer x rather than the number of digits, it is inefficient. There is no efficient algorithm for finding the factors of a composite number. This is why the RSA encryption scheme cannot be easily broken yet. However, there is an efficient algorithm for finding out the primality of a number alone.

### THE PRIME NUMBER THEOREM:
Euclid proved in 300 B.C. that **there are an infinite number of primes.** However, this does not tell us how many numbers we should expect to check in a sequence before running into a prime. The theorem below changes this.

Let π(x) be the number of prime numbers in the range from 2 to x. Then,

```
                 π(x)                  
lim x -> ∞    ________ = 1
               x / ln x
```

Ex.
**The prime number theorem says that the fraction of primes is close to (1 / ln x).** For x = 10,000, the prime percentage would be around 0.1086 and for x = 1,000,000,000, the prime percentage would be around 0.048. 

You can estimate the number of primes in the range from 2 to x by substituting x in the expression (x / ln x). This is the same as multiplying x by the percentages we figured out with the previous expression (1 / ln x). For instance, the number 10<sup>7</sup> has 620,421 primes since (10<sup>7</sup> / ln 10<sup>7</sup>) is approximately 620,421.