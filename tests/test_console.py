import unittest
import MySQLdb
from console import HBNBCommand

class TestConsoleMySQL(unittest.TestCase):
    """Test cases for console commands with MySQL database."""

    def setUp(self):
        """Set up MySQL connection and create a test database."""
        self.db = MySQLdb.connect(host="localhost",
                                  user="hbnb_dev",
                                  passwd="hbnb_dev_pwd",
                                  db="hbnb_dev_db")
        self.cursor = self.db.cursor()

    def tearDown(self):
        """Close MySQL connection and clean up."""
        self.cursor.close()
        self.db.close()

    def test_create_state_command(self):
        """Test if 'create State' command adds a new record in the states table."""
        initial_count = self.get_records_count("states")

        HBNBCommand().onecmd("create State name='California'")

        final_count = self.get_records_count("states")

        self.assertEqual(final_count, initial_count + 1)

    def get_records_count(self, table):
        """Get the count of records in the specified table."""
        self.cursor.execute(f"SELECT COUNT(*) FROM {table}")
        count = self.cursor.fetchone()[0]
        return count

if __name__ == '__main__':
    unittest.main()
