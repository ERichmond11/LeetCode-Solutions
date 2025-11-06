class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        for i in range (len(nums)-1, 0, -1):
            for j in range (i-1, -1, -1):
                if nums[i] == nums[j]:
                    nums.remove(nums[i])
                    break

        return len(nums)