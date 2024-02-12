class Solution:
    def RemoveDuplicates(self, nums: list[int]) -> int:
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[l] = nums[r]
                l += 1
        return l


solution = Solution()


nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]

length = solution.RemoveDuplicates(nums)

print("Returned Value:", length)
print("Modified Array:", nums[:length])

    

     