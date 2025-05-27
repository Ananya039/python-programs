string = input("Enter a string: ")
vowels = "aeiouAEIOU"
vowel_count= 0
consonant_count= 0
for char in string:
    if char.isalpha():
        if char in vowels:
            vowel_count +=1
        else:
            consonant_count +=1
print("Vowels are:", vowel_count)
print("Consonants are:",consonant_count)