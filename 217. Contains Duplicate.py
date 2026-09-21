class Solution:
    def containsDuplicate(self, nums):
        seen = {}

        for number in nums:
            if number in seen:
                return True

            seen[number] = True

        return False
