import unittest
import os
import json
from ..app import create_app, db

class UsersTest(unittest.TestCase):
  """
  Users Test Case
  """
  def setUp(self):
    """
    Test Setup
    """
    self.app = create_app("testing")
    self.client = self.app.test_client
    self.user = {
      'name': 'olawale',
      'email': 'olawale@mail.com',
      'password': 'passw0rd!'
    }

    with self.app.app_context():
      # create all tables
      db.create_all()
  

if __name__ == "__main__":
  unittest.main() 