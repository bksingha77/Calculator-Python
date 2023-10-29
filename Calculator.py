print("CALCULATOR USING PYTHON")

First = float(input("Enter the first number:"))
Second = float(input("Enter the second number here:"))

print("\nPress 1 for Addition + \nPress 2 for Substraction - \nPress 3 for Multiplication * \nPress 4 for Division \nPress 5 for Modules %")

choice = int(input("\nPress 1-5 given above: "))

if choice == 1:
  print(First + Second)
elif choice == 2:
  print(First - Second)
elif choice == 3:
  print(First * Second)
elif choice == 4:
  print(First / Second)
elif choice == 5:
  print(First % Second)
else:
  print("Oops! Invelid Input☹️")