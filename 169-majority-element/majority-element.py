class Solution:
    def majorityElement(self, nums):
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        for num in nums:
            if count[num] > len(nums) // 2:
                return num