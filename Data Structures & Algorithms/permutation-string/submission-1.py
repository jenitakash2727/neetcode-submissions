class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

            
        if len(s1) > len(s2):
            return False

        s1_count = {}
        window_count = {}

        # Frequency of s1
        for ch in s1:
            s1_count[ch] = s1_count.get(ch, 0) + 1

        # First window
        for i in range(len(s1)):
            ch = s2[i]
            window_count[ch] = window_count.get(ch, 0) + 1

        if s1_count == window_count:
            return True

        left = 0

        for right in range(len(s1), len(s2)):

            # Add new character
            new_char = s2[right]
            window_count[new_char] = window_count.get(new_char, 0) + 1

            # Remove old character
            old_char = s2[left]
            window_count[old_char] -= 1

            if window_count[old_char] == 0:
                del window_count[old_char]

            left += 1

            if s1_count == window_count:
                return True

        return False



            
            