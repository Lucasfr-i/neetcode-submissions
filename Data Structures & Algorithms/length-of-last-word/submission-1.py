class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        last_w = s.strip().split()
        return len(last_w[-1])