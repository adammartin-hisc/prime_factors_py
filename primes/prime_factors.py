class Primes(object):

	def factors(self, number):
		primes = []
		if number > 1:
			while number % 2 == 0:
				primes.append(2)
				number /= 2
			if number > 1:
				primes.append(number)
		return primes