# Exercise 3.18.1: Recursively computing sums of cubes.
def sum_of_cubes(n: int) -> int:
    if n == 0:
        return 0
    
    return (n*n*n) + sum_of_cubes(n - 1)

# Exercise 3.18.2: Recursively computing the product of two integers.
def product_of_two(x: int, y: int) -> int:
    if y == 1:
        return x
    
    return x + product_of_two(x, y - 1)

if __name__ == "__main__":
    print(f"SUM OF CUBES (n=3): {sum_of_cubes(3)}")
    print(f"PRODUCT OF TWO (x=8, y=7): {product_of_two(8, 7)}")