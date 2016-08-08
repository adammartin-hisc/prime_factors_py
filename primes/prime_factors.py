import math
class Primes(object):

	def factors(self, number):
		if number > 1:
			upperBound = int(round(math.sqrt(number))+1)
			for divisor in range(2,upperBound):
				if number % divisor == 0:
					return self.flatten([divisor, self.factors(number/divisor)])
			return [number]
		return []

	def flatten(self, list):
		new_list = []
		for item in list:
			if type(item) == type([]):
				new_list.extend(self.flatten(item))
			else:
				new_list.append(item)
		return new_list