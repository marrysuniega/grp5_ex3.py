# Function to calculate the length of a string
def calculate_length(input_string):
    return len(input_string)

# Function to count the number of characters in a string
def count_characters(input_string):
    return len(input_string)

# Function to replace all occurrences of the first character with '$'
def replace_first_char(input_string):
    if input_string:
        first_char = input_string[0]
        return first_char + input_string[1:].replace(first_char, '$')
    return input_string

# Function to swap the first two characters of two strings and concatenate them
def swap_and_concatenate(str1, str2):
    if len(str1) < 2 or len(str2) < 2:
        return "Both strings must have at least 2 characters."
    
    swapped_str1 = str2[:2] + str1[2:]
    swapped_str2 = str1[:2] + str2[2:]
    return swapped_str1 + " " + swapped_str2

# Using + to concatenate strings with spaces
def concatenate_strings_with_spaces(var1, var2, var3, var4):
    return var1 + " " + var2 + " " + var3 + " " + var4

# Using + to concatenate user input strings
def concatenate_user_input():
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")
    return str1 + " " + str2

# Using + to create a paragraph with name and age
def create_paragraph(name, age):
    return "My name is " + name + " and I am " + str(age) + " years old."

# Example usage
if __name__ == "__main__":
    # Calculate length of a string
    sample_string = "abababba"
    print("Length of string:", calculate_length(sample_string))
    
    # Count characters in a string
    print("Number of characters:", count_characters(sample_string))
    
    # Replace first char with '$'
    print("Modified string:", replace_first_char(sample_string))
    
    # Swap and concatenate two strings
    str1 = "sunny"
    str2 = "day"
    print("Swapped and concatenated:", swap_and_concatenate(str1, str2))
    
    # Concatenate four strings with spaces
    result = concatenate_strings_with_spaces("Python", "is", "fun", "today")
    print("Concatenated strings:", result)
    
    # Concatenate user input strings
    print("Concatenated user input:", concatenate_user_input())
    
    # Create a paragraph with name and age
    name = "Danilo"
    age = 30
    print(create_paragraph(name, age))
