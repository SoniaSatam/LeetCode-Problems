class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        total=0
        res=-1
        nums.sort()
        for n in nums:
            if total>n:
                res=total+n
            total+=n
        return res