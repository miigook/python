def conversion(num):
    binary_num = bin(num)
    octal_num = oct(num)
    hex_num = hex(num)

    print("<---------------->")
    print("Binary #:", binary_num)
    print("Octal #:", octal_num)
    print("Hexadecimal #: ", hex_num)
    print("<-------------------->")

decimal_num = int(input("Please enter a number: "))
conversion(decimal_num)