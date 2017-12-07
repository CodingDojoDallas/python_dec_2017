class Patient(self):

	def __init__(self, id, name, allergies, bed_num):
		self.id = id
		self.name = name
		self.allergies = allergies
		self.bed_num = 0


class Hospital(object):
	def __init__(self, patients, hname, capacity):
		self.patients = []
		self.hname = hname
		self.capacity = 580

	def admit(self):
		self.patients += 1
	