#https://leetcode.com/problems/valid-parentheses/
def isValid(s: str) -> bool:
    closeToOpen = {')': '(', '}': '{', ']': '['}
    stack = []
    
    for bracket in s:
        if bracket in closeToOpen:
            if stack and stack[-1] == closeToOpen[bracket]:
                stack.pop()
            else:
                return False
        else:
            stack.append(bracket)
        
    return True if len(stack) == 0 else False
    