"""Import this module first before importing your project stuff in the tests"""
import sys
import os

dname = os.path.dirname(__file__)
relpath = os.path.join(dname, '..')
abspath = os.path.abspath(relpath)
sys.path.insert(0, abspath)
