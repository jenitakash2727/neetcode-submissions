class Solution:
    def isPalindrome(self, s: str) -> bool:
            # left pointer start-la
        l = 0

        # right pointer end-la
        r = len(s) - 1

        while l < r:

            # special chars skip pannrom
            while l < r and not s[l].isalnum():
                l += 1

            # special chars skip pannrom
            while l < r and not s[r].isalnum():
                r -= 1

            # lowercase compare pannrom
            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True