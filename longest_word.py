def get_longest_word(sentence):
    words = sentence.strip(".").split(" ")
    longest_word = max(words, key=len)
    return longest_word

print(get_longest_word("Coding challenges are fun and educational."))