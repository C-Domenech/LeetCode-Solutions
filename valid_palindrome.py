class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s2 = ''
        # for ch in s[::-1]:
        #     if ch.isalnum():
        #         s2 += ch
        s = ''.join(ch for ch in s if ch.isalnum())
        # s2 = s[::-1]
        # s2 = ''.join(ch for ch in s[::-1] if ch.isalnum())
        return s.lower() == s[::-1].lower()


# 1. Darle la vuelta al string.
# 2. Eliminar los espacios y caracteres especiales
txt = "A man, a plan, a canal: Panama"
# txt = "A mama, Roma le aviva el amor a papa y a papa, Roma le aviva el amor a Mama."
# txt = "amanaplanacanalpanama"
# txt = "cara"
print(Solution().isPalindrome(txt))