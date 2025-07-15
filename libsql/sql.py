from sqlalchemy import text

class sql:
    """
    A class to handle SQL queries using a connection and query string.
    It can be used to execute SQL commands with parameters.
    """

    def __init__(self, connection, query=None, params=None):
        self.connection = connection
        self.query = query
        self.params = params or {}

    def dicts(self):
        result = self.connection.execute(text(self.query), self.params).mappings().all()
        return result

    def run(self):
        return self.connection.execute(text(self.query), self.params)
    
    def dict(self):
        """
        Returns the first row of the result as a dictionary.
        """
        result = self.connection.execute(text(self.query), self.params).mappings().first()
        return dict(result) if result else None
    
    def insert_one(self, table, data):
        """
        Inserts a single record into the specified table.
        :param table: The name of the table to insert into.
        :param data: A dictionary of column names and values to insert.
        """
        columns = ', '.join(data.keys())
        placeholders = ', '.join(f":{key}" for key in data.keys())
        query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        self.connection.execute(text(query), data)