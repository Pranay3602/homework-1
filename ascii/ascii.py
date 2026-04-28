print(ord('A'))
print(ord('a'))
print(ord('2'))
print(ord('@'))
print(chr(65))
print(chr(97))
char=input("enter a single character")
if type(char is str and len(char))==1:
    print("valid input")
else:
    print("please enter excactly one digit")
ascii_val=ord(char)
print(f"character: {char}")
print(f"ascii value:{ascii_val}")
if ascii_val >= 65 and ascii_val <= 90:

    print("Type: Uppercase Letter")

elif ascii_val >= 97 and ascii_val <= 122:

    print("Type: Lowercase Letter")

elif ascii_val >= 48 and ascii_val <= 57:

    print("Type: Digit")

elif ascii_val == 32:

    print("Type: Space")

else:

    print("Type: Special Character")