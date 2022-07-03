def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


print("Input two positive integers to find GCD: ")

a = int(input("Input first integer: "))
b = int(input("Input second integer: "))

print("The result is: ", gcd(a, b))