## GENERALIZED PRODUCT RULE

#### DESCRIPTION 
What if you had a situation where you had two sets with different numbers of elements in each set (different cardinalities), and you had to determine the number of possibilities for a given number of choices or steps? For example, let's say you are at the racetrack and there are ten horses running. Only one horse can take first, one horse can take second, and one horse can take third place. Since the horse winning first place affects the number of horses available in the set for second place, how would you determine the number of combinations of first, second, and third place wins?

In this lesson you will expand on your basic knowledge of the product rule from the first lesson to learn the generalized product rule. **Essentially, the number of items for each set or step is multiplied by the number in the next step, and so on.** This generalized rule will help you count large possibilities easily and efficiently in future computer science applications. 

#### THEOREM
**TL;DR: To calculate the number of possibilities using the generalized product rule, multiply the number of items for each set or step by the number in the next step, etc. In the lesson introduction there was an example with horses in a race. The number of possible outcomes is 10 x 9 x 8 = 720.**

Consider a set S of sequences of k items. Suppose there are:
- n<sub>1</sub> choices for the first item.
- For every possible choice for the first item, there are n<sub>2</sub> choices for the second item.
- For every possible choice for the first and second items, there are n<sub>3</sub> choices for the third item.
- . . . 
- For every possible choice for the first k-1 items, there are n<sub>k</sub> choices for the k<sup>th</sup> item.

Then **|S| = n<sub>1</sub> * n<sub>2</sub> * ... * n<sub>k</sub>**.

#### EXAMPLE
Let's say there are seven different fruit candies in one jar and four different chocolate candies in another jar. How many possibilities are there for two friends to choose two pieces of candy (one from each jar)?
Answer: The first person has 7 x 4 choices, and the second person has 6 x 3 choices. Total number of choices = 28 x 18 = 504.