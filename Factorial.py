def factorial(num):
    f=1
    for i in range(num,0,-1):
        f= f*i
    return f
x = int(input("Enter number whose factorial you would like to find: "))
answer = factorial(x)
print("Your answer is: ",answer)
