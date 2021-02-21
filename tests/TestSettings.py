import logging.config
import unittest
import os
from functools import partial

# Modules to Test
from src.utils.Settings import Settings


class TestSettings(unittest.TestCase):
    @classmethod
    def tag(cls, *tags):
        '''
        Decorator to add tags to a test class or method.
        '''

        def decorator(obj):
            setattr(obj, 'tags', set(tags))
            return obj

        return decorator

    @classmethod
    def setUpClass(cls):
        '''
        Set up for class to instantiate constructor of class under test
        '''
        super(TestSettings, cls).setUpClass()
        logging.disable(logging.CRITICAL)
        cls.config_write_dict = None
        # Settings class instantiate
        cls.config = Settings('testConfig.ini')
        # Create testLogs directory and testConfig.ini
        cls.dir = os.mkdir('testLogs')
        cls.file = open('testConfig.ini', 'w')

        cls.section = 'sqldb'
        # Initial values
        cls.host = 'aws'
        cls.username = 'user'
        cls.password = 'pass'
        cls.db_name = 'testDB'
        # Test Dictionary
        cls.testDict = {'host': cls.host, 'username': cls.username, 'password': cls.password, 'db_name': cls.db_name}

    def test_create_log_settings(self):
        '''
        Test:
        '''
        dir_true = True
        TestSettings.config.create_log_settings('testConfig.ini', 'testLogs', dir_true)
        self.assertTrue(os.path.isdir('testLogs'), 'Should be True')
        self.assertTrue(os.path.isfile('testConfig.ini'), 'Should be True')

    def test_db_config_write(self):
        '''
        Test Settings.db_config_write() vs testDict
        '''
        TestSettings.config_write_dict = TestSettings.config.db_config_write(section=TestSettings.section,
                                                                             host=TestSettings.host,
                                                                             username=TestSettings.username,
                                                                             password=TestSettings.password,
                                                                             db_name=TestSettings.db_name)
        config_dict = dict(TestSettings.config_write_dict.items(TestSettings.section))
        self.assertEqual(config_dict, TestSettings.testDict, 'Should be equal Dicts')

    def test_db_config_read(self):
        '''
        Test Settings.dbConfigWrite() vs testDict
        '''
        # Value must be written to file fiest
        self.test_db_config_write()
        config_read_dict = TestSettings.config.db_config_read(TestSettings.section)
        self.assertEqual(config_read_dict, self.testDict, "Dicts should be equal values")

    def test_check_log_dir(self):
        '''
        Test Settings.check_log_dir(file)
        '''
        log_dir = TestSettings.config.check_log_dir(directory='testLogs')
        self.assertTrue(log_dir)

    def test_check_log_config(self):
        '''
        Test Settings.check_log_config(file)
        '''
        log_config = TestSettings.config.check_log_config(file='testConfig.ini')
        self.assertTrue(log_config)

    @classmethod
    def tearDownClass(cls):
        super(TestSettings, cls).tearDownClass()
        logging.disable(logging.NOTSET)
        if os.path.exists('testConfig.ini'):
            os.remove('testConfig.ini')
        else:
            print("File testConfig.ini does not exist")
        if os.path.isdir('testLogs'):
            os.rmdir('testLogs')
        cls.host = ''
        cls.username = ''
        cls.password = ''
        cls.db_name = ''
        cls.testDict = {}


if __name__ == "__main__":
    unittest.main()
