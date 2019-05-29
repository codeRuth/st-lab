import sys
# Input three sides of triangle
a, b, c = [int (x) for x in sys.argv[1:]]

if a < 1 or a > 100 or b < 1 or b > 100 or c < 1 or c > 100:
    print("Out of Range")
    exit()

if(a > b + c or b > c + a or c > b + a):
    print("Not a Triangle")
    exit()

if(a == b and b == c):
    print("Equilateral")
elif(a == b or b == c or c == a):
    print("Isoceles")
else:
    print("Scalene")