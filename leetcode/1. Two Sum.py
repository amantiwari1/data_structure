class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        maps = {}
        for i in range(len(nums)):
            for j in range(len(nums)):
                if maps.get(target):
                    return maps[target]
                if i != j:
                    maps[nums[i]+nums[j]] = [i,j]
       
