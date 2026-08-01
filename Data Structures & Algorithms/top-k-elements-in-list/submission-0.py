class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        sorted_items = sorted(
            count.items(),
            key=lambda item: item[1],
            reverse=True
        )
        
        result = []
        
        for num, frequency in sorted_items[:k]:
            result.append(num)

        return result