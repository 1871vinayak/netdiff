import os
import unittest
from netdiff.olsr1 import Olsr1Parser


__all__ = ['TestOlsr1Parser']


CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
topology1 = open('{0}/topology1.json'.format(CURRENT_DIR)).read()


class TestOlsr1Parser(unittest.TestCase):

    def test_nochanges(self):
        parser = Olsr1Parser(old=topology1, new=topology1)
        result = parser.diff()
        self.assertTrue(type(result) is dict)
        self.assertTrue(type(result['added']) is list)
        self.assertTrue(type(result['removed']) is list)
        # ensure there are no differences
        self.assertEqual(len(result['added']), 0)
        self.assertEqual(len(result['removed']), 0)
