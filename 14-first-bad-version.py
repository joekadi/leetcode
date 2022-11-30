#https://leetcode.com/problems/first-bad-version/
#The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        
        
        while l <= r:
            mid = round((l+r)/2)
            
            bad_version = isBadVersion(mid)
            
            if bad_version:
                r = mid - 1
            else:
                l = mid +1
                
        return l
    
    
            