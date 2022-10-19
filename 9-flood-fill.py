#https://leetcode.com/problems/flood-fill/
from ast import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if(image[sr][sc] == color):
            return image
        fill(image, sr, sc, image[sr][sc], color)
        return image
        
        
def fill(image: List[List[int]], sr: int, sc: int, color: int, newColor: int):
    if (sr<0 or sc<0 or sr >= len(image) or sc >= len(image[0]) or image[sr][sc] != color):
        return

    image[sr][sc] = newColor
    fill(image, sr-1, sc, color, newColor)
    fill(image, sr+1, sc, color, newColor)
    fill(image, sr, sc+1, color, newColor)
    fill(image, sr, sc-1, color, newColor)
    return image

        