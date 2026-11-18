import arithematic.calculator

print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")

ch= int(input("Enter your choice:"))

if ch==1:
  arithematic.calculator.addition()
elif ch==2:
  arithematic.calculator.substraction()
elif ch==3:
  arithematic.calculator.multiplicaition()
elif ch==4:
  arithematic.calculator.division()
else:
 print("Invalid choice")

