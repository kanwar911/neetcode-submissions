class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        fmap = defaultdict(int)
        longest = 0
        start = 0

        for right in range(len(s)):
            fmap[s[right]] += 1

            window_length = right - start + 1
            most_common = max(fmap.values())
            replacements_needed = window_length - most_common

            while replacements_needed > k:
                fmap[s[start]] -= 1
                start += 1

                # recalculate after shrinking the window
                window_length = right - start + 1
                most_common = max(fmap.values())
                replacements_needed = window_length - most_common

            longest = max(longest, window_length)

        return longest