'''
Smallest Gap
Given a string, return the substring between the two identical characters that have the smallest number of characters between them (smallest gap).

There will always be at least one pair of matching characters.
The returned substring should exclude the matching characters.
If two or more gaps are the same length, return the characters from the first one.
For example, given "ABCDAC", return "DA".

Only "A" and "C" repeat in the string.
The number of characters between the two "A" characters is 3, and between the "C" characters is 2.
So return the string between the two "C" characters.

'''

def smallest_gap(s):
    last_seen = {}
    min_gap = float('inf')
    result = ""

    for i, ch in enumerate(s):
        if ch in last_seen:
            gap = i - last_seen[ch] - 1

            if gap < min_gap:
                min_gap = gap
                result = s[last_seen[ch] + 1:i]

        last_seen[ch] = i

    return result
