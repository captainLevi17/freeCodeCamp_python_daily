'''
Longest Common Substring
Given a string, return the longest substring that appears more than once.

The substrings can overlap.


'''

def get_longest_substring(s):
    longest_substring = ""
    
    for i in range(len(s)):
        print(f"Starting new substring search from index {i}")
        for j in range(i + 1, len(s) + 1):
            print(f"Checking substring from index {i} to {j}")
            substring = s[i:j]
            print(f"Checking substring: '{substring}'")
            if substring in s[i + 1:] and len(substring) > len(longest_substring):
                longest_substring = substring
                print(f"Found a longer substring: '{longest_substring}'")
    
    return longest_substring

print(get_longest_substring("abracadabra"))