import art
def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2
ops = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}
# print(ops["*"](4,8))
def calculator():
    print(art.logo)
    loop = True
    first_number = float(input("Enter the first number: "))
    while loop:
        for symbol in ops:
            print(symbol)
        operation = input("Enter the operation: ")
        second_number = float(input("Enter the second number: "))
        answer = ops[operation](first_number,second_number)
        print(f'{first_number} {operation} {second_number} = {answer}')

        loop = input(f'type "y" for continue with {first_number} or "n" to start new calculations')
        if loop == "y":
            first_number = answer
        else:
            loop = False
            print("\n"*20)
            calculator()
calculator()