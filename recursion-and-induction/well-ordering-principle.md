### WELL-ORDERING PRINCIPLE

The well-ordering principle says that any non-empty subset of the non-negative integers has a smallest element. 

**It can be shown that the principle of mathematical induction, the principle of strong induction, and the well-ordering principle are all equivalent.** In other words, using any one of the principles as an assumption, the other two principles can be proven. Below is a proof showing that if the well-ordering principle is true, then the principle of mathematical induction is true. 

### WELL-ORDERING IMPLIES INDUCTION

 **Proof by contrapositive: Well-ordering implies the principle of mathematical induction. if the well-ordering principle is true and S(n) is false for some n ≥ 1, then at least one of the two conditions for induction must fail.**

Suppose that S(n) is false for some n ≥ 1. Consider the set of integers n such that n ≥ 1 and S(n) is not true. By the well-ordering principle, there must be a smallest element m in that set. Note that m ≠ 0 because 0 is not a member of the set. (One of the criteria for an integer n to be included in the set is that n ≥ 1.) 

If m = 1, then S(1) is not true and the base case fails. If m ≥ 2, then S(m - 1) is true but S(m) is false. Letting k = m - 1, k ≥ 1 and S(k) is true but S(k + 1) is not true. Therefore, the inductive step fails for some k ≥ 1. Thus, if the statement S(n) is false for some n ≥ 1, then one of the two conditions for the principle of mathematical induction must be false.

### APPLICATION OF THE WELL-ORDERING PRINCIPLE

 Consider the statement: any postage costing ≥8 cents must be paid with 5 and 3 cent stamps. How could you prove this?

First, assume the opposite: there is a postage costing more than 8 cents that cannot be paid with 3 and 5 cents stamps. (This is called a "proof by contradiction.") Using set notation you can state this number is in a set **{x | x≠3a + 5b for a, b ∈ N}**. Since you are assuming it exists (though it actually does not) then by the well-ordering principle there is a smallest number for which you cannot make postage; let's call this number n. You can pay 8 = 3(1) + 5(1), and 9 = 3(3) + 0(5), and 10 = 3(0) + 5(2) postage; so n≥11. 

Now here is the trick. Using the well-ordering principle, you know that n is the smallest postage you could not pay. This means you can pay n - 3 cents for postage, and then you could pay n postage by using another 3 cent stamp. This is a contradiction and our assumption that we could not pay n postage must be false.

**TL;DR:** To show a certain property must hold for all n ∈ N, you can assume the contrary, and use the Well-Ordering Principle to derive a contradiction by selecting the "smallest counterexample."