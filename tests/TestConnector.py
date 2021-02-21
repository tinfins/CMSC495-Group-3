import logging.config
import unittest
#import testing.mysqld
import sqlalchemy
from src.utils.Settings import Settings
# Modules to Test
from src.utils.Connector import Connector


class TestConnector(unittest.TestCase):
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
        super(TestConnector, cls).setUpClass()
        logging.disable(logging.CRITICAL)
        # Read in config.ini for database info
        # Uses local config to not expose sensitive info
        settings = Settings(config_file='../config.ini')
        config = settings.db_config_read(section='sqldb')
        cls.username = 'test'
        cls.password = 'password'
        # Initialize Connector constructor
        cls.connector = Connector(TestConnector.username, TestConnector.password, config)

    def test_init(self):
        '''
        Test Connector __init_
        '''
        self.assertTrue(TestConnector.connector.settings_model.username is TestConnector.username,
                        'Mock value should match username')

    def test_create_engine(self):
        '''
        Test create_engine
        '''
        conn = TestConnector.connector.create_engine(TestConnector.connector.settings_model)
        mock_conn = sqlalchemy.create_engine('mysql+pymysql://')
        self.assertIsInstance(conn, type(mock_conn), 'Class type should match mock class type')

    def test_login(self):
        '''
        Test login
        '''
        mock_conn = sqlalchemy.create_engine('mysql+pymysql://')
        login = TestConnector.connector.login(mock_conn)
        self.assertIsNotNone(login, 'Pass if value is returned from server')

    @classmethod
    def tearDownClass(cls):
        '''
        Tear up for class to destroy items created during class under test
        '''
        super(TestConnector, cls).tearDownClass()
        logging.disable(logging.NOTSET)
        cls.settings = ''
        cls.username = ''
        cls.password = ''
        del cls.connector


if __name__ == "__main__":
    unittest.main()
