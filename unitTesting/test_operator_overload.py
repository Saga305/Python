import unittest as ut
import operator_overload as oo

class TestPoint(ut.TestCase):
	def test_add(self):
		p1 = oo.Point(1,1)
		p2 = oo.Point(1,1)
		self.assertAlmostEqual(p1 + p2,oo.Point(2,2))

	def test_sub(self):
		p1 = oo.Point(1,1)
		p2 = oo.Point(1,1)
		self.assertAlmostEqual(p1 - p2,oo.Point())

	def test_mul(self):
		p1 = oo.Point(1,1)
		p2 = oo.Point(1,1)
		self.assertAlmostEqual(p1 * p2,oo.Point(1,1))

	def test_div(self):
		p1 = oo.Point(1,1)
		p2 = oo.Point(1,1)
		self.assertAlmostEqual(p1 / p2,oo.Point(1,1))

	def test_floordiv(self):
		p1 = oo.Point(1,1)
		p2 = oo.Point(1,1)
		self.assertAlmostEqual(p1 // p2,oo.Point(1,1))

	def test_eq(self):
		p1 = oo.Point(1,1)
		p2 = oo.Point(1,1)
		self.assertAlmostEqual(p1 == p2,True)

	def test_noteq(self):
		p1 = oo.Point(1,2)
		p2 = oo.Point(1,3)
		self.assertAlmostEqual(p1 != p2,True)

	def test_and(self):
		p1 = oo.Point()
		p2 = oo.Point(1,3)
		self.assertAlmostEqual(p1 & p2,oo.Point())

	def test_invert(self):
		p1 = oo.Point()
		self.assertAlmostEqual(~p1,oo.Point(-1,-1))

	def test_xor(self):
		p1 = oo.Point(1,3)
		p2 = oo.Point(1,3)
		self.assertAlmostEqual(p1 ^ p2,oo.Point())
