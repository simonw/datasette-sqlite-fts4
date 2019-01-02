from datasette import hookimpl
from sqlite_fts4 import register_functions


@hookimpl
def prepare_connection(conn):
    register_functions(conn)
