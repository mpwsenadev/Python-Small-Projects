def vowel_checker(sentence):
    vowels = 'aeiouAEIOU'
    count = 0
    for letter in sentence:
        if letter in vowels:
            count += 1
    return count

sentence = input("Enter a sentence: ")
num_vowels = vowel_checker(sentence)
print("Number of vowels in the sentence:", num_vowels)
