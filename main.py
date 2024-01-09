
# number = int(input("Enter number 0-10:"))
# secret = 9
# while True:
#     if number == 0:
#         print("Game Over")
#         break
#     elif number == 9:
#         print("You Win")
#         break
#     else:
#         print("Try again")
#         number = int(input("Enter number:"))


# def max_number(lst):
#     max_num = list(set(lst))
#     return max_num
#
#
# input_lst = [5, 7, 19, 27, 20, 3]
# result = max_number(input_lst)
# print(result[-1])


# def upper_lst(lst_str):
#     new_list = []
#
#     for i in lst_str:
#         lst = i.upper()
#         new_list.append(lst)
#     return new_list
#
#
# input_list = ["Hi bro!"]
# result = upper_lst(input_list)
# print(result)


# def simple_num(x):
#     for i in range(2, (x//2)+1):
#         if x % i == 0:
#             return False
#     return True
#
#
# simple_input = 504
# result = simple_num(simple_input)
# print(result)


# new_num = 1
#
#
# def factorial_num(x):
#     global new_num
#     for i in range(2, x+1):
#         new_num *=i
#     return new_num
#
#
# input_num = int(input("Enter number:"))
# result = factorial_num(input_num)
# print(result)


# def even_numbers(lst):
#     new_list = []
#     for i in lst:
#         if i % 2 == 0:
#             new_list.append(i)
#     return new_list
#
#
# input_list = [2, 3, 6, 12, 9, 34, 27]
# result = even_numbers(input_list)
# print(result)

# def vowels_str(input_):
#     vowels = "aeiou"
#     count = 0
#     for i in input_:
#         if i in vowels:
#             count += 1
#     return count
#
#
# input_str = input("Enter string:")
# result = vowels_str(input_str)
# print(result)


# def double_list(lst):
#     new_list = []
#     for i in lst:
#         new_list.append(i * 2)
#     return new_list
#
#
# input_lst = [2, 10, 15, 3, 100]
# result = double_list(input_lst)
# print(result)


# def anagram_str(str1, str2):
#     str1 = str1.replace(" ", "").lower()
#     str2 = str2.replace(" ", "").lower()
#
#     sorted_str1 = sorted(str1)
#     sorted_str2 = sorted(str2)
#     return sorted_str1 == sorted_str2
#
#
# input_str1 = input("-->")
# input_str2 = input("_>")
# result = anagram_str(input_str1, input_str2)
# print(result)


# def merge_dictionaries(dict1, dict2):
#     result = {}
#
#     for key, value in dict1.items():
#         result[key] = value
#
#     for key, value in dict2.items():
#         if key in result:
#             result[key] += value
#         else:
#             result[key] = value
#     return result
#
#
# input_dict1 = {"a": 5, "b": 3, "c": 2}
# input_dict2 = {"b": 7, "c": 4, "d": 8}
# merge_dict = merge_dictionaries(input_dict1, input_dict2)
# print(merge_dict)


# def infinite_str(*args):
#     new_str = ""
#
#     for string in args:
#         new_str += string
#     return new_str
#
#
# str1 = "Calib"
# str2 = "ration"
# result = infinite_str(str1, str2)
# print(result)


# def sentence_string(sent):
#     words = sent.split()
#     return len(words)
#
#
# input_str = input("Enter sentence:")
# result = sentence_string(input_str)
# print(f"The number of words in a sentence:", result)


# def big_str(sentence):
#     words = sentence.split()
#     capitalize_words = []
#
#     for word in words:
#         capitalize_words.append(word.capitalize())
#     new_sentence = " ".join(capitalize_words)
#
#     return new_sentence
#
#
# input_sentence = input("Enter sentence:")
# result = big_str(input_sentence)
# print(result)


# def vowels_dict(*args):
#     vowels = "aeiouAEIOU"
#     new_dict = {}
#
#     for word in args:
#         for i in word:
#             if i in vowels:
#                 if i in new_dict:
#                     new_dict[i] += 1
#                 else:
#                     new_dict[i] = 1
#
#     return new_dict
#
#
# words = ["Sea", "Apple", "Potato"]
# result = vowels_dict(*words)
# print(result)

# n = int(input())
#
#
# if n % 2 == 1:
#     print("Weird")
# elif n % 2 == 0 and n in range(2, 6):
#     print("Not Weird")
# elif n % 2 == 0 and 6 <= n <= 20:
#     print("Weird")
# elif n % 2 == 0 and n > 20:
#     print("Not Weird")


import re


def valid_or_invalid(index):
    pattern = r'\b\d{5}\b'
    if re.match(pattern, index):
        print("Valid")
    else:
        print("Invalid")


input_index = "18007"
valid_or_invalid(input_index)






