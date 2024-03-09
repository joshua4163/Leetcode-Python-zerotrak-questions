class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans=[]
        nums= int(n/2)
        if n%2!=0:
            ans.append(0)
        for i in range(1,nums+1):
            ans.append(i)
            ans.append(-i)
        return ans
