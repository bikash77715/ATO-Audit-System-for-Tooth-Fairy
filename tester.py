# test cases for ATO case: Tooth Fairy

import unittest
# from main1pass import splitLinesToList, getStateList, getLostToothList, getTotalExpenditure, exportDetails, displayClaimsByState, compare2StatesByAverageToothLost
from main import *
class Tester(unittest.TestCase):
	"""docstring for Tester"""
	def __init__(self, arg=0):
		super(Tester, self).__init__()
		self.arg = arg
		self.file = open("addresses.csv", 'r')
		self.lines = self.file.readlines()
		self.splitted_lines = []
		for line in self.lines[:-1]:
			line = line[:-1]
			line_list = re.split(',', line)
			# print (line_list[6])
			self.splitted_lines.append(line_list)
		self.file.close()


	def runTest(self):
		pass

	def test_splitLinesToList(self):
		splitted_lines = splitLinesToList(self.lines)
		split_status = True
		for line in splitted_lines:
			if line is not list:
				split_status = False
		self.assertTrue(split_status)
		# self.assertTrue(splitLinesToList())

	def test_getStateList():
		self.assertIn('QLD', getStateList(self.splitted_lines))

	def test_getLostToothList(self):
		lost_teeth_list = getLostToothList(self.splitted_lines)
		tooth_lost_status = False
		for tooth in lost_teeth_list:
			if tooth.isdigit():
				tooth_lost_status = True
		self.assertTrue(tooth_lost_status)

	def test_getTotalExpenditure(self):
		lost_teeth_list = getLostToothList(self.splitted_lines)
		self.assertFalse(getTotalExpenditure(lost_teeth_list)<=0.0)

	def test_exportDetails(self):

		self.assertTrue(exportDetails('test.txt').find('success'))

	def test_displayClaimsByState(self):
		self.assertTrue(displayClaimsByState(self.splitted_lines).find('saved'))

	def test_compare2StatesByAverageToothLost():
		self.assertTrue(compare2StatesByAverageToothLost(['VIC', 'NSW'], self.splitted_lines).find('saved'))

unittest.main()