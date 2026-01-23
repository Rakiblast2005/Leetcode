class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n=len(nums)
        total=sum(nums)
        prefix_sum=0
        result=[]

        for i in range(n):
            left=nums[i]*i - prefix_sum
            right=(total - prefix_sum - nums[i])-nums[i]*(n-i-1)
            result.append(left+right)
            prefix_sum  +=nums[i]
        return result 