try:
    num=int(input("what is your age"))
    if num%2==0:
        print("your age is even")
    else:
        print("your age is odd")
except ValueError:
    print("check if your age is correct")