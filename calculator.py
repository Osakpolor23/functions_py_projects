# x = float(input("what's x?"))
# y = float(input("what's y?"))

# z = round((x / y), 3) 

# print(f"{z:,}")

def main():
    x = int(input("what's the value of x ?"))
    print("x squared is:", square(x))

def square(n):
    return pow(n,2)

main()
