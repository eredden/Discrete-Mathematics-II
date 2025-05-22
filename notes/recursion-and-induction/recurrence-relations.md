### INTRODUCTION TO RECURRENCE RELATIONS

The sequence a = {7, 10, 13, 16, 19, 22, 25, ...} is an example of a recursive sequence, where each new value relies on the value before it. There is a pattern that is applied: repeatedly a<sub>n</sub> = a<sub>n-1</sub> + 3, as recursion means to happen or occur again repeatedly. **Recursion can perform an infinite set of operations using a finite set of rules.**

**A recurrence relation is an equation that expresses a new term using previous terms.** To write the equation you need two pieces of information: the initial terms (typically a<sub>0</sub>) and a rule defining the new term based on the previous term.

Ex.
for n ≥ 0 a<sub>n</sub> = 
- 7, if n = 0                          
- (a<sub>n-1</sub> + 3), if n ≥ 1


### SEQUENCE TYPES

The generic recurrence relation sequences are:
- In **arithmetic** sequences, the recurrence relation involves adding a fixed value to the previous number. 
    - a<sub>0</sub> = a (initial value)
    - a<sub>n</sub> = d + a<sub>n-1</sub>, for n ≥ 1 (recurrence relation)
- In **geometric** sequences, each number is obtained by multiplying the previous number by a fixed constant.
    - a<sub>0</sub> = a (initial value)
    - a<sub>n</sub> = r * a<sub>n-1</sub>, for n ≥ 1 (recurrence relation)


The **Fibonacci sequence** was originally created by Leonardo Fibonacci to mathematically describe the population of rabbits. Suppose that f<sub>n</sub> is the number of pairs of rabbits at the end of month n. Assume that the first pair of rabbits obtained for the colony are born at the end of month 1, so f<sub>0</sub> = 0 and f<sub>1</sub> = 1. In month n, the colony has all the rabbits from the previous month (f<sub>n-1</sub>) plus all the new rabbits born in that month. Thus, the Fibonacci sequence is defined as follows:

- f<sub>0</sub> = 0 
- f<sub>1</sub> = 1
- f<sub>n</sub> = f<sub>n-1</sub> + f<sub>n-2</sub>, for n ≥ 2


Testing, testing, 123:
- f<sub>0</sub> = 3
- f<sub>1</sub> = 5
- f<sub>2</sub> = 15
- f<sub>3</sub> = 