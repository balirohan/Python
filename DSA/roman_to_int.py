class Solution(object):
    def roman_to_int(self, s):
        roman_to_int = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0

        for idx in range(len(s)):
            if idx + 1 < len(s) and roman_to_int[s[idx]] < roman_to_int[s[idx + 1]]:
                result -= roman_to_int[s[idx]]
            else:
                result += roman_to_int[s[idx]]
        return result
    

solution1 = Solution()
# print(solution1.roman_to_int("III"))
# print(solution1.roman_to_int("LVIII"))
print(solution1.roman_to_int("MCMXCIV"))