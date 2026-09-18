class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freqs = {}
        freqt = {}
        for letra in s:
            freqs[letra] = freqs.get(letra, 0) + 1
        for letra in t:
            freqt[letra] = freqt.get(letra, 0) + 1

        return freqt ==  freqs