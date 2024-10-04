class Solution:
    def findpermute(self,nums,fre,ds,ans):
        if len(ds)==len(nums):
            ans.append(ds[:])
            return 
        for i in range(len(nums)):
            if fre[i]==0:
                ds.append(nums[i])
                fre[i]=1
                self.findpermute(nums,fre,ds,ans)
                ds.pop()
                fre[i]=0  
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        fre =[0]*len(nums)
        ds=[]
        self.findpermute(nums,fre,ds,ans)
        return ans
        