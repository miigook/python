input = input("How old are you? ")

if input.isdigit():
    age = int(input)
    print("you will be ", age +1, "years old next year.")
else:
    print("Invalid entry: Enter a number")

print(dir(input))

