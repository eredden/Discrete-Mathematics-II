### ASYMPTOTIC COMPLEXITY NOTATION:
**For a given function f() with input n, Ω(f(n)) ≤ Θ(f(n)) ≤ O(f(n)).** Omega notation is the worst case scenario for an algorithm, theta notation is the average scenario, and big O notation is the best case scenario. When representing the asymptotic complexity of an algorithm, it is important to drop all constants and only display the term which has the greatest impact (i.e. increases the fastest). This is the same for time and storage complexity.

### ALGORITHMS AND ATOMIC OPERATIONS:
**An algorithm is a set of steps for solving a problem. An atomic operation is an individual step that an algorithm takes -- variable assignments, comparisons, arithmetic operations, etc.** If the asymptotic complexity of a given algorithm is the polynomial 2n + 1 (that many atomic operations are executed), then you can drop the coefficient 2 and the constant 1 and provide n as the complexity. Algorithms which always execute the same number of atomic operations run in constant time, represented by the number 1.

### BIG O NOTATION AND COMMON NAMES:
- O(1) - Constant Time
- O(log n) - Logarithmic Time
- O(n) - Linear Time
- O(n<sup>2</sup>) - Quadratic Time
- O(2<sup>n</sup>) - Exponential Time