from sqlalchemy import create_engine

# Global SQLAlchemy engine
engine = create_engine("mysql+pymysql://root:root@localhost/fast_api_test_db")


class Context:
    def __init__(self, request=None):
        self.request = request
        self.conn = None
        self.x_api_key = None
        self.user_code = None
        self._init_from_request()

    def _init_from_request(self):
        if self.request:
            self.x_api_key = self.request.headers.get("x-api-key")
            self.user_code = self.request.headers.get("user-code")
        self.conn = self._get_db_connection()

    def _get_db_connection(self):
        return engine  # Return SQLAlchemy engine instead of raw connector

    def close(self):
        pass  # Nothing to close in this setup
