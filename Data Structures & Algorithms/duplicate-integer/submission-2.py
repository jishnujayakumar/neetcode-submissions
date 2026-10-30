from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        views = defaultdict(int)

        for i in range(n):
            if nums[i] in views:
                return True
            else:
                views[nums[i]] += 1
        # O(n^2)
        # for i in range(n-1):
        #     for j in range(i+1, n):
        #         if nums[i] == nums[j]:
        #             return True

        return False
        