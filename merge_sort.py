arr = [2, 9, 5, 1, 0, 3]

# recursive call mid left right part and do merge


def merge_sort(arr):
  if len(arr) <= 1:
    return arr
    #base case
    #if array is empty or has one element, it is already sorted
    #return the array as is
    #return arr
  mid = len(arr) // 2
  left = merge_sort(arr[:mid])
  right = merge_sort(arr[mid:])

  return merge(left, right)


def merge(left, right):
  merged = []
  i = 0  # left index
  j = 0  # right index
  while i < len(left) and j < len(right):
    if left[i] > right[j]:
      merged.append(right[j])
      j += 1
    else:
      merged.append(left[i])
      i += 1
  merged.extend(left[i:])
  merged.extend(right[j:])
  return merged


print(merge_sort(arr))

# conversion count
'''
class Solution:
  # Function to count inversions in the array
  def inversionCount(self, arr):
      def merge_sort(arr):
          # Base case: when array has one or no elements, it's already sorted
          if len(arr) <= 1:
              return arr, 0

          # Step 1: Divide the array
          mid = len(arr) // 2
          left, inv_left = merge_sort(arr[:mid])  # Recursively sort the left half
          right, inv_right = merge_sort(arr[mid:])  # Recursively sort the right half

          # Step 2: Merge and count inversions
          merged, inv_merge = merge_and_count(left, right)

          # Total inversions = inversions from the left, right, and merged halves
          total_inversions = inv_left + inv_right + inv_merge
          return merged, total_inversions

      def merge_and_count(left, right):
          i = j = inv_count = 0
          merged = []

          # Merging the two sorted arrays while counting inversions
          while i < len(left) and j < len(right):
              if left[i] <= right[j]:
                  merged.append(left[i])  # No inversion, add from left
                  i += 1
              else:
                  merged.append(right[j])  # Inversion found, add from right
                  inv_count += len(left) - i  # All remaining elements in left are greater than right[j]
                  j += 1

          # Add the remaining elements from both arrays
          merged.extend(left[i:])
          merged.extend(right[j:])
          return merged, inv_count

      # We only care about the inversion count, so return that
      _, total_inversions = merge_sort(arr)
      return total_inversions

'''
