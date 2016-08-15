class Primes(object):

	def factors(self, number):
		result = []
		
		potential = 2
		while(potential <= number):
			while (number % potential == 0):
				result.append(potential)
				number /= potential
			potential += 1

		return result