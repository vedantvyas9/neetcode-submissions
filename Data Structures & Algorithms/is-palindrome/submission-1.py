class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp = []
        for c in s:
            if c.isalnum():
                temp.append(c.lower())
        print(temp)
        left = 0 
        right = len(temp) - 1
        while (left <= right):
            if (temp[left] != temp[right]):
                return False
            left += 1
            right -= 1
        return True 
        