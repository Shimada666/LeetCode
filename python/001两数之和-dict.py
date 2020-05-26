class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Hash Map implementation
        '''
        hashmap = {}
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in hashmap:
                return [hashmap[another_num], index]
            hashmap[num] = index
        return None
