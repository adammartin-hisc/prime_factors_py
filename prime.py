import unittest

from math import sqrt
from itertools import islice, count
# from functools import count


def _is_prime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n) - 1)))


def _is_list_prime_factor(number, factors):
    current_total = 1
    for f in factors:
        if not _is_prime(f):
            return False
        current_total *= f
    return number == current_total


class TestOptimusPrime(unittest.TestCase):

	def test_one_returns_empty_list(self):
		self.assertEquals(get_prime_factors(1), [])

	def test_two_returns_two(self):
		self.assertEquals(get_prime_factors(2), [2])

	def test_three_returns_three(self):
		self.assertEquals(get_prime_factors(3), [3])

	def test_four_returns_two_twice(self):
		self.assertEquals(get_prime_factors(4), [2, 2])

	def test_em_all(self):
		for i in xrange(1, 10000):
			factors = get_prime_factors(i)
			assert _is_list_prime_factor(i, factors), "{} not good yo, we got {}".format(i, factors)


def get_prime_factors(number):
	primes = []
	check = 2
	while number > 1:
		while number % check == 0:
			primes.append(check)
			number /= check
		check += 1
	return primes


if __name__ == "__main__":
	unittest.main()
