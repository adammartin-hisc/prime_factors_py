import math
class Primes(object):

	def factors(self, number, answer=[]):
		if number > 1:
			upperBound = int(round(math.sqrt(number))+1)
			for divisor in range(2,upperBound):
				if number % divisor == 0:
					answer.append(divisor)
					return self.factors(number/divisor, answer)
			answer.append(number)
			return answer
		return answer

	