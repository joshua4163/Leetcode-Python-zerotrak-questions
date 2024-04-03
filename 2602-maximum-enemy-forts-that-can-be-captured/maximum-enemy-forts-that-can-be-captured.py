class Solution:
    def captureForts(self, forts: List[int]) -> int:
        l = len(forts)
        cnt = mx = 0
        start = False

        for i in range(l):
            if forts[i] == 1:
                if start:
                    cnt = 0
                else:
                    start = not start
            elif forts[i] == -1:
                if start:
                    mx = max(mx, cnt)
                    cnt = 0
                    start = not start
            else:
                if start:
                    cnt += 1
                    forts[i] = 1

        start = False
        cnt = 0
        for i in range(l-1, -1, -1):
            if forts[i] == 1:
                if start:
                    cnt = 0
                else:
                    start = not start
            elif forts[i] == -1:
                if start:
                    mx = max(mx, cnt)
                    cnt = 0
                    start = not start
            else:
                if start:
                    cnt += 1

        return mx