class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        
        newList = []
        for i in range (len(nums)):
            for y in range (i+1, len(nums)):
                if i == len(nums):
                    break
                if (nums[i] == nums[y]):
                    newList.append(nums[i])

        return newList