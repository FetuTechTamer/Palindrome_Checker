def is_palindrome(s):
    # Remove spaces and convert to lowercase
    cleaned_string = ''.join(s.split()).lower()
    # Check if the string is the same forwards and backwards
    return cleaned_string == cleaned_string[::-1]

def main():
    print("Welcome to the Palindrome Checker!")
    
    # Get user input
    user_input = input("Enter a string to check if it's a palindrome: ")
    
    # Check if the input is a palindrome
    if is_palindrome(user_input):
        print(f'"{user_input}" is a palindrome.')
    else:
        print(f'"{user_input}" is not a palindrome.')

if __name__ == "__main__":
    main()
