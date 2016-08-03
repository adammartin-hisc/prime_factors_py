import unittest

from primes.prime_factors import Primes 
import nose.tools as nt

class PrimeTests(unittest.TestCase):
	def setUp(self):
		self.primes = Primes()

	def test_primes_of_0_is_an_empty_list(self):
		nt.assert_equal(self.primes.factors(0), [])

	def test_primes_of_1_is_an_empty_list(self):
		nt.assert_equal(self.primes.factors(1), [])

	def test_primes_of_2_is_2(self):
		nt.assert_equal(self.primes.factors(2), [2])

	def test_primes_of_3_is_3(self):
		nt.assert_equal(self.primes.factors(3), [3])

	def test_primes_of_4_is_2_and_2(self):
		nt.assert_equal(self.primes.factors(4), [2,2])

	def test_primes_of_6_is_2_and_3(self):
		nt.assert_equal(self.primes.factors(6), [2,3])