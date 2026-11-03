def is_palindrome(word):
    word = word.lower()
   # def reverse_string(text):
    reversed_text= ""
    for char in word: # text
        reversed_text=char + reversed_text
    return word == reversed_text
    

input_word = input("Enter a word: ")
if is_palindrome(input_word):
    print(f"'{input_word}' is a palindrome.")  
else:
     print(f"'{input_word}' is not a palindrome.")