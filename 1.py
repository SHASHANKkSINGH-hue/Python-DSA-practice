def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count


word = input("Enter a word: ")
vowel_count = count_vowels(word)
print(f"The number of vowels in '{word}' is: {vowel_count}")