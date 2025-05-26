## INTRO TO LINEAR HOMOGENOUS RECURRENCE RELATIONS

That's a mouthful. Recall that linear equations change at a constant rate. For example, y = 2x + 3 is linear, because y always changes twice as much as x. Graphically, the solutions of this equation form a line. Linear equations are not restricted to two dimensions. For example, w = x + 2y + 3x is also linear as the dependent variable changes at a constant rate with respect to any of the independent variables.

Recurrences are also **called** linear, as previous terms can be arranged as first-order polynomial expressions in the recurrence relation. However, their **growth is truly exponential**. For instance, the recurrence relation f<sub>n</sub> = 2f<sub>n - 1</sub> where f<sub>0</sub> = 1 yields the set {1, 2, 4, 8, 16, ...}.

There are many different kinds of recurrence relations, some of which are very difficult to solve. There are also recurrence relations for which there are no known explicit formula. **This material focuses on a particular class of recurrence relations called linear homogeneous recurrence relations. Each number in a sequence defined by a linear homogeneous recurrence relation is a linear combination of numbers that occur earlier in the sequence.**

### DEFINITION

A linear homogeneous recurrence relation of degree k has the following form: 

**f<sub>n</sub> = c<sub>1</sub>f<sub>n-1</sub> + c<sub>2</sub>f<sub>n-2</sub> + . . . + c<sub>k</sub>f<sub>n-k</sub>**

where the instances of c<sub>j</sub> are constants that do not depend on n, and c<sub>k</sub> != 0.


### DISCERNING HOMOGENEITY AND WHETHER A RECURRENCE RELATION IS LINEAR

- A recurrence relation is linear if any of the f<sub>n-j</sub> terms are multiplied by **constants.** Otherwise the recurrence is non-linear.
    - Note the usage of the word constant. No variable coefficients.
- A linear recurrence relation is homogeneous if all of the terms have a f<sub>n-j</sub>. Otherwise, it is non-homogeneous.
