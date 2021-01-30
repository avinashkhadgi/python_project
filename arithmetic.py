def add():
    res = num1 + num2
    print("Result :-",res)
def subtract():
    res = num1 - num2
    print("Result :-",res)
def mul():
    res = num1 * num2
    print("Result :-",res)
def div():
    res = num1 / num2
    print("Result :-",res)

print("1. add")
print("2. subtract")
print("3. mul")
print("4. div")
while True:
    choice = int(input("Enter your choice:-"))
    if (choice>=1 and choice<=4):
        print("Enter two numbers:-")
        num1 = int(input("Enter first No:-"))
        num2 = int(input("Enter second No:-"))
    if choice == 1:
        add()
    if choice == 2:
        subtract()    
    if choice == 3:
        mul()
    if choice == 4:
        div()    
        
