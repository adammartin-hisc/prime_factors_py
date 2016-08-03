import unittest

from primes.prime_factors import Primes 
import nose.tools as nt

class PrimeTests(unittest.TestCase):
	def setUp(self):
		self.primes = Primes()

	def test_primes_of_0_is_an_empty_list(self):
		nt.assert_equal(self.primes.factors(0), [])