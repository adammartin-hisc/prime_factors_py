class Primes(object):

	def factors(self, number):
		nums = []
		for n in range(2, number+1):
			if number % n == 0:
				nums.append(n)
		return nums