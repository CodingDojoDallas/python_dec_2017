#Call Center
class Call(object):
	def __init__(self, unique_id, caller_name, phone_num, timestamp, reason):
		unique_id = unique_id
		caller_name = caller_name
		phone_num = phone_num
		timestamp = timestamp
		reason = reason
	def display_info(self):
		print self.unique_id
		print self.caller_name
		print self.phone_num
		print self.timestamp
		print self.reason

class CallCenter(object):
	def __init__(self):
		self.calls = []
		self.queue_size = len(calls)
	def get_queue_size(self):
		return len(self.calls)
	def add(self, new_call):
		self.calls.append(new_call) 
	def remove(self, old_call):
		self.calls.remove(old_call)
		pass
	def info(self):
		for call in self.calls:
			call.display_info()

call1 = Call('1', 'Chris', '888-888-8888', '3:30pm', 'say hi')

call1.display_info()