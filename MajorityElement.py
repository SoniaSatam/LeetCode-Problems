class Solution:
    def MajorityElements(self, nums: list[int]) -> int:
        nums.sort()
        n=len(nums)
        return nums[n//2]
    
solution = Solution()


nums = [2,2,1,1,1,2,2]
majority = solution.MajorityElements(nums)

print("Returned Value:", majority)
