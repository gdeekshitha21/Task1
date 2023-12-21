def count_unique_characters(string):
    unique_chars=set(string)
    return len(unique_chars)
input_string="Hello Guvi Members"
unique_count=count_unique_characters(input_string)
print("The number of unique characters in the string is:", unique_count)