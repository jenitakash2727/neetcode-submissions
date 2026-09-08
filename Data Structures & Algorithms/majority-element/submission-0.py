from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        n = len(nums)

        for i in nums:
            print("i", i)
            count = 0

            for j in nums:
                print("j", j)
                if i == j:
                    count += 1

            if count > n // 2:
                return i