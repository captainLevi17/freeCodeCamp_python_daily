'''
Anagram Groups
Given an array of words, return a 2d array of the words grouped into anagrams.

Words are anagrams if they contain the same letters in any order.
Each word belongs to exactly one group.
Return order doesn't matter.
For example, given ["listen", "silent", "hello", "enlist", "world"], return [["listen", "silent", "enlist"], ["hello"], ["world"]].

'''

def group_anagrams(words):
    anagram_dict = {}
    for word in words:
        sorted_word = ''.join(sorted(word))
        if sorted_word not in anagram_dict:
            anagram_dict[sorted_word] = []
        anagram_dict[sorted_word].append(word)
    return list(anagram_dict.values())