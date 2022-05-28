# Check if two words are anagrams 
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True

word1 = "hello"
word2 = "check"

if(sorted(word1) == sorted(word2)):
    print("True")
else:
     print("False")


word1 = "below"
word2 = "elbow"

if(sorted(word1) == sorted(word2)):
    print("True")
else:
     print("False")

     

