class Solution:
    def isPalindrome(self, s: str) -> bool:
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^`&*_~'''
        s = s.lower()
        no_punct = ""
        for char in s:
            if char not in punctuations:
                no_punct = no_punct + char
        no_punct = no_punct.split(" ")
        s= "".join(no_punct)
        if s[::-1] == s:
            return True
        else:
            return False
