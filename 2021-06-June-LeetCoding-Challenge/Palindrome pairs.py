from typing import List

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(word):
            return word == word[::-1]

        word_dict = {word: i for i, word in enumerate(words)}
        results = []

        for i, word in enumerate(words):
            n = len(word)
            for j in range(n + 1):
                prefix = word[:j]
                suffix = word[j:]

                # Check if prefix is palindrome and reversed suffix exists in the dictionary
                if is_palindrome(prefix):
                    reversed_suffix = suffix[::-1]
                    if reversed_suffix in word_dict and word_dict[reversed_suffix] != i:
                        results.append([word_dict[reversed_suffix], i])

                # Check if suffix is palindrome and reversed prefix exists in the dictionary
                # j != n to avoid duplicate cases where the word is empty
                if j != n and is_palindrome(suffix):
                    reversed_prefix = prefix[::-1]
                    if reversed_prefix in word_dict and word_dict[reversed_prefix] != i:
                        results.append([i, word_dict[reversed_prefix]])

        return results

# Example usage
solution = Solution()
print(solution.palindromePairs(["bat", "tab", "cat"]))  # Output: [[0, 1], [1, 0]]
print(solution.palindromePairs(["abcd", "dcba", "lls", "s", "sssll"]))  # Output: [[0, 1], [1, 0], [3, 2], [2, 4]]
