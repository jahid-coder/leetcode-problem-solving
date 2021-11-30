from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        end = len(nums) - 1
        start, bestPos = 0, 0
        while(start <= end):
            mid = (start + end) // 2
            val = nums[mid]
            if(val == target):
                return mid
            elif(target < val):
                end = mid - 1
                bestPos = mid
            else:
                start = mid + 1
                bestPos = mid + 1
        return bestPos
