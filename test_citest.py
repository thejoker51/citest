'''
some sample code
'''


import CITest


class TestCITest:


	def test_addition(self):
		assert 4 == CITest.add(2,2)

	def test_subtraction(self):
		assert 2 == CITest.subtract(4,2)