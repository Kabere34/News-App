import unittest
from models import sources
Sources= sources.Sources

class sourcesTest(unittest.TestCase):
  '''
  Test class to test the behaviour of the sources class
  '''
  def SetUp(self):
    '''
    Set up method that will run before every Test
    '''
    self.sources_sources = Sources()
