import unittest


from compute_easter_date import compute_easter_date 


class TestComputeEasterDate(unittest.TestCase):

	def test_compute(self):
		annee_2006 = 2006
        	result = compute_easter_date(annee_2006)

		self.assertEquals(4, result[0])
		self.assertEquals(16, result[1] + 1)

		annee_2030 = 2030
		result = compute_easter_date(anne_2030)
		self.assertEquals(4, result[0])
		self.assertEquals(21, result[1])



if __name__ == '__main__':
	unittest.main()
