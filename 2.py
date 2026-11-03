def reverse_string(text):
    reversed_text= ""
    for char in text:
        reversed_text=char + reversed_text
    return reversed_text



word = input("Enter a word: ")
reversed_word = reverse_string(word)
print(f"The reversed word of '{word}' is: {reversed_word}")