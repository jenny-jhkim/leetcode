class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #Solution1
        #for i in range(k):
        #    nums.insert(0, nums[-1])
        #    nums.pop()

        #Solution2
        n = len(nums)
        k %= n #if k is greater than n
        nums_part1 = nums[0:n-k]
        nums_part2 = nums[n-k:]

        nums[:] = nums_part2 + nums_part1 #needs to update original list
