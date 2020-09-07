class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        up = word.upper()
        lo = word.lower()
        ca = word.capitalize()
        if word == up or word == lo or word == ca:
            return True
        else:
            return False


# a = 'USA'
a = 'FlaG'
# a = 'Canadá'
print(Solution().detectCapitalUse(a))
