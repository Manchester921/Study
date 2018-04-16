
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        i = -1
        index = []
        while(not index):
            i += 1
            temp = target - nums[i]
            for j in range(i+1, len(nums)):
                if nums[j] == temp:
                    index = [i, j]
                    break
        return index

obj1 = Solution()
c = obj1.twoSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8)
# c = twoSum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8)
print(c)