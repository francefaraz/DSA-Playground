class Solution:
  def partition(self, s: str) -> list[list[str]]:
      def is_palindrome(sub: str) -> bool:
          return sub == sub[::-1]

      def backtrack(start: int, path: list[str]):
          # Base case: If we've reached the end of the string
          if start == len(s):
              result.append(path[:])  # Add a copy of the current path
              return

          # Explore all possible partitions
          for end in range(start, len(s)):
              substring = s[start:end + 1]
              if is_palindrome(substring):
                  # Add the palindrome substring to the path
                  path.append(substring)
                  # Recurse for the remaining string
                  backtrack(end + 1, path)
                  # Backtrack
                  path.pop()

      result = []
      backtrack(0, [])
      return result
s = "aab"
solution = Solution()
print(solution.partition(s))  # Output: [["a", "a", "b"], ["aa", "b"]]