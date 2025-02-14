import time


def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  # Element found
        elif arr[mid] < target:
            low = mid + 1  # Search in the right half
        else:
            high = mid - 1  # Search in the left half

    return -1  # Element not found


# Start measuring time
start_time = time.perf_counter()

# Test binary search
result = binary_search([1, 2, 3, 4, 5, 6, 7, 8], 1)

# End measuring time
end_time = time.perf_counter()

# Output the result and execution time
print(f"Result: {result}")
print(f"Execution Time: {end_time - start_time:.6f} seconds")
execution_time_ms = (end_time - start_time) * 1000  # Convert to milliseconds
print(f"Execution Time: {execution_time_ms:.2f} milliseconds")

# An example of an algorithm with a time complexity of \( O(\log n) \) is **binary search**.

# ### Binary Search:

# Suppose you have a sorted array, and you want to find if a particular element exists in the array. Instead of checking each element one by one, you can divide the search space in half at each step.

# #### Algorithm:
# 1. Start with the entire array.
# 2. Find the middle element.
# 3. If the middle element is the target, you're done.
# 4. If the middle element is greater than the target, repeat the search on the left half of the array.
# 5. If the middle element is less than the target, repeat the search on the right half of the array.
# 6. Continue this process until you find the element or narrow down the search space to nothing.

#### Time Complexity:
# - The search space is divided in half with each iteration, so the number of operations grows logarithmically with the size of the array.
# - Thus, the time complexity is **\( O(\log n) \)**, where \( n \) is the number of elements in the array.

# This makes binary search much faster than linear search, which has a time complexity of \( O(n) \).
