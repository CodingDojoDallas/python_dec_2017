class Car(object):
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		self.tax = 0
		self.setTax()
		self.display_all()
		

	def setTax(self):
		if self.price > 10000:
			self.tax = .15
		else:
			self.tax = .12

	def display_all(self):
			print "Price = " + str(self.price) + "\nSpeed = " + str(self.speed) + "\nFuel = " + self.fuel + "\nMileage = " + self.mileage + "\nTax = " + str(self.tax) + "\n"

car1 = Car(2000, 35, "Full", "15mpg")
car2 = Car(50000, 50, "Half-Full", "40mpg")
car3 = Car(30000, 40, "Half-Empty", "30mpg")
car4 = Car(4000, 25, "Almost Empty", "35mpg")
car5 = Car(35000, 25, "Almost Full", "48mpg")
car6 = Car(20000, 30, "Empty", "24mpg")