name = input("What's your name: ")
if not name.isdigit():
    print("Hello there", name, end="!\n")
else:
    print("error: invalid entry. You must enter name")