import unittest
import sqlite3
from databases import IDatabase
from databases.sql_lite import SqlLiteDatabase

class TestSqlLiteDatabase(unittest.TestCase):

    def setUp(self):
        self.db = SqlLiteDatabase()

    def tearDown(self):
        self.db.conn.execute("DROP TABLE test_table")
        self.db.conn.close()

    def __table_exists(self, table_name):
        cursor = self.db.conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
        return cursor.fetchone() is not None

    def test_create_table_if_not_exists(self):
        # Test creating a table that does not exist
        self.db.create_table_if_not_exists('test_table', 'CREATE TABLE test_table (id INTEGER PRIMARY KEY, name TEXT)')
        self.assertTrue(self.__table_exists('test_table'))

        # Test that the table is not created if it already exists
        self.db.create_table_if_not_exists('test_table', 'CREATE TABLE test_table (id INTEGER PRIMARY KEY, name TEXT)')
        self.assertTrue(self.__table_exists('test_table'))

    def test_create(self):
        self.db.create_table_if_not_exists('test_table', 'CREATE TABLE test_table (id INTEGER PRIMARY KEY, name TEXT)')

        # Test inserting a row without params
        last_row_id = self.db.create("INSERT INTO test_table (name) VALUES ('test_name')")
        self.assertIsNotNone(last_row_id)

        # Test inserting a row with params
        last_row_id = self.db.create("INSERT INTO test_table (name) VALUES (?)", ('test_name_2',))
        self.assertIsNotNone(last_row_id)

    def test_read(self):
        self.db.create_table_if_not_exists('test_table', 'CREATE TABLE test_table (id INTEGER PRIMARY KEY, name TEXT)')
        self.db.create("INSERT INTO test_table (name) VALUES ('test_name')")

        # Test reading rows without params
        rows = self.db.read("SELECT * FROM test_table")
        self.assertEqual(len(rows), 1)

        # Test reading rows with params
        rows = self.db.read("SELECT * FROM test_table WHERE name = ?", ('test_name',))
        self.assertEqual(len(rows), 1)

    def test_update(self):
        self.db.create_table_if_not_exists('test_table', 'CREATE TABLE test_table (id INTEGER PRIMARY KEY, name TEXT)')
        self.db.create("INSERT INTO test_table (name) VALUES ('test_name')")

        # Test updating a row without params
        row_count = self.db.update("UPDATE test_table SET name = 'new_name' WHERE name = 'test_name'")
        self.assertEqual(row_count, 1)

        # Test updating a row with params
        row_count = self.db.update("UPDATE test_table SET name = ? WHERE name = ?", ('new_name_2', 'new_name'))
        self.assertEqual(row_count, 1)

    def test_delete(self):
        self.db.create_table_if_not_exists('test_table', 'CREATE TABLE test_table (id INTEGER PRIMARY KEY, name TEXT)')
        self.db.create("INSERT INTO test_table (name) VALUES ('test_name')")

        # Test deleting a row without params
        row_count = self.db.delete("DELETE FROM test_table WHERE name = 'test_name'")
        self.assertEqual(row_count, 1)

        # Test deleting a row with params
        self.db.create("INSERT INTO test_table (name) VALUES ('test_name_2')")
        row_count = self.db.delete("DELETE FROM test_table WHERE name = ?", ('test_name_2',))
        self.assertEqual(row_count, 1)