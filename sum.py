from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        sol = set()
        nums = sorted(nums)

        for i in range(len(nums)-2):
            j = i+1
            k = len(nums)-1
            while j < k:
                while nums[i] + nums[j] + nums[k] > 0:
                    if i == j or j == k or i == k:
                        break
                    k -= 1
                while nums[i] + nums[j] + nums[k] < 0:
                    if i == j or j == k or i == k:
                        break
                    j += 1
                if nums[i] + nums[j] + nums[k] == 0 and i != j != k:
                    sol.add(tuple(sorted([nums[i], nums[j], nums[k]])))
                    j += 1

        return list(sol)
