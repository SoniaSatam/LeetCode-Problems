class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        fp=-1
        lp=-1
        count=0
        for i in range(0,len(nums)):
            if target==nums[i]:
             if fp==-1:
              fp=i
              count+=1
             else:
                lp=i
                count+=1
        if count==1:
            lp=fp
        return(fp,lp)
    
solution = Solution()


nums = [2,2,1,1,1,2,2]
target=2
result = solution.searchRange(nums,target)

print(result)