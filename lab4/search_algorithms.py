## Step 1: Implement Linear Search with Comparison Count

def linear_search(arr, target):
    indices = []  # List to store indices where the target is found
    comparisons = 0  # Counter for comparisons
    for i in range(len(arr)):
        comparisons += 1  # Increment for each comparison
        if arr[i] == target:
            indices.append(i)
    return indices, comparisons  # Return the list of indices and comparison count

# Test the modified function
test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
result, comparisons = linear_search(test_list, 5)
print(f"Linear Search: Indices of 5 are {result}, Comparisons made: {comparisons}")


## Step 2: Implement Binary Search with Comparison Count

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    comparisons = 0  # Counter for comparisons
    
    while left <= right:
        comparisons += 1  # Increment for each comparison
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid, comparisons  # Return the index and comparison count if the target is found
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1, comparisons  # Return -1 and comparison count if the target is not in the list

# Test the function
test_list_sorted = sorted(test_list)
result, comparisons = binary_search(test_list_sorted, 6)
print(f"Binary Search: Index of 6 in sorted list is {result}, Comparisons made: {comparisons}")


## Step 3: Implement Recursive Binary Search with Comparison Count

def binary_search_recursive(arr, target, left, right, comparisons=0):
    if left > right:
        return -1, comparisons
    
    comparisons += 1  # Increment for each comparison
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid, comparisons
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right, comparisons)
    else:
        return binary_search_recursive(arr, target, left, mid - 1, comparisons)

# Test the recursive function
result, comparisons = binary_search_recursive(test_list_sorted, 6, 0, len(test_list_sorted) - 1)
print(f"Recursive Binary Search: Index of 6 in sorted list is {result}, Comparisons made: {comparisons}")


## Step 4: Compare Performance with Comparison Count

import time

def compare_search_algorithms(arr, target):
    # Linear Search
    start_time = time.time()
    linear_result, linear_comparisons = linear_search(arr, target)
    linear_time = time.time() - start_time
    
    # Binary Search (on sorted array)
    arr_sorted = sorted(arr)
    start_time = time.time()
    binary_result, binary_comparisons = binary_search(arr_sorted, target)
    binary_time = time.time() - start_time
    
    print(f"Linear Search: Found at indices {linear_result}, Comparisons: {linear_comparisons}, Time: {linear_time:.6f} seconds")
    print(f"Binary Search: Found at index {binary_result}, Comparisons: {binary_comparisons}, Time: {binary_time:.6f} seconds")

# Test with a larger list
large_list = list(range(10000))
compare_search_algorithms(large_list, 8888)


## Step 5: Implement Find Insertion Point with Comparison Count

def find_insertion_point(arr, target):
    left, right = 0, len(arr) - 1
    comparisons = 0  # Counter for comparisons
    
    while left <= right:
        comparisons += 1  # Increment for each comparison
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid, comparisons  # Target found, return index and comparisons count
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return left, comparisons  # Return insertion point and comparisons count

# Test the insertion point function
result, comparisons = find_insertion_point(test_list_sorted, 7)
print(f"Insertion Point for 7 in sorted list is {result}, Comparisons made: {comparisons}")


## Step 6: Create a Main Function with Comparison Count

def main():
    # Create a list of 20 random integers between 1 and 100
    import random
    test_list = [random.randint(1, 100) for _ in range(20)]
    
    print("Original list:", test_list)
    print("Sorted list:", sorted(test_list))
    
    target = random.choice(test_list)  # Choose a random target from the list
    print(f"\nSearching for: {target}")
    
    # Linear Search
    result, comparisons = linear_search(test_list, target)
    print(f"Linear Search: Found at indices {result}, Comparisons made: {comparisons}")
    
    # Binary Search (iterative)
    sorted_list = sorted(test_list)
    result, comparisons = binary_search(sorted_list, target)
    print(f"Binary Search (iterative): Found at index {result}, Comparisons made: {comparisons}")
    
    # Binary Search (recursive)
    result, comparisons = binary_search_recursive(sorted_list, target, 0, len(sorted_list) - 1)
    print(f"Binary Search (recursive): Found at index {result}, Comparisons made: {comparisons}")
    
    # Find Insertion Point
    insertion_point, comparisons = find_insertion_point(sorted_list, target)
    print(f"Insertion Point for {target} in sorted list is {insertion_point}, Comparisons made: {comparisons}")
    
    # Compare performance
    print("\nPerformance Comparison:")
    compare_search_algorithms(list(range(100000)), 99999)

if __name__ == "__main__":
    main()


## Step 7: Implement Jump Search with Comparison Count

import math

def jump_search(arr, target):
    length = len(arr)
    step = int(math.sqrt(length))  # Calculate optimal jump size
    comparisons = 0  # Counter for comparisons
    prev = 0
    
    # Finding the block where the target may be present
    while arr[min(step, length) - 1] < target:
        comparisons += 1
        prev = step
        step += int(math.sqrt(length))
        if prev >= length:
            return -1, comparisons  # Target not found
    
    # Performing linear search within the identified block
    while arr[prev] < target:
        comparisons += 1
        prev += 1
        if prev == min(step, length):
            return -1, comparisons  # Target not found within block
    
    # Check if target is found
    comparisons += 1
    if arr[prev] == target:
        return prev, comparisons
    return -1, comparisons  # Target not found

# Modify compare_search_algorithms to include Jump Search
def compare_search_algorithms(arr, target):
    # Linear Search
    start_time = time.time()
    linear_result, linear_comparisons = linear_search(arr, target)
    linear_time = time.time() - start_time
    
    # Binary Search (on sorted array)
    arr_sorted = sorted(arr)
    start_time = time.time()
    binary_result, binary_comparisons = binary_search(arr_sorted, target)
    binary_time = time.time() - start_time
    
    # Jump Search (on sorted array)
    start_time = time.time()
    jump_result, jump_comparisons = jump_search(arr_sorted, target)
    jump_time = time.time() - start_time
    
    print(f"Linear Search: Found at indices {linear_result}, Comparisons: {linear_comparisons}, Time: {linear_time:.6f} seconds")
    print(f"Binary Search: Found at index {binary_result}, Comparisons: {binary_comparisons}, Time: {binary_time:.6f} seconds")
    print(f"Jump Search: Found at index {jump_result}, Comparisons: {jump_comparisons}, Time: {jump_time:.6f} seconds")

# Test with a larger list
large_list = list(range(10000))
compare_search_algorithms(large_list, 8888)
