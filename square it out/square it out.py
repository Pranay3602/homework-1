user_input_text = input("Enter a number to find its square: ")
try:
    number = float(user_input_text)
    print(f"You entered the number: {number}")
    print("your square value is,", number*number)
except ValueError:
    print("That's not a valid number. Please try again")