class Primes(object):

	def factors(self, number):
		factors = []
		current_factor = 2
		while (number > 1):
			while (number % current_factor == 0):
				factors.append(current_factor)
				number /= current_factor
			current_factor += 1
		return factors