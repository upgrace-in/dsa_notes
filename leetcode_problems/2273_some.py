class Solution:
    def removeAnagrams(self, words):
        # iterate from the bottom up
        # keep track of the most recent anagram (start from last word)
        # create a helper function that indicates True/False if words are anagrams
        # iterate from the second to last word down and compare it to the current
        # possible anagram. if they are anagrams, pop(i + 1) and set the new
        # anagram to i. if they're not, just reset the new anagram
        # do this until i is -1
        # Time O(N) Space: O(1)

        curr = words[-1]

        for i in range(len(words) - 2, -1, -1):
            if sorted(words[i]) == sorted(curr):
                words.pop(i + 1)

            curr = words[i]

        return words

# words = ["abba","baba","bbaa","cd","cd"]
# words = ['abcd', 'acdb', 'dcab', 'cd', 'dc']
# words = ['a', 'b', 'cd', 'cd', 'e']
words = ["z","z","z","gsw","wsg","gsw","krptu"]
# s = Solution()
# print(s.removeAnagrams(words))