from __future__ import print_function

import psycopg2
import psycopg2.extras
import ConfigParser

MY_CONF = './client.cfg'

def load_creds():
    """Load credential from config file."""
    config = ConfigParser.ConfigParser()
    config.read(MY_CONF)
    return config._sections['credentials']

class RedshiftOperator(object):
    """Operations with redshift."""

    def __init__(self, credentials):
        """Save credential to class attr."""
        self.conn_str = (
            "dbname='{database}' user='{user}' host='{host}' password='{password}' port='{port}' connect_timeout=5".format(
                **credentials)
        )
        print (self.conn_str)
        self.connect()

    def connect(self):
        """Connect to DB and return cursor."""
        try:
            connection = psycopg2.connect(self.conn_str)
        except:
            print('Unable to connect to the database')
        else:
            self.cursor = connection.cursor(
                cursor_factory=psycopg2.extras.DictCursor)

    def get_all_tables(self):
        """Return userinfo."""
        query = "select usename from pg_user;"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return rows

def lambda_handler(event, context):
    creds = load_creds()
    db = RedshiftOperator(creds)
    tables = db.get_all_tables()
    return tables


if __name__ == '__main__':
  event = {"url": "https://pages.github.com/"}
  pt = lambda_handler(event, 'handler')
  print(pt)
