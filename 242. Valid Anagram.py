class Solution:
    def isAnagram(self, s, t):
        frequency_s = {}
        frequency_t = {}

        for character in s:
            if character in frequency_s:
                frequency_s[character] += 1
            else:
                frequency_s[character] = 1

        for character in t:
            if character in frequency_t:
                frequency_t[character] += 1
            else:
                frequency_t[character] = 1

        return frequency_s == frequency_t
