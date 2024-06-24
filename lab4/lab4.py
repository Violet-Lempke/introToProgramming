import math
'''Menu Function prompts the user to enter a number that determines the task they
would like to complete'''
def menu():
	choice = int(input("\nTo determine whether or not a set of lines can be a
triangle, Enter 1,\nTo determine a right triangle Enter 2\nTo check if a set of
coordinates form a square Enter 3\nTo have a conversation enter 4\nTo create a
cascade enter 5\nTo quit enter 6\n"))
	if (choice == 1):
		triangleCheck()
		menu()
	elif (choice == 2):
		rightTriangleCheck()
		menu()
	elif (choice == 3):
		squareCheck()
		menu()
	elif (choice == 4):
		s = str(input("Say Hello\n"))
		conversation(s)
	elif(choice ==5):
		print("Enter the value to be cascaded:")
		n = int(input())
		cascade(n)
''' isTriangle Function takes 3 values and determines if they are lengths that can
form a triangle'''
#x = first length
#y = second length
#z = third length
def isTriangle(x, y, z):
	if (x + y >= z)and(x + z >= y)and(y + z >= x): #this line utilizes the triangle inequality theorem to determine whether or not the given lengths can form a triangle
		return "yes"
	else:
		return "no"
''' isRightTriangle Function takes 3 values and determines if they are lengths that
can form a right triangle'''
#x = first length
#y = second length
#z = third length
def isRightTriangle(x, y, z):
	if (x ^ 2 + y ^ 2 == z ^ 2): #if through elif utilizes the pythagorean theorem to determine whether or not the given lengths can form a right triangle return "yes"
	elif (y ^ 2 + z ^ 2 == x ^ 2):
		return "yes"
	elif (x ^ 2 + z ^ 2 == y ^ 2):
		return "yes"
	else:
		return "no"
''' getLengths prompts the user to input 3 values which will be used as the lengths
for a triangle'''
def getLengths():
	print("Enter the lengths of 3 sides:")
	x, y, z = int(input("Value 1:")),int(input("Value 2:")),int(input("Value
3:"))#prompts the user to enter three values and stores these value as x, y, and z
return x, y, z
'''squareCheck determines whether or not four coordinate points can form a
square'''
def squareCheck():
	print("Enter 4 coordinate points:")
	x1, y1 = int(input("x1=")),int(input("y1="))#These lines prompt the user to input their points and then stores them.
	x2, y2 = int(input("x2=")),int(input("y2="))
	x3, y3 = int(input("x3=")),int(input("y3="))
	x4, y4 = int(input("x4=")),int(input("y4="))
	p1 = [x1, y1]#these lines store the coordinates that go together into a list.
	p2 = [x2, y2]
	p3 = [x3, y3]
	p4 = [x4, y4]
	s1 = x1 + y1 + .1 #The purpose of these lines is to ensure that the points are in order from left to right, this ensures that a false negative is not recieved.
	s2 = x2 + y2 + .2
	s3 = x3 + y3 + .3
	s4 = x4 + y4 + .4
	sums = [s1, s2, s3, s4]
	sums.sort()
	indexs1 = sums.index(s1)
	indexs2 = sums.index(s2)
	indexs3 = sums.index(s3)
	indexs4 = sums.index(s4)
	sums[indexs1] = p1
	sums[indexs2] = p2
	sums[indexs3] = p3
	sums[indexs4] = p4
	p1 = sums[0]#These lines arrange the coordinates in size order.
	p2 = sums[1]
	p3 = sums[2]
	p4 = sums[3]
	d1 = math.sqrt(abs((p2[0]) - p1[0] ^ 2) + abs((p2[1] - p1[1]) ^ 2))#Determine the distance between the points.
	d2 = math.sqrt(abs((p3[0] - p1[0]) ^ 2) + abs((p3[1] - p1[1]) ^ 2))
	d3 = math.sqrt(abs((p4[0] - p1[0]) ^ 2) + abs((p4[1] - p1[1]) ^ 2))
	d4 = math.sqrt(abs((p1[0] - p4[0]) ^ 2) + abs((p1[1] - p4[1]) ^ 2))
	if (d1 == d2):#Checks if the distances can form a square and informs the user of the result.
		if (d1 + d2 == d3) or (d1 + d2 == d4):
			print("\nYes, it is a Square")
			menu()
	else:
		print("\nNo, it is not a Square")
		menu()
''' triangleCheck function utilizes the getLengths and isTriangle functions to
collect three lengths and determine if they can form a triangle, it then displays
the result to the user.'''
def triangleCheck():
	x, y, z = getLengths() #utilizes get lengths to recieve three lengths that are stored as x, y, and z
	triangleResult = isTriangle(x, y, z) #utilizes isTriangle to determine if the stored lengths can form a triangle
	if (triangleResult == "yes"): #if isTriangle determines that the lengths entered can form a triangle this line informs the user of the result
		print("\nA triangle can have sides of length "+str(x)+", "+str(y)+", and "+str(z)+".")
	else:#if isTriangle determines that the lengths entered can not form a triangle this line informs the user of the result
		print("\nA triangle can not have sides of length "+str(x)+", "+str(y)+", and "+str(z)+".")
'''rightTriangleCheck function utilizes getLengths and isRightTriangle to collect
three lengths and determine if they form a right triangle, it then displays the
result to the user.'''
def rightTriangleCheck():
	x, y, z = getLengths()#utilizes get lengths to recieve three lengths that are stored as x, y, and z
	triangleResult = isRightTriangle(x, y, z)#utilizes isRightTriangle to determine if the stored lengths can form a right triangle
	if (triangleResult == "yes"):#if isRightTriangle determines that the lengths entered can form a right triangle this line informs the user of the result
		print("\nA right triangle can have sides of length "+str(x)+", "+str(y)+", and "+str(z)+".")
	else:#if isRightTriangle determines that the lengths entered can not form a right triangle this line informs the user of the result
		print("\nA right triangle can not have sides of length "+str(x)+", "+str(y) +", and "+str(z)+".")
'''conversations takes input from the user and returns it back to them asking if it
was what they said'''
def conversation(s):
	if (s == "bye"):#if the input is given is bye then the program outputs have a
		nice day and returns to the menu.
		print("Have a nice day!")
menu()
	else:
		print("Did you say "+s+"?")#Print the output and recieves a new input that is given to the function.
		s = str(input())
		conversation(s)
'''cascade takes an input from the user and makes a pattern out of it'''
def cascade(n):
	print(n)
	if (n // 10 != 0):
		cascade(n//10)
		print(n)
def main():
	menu()
main()
