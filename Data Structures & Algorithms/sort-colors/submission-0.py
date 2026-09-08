from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
   
        sorted_nums = self.merge_sort(nums)

        for i in range(len(nums)):
            nums[i] = sorted_nums[i]
    
    def merge_sort(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        
        mid = len(nums) // 2
        left = self.merge_sort(nums[:mid])
        right = self.merge_sort(nums[mid:])
        
        return self.merge(left, right)
    
    def merge(self, left: List[int], right: List[int]) -> List[int]:
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])
        
        return result


nums = [1, 0, 1, 2]
sol = Solution()
sol.sortColors(nums)
print(nums) 

nums2 = [2, 0, 2, 1, 1, 0]
sol.sortColors(nums2)
print(nums2)  