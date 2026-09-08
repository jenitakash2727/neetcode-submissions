from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        stack = []

        # push all characters
        for ch in s:
            stack.append(ch)

        # pop and replace
        for i in range(len(s)):
            s[i] = stack.pop()