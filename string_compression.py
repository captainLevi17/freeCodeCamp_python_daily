'''
String Compression
Given a string sentence, return a compressed version of the sentence where consecutive duplicate words are replaced by the word followed with the number of times it repeats in parentheses.

Only consecutive duplicates are compressed.
Words are separated by single spaces.
For example, given "yes yes yes please", return "yes(3) please".
'''
def compress_string(sentence):
    words = sentence.split()
    compressed_words = []
    count = 0
    for i in words:
        if i not in compressed_words and count == 0:
            compressed_words.append(i)
            count += 1
        elif i == compressed_words[-1]:
            count += 1
        else:
            if count > 1:
                compressed_words[-1] = f"{compressed_words[-1]}({count})"
            count = 1
            compressed_words.append(i)
    if count > 1:
        compressed_words[-1] = f"{compressed_words[-1]}({count})"
    sentence = ' '.join(compressed_words)
        
    return sentence

compress_string("yes yes yes please")