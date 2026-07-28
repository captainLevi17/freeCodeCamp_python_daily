'''
Lucky Number
Given a string of a person's first and last name, calculate their lucky number using the following rules:

First and last names are separated by a space
Find the vowel and consonant count for each name
Multiply the smaller vowel and consonant counts by each other and then by the length of the smaller name
Do the same for the two larger counts and the larger name
Subtract the smaller value from the larger one to get their lucky number
If the final value is zero (0), return 13.

'''

def get_lucky_number(name):
    vowels = set("aeiouAEIOU")
    first_name, last_name = name.split()
    
    def count_vowels_and_consonants(s):
        vowel_count = sum(1 for char in s if char in vowels)
        consonant_count = sum(1 for char in s if char.isalpha() and char not in vowels)
        return vowel_count, consonant_count
    
    first_vowels, first_consonants = count_vowels_and_consonants(first_name)
    last_vowels, last_consonants = count_vowels_and_consonants(last_name)
    
    smaller_vowel_count = min(first_vowels, last_vowels)
    larger_vowel_count = max(first_vowels, last_vowels)
    
    smaller_consonant_count = min(first_consonants, last_consonants)
    larger_consonant_count = max(first_consonants, last_consonants)
    
    smaller_name_length = min(len(first_name), len(last_name))
    larger_name_length = max(len(first_name), len(last_name))
    
    smaller_value = smaller_vowel_count * smaller_consonant_count * smaller_name_length
    larger_value = larger_vowel_count * larger_consonant_count * larger_name_length
    
    lucky_number = larger_value - smaller_value
    
    return 13 if lucky_number == 0 else lucky_number
'''
Lucky Number
Given a string of a person's first and last name, calculate their lucky number using the following rules:

First and last names are separated by a space
Find the vowel and consonant count for each name
Multiply the smaller vowel and consonant counts by each other and then by the length of the smaller name
Do the same for the two larger counts and the larger name
Subtract the smaller value from the larger one to get their lucky number
If the final value is zero (0), return 13.

'''

def get_lucky_number(name):
    vowels = set("aeiouAEIOU")
    print(vowels)
    first_name, last_name = name.split()
    
    def count_vowels_and_consonants(s):
        vowel_count = sum(1 for char in s if char in vowels)
        consonant_count = sum(1 for char in s if char.isalpha() and char not in vowels)
        return vowel_count, consonant_count
    
    first_vowels, first_consonants = count_vowels_and_consonants(first_name)
    last_vowels, last_consonants = count_vowels_and_consonants(last_name)
    
    smaller_vowel_count = min(first_vowels, last_vowels)
    larger_vowel_count = max(first_vowels, last_vowels)
    
    smaller_consonant_count = min(first_consonants, last_consonants)
    larger_consonant_count = max(first_consonants, last_consonants)
    
    smaller_name_length = min(len(first_name), len(last_name))
    larger_name_length = max(len(first_name), len(last_name))
    
    smaller_value = smaller_vowel_count * smaller_consonant_count * smaller_name_length
    larger_value = larger_vowel_count * larger_consonant_count * larger_name_length
    
    lucky_number = larger_value - smaller_value
    
    return 13 if lucky_number == 0 else lucky_number