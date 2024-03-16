class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        stringArray = s.split()
        return len(stringArray[-1])