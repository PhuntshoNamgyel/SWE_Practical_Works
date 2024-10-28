## Step 1: Implement a Recursive Fibonacci Generator

def fibonacci_recursive(n):
    # Base case: If n is 0 or 1, return n (F(0) = 0, F(1) = 1)
    if n <= 1:
        return n
    else:
        # Recursive case: Return the sum of the previous two Fibonacci numbers
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Test the recursive function by printing the first 10 Fibonacci numbers
for i in range(10):
    print(f"F({i}) = {fibonacci_recursive(i)}")


## Step 2: Implement an Iterative Fibonacci Generator

def fibonacci_iterative(n):
    # Handle edge cases where n is 0 or 1, returning initial parts of the sequence
    if n <= 0:
        return [0]
    elif n == 1:
        return [0, 1]
    
    # Initialize the sequence list and starting values for iteration
    fib_list = [0, 1]
    a, b = 0, 1
    # Loop to generate the Fibonacci sequence up to n terms
    for _ in range(2, n + 1):
        a, b = b, a + b
        fib_list.append(b)  # Append the next number in the sequence
    return fib_list

# Test the modified iterative function to generate a Fibonacci sequence up to the 10th term
n = 10
print(f"Fibonacci sequence up to F({n}): {fibonacci_iterative(n)}")


## Step 3: Compare Performance

import time

def measure_time(func, n):
    # Measure the execution time of the given function
    start = time.time()  # Start time
    result = func(n)     # Run the function with input n
    end = time.time()    # End time
    return result, end - start  # Return the result and the time taken

# Test both recursive and iterative functions, comparing their execution times for n = 30
n = 30
recursive_result, recursive_time = measure_time(fibonacci_recursive, n)
iterative_result, iterative_time = measure_time(fibonacci_iterative, n)

print(f"Recursive: F({n}) = {recursive_result}, Time: {recursive_time:.6f} seconds")
print(f"Iterative: F({n}) = {iterative_result[-1]}, Time: {iterative_time:.6f} seconds")


## Step 4: Implement a Generator Function for Fibonacci Sequence

def fibonacci_generator(limit):
    # Initialize starting values for the sequence
    a, b = 0, 1
    count = 0
    while count < limit:
        yield a  # Produce the next Fibonacci number
        a, b = b, a + b  # Update values to next in sequence
        count += 1

# Test the generator to produce and print the first 10 Fibonacci numbers
for i, fib in enumerate(fibonacci_generator(10)):
    print(f"F({i}) = {fib}")


## Step 5: Implement Memoization for Recursive Fibonacci

def fibonacci_memoized(n, memo={}):
    # Check if the result is already computed and stored in 'memo'
    if n in memo:
        return memo[n]
    # Base case: If n is 0 or 1, return n
    if n <= 1:
        return n
    # Recursive case with memoization: Store the result in 'memo' to avoid duplicate computation
    memo[n] = fibonacci_memoized(n-1, memo) + fibonacci_memoized(n-2, memo)
    return memo[n]

# Test the memoized recursive function to print the first 10 Fibonacci numbers
for i in range(10):
    print(f"F({i}) = {fibonacci_memoized(i)}")

# Compare performance of memoized version with the original recursive function for n = 30
n = 30
memoized_result, memoized_time = measure_time(fibonacci_memoized, n)
print(f"Memoized: F({n}) = {memoized_result}, Time: {memoized_time:.6f} seconds")


## Step 6: Find the Index of the First Fibonacci Number that Exceeds a Given Value

def find_fibonacci_index_exceeding(value):
    # Start with the first two Fibonacci numbers
    a, b = 0, 1
    index = 1  # Initial index for Fibonacci sequence starting at F(1)
    # Loop until a Fibonacci number larger than the given value is found
    while b <= value:
        a, b = b, a + b  # Move to the next Fibonacci number
        index += 1  # Increment the index
    return index  # Return the index where the Fibonacci number first exceeds the value

# Test the function by finding the index of the first Fibonacci number exceeding a given value
value = 50
print(f"The index of the first Fibonacci number that exceeds {value} is {find_fibonacci_index_exceeding(value)}")


## Step 7: Determine if a Given Number is a Fibonacci Number

import math

def is_fibonacci_number(n):
    # Helper function to check if x is a perfect square
    def is_perfect_square(x):
        s = int(math.isqrt(x))  # Calculate integer square root
        return s * s == x  # Check if the square of s equals x

    # Check if 5*n^2 + 4 or 5*n^2 - 4 is a perfect square
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

# Test the function
test_numbers = [0, 1, 4, 5, 15, 18, 22, 26]
for number in test_numbers:
    print(f"{number} is a Fibonacci number: {is_fibonacci_number(number)}")


## Step 8: Calculate the Ratio Between Consecutive Fibonacci Numbers

def fibonacci_ratio(n):
    # Start with the first two Fibonacci numbers
    a, b = 0, 1
    ratios = []
    # Calculate ratios up to the (n-1)th ratio as we need pairs to form ratios
    for _ in range(n - 1):
        a, b = b, a + b  # Move to the next Fibonacci number
        if a != 0:  # Avoid division by zero when calculating the ratio
            ratios.append(b / a)  # Append the ratio of consecutive Fibonacci numbers
    return ratios

# Test the function and observe how the ratios approach the golden ratio (~1.618)
n = 15
ratios = fibonacci_ratio(n)
for i, ratio in enumerate(ratios, start=1):
    print(f"Ratio {i}: {ratio}")

print(f"\nAs we increase n, the ratios approach the golden ratio (~1.618).")
