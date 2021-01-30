import unittest
import os

# Modules to Test
from big_teacher.src import Settings


class TestSettings(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super(TestSettings, cls).setUpClass()
        print("setUpClass has started...")
        # Settings class instantiate
        cls.config = Settings.Settings('testConfig.ini', 'mysql_db')
        # Initial values
        cls.host = 'aws'
        cls.username = 'user'
        cls.password = 'pass'
        cls.db_name = 'testDB'
        # Test Dictionary
        cls.testDict = {'host': cls.host, 'username': cls.username, 'password': cls.password, 'db_name': cls.db_name}

    def test_db_config_write(self):
        '''
        Test Settings.dbConfigWrite() vs testDict
        '''
        config_write_dict = self.config.db_config_write(host=self.host, username=self.username, password=self.password, db_name=self.db_name)
        self.assertEqual(config_write_dict, self.testDict, "Dicts should be equal values")

    @classmethod
    def tearDownClass(cls):
        super(TestSettings, cls).tearDownClass()
        print("tearDownClass has started...")
        if os.path.exists('testConfig.ini'):
            os.remove('testConfig.ini')
        else:
            print("File testConfig.ini does not exist")
        cls.host = ''
        cls.username = ''
        cls.password = ''
        cls.db_name = ''
        cls.testDict = {}


if __name__ == "__main__":
    unittest.main()
