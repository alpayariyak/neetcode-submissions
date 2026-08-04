class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consecutive = 0
        current_counter = 0
        
        for num in nums:
            
            if num == 1:
                current_counter += 1
            else:
                max_consecutive = max(current_counter, max_consecutive)
                current_counter = 0

        max_consecutive = max(current_counter, max_consecutive)

        return max_consecutive