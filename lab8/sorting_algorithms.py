# Step 1: Implement Bubble Sort

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Test the function
test_arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(test_arr.copy())
print("Bubble Sort Result:", sorted_arr)


# Step 2: Implement Merge Sort

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Test the function
test_arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = merge_sort(test_arr)
print("Merge Sort Result:", sorted_arr)


# Step 3: Implement Quick Sort

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

# Test the function
test_arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = quick_sort(test_arr)
print("Quick Sort Result:", sorted_arr)


# Step 4: Implement In-Place Quick Sort

def quick_sort_in_place(arr, low, high):
    # Recursively sort the array in place
    if low < high:
        pivot_index = partition(arr, low, high)  # Partition the array
        quick_sort_in_place(arr, low, pivot_index - 1)  # Sort left side
        quick_sort_in_place(arr, pivot_index + 1, high)  # Sort right side

def partition(arr, low, high):
    pivot = arr[low]  # Choosing the first element as pivot
    left = low + 1
    right = high

    done = False
    while not done:
        # Move the left index to the right as long as it's less than or equal to the pivot
        while left <= right and arr[left] <= pivot:
            left += 1
        # Move the right index to the left as long as it's greater than or equal to the pivot
        while arr[right] >= pivot and right >= left:
            right -= 1
        if right < left:
            done = True  # All elements are partitioned
        else:
            arr[left], arr[right] = arr[right], arr[left]  # Swap elements

    arr[low], arr[right] = arr[right], arr[low]  # Place the pivot in the correct position
    return right  # Return the pivot index

# Test the function
test_arr = [64, 34, 25, 12, 22, 11, 90]
quick_sort_in_place(test_arr, 0, len(test_arr) - 1)  # Perform in-place quick sort
print("In-place Quick Sort Result:", test_arr)


# Step 5: Modified Bubble Sort with Early Exit

def modified_bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False  # Flag to detect any swaps in this pass
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:  # If the current element is greater than the next
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap elements
                swapped = True  # A swap occurred
        # If no two elements were swapped by inner loop, the array is already sorted
        if not swapped:
            break  # Exit the loop early since the array is sorted
    return arr

# Test the function
test_arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = modified_bubble_sort(test_arr.copy())  # Perform modified bubble sort
print("Modified Bubble Sort Result:", sorted_arr)


# Step 6: Hybrid Sort (Merge Sort with Insertion Sort for Small Subarrays)

def insertion_sort(arr, left, right):
    # Perform insertion sort on a subarray
    for i in range(left + 1, right + 1):
        key = arr[i]  # Current element to be positioned
        j = i - 1
        # Move elements that are greater than key one position ahead of their current position
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  # Place key in the correct position

def hybrid_merge_sort(arr, threshold=10):
    # Use insertion sort for small arrays, merge sort otherwise
    if len(arr) <= threshold:
        insertion_sort(arr, 0, len(arr) - 1)  # Apply insertion sort
        return arr
    else:
        mid = len(arr) // 2  # Find the mid index
        left = hybrid_merge_sort(arr[:mid], threshold)  # Sort left half
        right = hybrid_merge_sort(arr[mid:], threshold)  # Sort right half
        return merge(left, right)  # Merge the sorted halves

# Test the function
test_arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = hybrid_merge_sort(test_arr)  # Perform hybrid merge sort
print("Hybrid Merge Sort Result:", sorted_arr)


# Step 7: Compare Performances

import time
import random

def compare_sorting_algorithms(arr):
    # Wrapping quick_sort_in_place to provide the additional parameters
    def quick_sort_in_place_wrapper(arr):
        quick_sort_in_place(arr, 0, len(arr) - 1)  # Sort in place
        return arr

    # List of sorting algorithms to compare
    algorithms = [
        ("Bubble Sort", bubble_sort),                          # Step 1
        ("Modified Bubble Sort", modified_bubble_sort),        # Step 5
        ("Merge Sort", merge_sort),                            # Step 2
        ("Hybrid Merge Sort", hybrid_merge_sort),              # Step 6
        ("Quick Sort", quick_sort),                            # Step 3
        ("In-place Quick Sort", quick_sort_in_place_wrapper)   # Step 4
    ]
    
    # Measure and print the execution time of each sorting algorithm
    for name, func in algorithms:
        arr_copy = arr.copy()  # Create a copy of the array for each algorithm
        start_time = time.time()  # Start the timer
        func(arr_copy)  # Call each algorithm with a copy of the array
        end_time = time.time()  # End the timer
        print(f"{name} took {end_time - start_time:.6f} seconds")

# Generate a large random array
large_arr = [random.randint(1, 1000) for _ in range(1000)]

# Compare the algorithms
compare_sorting_algorithms(large_arr)


# Step 8: Visualize Sorting Algorithms Using Matplotlib

import matplotlib.pyplot as plt
import matplotlib.animation as animation

def capture_snapshots(sort_func, arr):
    """Wrapper to capture each state of the array during sorting."""
    snapshots = []
    
    # Define a helper function to append array states to snapshots
    def add_snapshot():
        snapshots.append(arr.copy())
    
    # Call the sorting function with the snapshot callback
    sort_func(arr, add_snapshot)
    
    return snapshots

def visualize_sorting_snapshots(snapshots, sort_name):
    """Animate array sorting snapshots using matplotlib."""
    fig, ax = plt.subplots()
    ax.set_title(f"{sort_name} Visualization")
    bar_rects = ax.bar(range(len(snapshots[0])), snapshots[0], align="edge", color="darkblue")
    ax.set_xlim(0, len(snapshots[0]) - 1)
    ax.set_ylim(0, int(1.1 * max(max(snapshots, key=max))))

    def update_bars(frame):
        for rect, val in zip(bar_rects, snapshots[frame]):
            rect.set_height(val)

    ani = animation.FuncAnimation(fig, update_bars, frames=len(snapshots), repeat=False, interval=150)
    plt.show()

# Modified sorting functions to include snapshot capturing

def bubble_sort_snapshots(arr, add_snapshot):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            add_snapshot()  # Capture array state after each swap
    return arr

def merge_sort_snapshots(arr, add_snapshot):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort_snapshots(arr[:mid], add_snapshot)
    right = merge_sort_snapshots(arr[mid:], add_snapshot)

    merged = merge_and_capture(left, right, arr, add_snapshot)
    add_snapshot()  # Capture array state after merging
    return merged

def merge_and_capture(left, right, merged, add_snapshot):
    i = j = k = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged[k] = left[i]
            i += 1
        else:
            merged[k] = right[j]
            j += 1
        k += 1
        add_snapshot()  # Capture array state at each comparison

    while i < len(left):
        merged[k] = left[i]
        i += 1
        k += 1
        add_snapshot()

    while j < len(right):
        merged[k] = right[j]
        j += 1
        k += 1
        add_snapshot()

    return merged

def quick_sort_snapshots(arr, add_snapshot):
    def quick_sort_helper(arr, low, high):
        if low < high:
            pivot_index = partition_and_capture(arr, low, high, add_snapshot)
            quick_sort_helper(arr, low, pivot_index - 1)
            quick_sort_helper(arr, pivot_index + 1, high)
        add_snapshot()

    quick_sort_helper(arr, 0, len(arr) - 1)
    return arr

def partition_and_capture(arr, low, high, add_snapshot):
    pivot = arr[low]
    left = low + 1
    right = high

    while True:
        while left <= right and arr[left] <= pivot:
            left += 1
        while arr[right] >= pivot and right >= left:
            right -= 1
        if right < left:
            break
        arr[left], arr[right] = arr[right], arr[left]
        add_snapshot()  # Capture array state at each swap

    arr[low], arr[right] = arr[right], arr[low]
    add_snapshot()  # Capture array state after pivot swap
    return right

# Test the visualizations

test_arr = [64, 34, 25, 12, 22, 11, 90]

# Bubble Sort Visualization
snapshots = capture_snapshots(bubble_sort_snapshots, test_arr.copy())
visualize_sorting_snapshots(snapshots, "Bubble Sort")

# Merge Sort Visualization
snapshots = capture_snapshots(merge_sort_snapshots, test_arr.copy())
visualize_sorting_snapshots(snapshots, "Merge Sort")

# Quick Sort Visualization
snapshots = capture_snapshots(quick_sort_snapshots, test_arr.copy())
visualize_sorting_snapshots(snapshots, "Quick Sort")


