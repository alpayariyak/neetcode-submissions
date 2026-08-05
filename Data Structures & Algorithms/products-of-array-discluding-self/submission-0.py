def get_prefix_product(numlist):
    #Exclusive, meaning that prefixes[i] does not include nums[i]
    prefixes = []
    product = 1
    for n in numlist:
        prefixes.append(product)
        product *= n
    return prefixes

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = get_prefix_product(nums)
        postfixes = get_prefix_product(nums[::-1])[::-1]
        return [prefixes[i] * postfixes[i] for i in range(len(nums))]
