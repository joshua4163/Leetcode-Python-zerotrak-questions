class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in range(len(image)):
            len1 = image[i]
            left = 0
            right = len(len1) - 1
            while left<right:
                len1[left],len1[right] = len1[right],len1[left]
                left += 1
                right -= 1
            
            #replacing 0 -> 1
            for j in range(len(len1)):
                len1[j] = 1 - len1[j]
            image[i] = len1
        return image