from random import choice

number1=input("Enter first num: ")
num1=int(number1)

number2=input("Enter second num: ")
num2=int(number2)

while True:
    choice=input('Enter the sign(+,-,*,/ or q to quit): ')
    if choice == "+":
        print('your sum is: ',num1 + num2)
    elif choice == '-':
        print('your sub is: ',num1 - num2)
    elif choice == '*':
        print('your product is: ',num1 * num2)
    elif choice == '/':
        print('your result is: ',num1 / num2)
    elif choice == 'q':
        print('closed')
        break
    else:
        print('Invalid choice')

