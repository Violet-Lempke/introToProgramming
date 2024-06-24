import turtle
fin = turtle.Turtle()
print(fin)
def setTurtle(x, y, angle):
	fin.pu()
	fin.lt(angle)
	fin.goto(x,y)
	fin.pd()
def rightAngle():
	fin.fd(100)
	fin.lt(90)
	fin.fd(100)
def defaultSquare():
	for i in range(4):
		rightAngle()
def houseBase():
	for i in range(2):
		fin.fd(200)
		fin.lt(90)
		fin.fd(100)
		fin.lt(90)
def houseRoof():
	fin.lt(45)
	fin.fd(141.42)
	fin.lt(90)
	fin.fd(141.42)
def houseDoor():
	fin.fd(50)
	fin.lt(270)
	fin.fd(30)
	fin.lt(270)
	fin.fd(50)
def houseWindow():
	for i in range(50):
		fin.fd(2.5)
		fin.lt(7.2)
def windowPane():
	fin.lt(90)
	fin.fd(40)
	fin.lt(180)
	fin.fd(20)
	fin.lt(90)
	fin.fd(20)
	fin.lt(180)
	fin.fd(40)
	fin.lt(180)
def doorKnob():
	setTurtle(90,25,0)
	for i in range(4):
		fin.fd(5)
		fin.lt(90)
def moon():
	setTurtle(-50,235,270)
	for i in range(25):
		fin.fd(2.5)
		fin.lt(7.2)
	setTurtle(-45,235,180)
	for i in range(25):
		fin.fd(2.5)
		fin.lt(7.2)
def ursaMajor():
	setTurtle(200,250,0)
	fin.fd(50)
	fin.lt(315)
	fin.fd(25)
	fin.lt(5)
	fin.fd(25)
	fin.lt(2)
	fin.fd(25)
	fin.lt(38)
	fin.fd(90)
	fin.lt(255)
	fin.fd(45)
	fin.lt(285)
	fin.fd(70)
	fin.lt(280)
	fin.fd(48)
houseBase()
setTurtle(200, 100, 90)
houseRoof()
setTurtle(86, 0, 225)
houseDoor()
setTurtle(20, 70, 0)
houseWindow()
windowPane()
setTurtle(143, 70, 0)	
houseWindow()
windowPane()
doorKnob()
moon()
ursaMajor()
setTurtle(0, 0, 0)
turtle.mainloop()
