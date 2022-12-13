
"""
This module defines five tests of pcp function from tonelocator
    module, including smoke, one-shot, and edge tests.
"""

import unittest
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay


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
        return

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
            pcp.pcp
