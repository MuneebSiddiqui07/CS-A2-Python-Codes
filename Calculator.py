num1 = float(input("Enter a number: "))
operator = input("Enter an operator: ")
num2 = float(input("Enter another number: "))

calculatorKeyboard=[
7   8   9
4   5   6   x   /
3   2   1   +   -
0   .       Ans =
]
if operator == '+':
    ans=str(num1 + num2)
elif operator == 'x':
    ans= str(num1* num2)
elif operator == '-':
    ans= str(num1 - num2)
elif operator == '/':
    ans= str(num1 / num2)

print(ans)
