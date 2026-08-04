from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1
        
        counts = sorted(counts.items(), key=lambda item: item[1], reverse=True)

        return [ num for num, count in counts[:k]] 