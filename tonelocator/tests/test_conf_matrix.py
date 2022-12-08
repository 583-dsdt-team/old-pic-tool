"""
This module defines five tests of conf_matrix function from tonelocator
    module, including a smoke test, a one-shot test, and three edge
    tests.
"""

import unittest
import pandas as pd
from tonelocator import conf_matrix


class TestConfMatrix(unittest.TestCase):
    """
    Creates unittest class containing XXXX tests of conf_matrix
    """
    def test_smoke(self):
        """
        Conducts a simple smoke test with a set of made-up arguments.
        """
        p = {'picid': ['A', 'B', 'C'], 
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
        t = {'picid': ['A', 'B', 'C'], 
             '0': [0.2, 0, 0],
             '1': [0.1, 0, 0],
             '2': [0.5, 0, 0],
             '3': [0.1, 0.1, 0],
             '4': [0.1, 0.1, 0],
             '5': [0, 0.2, 0],
             '6': [0, 0.4 .3],
             '7': [0, 0, .4],
             '8': [0, 0, 0],
             '9': [0, 0, 0],}        
        tonelocator.conf_matrix(true=t, pred=p)
        return

 #   def test_oneshot(self):
        """
        Conducts a one-shot test of ...
        """
    # test that result is of type confusion matrix 

 #   def test_edge1(self):
        """
        Conducts edge test of case where a bin is tied for highest %
        """


  #  def test_edge2(self):
        """
        Conducts an edge test of case where picid doesn't uniquely identify obs in pred
        """

  #  def test_edge3(self):
        """
        Conducts an edge test of case where picid doesn't uniquely identify obs in true
        """

  #  def test_edge4(self):
        """
        Conducts an edge test of case where there are more picid's in pred than true
        """
  #  def test_edge5(self):
        """
        Conducts an edge test of case where there are more picid's in true than pred
        """

  #  def test_edge5(self):
        """
        Conducts an edge test of case where there isn't a column called picid
        """
  #  def test_edge6(self):
        """
        Conducts an edge test of case where there isn't a column for each bin
        """

  #  def test_edge7(self):
        """
        Conducts an edge test of case where true isn't a pandas dataframe 
        """

  #  def test_edge8(self):
        """
        Conducts an edge test of case where pred isn't a pandas dataframe 
        """

