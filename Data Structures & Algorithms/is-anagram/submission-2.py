class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        anagram = True
        for letter in set(s): 
            if letter not in set(t): 
                return not anagram 
            if s.count(letter) != t.count(letter): 
                return not anagram
        return anagram

