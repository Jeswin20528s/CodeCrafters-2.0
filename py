print("\n        Calculator Menu")
print("\n1.Addition")
print("2.Substraction")
print("3.Multiplication")
print("4.Division")
print("5.Module")
print("6.Exit")

value = input("\nenter your choice : ")

x=int(input("enter a 1st number ="))
y=int(input("enter a 2nd number ="))

if value == "1":
    print("\naddition = " ,x+y)