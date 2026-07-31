class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myMap = {}

        for i, n in enumerate(nums):
            myMap[n] = i
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in myMap and myMap[diff] != i:
                return [i, myMap[diff]]    
        return []