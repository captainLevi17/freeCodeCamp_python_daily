'''
Add Punctuation
Given a string of sentences with missing periods, add a period (".") in the following places:

Before each space that comes immediately before an uppercase letter
And at the end of the string
Return the resulting string.
'''
def add_punctuation(sentences):
    result = ""
    for i in range(len(sentences)):
        if i > 0 and i != len(sentences) - 1 and sentences[i+1].isupper() and sentences[i] == " ":
            result += "."
        result += sentences[i]
    if not result.endswith("."):
        result += "."
    return result

print(add_punctuation("JavaScript is great Sometimes"))