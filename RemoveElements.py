class Solution:
    def RemoveElements(self,nums: list[int], val:int) -> int:
         j=0
         count=0
         for v in nums:
              
              if v!=val:
                   nums[j]=v
                   j+=1
              else:
                   count+=1
         return count
    
solution = Solution()


nums = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
val=2
j = solution.RemoveElements(nums,val)

print("Occurences of Value:",j)
print("Modified Array:", nums)