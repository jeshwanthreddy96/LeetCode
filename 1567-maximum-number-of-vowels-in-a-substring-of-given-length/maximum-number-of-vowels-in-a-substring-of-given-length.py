class Solution(object):
    def maxVowels(self, s, k):
        vowels = "aeiou"
        l = 0
        count = 0
        ans = 0

        for r in range(len(s)):
            if s[r] in vowels:
                count += 1

            if r - l + 1 > k:
                if s[l] in vowels:
                    count -= 1
                l += 1

            if r - l + 1 == k:
                ans = max(ans, count)

        return ans
