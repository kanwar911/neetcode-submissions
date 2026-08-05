class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)):
            anchor = nums[i]
             # Skip duplicate anchors
            if i > 0 and anchor == nums[i - 1]:
                continue
            
            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = anchor + nums[left] + nums[right]
                if total == 0:
                    res.append([anchor, nums[left], nums[right]])
                    left += 1
                    right -= 1

                     # Skip duplicate left values
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    # Skip duplicate right values
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1
                else:
                    right -= 1
        return res