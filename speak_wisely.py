'''
Speak Wisely, You Must
Given a sentence, return a version of it that sounds like advice from a wise teacher using the following rules:

Words are separated by a single space.
Find the first occurrence of one of the following words in the sentence: "have", "must", "are", "will", "can".
Move all words before and including that word to the end of the sentence and:
Preserve the order of the words when you move them.
Make them all lowercase.
And add a comma and space before them.
Capitalize the first letter of the new first word of the sentence.
All given sentences will end with a single punctuation mark. Keep the original punctuation of the sentence and move it to the end of the new sentence.
Return the new sentence, make sure there's a single space between each word and no spaces at the beginning or end of the sentence.
For example, given "You must speak wisely." return "Speak wisely, you must."


'''

def wise_speak(sentence):
    keywords = ["have", "must", "are", "will", "can"]
    words = sentence[:-1].split()  # Exclude the punctuation at the end
    punctuation = sentence[-1]  # Store the punctuation

    for i in keywords:
        if i in words:
            index = words.index(i)
            first_part = words[:index + 1]
            second_part = words[index + 1:]
            second_part[-1] = second_part[-1] + ','
            first_part[-1] = first_part[-1] + punctuation
            print(first_part, second_part)

            # Rearranging the sentence
            new_sentence = second_part + [word.lower() for word in first_part]
            new_sentence[0] = new_sentence[0].capitalize()  # Capitalize the first word

            return ' '.join(new_sentence)


print(wise_speak("You must speak wisely."))