#Hospital
class Patient(object):
	def __init__(self, user_id, name, allergies):
		self.user_id = user_id
		self.name = name
		self.allergies = allergies
		bed_num = 0

class Hospital(object):
	def __init__(self, hos_name, capacity):
		self.patients = []
		self.hos_name = hos_name
		self.cap = cap
		self.beds = self.initialize_beds()

	def initialize_beds(self):
		beds = []
		for i in range(0, self.cap):
			beds.append({"bed_id ": i, "Available ": True})
		return beds

	def admit(self):
		if len(self.patient) <= self.cap:
			self.patients.append(patient)
			for i in range(0, len(self.beds)):
				if self.beds[i]["Available"]:
					patient.bed_num = self.beds[i]["bed_id"]

    def discharge(self, patient_id):
        for patient in self.patients:
            if patient.id == patient_id:
                for bed in self.beds:
                    if bed["bed_id"] == patient.bed_num:
                        bed["Available"] = True
                        break

                self.patients.remove(patient)
                return "Patient #{} sucessfully discharged.  Bed #{} now available".format(patient.id, patient.bed_num)
        return "Patient not found"
