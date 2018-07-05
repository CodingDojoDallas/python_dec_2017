#Product

class Product(object):
	def __init__(self, price, item_name, weight, brand):
		self.price = price
		self.item_name = item_name
		self.weight = weight
		self.brand = brand
		self.status = "for sale"
		self.tax = .15
		# self.reason = ""

	def sell(self):
		self.add_tax(self.tax)
		self.status = "sold"
		self.display_info()

	def add_tax(self, tax):
		self.tax = self.price * self.tax
		self.price += self.tax
		return self.price

	def return_item(self, reason):
		if reason == "defective":
			self.status = "defective"
		else:
			self.status = "for sale"
		self.display_info()

	def display_info(self):
		print self.brand + self.item_name + "\nPrice = " + str(self.price) + "\nWeight = " + str(self.weight) + "\nStatus = " + self.status + "\nTax = " + str(self.tax) + "\n"

schwinn_bike = Product(2000, "bike", 40, "Schwinn")
schwinn_bike.display_info()
schwinn_bike.sell()
schwinn_bike.return_item("defective")