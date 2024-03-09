class Solution:
    def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        x = arrivalTime + delayedTime
        if x >= 24:
            return x - 24
        return x