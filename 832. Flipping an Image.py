class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i,row in enumerate(image):
            row = row[::-1]
            image[i] = row
            for j,e in enumerate(image[i]):
                if e == 1:
                    image[i][j] = 0
                else:
                    image[i][j] = 1
            
        return image

