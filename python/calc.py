import inquirer

questions = [ inquirer.List(
    "operator",
    message="Please choose an operator: ",
    choices=["+", "-", "*", "/", "//", "**"], default="+"
     ),
    inquirer.Text("num1", message="Enter first number"),
    inquirer.Text("num2", message="Enter second number"),
]   




answer = inquirer.prompt(questions)
print(answer)

if answer['operator'] == '+':
    result = int(answer['num1']) + int(answer['num2'])
    print("Answer:", result)
elif answer['operator'] == '-':
    result = int(answer['num1']) - int(answer['num2'])
    print("Answer:", result)
elif answer['operator'] == '*':
    result = int(answer['num1']) * int(answer['num2'])
    print("Answer:", result)
elif answer['operator'] == '/':
    result = int(answer['num1']) / int(answer['num2'])
    print("Answer:", result)
elif answer['operator'] == '//':
    result = int(answer['num1']) // int(answer['num2'])
    print("Answer:", result)


lister = ["a","\n" "b", "c", "d"]
print(lister)