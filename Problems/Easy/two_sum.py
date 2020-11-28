class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        store = {}
        index = 0
        for each in nums:
            main_val = target - each
            
            if main_val in store.keys():
                return [store[main_val], index]
            else:
                store[each] = index
                index = index + 1