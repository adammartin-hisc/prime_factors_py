import unittest

from primes.prime_factors import Primes 
import nose.tools as nt

class PrimeTests(unittest.TestCase):
	def setUp(self):
		self.primes = Primes()

	def test_primes_is_an_empty_list(self):
		result = self.primes.factors(0)
		nt.assert_equal(result, [])

	def test_primes_has_results(self):
		result = self.primes.factors(2)
		nt.assert_equal(len(result), 1)
		nt.assert_equal(result[0], 2)

	def test_primes_has_results_for_three(self):
		result = self.primes.factors(3)
		nt.assert_equal(result, [3])

	def test_primes_has_results_for_four(self):
		result = self.primes.factors(4)
		nt.assert_equal(result, [2, 2])
