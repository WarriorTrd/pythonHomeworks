#q1
# name = input("Enter your name: ")
# year = int(input("enter the year u were born: "))
# print(f"{name} is {2024-year} years old")

#q2
#txt = 'LMaasleitbtui'.lower()








#q3

# my_string = input("Enter the string: ")
# print("lenght of your string is: ",len(my_string))
# print(my_string.upper())
# print(my_string.lower())

#q4

# string=input("enter ur string: ")
# if string == string[::-1]  :
#     print("this string is polindrome")  
# else :
#     print("this string is not polindrome")     

#q5
# txt=input("enter yor text: ")
# vowel="aeiouAEIOU"
# counter_vowel=0
# counter_consonant=0
# for i in txt:
#     if i in vowel:
#         counter_vowel+=1
#     else:
#         counter_consonant+=1
# print(f"there are {counter_vowel} vowels and {counter_consonant} consonants in your string ")        


#q6

# first_string = input("Enter the main string: ")
# second_string = input("Enter the substring to check: ")
# print("Contains:", second_string in first_string)


#q7
# sentence = input("Enter a sentence: ")
# old_word = input("Enter the word to replace: ")
# new_word = input("Enter the new word: ")
# print("Updated sentence:", sentence.replace(old_word, new_word))

#q8

# string = input("Enter a string: ")
# print("First:", string[0], "Last:", string[-1])

#q9
# string = input("Enter a string: ")
# print("Reversed:", string[::-1])

#q10
# sentence = input("Enter ur sentence: ")
# print(f"Your sentence has {len(sentence.split())} words in it")


#q11
# string=input("Enter your string: ")
# print("Has digits:", any(string.isdigit() for i in string))

#q12
# words = input("Enter words separated by space: ").split()
# separator = input("Enter your separator (e.g., -, ,): ")
# print("Joined as a single string:", separator.join(words))


#q13
# string = input("Enter your string: ")
# print("Without spaces:", string.replace(" ", ""))

#q14
# str1 = input("Enter first string: ")
# str2 = input("Enter second string: ")
# print("Equal:", str1 == str2)

#q15
# sentence = input("Enter your sentence: ")
# words = sentence.split()
# acronym = "".join(word[0] for word in words)  # Ensure uppercase
# print("Acronym:", acronym)


#q16
# string=input("Enter your string: ")
# character=input("Enter the character u want to remove: ")
# new_string=string.replace(character,"")
# print("New string: ",new_string)

#q17
# string=input("Enter your string: ")
# symbol=input("Enter the symbol: ")
# vowel="aeiouAEIOU"
# new_string=""
# for i in string:
#     if i in vowel:
#         new_string+=symbol
#     else:
#         new_string+=i  
      
# print(new_string)   

#q18
# sentence = input("Enter your sentence: ")
# start = input("Enter the word it should start with: ")
# end = input("Enter the word it should end with: ")
# print("Starts with:", sentence.startswith(start))
# print("Ends with:", sentence.endswith(end)) 