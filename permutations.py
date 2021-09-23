class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        if(len(nums)==1 or len(nums)==0):
            return([nums])
        if(len(nums)==2):
            return([nums]+[nums[::-1]])
        for i in range(len(nums)):
            ans += [[nums[i]]+j for j in self.permute(nums[:i]+nums[i+1:])]
        return(ans)
