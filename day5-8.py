def is_anagram(string1, string2):
    string1=string1.replace(",").lower()
    string2=string2.replace(",").lower()
string1="Galla"
string2="Deekshitha"  
is_anagram_result=is_anagram(string1,string2) 
print("are the strings anagram?",is_anagram_result) 