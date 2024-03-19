class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        dis = k
        for i in nums:
            if i == 1:
                if dis < k:
                    return False
                dis = 0
            else:
                dis += 1
        return True