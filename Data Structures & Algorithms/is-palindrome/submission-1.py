class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = ""
        for i in s:
          if i.isalpha():
            n+=i.lower()
          elif i.isalnum():
                n+=i
          else:
              continue   
        return n == n[::-1]