
"""
This module defines five tests of pcp function from tonelocator
    module, including smoke, one-shot, and edge tests.
"""

import unittest
import pandas as pd
from tonelocator import pcp


class TestPCP(unittest.TestCase):
    """
    Creates unittest class containing tests of pcp.py
    """
    def test_smoke(self):
        """
        Conducts a simple smoke test with a set of made-up arguments to
        make sure that no errors are thrown - bybin==False
        """
        pdf = {'picid': ['A', 'B', 'C'],
             '0': [0.1, 0, 0],
             '1': [0.2, 0, 0],
             '2': [0.3, 0, 0],
             '3': [0.2, 0.1, 0],
             '4': [0.1, 0.5, 0],
             '5': [0, 0.2, 0],
             '6': [0, 0, .2],
             '7': [0, 0, .4],
             '8': [0, 0, 0],
             '9': [0, 0, 0],}
        pdf = pd.DataFrame(pdf)
        tdf = {'picid': ['A', 'B', 'C'],
             '0': [0.2, 0, 0],
             '1': [0.1, 0, 0],
             '2': [0.5, 0, 0],
             '3': [0.1, 0.1, 0],
             '4': [0.1, 0.1, 0],
             '5': [0, 0.2, 0],
             '6': [0, 0.4, .3],
             '7': [0, 0, .4],
             '8': [0, 0, 0],
             '9': [0, 0, 0],}
        tdf = pd.DataFrame(tdf)
        pcp.pcp(true=tdf, pred=pdf)

    def test_oneshot(self):
        """
        Conducts a one-shot test with a known result - same DFs
        """
        pdf = {'picid': ['A', 'B', 'C'],
             '0': [0.1, 0, 0],
             '1': [0.2, 0, 0],
             '2': [0.3, 0, 0],
             '3': [0.2, 0.1, 0],
             '4': [0.1, 0.5, 0],
             '5': [0, 0.2, 0],
             '6': [0, 0, .2],
             '7': [0, 0, .4],
             '8': [0, 0, 0],
             '9': [0, 0, 0],}
        pdf = pd.DataFrame(data=pdf)
        tdf = {'picid': ['A', 'B', 'C'],
             '0': [0.1, 0, 0],
             '1': [0.2, 0, 0],
             '2': [0.3, 0, 0],
             '3': [0.2, 0.1, 0],
             '4': [0.1, 0.5, 0],
             '5': [0, 0.2, 0],
             '6': [0, 0, .2],
             '7': [0, 0, .4],
             '8': [0, 0, 0],
             '9': [0, 0, 0],}
        tdf = pd.DataFrame(data=tdf)
        self.assertAlmostEqual(pcp.pcp(true=tdf, pred=pdf), 1, 2)

    def test_edge1(self):
        """
        Conducts an edge test of case where picid doesn't uniquely identify obs in pred
        """
        pdf = {'picid': ['A', 'A', 'C'],
             '0': [0.1, 0, 0],
             '1': [0.2, 0, 0],
             '2': [0.3, 0, 0],
             '3': [0.2, 0.1, 0],
             '4': [0.1, 0.5, 0],
             '5': [0, 0.2, 0],
             '6': [0, 0, .2],
             '7': [0, 0, .4],
             '8': [0, 0, 0],
             '9': [0, 0, 0],}
        pdf = pd.DataFrame(data=pdf)
        tdf = {'picid': ['A', 'B', 'C'],
             '0': [0.2, 0, 0],
             '1': [0.1, 0, 0],
             '2': [0.5, 0, 0],
             '3': [0.1, 0.1, 0],
             '4': [0.1, 0.1, 0],
             '5': [0, 0.2, 0],
             '6': [0, 0.4, .3],
             '7': [0, 0, .4],
             '8': [0, 0, 0],
             '9': [0, 0, 0],}
        tdf = pd.DataFrame(data=tdf)
        with self.assertRaises(ValueError):
            pcp.pcp(true=tdf, pred=pdf)

    def test_edge2(self):
        """
        Conducts an edge test of case where picid doesn't uniquely identify obs in true
        """
        pdf = {'picid': ['A', 'B', 'C'],
             '0': [0.1, 0, 0],
             '1': [0.2, 0, 0],
             '2': [0.3, 0, 0],
             '3': [0.2, 0.1, 0],
             '4': [0.1, 0.5, 0],
             '5': [0, 0.2, 0],
             '6': [0, 0, .2],
             '7': [0, 0, .4],
             '8': [0, 0, 0],
             '9': [0, 0, 0],}
        pdf = pd.DataFrame(data=pdf)
        tdf = {'picid': ['A', 'B', 'B'],
             '0': [0.2, 0, 0],
             '1': [0.1, 0, 0],
             '2': [0.5, 0, 0],
             '3': [0.1, 0.1, 0],
             '4': [0.1, 0.1, 0],
             '5': [0, 0.2, 0],
             '6': [0, 0.4, .3],
             '7': [0, 0, .4],
             '8': [0, 0, 0],
             '9': [0, 0, 0],}
        tdf = pd.DataFrame(data=tdf)
        with self.assertRaises(ValueError):
            pcp.pcp(true=tdf, pred=pdf)

    def test_edge3(self):
        """
        Conducts an edge test of case where there are more picid's in pred than true
        """
        pdf = {'picid': ['A', 'B', 'C', 'D'],
             '0': [0.1, 0, 0, .4],
             '1': [0.2, 0, 0, .1],
             '2': [0.3, 0, 0, 0],
             '3': [0.2, 0.1, 0, 0],
             '4': [0.1, 0.5, 0, 0],
             '5': [0, 0.2, 0, 0],
             '6': [0, 0, .2, 0],
             '7': [0, 0, .4, 0],
             '8': [0, 0, 0, 0],
             '9': [0, 0, 0, .2],}
        pdf = pd.DataFrame(data=pdf)
        tdf = {'picid': ['A', 'B', 'C'],
             '0': [0.2, 0, 0],
             '1': [0.1, 0, 0],
             '2': [0.5, 0, 0],
             '3': [0.1, 0.1, 0],
             '4': [0.1, 0.1, 0],
             '5': [0, 0.2, 0],
             '6': [0, 0.4, .3],
             '7': [0, 0, .4],
             '8': [0, 0, 0],
             '9': [0, 0, 0],}
        tdf = pd.DataFrame(data=tdf)
        with self.assertRaises(ValueError):
            pcp.pcp(true=tdf, pred=pdf)

    def test_edge4(self):
        """
        Conducts an edge test of case where there are more picid's in true than pred
        """

        tdf = {'picid': ['A', 'B', 'C', 'D'],
             '0': [0.1, 0, 0, .4],
             '1': [0.2, 0, 0, .1],
             '2': [0.3, 0, 0, 0],
             '3': [0.2, 0.1, 0, 0],
             '4': [0.1, 0.5, 0, 0],
             '5': [0, 0.2, 0, 0],
             '6': [0, 0, .2, 0],
             '7': [0, 0, .4, 0],
             '8': [0, 0, 0, 0],
             '9': [0, 0, 0, .2],}
        tdf = pd.DataFrame(data=tdf)
        pdf = {'picid': ['A', 'B', 'C'],
             '0': [0.2, 0, 0],
             '1': [0.1, 0, 0],
             '2': [0.5, 0, 0],
             '3': [0.1, 0.1, 0],
             '4': [0.1, 0.1, 0],
             '5': [0, 0.2, 0],
             '6': [0, 0.4, .3],
             '7': [0, 0, .4],
             '8': [0, 0, 0],
             '9': [0, 0, 0],}
        pdf = pd.DataFrame(data=pdf)
        with self.assertRaises(ValueError):
            pcp.pcp(true=tdf, pred=pdf)

    def test_edge5(self):
        """
        Conducts an edge test of case where there isn't a column called picid
        """
        tdf = {'photoid': ['A', 'B', 'C'],
             '0': [0.1, 0, 0],
             '1': [0.2, 0, 0],
             '2': [0.3, 0, 0],
             '3': [0.2, 0.1, 0],
             '4': [0.1, 0.5, 0],
             '5': [0, 0.2, 0],
             '6': [0, 0, .2],
             '7': [0, 0, .4],
             '8': [0, 0, 0],
             '9': [0, 0, 0],}
        tdf = pd.DataFrame(data=tdf)
        pdf = {'filename': ['A', 'B', 'C'],
             '0': [0.2, 0, 0],
             '1': [0.1, 0, 0],
             '2': [0.5, 0, 0],
             '3': [0.1, 0.1, 0],
             '4': [0.1, 0.1, 0],
             '5': [0, 0.2, 0],
             '6': [0, 0.4, .3],
             '7': [0, 0, .4],
             '8': [0, 0, 0],
             '9': [0, 0, 0],}
        pdf = pd.DataFrame(data=pdf)
        with self.assertRaises(ValueError):
            pcp.pcp(true=tdf, pred=pdf)

    def test_edge6(self):
        """
        Conducts an edge test of case where there isn't a column for each bin
        """
        tdf = {'picid': ['A', 'B', 'C'],
             '0': [0.1, 0, 0],
             '1': [0.2, 0, 0],
             '3': [0.2, 0.1, 0],
             '4': [0.1, 0.5, 0],
             '5': [0, 0.2, 0],
             '6': [0, 0, .2],
             '7': [0, 0, .4],
             '8': [0, 0, 0],
             '9': [0, 0, 0],}
        tdf = pd.DataFrame(data=tdf)
        pdf = {'picid': ['A', 'B', 'C'],
             '0': [0.2, 0, 0],
             '1': [0.1, 0, 0],
             '2': [0.5, 0, 0],
             '3': [0.1, 0.1, 0],
             '4': [0.1, 0.1, 0],
             '5': [0, 0.2, 0],
             '6': [0, 0.4, .3],
             '7': [0, 0, .4],
             '8': [0, 0, 0],
             '9': [0, 0, 0],}
        pdf = pd.DataFrame(data=pdf)
        with self.assertRaises(ValueError):
            pcp.pcp(true=tdf, pred=pdf)

    def test_edge7(self):
        """
        Conducts an edge test of case where true isn't a pandas dataframe
        """
        tdf = {'picid': ['A', 'B', 'C'],
             '0': [0.1, 0, 0],
             '1': [0.2, 0, 0],
             '2': [0.3, 0, 0],
             '3': [0.2, 0.1, 0],
             '4': [0.1, 0.5, 0],
             '5': [0, 0.2, 0],
             '6': [0, 0, .2],
             '7': [0, 0, .4],
             '8': [0, 0, 0],
             '9': [0, 0, 0],}
        pdf = {'picid': ['A', 'B', 'C'],
             '0': [0.2, 0, 0],
             '1': [0.1, 0, 0],
             '2': [0.5, 0, 0],
             '3': [0.1, 0.1, 0],
             '4': [0.1, 0.1, 0],
             '5': [0, 0.2, 0],
             '6': [0, 0.4, .3],
             '7': [0, 0, .4],
             '8': [0, 0, 0],
             '9': [0, 0, 0],}
        pdf = pd.DataFrame(data=pdf)
        with self.assertRaises(ValueError):
            pcp.pcp(true=tdf, pred=pdf)

    def test_edge8(self):
        """
        Conducts an edge test of case where pred isn't a pandas dataframe
        """
        tdf = {'picid': ['A', 'B', 'C'],
             '0': [0.1, 0, 0],
             '1': [0.2, 0, 0],
             '2': [0.3, 0, 0],
             '3': [0.2, 0.1, 0],
             '4': [0.1, 0.5, 0],
             '5': [0, 0.2, 0],
             '6': [0, 0, .2],
             '7': [0, 0, .4],
             '8': [0, 0, 0],
             '9': [0, 0, 0],}
        pdf = {'picid': ['A', 'B', 'C'],
             '0': [0.2, 0, 0],
             '1': [0.1, 0, 0],
             '2': [0.5, 0, 0],
             '3': [0.1, 0.1, 0],
             '4': [0.1, 0.1, 0],
             '5': [0, 0.2, 0],
             '6': [0, 0.4, .3],
             '7': [0, 0, .4],
             '8': [0, 0, 0],
             '9': [0, 0, 0],}
        tdf = pd.DataFrame(data=tdf)
        with self.assertRaises(ValueError):
            pcp.pcp(true=tdf, pred=pdf)
