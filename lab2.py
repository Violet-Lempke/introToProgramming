'''Violet Lempke'''
'''Lab #2'''
import math
def taskSelection():
	print("\nTo find the volume of a sphere enter 1\nTo find the wholesale cost of
a book enter 2\nTo talk to the animals enter 3\nTo calculate the time it takes for
you to run a distance enter 4")
	response = int(input())
	if response == 1:
		sphereVolume()
	elif response == 2:
		printTotalWholesaleCost()
	elif response == 3:
		printAnimalSounds()
	elif response == 4:
		printBreakfestTime()
def sphereVolume():
	radius = int(input("Enter the radius of your sphere: "))
	volume = (4/3)*math.pi*radius**3
	print("The volume of a sphere with radius "+str(radius)+" is: "+str(volume))
	taskSelection()
def printTotalWholesaleCost():
	copies = int(input("Enter number of books: "))
	cost = float(input("Enter Price of Book: $"))
	shipping = (copies-1)*.75+3
	adjustedCost = (cost*copies)-((cost*copies)*.40)
	totalCost = shipping+adjustedCost
	print(totalCost)
	taskSelection()
def printAnimalSounds():
	horse_sound = "neigh"
	duck_sound = "quack"
	cow_sound = "moo"
	goat_sound = "bleat"
	num_horses = int(input("How many horses?: "))
	num_ducks = int(input("How many ducks?: "))
	num_cows = int(input("How many cows?: "))
	num_goats = int(input("How many horses?: "))
	print(horse_sound*num_horses+duck_sound*num_ducks+cow_sound*num_cows+goat_sound*num
_goats)
def printBreakfestTime():
	startHour = int(input("Enter starting hour: "))
	startMinute = int(input("Enter starting minute: "))
	startSecond = int(input("Enter starting second: "))
	easy_mile_minutes = int(input("Minutes in an easy mile: "))
	easy_mile_seconds = int(input("Seconds in an easy mile: "))
	tempo_mile_minutes = int(input("Minutes in a tempo mile: "))
	tempo_mile_seconds = int(input("Seconds in a tempo mile: "))
	easyMileNumber = float(input("Number of easy miles: "))
	tempoMileNumber = float(input("Number of tempo miles: "))
	totalMiles = easyMileNumber+tempoMileNumber
	print(totalMiles)
	convertedEasyMinutes = easy_mile_minutes*60
	totalEasySeconds = convertedEasyMinutes+easy_mile_seconds
	finalEasySeconds = float(totalEasySeconds*easyMileNumber)
	convertedTempoMinutes = tempo_mile_minutes*60
	totalTempoSeconds =
	float((convertedTempoMinutes+tempo_mile_seconds)*tempoMileNumber)
	totalSeconds = finalEasySeconds+totalTempoSeconds
	totalMinutes = int(totalSeconds/60)
	adjustedSeconds = int(totalSeconds%60)
	totalHours = int(totalMinutes/60)
	adjustedMinutes = int(totalMinutes%60)
	arrivalHour = startHour+totalHours
	arrivalMinute = startMinute+adjustedMinutes
	arrivalSecond = adjustedSeconds+startSecond
	print("\nTotal Time Taken: "+str(totalHours)+":"+str(adjustedMinutes)
+":"+str(adjustedSeconds))
	print("\nArrival Time: "+str(arrivalHour)+":"+str(arrivalMinute)
+":"+str(arrivalSecond))
	taskSelection()
def main():
	taskSelection()
main()
