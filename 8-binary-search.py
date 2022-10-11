#https://leetcode.com/problems/binary-search/
from ast import List
#O(n) solution - not a binary search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1

#O(log(n)) solution - a binary search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            m = (left+right) // 2
            if nums[m] < target:
                left = m + 1
            elif nums[m] > target:
                right = m -1
            else:
                return m
        return -1
