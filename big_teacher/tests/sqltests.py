from unittest import TestCase, mock
import MysqlConnector


class TestSimple(TestCase):

    @mock.patch('MysqlConnector')
    def test_getdata(self, MysqlConnector):
        mock_cursor = mock.MagicMock()
        test_data = [{'password': 'secret', 'id': 1}]
        mock_cursor.fetchall.return_value = test_data
        mock_pymysql.connect.return_value.__enter__.return_value = mock_cursor
        
mock_connections.__getitem__(DEFAULT_DB_ALIAS).cursor.return_value.__enter__.return_value

        self.assertEqual(test_data, simple.get_user_data())
        
if __name__ == '__main__':
    unittest. main()