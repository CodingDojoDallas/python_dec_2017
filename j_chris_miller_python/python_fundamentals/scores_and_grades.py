#Scores and Grades
from random import *
def scores_and_grades():
	for i in range(10):
		num = randint(60,100)
		if num > 59 and num < 70:
			grade = "D"
		if num > 69 and num < 80:
			grade = "C"
		if num > 79 and num < 90:
			grade = "B"
		if num > 89 and num <= 100:
			grade = "A"
		print "Score: " + str(num) + ";" + "Your grade is " + str(grade)

scores_and_grades()