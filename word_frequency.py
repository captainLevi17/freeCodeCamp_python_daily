'''
Word Frequency
Given a paragraph, return an array of the three most frequently occurring words.

Words in the paragraph will be separated by spaces.
Ignore case in the given paragraph. For example, treat Hello and hello as the same word.
Ignore punctuation in the given paragraph. Punctuation consists of commas (,), periods (.), and exclamation points (!).
The returned array should have all lowercase words.
The returned array should be in descending order with the most frequently occurring word first.
'''

def get_words(paragraph):
    # Remove punctuation and convert to lowercase
    cleaned_paragraph = paragraph.replace(',', '').replace('.', '').replace('!', '').lower()
    
    # Split the paragraph into words
    words = cleaned_paragraph.split()
    
    # Count the frequency of each word
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1


    # Sort the words by frequency in descending order
    sorted_words = sorted(word_count.items(), key=lambda item: item[1], reverse=True)
    
    # Get the top three most frequent words
    top_three_words = [word for word, count in sorted_words[:3]]
    
    return top_three_words

