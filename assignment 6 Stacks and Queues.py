#Exercise 1

stack = []
top = -1

def push(ele: str):
    global top
    top += 1
    stack[top] = ele

def pop():
    global top
    ele = stack[top]
    top -= 1
    return ele

def isPalindrome(string: str) -> bool:
    global stack
    length = len(string)

    stack = ['0'] * (length + 1)

    # Finding the mid
    mid = length // 2
    i = 0

    while i < mid:
        push(string[i])
        i += 1

    # Checking if the length of the string is odd, if odd then neglect the middle character
    if length % 2 != 0:
        i += 1

    # While not the end of the string
    while i < length:
        ele = pop()

        # If the characters differ then the given string is not a palindrome
        if ele != string[i]:
            return False
        i += 1

    return True

# Get user input for the word
user_input = str(input("Enter the word: "))
string = user_input

if isPalindrome(string):
    print("The given input is a palindrome.")
else:
    print("The given input is not a palindrome.")

 
        

# Exercise 2

def areBracketsBalanced(expr):
    stack = []

    # Traversing the Expression
    for char in expr:
        if char == "{":
            stack.append(char)
        elif char == "}":
            if not stack:
                return False
            stack.pop()

    # Check Empty Stack
    if stack:
        return False
    return True

# Get user input for the expression
user_input = str(input("Enter the expression: "))
expr = user_input

if areBracketsBalanced(expr):
    print("Balanced")
else:
    print("Not Balanced")
    
    
    

#Stack

def decode_message(encoded_message):
    stack = []

    for char in encoded_message:
        if char.isalpha() or char.isspace():
            stack.append(char)
        elif char == '*':
            if stack:
                stack.pop()

    decoded_message = ''
    while stack:
        decoded_message += stack.pop()

    return decoded_message

# Get user input
user_input = input("Enter the encoded message: ")

# Decode the message
decoded_message = decode_message(user_input)

# Print the result
print("Decoded Message:", decoded_message)


