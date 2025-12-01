#Check if three lengths form an Equilateral, Isosceles, or Scalene triangle
a = int(input("Please enter the value-1: "))
b = int(input("Please enter the value-2: "))
c = int(input("Please enter the value-3: "))
if a == b and b == c and c == a:
    print("Equlateral")
elif a != b and b != c and c != a:
    print("Isoletral")
else:
    print("Scalar")