def count_vowels(string):
   vowels={'A':0, 'E':0, 'I':0, 'O':0, 'U':0}
   total_vowels=0
   
   for char in string.upper():
    if char in string.upper():
      #vowels[char]+=1
      total_vowels+=1

    return total_vowels, vowels  
string= "Guvi Geeks Network Private Limited"
total_vowels, vowel_count= count_vowels(string)

print("Total number of vowels:", total_vowels)
print("Count of each individual vowel:")
#print("string")
for vowel, count in vowel_count.items():
  print(vowel,":",count)     


