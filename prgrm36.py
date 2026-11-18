num=int(input("Enter a number: "))
check= lambda n:"Even" if n % 2 == 0 else "Odd"
print("The number is", check(num))
