import unittest
from models import sources
from models import news_src
Sources= sources.Sources

class sourcesTest(unittest.TestCase):
  '''
  Test class to test behaviour of the sources class
  '''
  def SetUp(self):
    '''
    Set up method that will run before every Test
    '''
    self.sources_sources = Sources()






