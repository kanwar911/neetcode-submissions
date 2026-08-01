class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        heap =[]

        for num, freq in count.items():
            heapq.heappush(heap, (-freq, num))
        res = []

        for _ in range(k):
            neg_freq, num = heapq.heappop(heap)
            res.append(num)
        return res