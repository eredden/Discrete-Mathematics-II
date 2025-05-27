## INTRO TO LINEAR HOMOGENOUS RECURRENCE RELATIONS

That's a mouthful. Recall that linear equations change at a constant rate. For example, y = 2x + 3 is linear, because y always changes twice as much as x. Graphically, the solutions of this equation form a line. Linear equations are not restricted to two dimensions. For example, w = x + 2y + 3x is also linear as the dependent variable changes at a constant rate with respect to any of the independent variables.

Recurrences are also **called** linear, as previous terms can be arranged as first-order polynomial expressions in the recurrence relation. However, their **growth is truly exponential**. For instance, the recurrence relation f<sub>n</sub> = 2f<sub>n - 1</sub> where f<sub>0</sub> = 1 yields the set {1, 2, 4, 8, 16, ...}.

There are many different kinds of recurrence relations, some of which are very difficult to solve. There are also recurrence relations for which there are no known explicit formula. **This material focuses on a particular class of recurrence relations called linear homogeneous recurrence relations. Each number in a sequence defined by a linear homogeneous recurrence relation is a linear combination of numbers that occur earlier in the sequence.**

### DEFINITION

A linear homogeneous recurrence relation of degree k has the following form: 

**f<sub>n</sub> = c<sub>1</sub>f<sub>n-1</sub> + c<sub>2</sub>f<sub>n-2</sub> + . . . + c<sub>k</sub>f<sub>n-k</sub>**

where the instances of c<sub>j</sub> are constants that do not depend on n, and c<sub>k</sub> != 0.

### DEGREES

The degree of a linear homogeneous recurrence relation is similar to getting the degree of a polynomial, except you are targetting the exponent with the largest number subtracted from n, and then getting the absolute value of that number. For the recurrence relation f<sub>n</sub> = f<sub>n-1</sub> + <sub>n-2</sub>, the degree is 2.

### DISCERNING HOMOGENEITY AND WHETHER A RECURRENCE RELATION IS LINEAR

- A recurrence relation is linear if any of the f<sub>n-j</sub> terms are multiplied by **constants.** Otherwise the recurrence is non-linear.
    - Note the usage of the word constant. No variable coefficients.
- A linear recurrence relation is homogeneous if all of the terms have a f<sub>n-j</sub>. Otherwise, it is non-homogeneous.


## SOLVING LINEAR HOMOGENEOUS RECURRENCE RELATIONS

### DERIVING THE CHARACTERISTIC EQUATION

**To solve a linear recurrence relation, we start with the guess that f<sub>n</sub> has the form x<sup>n</sup> for some x.** While there are mathematical tools to derive the solution to linear homogeneous recurrence relations without resorting to a guess, we know from experience that an exponential function is a good place to start. Factoring out the common base of all terms in the exponential expression and dividing it out of the equation gives rise to the characteristic equation for the recurrence. **The characteristic equation for a linear recurrence relation can be used to solve for x, the base of the exponent in the solution.**

Ex. getting the characteristic equation for the Fibonacci sequence (recurrence relation):
- The sequence is: f<sub>n</sub> = f<sub>n-1</sub> + f<sub>n-2</sub>
- Assume that: 
    - f<sub>n</sub> = x<sup>n</sup>, 
    - f<sub>n-2</sub> = x<sup>n-1</sup>, 
    - f<sub>n-2</sub> = x<sup>n-2</sup>
- Then the exponential expression x<sup>n</sup> = x<sup>n-1</sup> + x<sup>n-2</sup> is the same as the sequence shown above.
- We factor out the smallest power x<sup>n-2</sup> from all terms to become independent of n, as we want to solve for x: x<sup>2</sup> * x<sup>n-2</sup> = x * x<sup>n-2</sup> + 1 * x<sup>n-2</sup>
- Divide by x<sup>n-2</sup> to get x<sup>2</sup> = x + 1, which is the same as x<sup>2</sup> - x - 1 = 0. This is the characteristic equation.

### FINDING VALUES OF X THAT SOLVE THE EQUATION

Once the characteristic equation has been determined, the next step is to find all values of x that solve the equation. Since the characteristic equation has the form p(x) = 0, for some polynomial p(x), the goal is to find the roots of the polynomial. Some polynomials have complex roots. This material only covers the case where the characteristic equation has real roots. We first consider the case where all the roots are distinct. For example, the characteristic equation for the Fibonacci sequence gives rise to the binomial equation: 
- **x<sup>2</sup> - x - 1 = 0**

Solving for x yields two distinct solutions: 
- **x = (1 + sqrt(5)) / 2**,
- **x = 1 - sqrt(5) / 2**

 Both values for x satisfy the recursive relation. In fact, any linear combination of the two solutions satisfies the recurrence relation f<sub>n</sub> = f<sub>n-1</sub> + f<sub>n-2</sub>. A linear combination of the two solutions has the following form, where the variables s and t can be any real numbers: 

f<sub>n</sub> = s( (1 + sqrt(5)) / 2 )<sup>n</sup> + t( (1 - sqrt(5)) / 2 )<sup>n</sup>

Thus, there are an infinite number of solutions to the recurrence relation. However, not all of the solutions satisfy the initial values. **The expression denoting the infinite set of solutions to a recurrence relation without initial values is called the general solution to the recurrence relation.** The initial values add constraints that narrow down the set of possible solutions to particular values for s and t.

### THEOREM FOR SOLVING LINEAR HOMOGENEOUS RECURRENCE RELATIONS

If g<sub>n</sub> and h<sub>n</sub> satisfy a linear homogeneous recurrence relation then so does f<sub>n</sub> = s * g<sub>n</sub> + t * h<sub>n</sub> for any real numbers s and t.

### FINDING THE UNIQUE SOLUTION USING INITIAL VALUES

The solutions to the characteristic equations give a set of solutions to the recurrence relation. The theorem above says that any linear combination of the solutions will also be a solution to the recurrence relation. **The final step is to use the initial values to find the exact linear combination that satisfies the recurrence relation and the initial values. If the recurrence relation has degree d, then d initial values are required.**

Ex. continuing to solve the Fibonacci recurrence relation from before:

1. Let f<sub>0</sub> = 0. Plug in n = 0 into the general form (linear combination) for f<sub>n</sub>.
2. Simplifying the expression yields: 

**f<sub>0</sub> = c<sub>1</sub> + c<sub>2</sub> = 0**


3. Let f<sub>1</sub> = 1. Plug in n = 1 into the general form (linear combination) for f<sub>n</sub>.
4. This yields the second linear equation, giving us two variables and two linear equations:

**f<sub>1</sub> = c<sub>1</sub>( (1 + sqrt(5)) / 2 ) + c<sub>2</sub>( (1 - sqrt(5)) / 2 ) = 1**

5. Now we apply standard steps for solving a system of linear equations to get the values of c<sub>1</sub> and c<sub>2</sub>, and insert them into the general form for f<sub>n</sub>:
    - **c<sub>1</sub> = 1 / sqrt(5)**
    - **c<sub>2</sub> = -1 / sqrt(5)**

**f<sub>n</sub> = (1 / sqrt(5))( (1 + sqrt(5)) / 2 ) + (-1 / sqrt(5))( (1 - sqrt(5)) / 2 ) = 1**

6. Now you have the closed form solution for f<sub>n</sub>!