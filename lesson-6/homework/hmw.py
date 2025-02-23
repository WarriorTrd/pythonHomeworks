
#task 1

# def check(func):
#     def wrapper(a,b):
#         if b==0:
#             print("denominator can't be zero!")
#             return None
#         else:
#            return func(a,b)
#     return wrapper



# @check
# def div(a, b):
#    return a / b   
# a=int(input("enter the value for your nominator: "))
# b=int(input("enter the value ofr your denominator")) 
# result = div(a, b)

# if result is not None:
#     print(f"The result of the division is: {result}")        



#task 2


# try:
#     file = open("sample.txt", "r")
#     content = file.read()  
#     file.close()
# except FileNotFoundError:
#     paragraph = input("File not found! Please provide content to create a new file: ")
#     file = open("sample.txt", "a")  
#     file.write(paragraph)  
#     file.close()

#     file = open("sample.txt", "r")
#     content = file.read()  
#     file.close()

# new = content.split()  

# tlen = len(new)  
# print(f"Total number of words in the file is: {tlen}")

# word_counts = {}
# for word in new:
#     word = word.lower()
#     if word not in word_counts:
#         word_counts[word] = 1
#     else:
#         word_counts[word] += 1

# for word, count in word_counts.items():
#     print(f"Word '{word}' appears {count} times.")

# n = int(input("number of top common words do you want: "))

# sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
# common_words = sorted_words[:n]

# print(f"total words: {tlen}")
# print(f"top {n} most common words:")
# for word, count in common_words:
#     print(f"{word} - {count} times")

# n_new = open("word_count_report.txt", "w")
# n_new.write(f"total Words: {tlen}\n")
# n_new.write(f"top {n} Words:\n")
# for word, count in common_words:
#     n_new.write(f"{word} - {count}\n")
# n_new.close()

# print("process  finished")
       




   






