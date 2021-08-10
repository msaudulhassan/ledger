class Name(str):
	def __init__(self, name):
		self.name = name

	def __eq__(self, other):
		if type(other) in [Name, Person]:
			return self.name.lower() == other.name.lower()
		elif type(other) is str:
			return self.name.lower() == other.lower()
		else:
			raise TypeError('expected Name, Person or string')

	def __hash__(self):
		return hash(self.name)

	def __repr__(self):
		return self.name


class Person():
	def __init__(self, name, init_amount=0):
		self.name = name if type(name) is Name else Name(name)
		self.balance = init_amount

	def update_balance(self, sign, amount):
		if sign == '+':
			self.balance += amount
		elif sign == '-':
			self.balance -= amount
		else:
			raise ValueError("illegal sign: must be '+' or '-'")

	def __eq__(self, other):
		if type(other) in [Name, Person]:
			return self.name == other.name
		elif type(other) is str:
			return self.name == other
		else:
			raise TypeError('expected Name, Person or string')

	def __repr__(self):
		return '(%s, $%.2f)' % (self.name, self.balance)


class People():
	def __init__(self):
		self.person_list = {}

	def add_person(self, name):
		self.person_list[name] = Person(name)

	def get_person(self, name):
		return self[name]

	def __getitem__(self, name):
		return self.person_list[name]

	def __iter__(self):
		for name, person in self.person_list.items():
			yield person