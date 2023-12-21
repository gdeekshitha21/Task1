def count_words(string):
    words=string.split()
    return len(words)

string= "Hello Team, how are you"
word_count=count_words(string)
print("The number of words in the string is:",word_count)