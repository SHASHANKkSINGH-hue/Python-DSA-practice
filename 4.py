def is_anagram(w1,w2):
    return sorted(w1.lower()) == sorted(w2.lower())

    
word1=input("Type the First word\n")
word2=input("Type the Second Word\n")

if is_anagram(word1,word2):
    print("Given words are Anagram ")
else:
    print("Not an Anagram")




