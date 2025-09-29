def get_longest_word(sentence):
    # Remove the period at the end and split the sentence into words
    words = sentence.strip(".").split(" ")
    # Find the longest word using the max function with key=len
    longest_word = max(words, key=len)
    return longest_word