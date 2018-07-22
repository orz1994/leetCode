"""
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

数组中两个数相加，得到目标。

排序后的数组查找最快的就是二分法了。
基本思路：
排序，
二分查找。

用目标逐个相减然后查找是否存在（其实可以顺便返回位置，这样就不用index了。）。

所以时间复杂度 O(nlogn)

改进：
有O(n) 方式。

测试数据：
https://leetcode.com/problems/two-sum/description/

"""

class Solution(object):
    def binarySearch(self, rawList, target):
        split = len(rawList) // 2
        
        left = rawList[:split]
        right = rawList[split:]
        
        
        if not left and not right:
            return None
        
        if left and left[-1] == target:
            return True
        
        if right and right[0] == target:
            return True
        
        if len(left) > 1 and left[-1] > target:
            return self.binarySearch(left, target)
        
        if len(right) > 1 and right[0] < target:
            return self.binarySearch(right, target)
        
        
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        sortedNums = sorted(nums)
        for i, data in enumerate(sortedNums):
            
            # if data <= target:
            
            if self.binarySearch(sortedNums[:i]+sortedNums[i+1:], target-data):
                result = sorted([nums.index(data), nums.index(target-data)])
                if result[0] == result[1]:
                    return [result[0], nums[result[0]+1:].index(target-data)+result[0]+1]
                
                return result
            # elif target < 0 and data > target:
                # if self.binarySearch(nums[:i]+nums[i+1:], target-data):
                    # return sorted([i, nums[i+1:].index(target-data)+i+1])
