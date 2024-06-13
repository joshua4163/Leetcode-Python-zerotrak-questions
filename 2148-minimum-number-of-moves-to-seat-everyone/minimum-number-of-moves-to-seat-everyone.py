class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        k = 0
        for i in range(len(students)):
            k += abs(seats[i] - students[i])
        return k