class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        myset = set(nums)
        longest = 0
        for num in myset:
            if num - 1 not in myset:
                length = 1
                start = num
                while(start + 1) in myset:
                    length += 1
                    start += 1
                longest = max(longest, length)

        return longest