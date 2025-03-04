class Solution(object):
    def is_palindrome(self, x):
        y = x
        rev = 0
        while y > 0:
            rem = y % 10
            rev = (rev * 10) + rem
            y = y // 10
        return True if x == rev else False
    
solution1 = Solution()
# print(solution1.is_palindrome(121))
# print(solution1.is_palindrome(-121))
# print(solution1.is_palindrome(10))
print(solution1.is_palindrome(1221))