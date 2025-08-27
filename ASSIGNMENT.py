 # =============================================================================
# COMPREHENSIVE PYTHON Q&A
# =============================================================================


1) What are the types of Applications?
   
   Types of applications include:
   - Web Applications (run in browsers)
   - Desktop Applications (run on operating systems)
   - Mobile Applications (run on mobile devices)
   - Enterprise Applications (for business organizations)
   - Embedded Systems Applications (run on specialized hardware)
   - Cloud Applications (hosted on cloud platforms)
   - Command Line Applications (run in terminal/console)



2) What is programming?
   
   Programming is the process of creating instructions for computers to execute.
   It involves writing code in programming languages to solve problems, automate tasks,
   and create software applications that perform specific functions.
 

 
3) What is Python?
   
   Python is a high-level, interpreted, object-oriented programming language known for:
   - Simple and readable syntax
   - Dynamic typing and automatic memory management
   - Extensive standard library
   - Support for multiple programming paradigms
   - Cross-platform compatibility
   - Large community and ecosystem
 

# =============================================================================
# PROGRAMMING EXERCISES
# =============================================================================

4)  Write a Python program to check if a number is positive, negative or zero
def check_number_sign(number):
    """
    Check if a number is positive, negative or zero.
    """
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

# Test the function
print("4) Number Sign Check:")
print(f"5 is {check_number_sign(5)}")
print(f"-3 is {check_number_sign(-3)}")
print(f"0 is {check_number_sign(0)}")
print()

 5)  Write a Python program to get the Factorial number of given numbers
def factorial(n):
    """
    Calculate factorial of a number.
    """
    if n < 0:
        return "Factorial not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

print("5) Factorial Calculation:")
print(f"Factorial of 5: {factorial(5)}")
print(f"Factorial of 0: {factorial(0)}")
print()

6) Write a Python program to get the Fibonacci series of given range
def fibonacci_series(n):
    """
    Generate Fibonacci series up to n terms.
    """
    series = []
    a, b = 0, 1
    
    if n <= 0:
        return series
    elif n == 1:
        return [a]
    
    series = [a, b]
    for _ in range(2, n):
        a, b = b, a + b
        series.append(b)
    
    return series

print("6) Fibonacci Series:")
print(f"First 10 Fibonacci numbers: {fibonacci_series(10)}")
print()

 
7) How memory is managed in Python?
   
   Python memory management involves:
   - Private heap space: All objects are stored in a private heap
   - Memory allocator: Manages allocation of heap space
   - Garbage collector: Automatically reclaims memory from unused objects
   - Reference counting: Tracks references to objects
   - Generational garbage collection: For cyclic references
 

 
8) What is the purpose of continue statement in python?
   
   The continue statement is used to skip the current iteration of a loop
   and move to the next iteration. It's useful when you want to skip certain
   elements or conditions within a loop without breaking out of the loop entirely.


 9)Write python program that swap two number with temp variable and without temp variable. 
def swap_with_temp(a, b):
    """Swap using temporary variable"""
    temp = a
    a = b
    b = temp
    return a, b

def swap_without_temp(a, b):
    """Swap without temporary variable"""
    a = a + b
    b = a - b
    a = a - b
    return a, b

# Pythonic way (tuple unpacking)
def swap_pythonic(a, b):
    """Pythonic way to swap"""
    a, b = b, a
    return a, b

print("9) Number Swapping:")
x, y = 5, 10
print(f"Original: x={x}, y={y}")
print(f"With temp: {swap_with_temp(x, y)}")
print(f"Without temp: {swap_without_temp(x, y)}")
print(f"Pythonic way: {swap_pythonic(x, y)}")
print()

 10)  Write a Python program to find whether a given number is even or odd, print out an appropriate message to the user. 
def check_even_odd(number):
    """
    Check if a number is even or odd.
    """
    if number % 2 == 0:
        return f"{number} is even"
    else:
        return f"{number} is odd"

print("10) Even/Odd Check:")
print(check_even_odd(7))
print(check_even_odd(12))
print()

 11)  Write a Python program to test whether a passed letter is a vowel or not. 
def is_vowel(letter):
    """
    Check if a letter is a vowel.
    """
    vowels = 'aeiouAEIOU'
    if len(letter) != 1:
        return "Please enter a single letter"
    
    if letter in vowels:
        return f"'{letter}' is a vowel"
    else:
        return f"'{letter}' is not a vowel"

print("11) Vowel Check:")
print(is_vowel('a'))
print(is_vowel('b'))
print(is_vowel('E'))
print()

 12) Write a Python program to sum of three given integers. However, if two values are equal sum will be zero. 
def conditional_sum(a, b, c):
    """
    Sum three integers, return zero if any two are equal.
    """
    if a == b or a == c or b == c:
        return 0
    else:
        return a + b + c

print("12) Conditional Sum:")
print(f"Sum of 1, 2, 3: {conditional_sum(1, 2, 3)}")
print(f"Sum of 2, 2, 3: {conditional_sum(2, 2, 3)}")
print()

 13) Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5. 

def check_special_condition(a, b):
    """
    Return True if:
    - Two integers are equal, or
    - Their sum is 5, or
    - Their difference is 5
    """
    if a == b or a + b == 5 or abs(a - b) == 5:
        return True
    return False

print("13) Special Condition Check:")
print(f"3, 3: {check_special_condition(3, 3)}")
print(f"2, 3: {check_special_condition(2, 3)}")
print(f"8, 3: {check_special_condition(8, 3)}")
print(f"1, 4: {check_special_condition(1, 4)}")
print()

 14) Write a python program to sum of the first n positive integers.
def sum_first_n_positive(n):
    """
    Calculate sum of first n positive integers.
    """
    if n <= 0:
        return 0
    return n * (n + 1) // 2

print("14) Sum of First N Positive Integers:")
print(f"Sum of first 5 positive integers: {sum_first_n_positive(5)}")
print(f"Sum of first 10 positive integers: {sum_first_n_positive(10)}")
print()

 15) Write a Python program to calculate the length of a string. 
def string_length(s):
    """
    Calculate length of a string.
    """
    return len(s)

print("15) String Length:")
print(f"Length of 'Hello': {string_length('Hello')}")
print(f"Length of 'Python Programming': {string_length('Python Programming')}")
print()

 16)Write a Python program to count the number of characters (character frequency) in a string 

def character_frequency(string):
    """
    Count frequency of each character in a string.
    """
    freq = {}
    for char in string:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

print("16) Character Frequency:")
test_string = "programming"
freq_result = character_frequency(test_string)
print(f"Frequency in '{test_string}': {freq_result}")
print()

 
17) What are negative indexes and why are they used?
   
   Negative indexes in Python allow accessing elements from the end of a sequence.
   Example: -1 refers to the last element, -2 to the second last, etc.
   
   They are used for:
   - Convenient access to elements from the end
   - Simplifying code when working with the end of sequences
   - Making certain operations more intuitive and readable
 

 18) Write a Python program to count occurrences of a substring in a string.
def count_substring_occurrences(main_string, substring):
    """
    Count occurrences of a substring in a string.
    """
    return main_string.count(substring)

print("18) Substring Occurrences:")
main_str = "hello world, hello python, hello programming"
sub_str = "hello"
count = count_substring_occurrences(main_str, sub_str)
print(f"Substring '{sub_str}' appears {count} times in: '{main_str}'")

# Alternative method without using count()
def count_substring_manual(main_string, substring):
    """
    Count substring occurrences manually.
    """
    count = 0
    start = 0
    while start < len(main_string):
        pos = main_string.find(substring, start)
        if pos == -1:
            break
        count += 1
        start = pos + 1
    return count

print(f"Manual count: {count_substring_manual(main_str, sub_str)}")

# =============================================================================
# DEMONSTRATION
# =============================================================================

if __name__ == "__main__":
    print("\n" + "="*50)
    print("DEMONSTRATING ALL FUNCTIONS")
    print("="*50)
    
    # Demonstrate all functions
    print("Testing all implemented functions...")
    
    # You can add more test cases here to demonstrate all functions
    
 19)  Write a Python program to count the occurrences of each word in a sentence.
def count_word_occurrences(sentence):
    """
    Count occurrences of each word in a given sentence.
    """
    words = sentence.split()
    word_count = {}
    
    for word in words:
        # Remove punctuation and convert to lowercase for better counting
        cleaned_word = word.strip('.,!?;:"').lower()
        if cleaned_word:
            if cleaned_word in word_count:
                word_count[cleaned_word] += 1
            else:
                word_count[cleaned_word] = 1
    
    return word_count

print("19) Word Occurrences Count:")
test_sentence = "Hello world! Hello Python. World of python programming."
word_occurrences = count_word_occurrences(test_sentence)
print(f"Sentence: '{test_sentence}'")
print(f"Word occurrences: {word_occurrences}")
print()

 20) Write a Python program to get a single string from two given strings,separated by a space and swap the first two characters of each string. 
def swap_first_two_chars(str1, str2):
    """
    Get a single string from two given strings, separated by a space
    and swap the first two characters of each string.
    """
    if len(str1) < 2 or len(str2) < 2:
        return "Both strings should have at least 2 characters"
    
    new_str1 = str2[:2] + str1[2:]
    new_str2 = str1[:2] + str2[2:]
    
    return f"{new_str1} {new_str2}"

print("20) Swap First Two Characters:")
result = swap_first_two_chars("abc", "xyz")
print(f"'abc' and 'xyz' -> {result}")
result = swap_first_two_chars("hello", "world")
print(f"'hello' and 'world' -> {result}")
print()

 21)) Write a Python program to add 'in' at the end of a given string (lengthshould be at least 3). If the given string already ends with 'ing' thenadd 'ly' instead if the string length of the given string is less than 3,leave it unchanged. 
def modify_string(s):
    """
    Add 'in' at the end of a given string (length should be at least 3).
    If the given string already ends with 'ing' then add 'ly' instead.
    If the string length is less than 3, leave it unchanged.
    """
    if len(s) < 3:
        return s
    
    if s.endswith('ing'):
        return s + 'ly'
    else:
        return s + 'in'

print("21) String Modification:")
print(f"'abc' -> '{modify_string('abc')}'")
print(f"'string' -> '{modify_string('string')}'")
print(f"'ing' -> '{modify_string('ing')}'")
print(f"'test' -> '{modify_string('test')}'")
print(f"'ab' -> '{modify_string('ab')}'")
print()

 22) ) Write a Python function to reverses a string if its length is a multiple of 4. 
def reverse_if_multiple_of_4(s):
    """
    Reverse a string if its length is a multiple of 4.
    """
    if len(s) % 4 == 0:
        return s[::-1]
    return s

print("22) Reverse if Multiple of 4:")
print(f"'abcd' (length 4) -> '{reverse_if_multiple_of_4('abcd')}'")
print(f"'python' (length 6) -> '{reverse_if_multiple_of_4('python')}'")
print(f"'abcdefgh' (length 8) -> '{reverse_if_multiple_of_4('abcdefgh')}'")
print()

 23) Write a Python program to get a string made of the first 2 and the last2 chars from a given a string. If the string length is less than 2, return instead of the empty string. 
def first_last_two_chars(s):
    """
    Get a string made of the first 2 and last 2 chars from a given string.
    If the string length is less than 2, return empty string.
    """
    if len(s) < 2:
        return ""
    
    return s[:2] + s[-2:]

print("23) First and Last Two Characters:")
print(f"'python' -> '{first_last_two_chars('python')}'")
print(f"'ab' -> '{first_last_two_chars('ab')}'")
print(f"'a' -> '{first_last_two_chars('a')}'")
print(f"'hello world' -> '{first_last_two_chars('hello world')}'")
print()

 24) )Write a Python function to insert a string in the middle of a string
def insert_string_middle(original, to_insert):
    """
    Insert a string in the middle of another string.
    """
    mid = len(original) // 2
    return original[:mid] + to_insert + original[mid:]

print("24) Insert String in Middle:")
print(f"'[[]]' with 'Python' -> '{insert_string_middle('[[]]', 'Python')}'")
print(f"'HelloWorld' with 'Beautiful' -> '{insert_string_middle('HelloWorld', 'Beautiful')}'")
print()

 
25) What is List? How will you reverse a list?

   A list in Python is an ordered, mutable collection of items that can be of different data types.
   It's one of Python's most versatile data structures.

   Ways to reverse a list:
   1. Using reverse() method (in-place): list.reverse()
   2. Using slicing: reversed_list = list[::-1]
   3. Using reversed() function: reversed_list = list(reversed(original_list))
 

 
26) How will you remove last object from a list?

   Ways to remove last object from a list:
   1. Using pop() method: list.pop()
   2. Using slicing: list = list[:-1]
   3. Using del statement: del list[-1]
 
 
27) Suppose list1 is [2, 33, 222, 14, and 25], what is list1 [-1]?

   list1[-1] would return 25, because negative indexing starts from the end of the list.
   -1 refers to the last element, -2 to the second last, and so on.

    
28) Differentiate between append() and extend() methods?

   append(): 
   - Adds its argument as a single element to the end of the list
   - The length of the list increases by 1
   - Example: [1, 2, 3].append([4, 5]) becomes [1, 2, 3, [4, 5]]

   extend():
   - Iterates over its argument and adds each element to the list
   - The length of the list increases by the number of elements in the iterable
   - Example: [1, 2, 3].extend([4, 5]) becomes [1, 2, 3, 4, 5]
 

 29) Write a Python function to get the largest number, smallest num and sum of all from a list
def list_analysis(numbers):
    """
    Get the largest number, smallest number and sum of all from a list.
    """
    if not numbers:
        return None, None, 0
    
    largest = max(numbers)
    smallest = min(numbers)
    total_sum = sum(numbers)
    
    return largest, smallest, total_sum

print("29) List Analysis:")
test_list = [10, 5, 20, 1, 15, 8]
largest, smallest, total = list_analysis(test_list)
print(f"List: {test_list}")
print(f"Largest: {largest}, Smallest: {smallest}, Sum: {total}")

# Test with empty list
largest, smallest, total = list_analysis([])
print(f"Empty list -> Largest: {largest}, Smallest: {smallest}, Sum: {total}")
print()

# =============================================================================
# DEMONSTRATION OF LIST OPERATIONS
# =============================================================================

print("="*50)
print("DEMONSTRATING LIST OPERATIONS")
print("="*50)

# 25) List reversal examples
print("25) List Reversal Examples:")
original_list = [1, 2, 3, 4, 5]

# Method 1: reverse() method (in-place)
list1 = original_list.copy()
list1.reverse()
print(f"reverse() method: {list1}")

# Method 2: Slicing
list2 = original_list[::-1]
print(f"Slicing: {list2}")

# Method 3: reversed() function
list3 = list(reversed(original_list))
print(f"reversed() function: {list3}")
print()

# 26) Remove last object examples
print("26) Remove Last Object Examples:")
test_list = [1, 2, 3, 4, 5]

# Method 1: pop()
list_copy = test_list.copy()
last_item = list_copy.pop()
print(f"pop() -> List: {list_copy}, Removed: {last_item}")

# Method 2: Slicing
list_copy = test_list.copy()
new_list = list_copy[:-1]
print(f"Slicing -> List: {new_list}")

# Method 3: del statement
list_copy = test_list.copy()
del list_copy[-1]
print(f"del statement -> List: {list_copy}")
print()

# 27) Negative indexing example
print("27) Negative Indexing Example:")
list1 = [2, 33, 222, 14, 25]
print(f"list1 = {list1}")
print(f"list1[-1] = {list1[-1]}")
print(f"list1[-2] = {list1[-2]}")
print(f"list1[-3] = {list1[-3]}")
print()

# 28) append() vs extend() demonstration
print("28) append() vs extend() Demonstration:")
# append() example
list_append = [1, 2, 3]
list_append.append([4, 5])
print(f"append([4, 5]): {list_append}")

# extend() example
list_extend = [1, 2, 3]
list_extend.extend([4, 5])
print(f"extend([4, 5]): {list_extend}")

# extend() with string
list_extend_str = [1, 2, 3]
list_extend_str.extend("abc")
print(f"extend('abc'): {list_extend_str}")
print()

# =============================================================================
# ADDITIONAL UTILITY FUNCTIONS
# =============================================================================

def demonstrate_all_functions():
    """Demonstrate all functions from both parts"""
    print("="*60)
    print("COMPREHENSIVE DEMONSTRATION OF ALL FUNCTIONS")
    print("="*60)
    
    # Demonstrate functions from both parts
    print("4) Number sign check:", check_number_sign(-5))
    print("5) Factorial of 6:", factorial(6))
    print("6) Fibonacci series (8 terms):", fibonacci_series(8))
    print("9) Swap numbers (5, 10):", swap_pythonic(5, 10))
    print("10) Even/odd check:", check_even_odd(15))
    print("11) Vowel check:", is_vowel('i'))
    print("12) Conditional sum (1,2,2):", conditional_sum(1, 2, 2))
    print("13) Special condition (7,2):", check_special_condition(7, 2))
    print("14) Sum of first 6 positive integers:", sum_first_n_positive(6))
    print("15) String length:", string_length("Hello World"))
    print("16) Character frequency:", character_frequency("mississippi"))
    print("18) Substring count:", count_substring_occurrences("banana", "na"))
    print("19) Word occurrences:", count_word_occurrences("test test hello test"))
    print("20) Character swap:", swap_first_two_chars("hello", "world"))
    print("21) String modification:", modify_string("testing"))
    print("22) Reverse multiple of 4:", reverse_if_multiple_of_4("abcd"))
    print("23) First/last two chars:", first_last_two_chars("programming"))
    print("24) Insert in middle:", insert_string_middle("[[[]]]", "Python"))
    print("29) List analysis:", list_analysis([10, 2, 8, 1, 9]))

if __name__ == "__main__":
    demonstrate_all_functions()

 
30) How will you compare two lists?

   There are several ways to compare two lists in Python:

   1. Element-wise comparison: list1 == list2 (checks if both lists have same elements in same order)
   2. Check if lists are identical: list1 is list2 (checks if they are the same object in memory)
   3. Check if all elements are equal regardless of order: sorted(list1) == sorted(list2)
   4. Check if one list contains all elements of another: all(item in list2 for item in list1)
   5. Using set operations for unordered comparison: set(list1) == set(list2)
 
 31) Write a Python program to count the number of strings where the stringlength is 2 or more and the first and last character are same from a given listof strings.
def count_special_strings(string_list):
    """
    Count strings where length is 2 or more and first and last character are same.
    """
    count = 0
    for s in string_list:
        if len(s) >= 2 and s[0].lower() == s[-1].lower():
            count += 1
    return count

print("31) Count Strings with Same First/Last Character:")
test_strings = ['aba', 'abc', 'aa', 'a', 'hello', 'level', 'python', 'madam']
result = count_special_strings(test_strings)
print(f"List: {test_strings}")
print(f"Count: {result}")
print()

 32) Write a Python program to remove duplicates from a list. 
def remove_duplicates(input_list):
    """
    Remove duplicates from a list while preserving order.
    """
    # Method 1: Using set (doesn't preserve order in older Python versions)
    # return list(set(input_list))
    
    # Method 2: Using dict (preserves order)
    return list(dict.fromkeys(input_list))

    # Method 3: Using loop (preserves order)
    # unique_list = []
    # for item in input_list:
    #     if item not in unique_list:
    #         unique_list.append(item)
    # return unique_list

print("32) Remove Duplicates:")
duplicate_list = [1, 2, 2, 3, 4, 4, 5, 1, 6]
unique_list = remove_duplicates(duplicate_list)
print(f"Original: {duplicate_list}")
print(f"Unique: {unique_list}")
print()

 33) )Write a Python program to check a list is empty or not. 
def is_list_empty(input_list):
    """
    Check if a list is empty or not.
    """
    # Method 1: Using len()
    # return len(input_list) == 0
    
    # Method 2: Direct boolean evaluation (Pythonic way)
    return not bool(input_list)

print("33) Check Empty List:")
print(f"[] is empty: {is_list_empty([])}")
print(f"[1, 2, 3] is empty: {is_list_empty([1, 2, 3])}")
print(f"[''] is empty: {is_list_empty([''])}")
print()

 34) Write a Python function that takes two lists and returns true if theyhave at least one common member. 
def has_common_member(list1, list2):
    """
    Return True if two lists have at least one common member.
    """
    # Method 1: Using set intersection
    return bool(set(list1) & set(list2))
    
    # Method 2: Using any() with generator expression
    # return any(item in list2 for item in list1)
    
    # Method 3: Using loop
    # for item in list1:
    #     if item in list2:
    #         return True
    # return False

print("34) Check Common Members:")
list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]
list_c = [9, 10, 11]
print(f"List A: {list_a}")
print(f"List B: {list_b}")
print(f"List C: {list_c}")
print(f"A and B have common members: {has_common_member(list_a, list_b)}")
print(f"A and C have common members: {has_common_member(list_a, list_c)}")
print()

 35)Write a Python program to generate and print a list of first and last 5elements where the values are square of numbers between 1 and 30. 
def generate_square_list():
    """
    Generate and print a list of first and last 5 elements where
    values are squares of numbers between 1 and 30.
    """
    # Generate squares for numbers 1 to 30
    all_squares = [x**2 for x in range(1, 31)]
    
    # Get first 5 and last 5 elements
    first_five = all_squares[:5]
    last_five = all_squares[-5:]
    
    return first_five + last_five

print("35) First and Last 5 Squares (1-30):")
squares_list = generate_square_list()
print(f"Squares list: {squares_list}")
print()

 36) Write a Python function that takes a list and returns a new list with unique elements of the first list. 
def get_unique_elements(input_list):
    """
    Return a new list with unique elements of the first list.
    """
    # Using set to get unique elements, then convert back to list
    return list(set(input_list))

print("36) Get Unique Elements:")
original_list = [1, 2, 2, 3, 4, 4, 4, 5, 1, 6, 7, 7]
unique_elements = get_unique_elements(original_list)
print(f"Original: {original_list}")
print(f"Unique: {unique_elements}")
print()

 37) Write a Python program to convert a list of characters into a string
def char_list_to_string(char_list):
    """
    Convert a list of characters into a string.
    """
    # Method 1: Using join()
    return ''.join(char_list)
    
    # Method 2: Using loop
    # result = ''
    # for char in char_list:
    #     result += char
    # return result

print("37) Convert Character List to String:")
char_list = ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
result_string = char_list_to_string(char_list)
print(f"Character list: {char_list}")
print(f"Result string: '{result_string}'")
print()

 38) Write a Python program to select an item randomly from a list.
import random

def select_random_item(input_list):
    """
    Select an item randomly from a list.
    """
    if not input_list:
        return None
    return random.choice(input_list)

print("38) Select Random Item:")
sample_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
for _ in range(5):
    random_item = select_random_item(sample_list)
    print(f"Random selection: {random_item}")
print()

 39) Write a Python program to find the second smallest number in a list. 
def second_smallest(numbers):
    """
    Find the second smallest number in a list.
    """
    if len(numbers) < 2:
        return None
    
    # Remove duplicates and sort
    unique_sorted = sorted(set(numbers))
    
    if len(unique_sorted) < 2:
        return None
    
    return unique_sorted[1]

print("39) Find Second Smallest Number:")
test_numbers = [5, 2, 8, 1, 9, 3, 1, 2, 5]
second_small = second_smallest(test_numbers)
print(f"List: {test_numbers}")
print(f"Second smallest: {second_small}")

# Test with duplicates
test_numbers2 = [1, 1, 1, 1]
second_small2 = second_smallest(test_numbers2)
print(f"List: {test_numbers2}")
print(f"Second smallest: {second_small2}")
print()

 40) Write a Python program to get unique values from a list 
def get_unique_values(input_list):
    """
    Get unique values from a list while preserving order.
    """
    # Using dict to preserve order
    return list(dict.fromkeys(input_list))

print("40) Get Unique Values (Order Preserved):")
duplicate_list = [3, 1, 2, 3, 4, 2, 1, 5, 4, 6]
unique_ordered = get_unique_values(duplicate_list)
print(f"Original: {duplicate_list}")
print(f"Unique (ordered): {unique_ordered}")
print()

 41) Write a Python program to check whether a list contains a sub list 
def contains_sublist(main_list, sublist):
    """
    Check whether a list contains a sublist.
    """
    if not sublist:
        return True
    
    sub_len = len(sublist)
    for i in range(len(main_list) - sub_len + 1):
        if main_list[i:i + sub_len] == sublist:
            return True
    return False

print("41) Check if List Contains Sublist:")
main_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sublist1 = [3, 4, 5]
sublist2 = [5, 6, 7, 8]
sublist3 = [2, 4, 6]  # Not contiguous

print(f"Main list: {main_list}")
print(f"Contains {sublist1}: {contains_sublist(main_list, sublist1)}")
print(f"Contains {sublist2}: {contains_sublist(main_list, sublist2)}")
print(f"Contains {sublist3}: {contains_sublist(main_list, sublist3)}")
print()

 42) Write a Python program to split a list into different variables. 
def split_list(input_list):
    """
    Split a list into different variables.
    """
    if len(input_list) < 3:
        return "List too short to split meaningfully"
    
    # Unpack into variables (number should match list length)
    first, second, *rest, last = input_list
    return first, second, rest, last

print("42) Split List into Variables:")
sample_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = split_list(sample_list)
print(f"Original list: {sample_list}")
print(f"Split result: first={result[0]}, second={result[1]}, rest={result[2]}, last={result[3]}")
print()

 
43) What is tuple? Difference between list and tuple.

   Tuple: A tuple is an ordered, immutable collection of elements in Python.
   
   Differences between List and Tuple:
   1. Mutability:
      - Lists are mutable (can be modified after creation)
      - Tuples are immutable (cannot be modified after creation)
   
   2. Syntax:
      - Lists use square brackets: [1, 2, 3]
      - Tuples use parentheses: (1, 2, 3) or just commas: 1, 2, 3
   
   3. Performance:
      - Tuples are generally faster than lists
      - Tuples use less memory than lists
   
   4. Use Cases:
      - Lists: For collections that need to be modified
      - Tuples: For fixed collections, dictionary keys, function return values
   
   5. Methods:
      - Lists have more built-in methods (append, extend, pop, etc.)
      - Tuples have fewer methods (count, index)
 

 44) Write a Python program to create a tuple with different data types.
def create_mixed_tuple():
    
    Create a tuple with different data types.
    
    mixed_tuple = (
        42,                   # integer
        3.14,                 # float
        "hello",              # string
        True,                 # boolean
        [1, 2, 3],            # list
        {"name": "John"},     # dictionary
        (4, 5, 6),            # nested tuple
        None                  # None type
    )
    return mixed_tuple

print("44) Tuple with Different Data Types:")
mixed_tuple = create_mixed_tuple()
print("Mixed tuple:", mixed_tuple)
print("Types of elements:")
for i, item in enumerate(mixed_tuple):
    print(f"  {i}: {item} ({type(item).__name__})")
print()

 45))Write a Python program to unzip a list of tuples into individual lists.
def unzip_tuples(tuple_list):
    """
    Unzip a list of tuples into individual lists.
    """
    if not tuple_list:
        return []
    
    # Using zip with * operator to unzip
    return list(zip(*tuple_list))

print("45) Unzip List of Tuples:")
tuple_list = [(1, 'a', True), (2, 'b', False), (3, 'c', True), (4, 'd', False)]
unzipped = unzip_tuples(tuple_list)
print(f"Original: {tuple_list}")
print(f"Unzipped: {unzipped}")

# Access individual lists
if unzipped:
    numbers, letters, flags = unzipped
    print(f"Numbers: {list(numbers)}")
    print(f"Letters: {list(letters)}")
    print(f"Flags: {list(flags)}")
print()

# =============================================================================
# DEMONSTRATION OF ALL FUNCTIONS
# =============================================================================

def demonstrate_all_functions():
    """Demonstrate all functions from this part"""
    print("="*60)
    print("DEMONSTRATION OF ALL FUNCTIONS - PART 3")
    print("="*60)
    
    # Demonstrate list comparison
    print("30) List Comparison Examples:")
    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    list3 = [3, 2, 1]
    print(f"list1 == list2: {list1 == list2}")
    print(f"list1 is list2: {list1 is list2}")
    print(f"sorted(list1) == sorted(list3): {sorted(list1) == sorted(list3)}")
    print()
    
    # Demonstrate other functions
    print("31) Special strings count:", count_special_strings(['aa', 'bb', 'abc', 'aba']))
    print("32) Remove duplicates:", remove_duplicates([1, 2, 2, 3, 3, 3, 4]))
    print("33) Is empty check:", is_list_empty([]))
    print("34) Common members:", has_common_member([1, 2, 3], [3, 4, 5]))
    print("35) Squares list:", generate_square_list())
    print("36) Unique elements:", get_unique_elements([1, 2, 2, 3, 3, 4]))
    print("37) Char list to string:", char_list_to_string(['H', 'i', '!']))
    print("38) Random item:", select_random_item(['a', 'b', 'c']))
    print("39) Second smallest:", second_smallest([5, 2, 8, 1, 9]))
    print("40) Unique values:", get_unique_values([3, 1, 2, 3, 2, 1]))
    print("41) Contains sublist:", contains_sublist([1, 2, 3, 4, 5], [2, 3, 4]))
    print("42) Split list:", split_list([1, 2, 3, 4, 5]))
    print("44) Mixed tuple:", create_mixed_tuple())
    print("45) Unzip tuples:", unzip_tuples([(1, 'a'), (2, 'b')]))

if __name__ == "__main__":
    demonstrate_all_functions()

 46) Write a Python program to convert a list of tuples into a dictionary. 
def tuples_to_dict(tuple_list):
    """
    Convert a list of tuples into a dictionary.
    """
    return dict(tuple_list)

print("46) Convert List of Tuples to Dictionary:")
tuple_list = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
result_dict = tuples_to_dict(tuple_list)
print(f"Tuple list: {tuple_list}")
print(f"Dictionary: {result_dict}")
print()

 47) How will you create a dictionary using tuples in python? 
def create_dict_from_tuples():
    """
    Create a dictionary using tuples as keys.
    """
    # Using tuples as keys (tuples are immutable, so they can be dictionary keys)
    tuple_dict = {
        (1, 2): 'point1',
        (3, 4): 'point2',
        (5, 6): 'point3'
    }
    return tuple_dict

print("47) Create Dictionary Using Tuples as Keys:")
tuple_dict = create_dict_from_tuples()
print(f"Dictionary with tuple keys: {tuple_dict}")
print(f"Access value with tuple key (1,2): {tuple_dict[(1,2)]}")
print()

 48) Write a Python script to sort (ascending and descending) adictionary by value. 
def sort_dict_by_value(input_dict, ascending=True):
    """
    Sort a dictionary by value in ascending or descending order.
    """
    if ascending:
        return dict(sorted(input_dict.items(), key=lambda item: item[1]))
    else:
        return dict(sorted(input_dict.items(), key=lambda item: item[1], reverse=True))

print("48) Sort Dictionary by Value:")
sample_dict = {'apple': 5, 'banana': 2, 'cherry': 8, 'date': 1}
print(f"Original dictionary: {sample_dict}")
print(f"Ascending order: {sort_dict_by_value(sample_dict, True)}")
print(f"Descending order: {sort_dict_by_value(sample_dict, False)}")
print()

 49) )Write a Python script to concatenate following dictionaries to create a new one. 
def concatenate_dicts(*dicts):
    """
    Concatenate multiple dictionaries to create a new one.
    """
    result = {}
    for d in dicts:
        result.update(d)
    return result

print("49) Concatenate Dictionaries:")
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5, 'f': 6}
concatenated = concatenate_dicts(dict1, dict2, dict3)
print(f"Dict1: {dict1}")
print(f"Dict2: {dict2}")
print(f"Dict3: {dict3}")
print(f"Concatenated: {concatenated}")
print()

 50) Write a Python script to check if a given key already exists in a dictionary.
def key_exists(dictionary, key):
    """
    Check if a given key already exists in a dictionary.
    """
    # Method 1: Using 'in' keyword (recommended)
    return key in dictionary
    
    # Method 2: Using get() method
    # return dictionary.get(key) is not None
    
    # Method 3: Using try-except
    # try:
    #     _ = dictionary[key]
    #     return True
    # except KeyError:
    #     return False

print("50) Check if Key Exists:")
test_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
print(f"Dictionary: {test_dict}")
print(f"Key 'age' exists: {key_exists(test_dict, 'age')}")
print(f"Key 'salary' exists: {key_exists(test_dict, 'salary')}")
print()

 
51) How Do You Traverse Through a Dictionary Object in Python?

   There are several ways to traverse through a dictionary:

   1. By keys: 
        for key in dictionary:
            print(key, dictionary[key])
   
   2. By items (key-value pairs):
        for key, value in dictionary.items():
            print(key, value)
   
   3. By values only:
        for value in dictionary.values():
            print(value)
   
   4. By keys only (explicit):
        for key in dictionary.keys():
            print(key, dictionary[key])
 

 
52) How Do You Check the Presence of a Key in A Dictionary?

   Methods to check key presence:
   
   1. Using 'in' keyword (most Pythonic):
        if key in dictionary:
   
   2. Using get() method:
        if dictionary.get(key) is not None:
   
   3. Using try-except block:
        try:
            value = dictionary[key]
            # Key exists
        except KeyError:
            # Key doesn't exist
   
   4. Using keys() method:
        if key in dictionary.keys():
 

 53) Write a Python script to print a dictionary where the keys are numbers between 1 and 15. 
def create_number_dict():
    """
    Create a dictionary where keys are numbers between 1 and 15.
    """
    return {i: i**2 for i in range(1, 16)}  # Using dictionary comprehension

print("53) Dictionary with Keys 1-15:")
number_dict = create_number_dict()
print(f"Number dictionary: {number_dict}")
print()

 54) Write a Python program to check multiple keys exists in a dictionary 
def check_multiple_keys(dictionary, keys):
    """
    Check if multiple keys exist in a dictionary.
    """
    return all(key in dictionary for key in keys)

print("54) Check Multiple Keys Exist:")
test_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
keys_to_check = ['a', 'b', 'c']
keys_to_check2 = ['a', 'x', 'c']
print(f"Dictionary: {test_dict}")
print(f"All keys {keys_to_check} exist: {check_multiple_keys(test_dict, keys_to_check)}")
print(f"All keys {keys_to_check2} exist: {check_multiple_keys(test_dict, keys_to_check2)}")
print()

 55) Write a Python script to merge two Python dictionaries
def merge_dicts(dict1, dict2):
    """
    Merge two Python dictionaries.
    """
    # Method 1: Using update() (modifies dict1)
    # result = dict1.copy()
    # result.update(dict2)
    # return result
    
    # Method 2: Using dictionary unpacking (Python 3.5+)
    return {**dict1, **dict2}
    
    # Method 3: Using | operator (Python 3.9+)
    # return dict1 | dict2

print("55) Merge Two Dictionaries:")
dict_a = {'a': 1, 'b': 2}
dict_b = {'b': 3, 'c': 4}  # Note: key 'b' will be overwritten
merged = merge_dicts(dict_a, dict_b)
print(f"Dict A: {dict_a}")
print(f"Dict B: {dict_b}")
print(f"Merged: {merged}")
print()

 56) Write a Python program to map two lists into a dictionary Sample output: Counter ({'a': 400, 'b': 400,’d’: 400, 'c': 300})
def map_lists_to_dict(keys, values):
    """
    Map two lists into a dictionary.
    """
    # Method 1: Using zip() and dict()
    return dict(zip(keys, values))
    
    # Method 2: Using dictionary comprehension
    # return {keys[i]: values[i] for i in range(min(len(keys), len(values)))}

print("56) Map Two Lists to Dictionary:")
keys_list = ['a', 'b', 'c', 'd']
values_list = [100, 200, 300, 400]
mapped_dict = map_lists_to_dict(keys_list, values_list)
print(f"Keys: {keys_list}")
print(f"Values: {values_list}")
print(f"Mapped dictionary: {mapped_dict}")

# Handle unequal length lists
keys_list2 = ['a', 'b', 'c']
values_list2 = [400, 400, 300, 400]  # Extra value will be ignored
mapped_dict2 = map_lists_to_dict(keys_list2, values_list2)
print(f"Unequal lists -> Keys: {keys_list2}, Values: {values_list2}")
print(f"Mapped dictionary: {mapped_dict2}")
print()

 57) Write a Python program to find the highest 3 values in a dictionary 
def highest_three_values(input_dict):
    """
    Find the highest 3 values in a dictionary.
    """
    if len(input_dict) < 3:
        return "Dictionary should have at least 3 items"
    
    # Sort by values in descending order and get first 3
    sorted_items = sorted(input_dict.items(), key=lambda x: x[1], reverse=True)
    return dict(sorted_items[:3])

print("57) Highest 3 Values in Dictionary:")
sample_dict = {'a': 100, 'b': 500, 'c': 300, 'd': 800, 'e': 200, 'f': 600}
top_three = highest_three_values(sample_dict)
print(f"Original: {sample_dict}")
print(f"Top 3 values: {top_three}")
print()

 58) Write a Python program to combine values in python list of dictionaries.Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount':300}, o {'item': 'item1', 'amount': 750}]Expected Output:• Counter ({'item1': 1150, 'item2': 300})from collections import Counter
def combine_dict_values(dict_list):
    """
    Combine values in Python list of dictionaries.
    """
    result = Counter()
    for d in dict_list:
        result[d['item']] += d['amount']
    return result

print("58) Combine Values in List of Dictionaries:")
data = [
    {'item': 'item1', 'amount': 400},
    {'item': 'item2', 'amount': 300},
    {'item': 'item1', 'amount': 750},
    {'item': 'item3', 'amount': 200},
    {'item': 'item2', 'amount': 150}
]
combined = combine_dict_values(data)
print(f"Sample data: {data}")
print(f"Combined values: {combined}")
print()

 59) )Write a Python program to create a dictionary from a string.Note: Track the count of the letters from the string
def string_to_dict_count(input_string):
    """
    Create a dictionary from a string tracking letter counts.
    """
    # Using dictionary comprehension
    return {char: input_string.count(char) for char in set(input_string)}
    
    # Alternative using Counter
    # from collections import Counter
    # return dict(Counter(input_string))

print("59) Dictionary from String (Letter Count):")
test_string = "w3resource"
char_count = string_to_dict_count(test_string)
print(f"String: '{test_string}'")
print(f"Character count: {char_count}")
print()

 # 60) Sample string: 'w3resource' Expected output:• {'3': 1,’s’: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}
def char_frequency(sample_str):
    freq = {}
    for char in sample_str:
        freq[char] = freq.get(char, 0) + 1
    return freq

# Sample usage for question 60
sample_string = 'w3resource'
print(f"60) Character frequency: {char_frequency(sample_string)}")

 61) Write a Python function to calculate the factorial of a number (a nonnegative integer) 
def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

 62) Write a Python function to check whether a number is in a given range 
def is_in_range(number, start, end):
    return start <= number <= end

 63) Write a Python function to check whether a number is perfect or not
def is_perfect_number(n):
    if n <= 0:
        return False
    divisors_sum = 0
    for i in range(1, n):
        if n % i == 0:
            divisors_sum += i
    return divisors_sum == n

 64) Write a Python function that checks whether a passed string is palindrome or not 
def is_palindrome(s):
    # Remove spaces and convert to lowercase for better checking
    s = s.replace(" ", "").lower()
    return s == s[::-1]

 65)How Many Basic Types of Functions Are Available in Python?
"""
Python has two basic types of functions:
1. Built-in functions: Pre-defined functions that come with Python (e.g., print(), len(), range())
2. User-defined functions: Functions created by users using the 'def' keyword
"""

 66) How can you pick a random item from a list or tuple? 
import random

def random_from_sequence(sequence):
    return random.choice(sequence)

 67)How can you pick a random item from a range?
def random_from_range(start, stop, step=1):
    return random.randrange(start, stop, step)

 68))How can you get a random number in python?
def get_random_number():
    # Returns random float between 0 and 1
    return random.random()

def get_random_int(start, end):
    # Returns random integer in range [start, end]
    return random.randint(start, end)

 69)How will you set the starting value in generating random numbers? 
def set_random_seed(seed_value):
    random.seed(seed_value)

 

 70) How will you randomize the items of a list in place? 
def randomize_list_in_place(lst):
    random.shuffle(lst)
    return lst

 71) What is File function in python? What are keywords to create and write file. 

 
File functions in Python are used to work with files (create, read, write, append).
Keywords to create and write files:
- open(): Used to open a file
- 'w': Write mode (creates new file or overwrites existing)
- 'a': Append mode (appends to existing file)
- 'x': Exclusive creation mode (fails if file exists)
- 'r': Read mode (default)
 

 72) Write a Python program to read an entire text file.
def read_entire_file(filename):
    with open(filename, 'r') as file:
        content = file.read()
    return content

 73) Write a Python program to append text to a file and display the text
def append_to_file(filename, text):
    with open(filename, 'a') as file:
        file.write(text + '\n')
    
    # Display the appended text
    print(f"Appended text: {text}")
    return text

 74) )Write a Python program to read first n lines of a file. 

def read_first_n_lines(filename, n):
    with open(filename, 'r') as file:
        lines = []
        for i, line in enumerate(file):
            if i < n:
                lines.append(line.strip())
            else:
                break
    return lines

 75)Write a Python program to read last n lines of a file
def read_last_n_lines(filename, n):
    with open(filename, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines[-n:]]

 76)Write a Python program to read a file line by line and store it into a list
def read_file_to_list(filename):
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file]
    return lines

 77) Write a Python program to read a file line by line store it into a variable. 
def read_file_to_variable(filename):
    content = ""
    with open(filename, 'r') as file:
        for line in file:
            content += line
    return content

 78)Write a python program to find the longest words
def find_longest_words(text):
    words = text.split()
    if not words:
        return []
    
    max_length = max(len(word) for word in words)
    return [word for word in words if len(word) == max_length]

 79)Write a Python program to count the number of lines in a text file
def count_lines(filename):
    with open(filename, 'r') as file:
        return sum(1 for line in file)

 80)Write a Python program to count the frequency of words in a file. 
def count_word_frequency(filename):
    with open(filename, 'r') as file:
        content = file.read()
        words = content.split()
        return Counter(words)

 81) Write a Python program to write a list to a file.
def write_list_to_file(filename, data_list):
    with open(filename, 'w') as file:
        for item in data_list:
            file.write(str(item) + '\n')

 82)Write a Python program to copy the contents of a file to another file. 
def copy_file(source_filename, dest_filename):
    with open(source_filename, 'r') as source:
        with open(dest_filename, 'w') as dest:
            dest.write(source.read())

 83))Explain Exception handling? What is an Error in Python? 
 
Exception handling: A mechanism to handle runtime errors gracefully using try-except blocks.
Error in Python: An issue that occurs during program execution that disrupts normal flow.
Types: Syntax errors (compile-time) and exceptions (runtime errors).
 

 84)How many except statements can a try-except block have? Name Some built-in exception classes: 

 
A try-except block can have multiple except statements to handle different exceptions.
Some built-in exception classes:
- ValueError, TypeError, IndexError, KeyError, FileNotFoundError, ZeroDivisionError
- ImportError, AttributeError, NameError, MemoryError, RuntimeError
 

 85) When will the else part of try-except-else be executed?
 
The else part executes only if no exception occurs in the try block.
 

 86) Can one block of except statements handle multiple exception? 

 
Yes, one except block can handle multiple exceptions:
except (ValueError, TypeError) as e:
 

 87)When is the finally block executed? 
 
The finally block always executes, whether an exception occurred or not.
It's used for cleanup operations (like closing files).
 

 88)What happens when „1‟== 1 is executed?
 
It returns False because we're comparing a string '1' with integer 1.
Python doesn't perform implicit type conversion in comparisons.
 

 89)How Do You Handle Exceptions with Try/Except/Finally in Python? Explain with coding snippets. 
def exception_handling_example():
    try:
        # Code that might raise an exception
        num = int(input("Enter a number: "))
        result = 10 / num
        print(f"Result: {result}")
    
    except ValueError:
        print("Error: Please enter a valid integer!")
    
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    else:
        print("No exceptions occurred!")
    
    finally:
        print("This always executes (cleanup code here)")

 90)Write python program that user to enter only odd numbers, else will raise an exception. 
def accept_only_odd_numbers():
    while True:
        try:
            num = int(input("Enter an odd number: "))
            
            if num % 2 == 0:
                raise ValueError("Even number entered! Please enter an odd number.")
            
            print(f"Thank you! You entered odd number: {num}")
            break
        
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"Unexpected error: {e}")

 
