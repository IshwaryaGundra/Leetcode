class Solution:
    def twoSum(self, arr,k):
        i=0
        n=len(arr)
        j=n-1
        while(i<=j):
            if arr[i]+arr[j]==k:
                return [i+1,j+1]
            elif arr[i]+arr[j]>k:
                j=j-1
            else:
                i=i+1
        return