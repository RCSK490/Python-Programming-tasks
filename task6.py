a=int(input("side 1 of triangle"))
b=int(input("side 2 of triangle"))
c=int(input("side 3 of triangle"))
if(a==b and b==c and c==a):
 print ("The triangle is an equilateral triangle")
elif(a==b or b==c or c==a):
 print("The triangle is an isoceles triangle")
else:
 print("The triangle is a scalene triangle")