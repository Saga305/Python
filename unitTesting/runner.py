import unittest as ut
import test_operator_overload as tp

with open("Result.txt", 'w') as write_stream:
	suite_loader = ut.TestLoader()
	suite = suite_loader.loadTestsFromTestCase(tp.TestPoint)
	runner = ut.TextTestRunner(stream=write_stream)
	runner.run(suite)
