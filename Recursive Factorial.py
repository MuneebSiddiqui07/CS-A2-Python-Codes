def RecursiveFactorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num*RecursiveFactorial(num - 1)
num = int(input("Enter a number: "))
answer = RecursiveFactorial(num)
print("Your answer is: ", answer)
