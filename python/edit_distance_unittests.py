#!/usr/bin/python

import unittest
from edit_distance import edit_distance

class EditDistanceTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_case_001(self):
        text = "Saptarshi"
        pattern = "Shilpita"
        self.assertEqual(edit_distance(text, pattern), 8, "incorrect distance")
        self.assertEqual(edit_distance(text, pattern, dp=True), 8, "incorrect distance")

    def test_case_002(self):
        text = "petiti"
        pattern = "acti"
        self.assertEqual(edit_distance(text, pattern), 4, "incorrect distance")
        self.assertEqual(edit_distance(text, pattern, dp=True), 4, "incorrect distance")

    def test_case_003(self):
        text = "petition"
        pattern = "action"
        self.assertEqual(edit_distance(text, pattern), 4, "incorrect distance")
        self.assertEqual(edit_distance(text, pattern, dp=True), 4, "incorrect distance")

    def test_case_004(self):
        text = "ABCDT"
        pattern = "ACT"
        self.assertEqual(edit_distance(text, pattern), 2, "incorrect distance")
        self.assertEqual(edit_distance(text, pattern, dp=True), 2, "incorrect distance")

    def test_case_005(self):
        text = "ABCD"
        pattern = "AD"
        self.assertEqual(edit_distance(text, pattern), 2, "incorrect distance")
        self.assertEqual(edit_distance(text, pattern, dp=True), 2, "incorrect distance")

    def test_case_006(self):
        text = "ABCD"
        pattern = "AE"
        self.assertEqual(edit_distance(text, pattern), 3, "incorrect distance")
        self.assertEqual(edit_distance(text, pattern, dp=True), 3, "incorrect distance")

    def test_case_007(self):
        text = "ABCD"
        pattern = "A"
        self.assertEqual(edit_distance(text, pattern), 3, "incorrect distance")
        self.assertEqual(edit_distance(text, pattern, dp=True), 3, "incorrect distance")

    def test_case_008(self):
        text = "ABCD"
        pattern = "X"
        self.assertEqual(edit_distance(text, pattern), 4, "incorrect distance")
        self.assertEqual(edit_distance(text, pattern, dp=True), 4, "incorrect distance")

    def test_case_009(self):
        text = "ABCD"
        pattern = "AC"
        self.assertEqual(edit_distance(text, pattern), 2, "incorrect distance")
        self.assertEqual(edit_distance(text, pattern, dp=True), 2, "incorrect distance")

    def test_case_010(self):
        text = "a1b2c3d4"
        pattern = "a4b3c2d1"
        self.assertEqual(edit_distance(text, pattern), 4, "incorrect distance")
        self.assertEqual(edit_distance(text, pattern, dp=True), 4, "incorrect distance")

    def test_case_011(self):
        text = "atcgactg"
        pattern = "cacg"
        self.assertEqual(edit_distance(text, pattern), 4, "incorrect distance")
        self.assertEqual(edit_distance(text, pattern, dp=True), 4, "incorrect distance")

    def tearDown(self):
        pass

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    suite = unittest.TestSuite()
    suite.addTest(EditDistanceTestCase('test_case_001'))
    suite.addTest(EditDistanceTestCase('test_case_002'))
    suite.addTest(EditDistanceTestCase('test_case_003'))
    suite.addTest(EditDistanceTestCase('test_case_004'))
    suite.addTest(EditDistanceTestCase('test_case_005'))
    suite.addTest(EditDistanceTestCase('test_case_006'))
    suite.addTest(EditDistanceTestCase('test_case_007'))
    suite.addTest(EditDistanceTestCase('test_case_008'))
    suite.addTest(EditDistanceTestCase('test_case_009'))
    suite.addTest(EditDistanceTestCase('test_case_010'))
    suite.addTest(EditDistanceTestCase('test_case_011'))
    runner.run(suite)
