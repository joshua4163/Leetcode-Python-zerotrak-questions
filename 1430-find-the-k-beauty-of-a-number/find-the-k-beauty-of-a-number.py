class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num_str = str(num)  # Convert num to string
        c = 0
        for r in range(len(num_str) - k + 1):
            window = int(num_str[r:r+k])  # Extract substring and convert to integer
            if window != 0 and num % window == 0:  # Check if substring is divisible by num
                c += 1
        return c