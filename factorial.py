def factorial(num):
    if num == 1:
        return num
    return num * factorial(num - 1)

print("Enter the number")
num = int(input())
print(factorial(num))
