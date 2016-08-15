import unittest

from primes.prime_factors import Primes 
import nose.tools as nt

class PrimeTests(unittest.TestCase):
	def setUp(self):
		self.primes = Primes()

	def test_primes_of_0_is_an_empty_list(self):
		nt.assert_equal([], self.primes.factors(0))

	def test_primes_of_2_is_a_list_of_2(self):
		nt.assert_equal([2], self.primes.factors(2))

	def test_primes_of_4_is_a_list_of_2_2(self):
		nt.assert_equal([2,2], self.primes.factors(4))

	def test_primes_of_6_is_a_list_of_2_3(self):
		nt.assert_equal([2,3], self.primes.factors(6))

	def test_primes_of_8_is_a_list_of_2_2_2(self):
		nt.assert_equal([2,2,2], self.primes.factors(8))

	def test_primes_of_9_is_a_list_of_3_3(self):
		nt.assert_equal([3,3], self.primes.factors(9))