#48)Write a Python function that takes a list of words and returns the length of the longest one.
words = ['Chinesse', 'Italian', 'Indian']
word_len = []
for n in words:
    word_len.append((len(n), n))
word_len.sort()

print("\nLongest word: ",word_len[-1][1])
print("Length of the longest word: ",word_len[-1][0])