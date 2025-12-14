'''
Most Frequent
Given an array of elements, return the element that appears most frequently.

There will always be a single most frequent element.
'''
def most_frequent(arr):
    frequency = {}
    for item in arr:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1
    for item, count in frequency.items():
        if count == max(frequency.values()):
            return item 
