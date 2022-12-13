
"""
This module defines five tests of conf_matrix function from tonelocator
    module, including a smoke test, a one-shot test, and eight edge
    tests.
"""

import unittest
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay


class TestConfMatrix(unittest.TestCase):
    """
    Creates unittest class containing XXXX tests of conf_matrix
    """
    def test_smoke(self):
        """
        Conducts a simple smoke test with a set of made-up arguments to
        make sure that no errors are thrown.
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
        conf_matrix.conf_matrix(true=tdf, pred=pdf)
        return

    def test_oneshot(self):
        """
        Conducts a one-shot test to make sure that a confusion matrix is returned.
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
        mat = conf_matrix.conf_matrix(true=tdf, pred=pdf)
        self.assertIsInstance(mat, ConfusionMatrixDisplay)

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
            conf_matrix.conf_matrix(true=tdf, pred=pdf)
 
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
            conf_matrix.conf_matrix(true=tdf, pred=pdf)

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
            conf_matrix.conf_matrix(true=tdf, pred=pdf)

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
            conf_matrix.conf_matrix(true=tdf, pred=pdf)

    def test_edge5(self):
        """
        Conducts an edge test of case where there isn't a column called picid
        """
        tdf = {'photoid': ['A', 'B', 'C', 'D'], 
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
            conf_matrix.conf_matrix(true=tdf, pred=pdf)
            
    def test_edge6(self):
        """
        Conducts an edge test of case where there isn't a column for each bin
        """
        tdf = {'picid': ['A', 'B', 'C', 'D'], 
             '0': [0.1, 0, 0, .4],
             '1': [0.2, 0, 0, .1],
             '2': [0.3, 0, 0, 0],
             '3': [0.2, 0.1, 0, 0],
             '4': [0.1, 0.5, 0, 0],
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
            conf_matrix.conf_matrix(true=tdf, pred=pdf)
            
    def test_edge7(self):
        """
        Conducts an edge test of case where true isn't a pandas dataframe 
        """
        tdf = {'picid': ['A', 'B', 'C', 'D'], 
             '0': [0.1, 0, 0, .4],
             '1': [0.2, 0, 0, .1],
             '2': [0.3, 0, 0, 0],
             '3': [0.2, 0.1, 0, 0],
             '4': [0.1, 0.5, 0, 0],
             '5': [0.1, 0.5, 0, 0],
             '6': [0, 0, .2, 0],
             '7': [0, 0, .4, 0],
             '8': [0, 0, 0, 0],
             '9': [0, 0, 0, .2],}
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
            conf_matrix.conf_matrix(true=tdf, pred=pdf)
            
    def test_edge8(self):
        """
        Conducts an edge test of case where pred isn't a pandas dataframe 
        """
        tdf = {'picid': ['A', 'B', 'C', 'D'], 
             '0': [0.1, 0, 0, .4],
             '1': [0.2, 0, 0, .1],
             '2': [0.3, 0, 0, 0],
             '3': [0.2, 0.1, 0, 0],
             '4': [0.1, 0.5, 0, 0],
             '5': [0.1, 0.5, 0, 0],
             '6': [0, 0, .2, 0],
             '7': [0, 0, .4, 0],
             '8': [0, 0, 0, 0],
             '9': [0, 0, 0, .2],}
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
            conf_matrix.conf_matrix(true=tdf, pred=pdf)
            