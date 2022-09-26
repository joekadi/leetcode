#https://leetcode.com/problems/two-sum/
from ast import List

def twoSum(nums: List[int], target: int) -> List[int]:
    valIndexMap = {}
    for i,n in enumerate(nums):
        diff = target - n
        if diff in valIndexMap:
            return[valIndexMap[diff], i]
        valIndexMap[n] = i
