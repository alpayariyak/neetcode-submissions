from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l2n = defaultdict(int)

        for letter in s:
            l2n[letter] += 1

        for letter in t:
            l2n[letter] -= 1
            if l2n[letter] < 0:
                return False
        
        final_counts = set(l2n.values())
        if len(final_counts) == 1 and final_counts.pop() == 0:
            return True 
        else:
            return False
