from datasette import hookimpl
from sqlite_fts4_rank import register_functions


@hookimpl
def prepare_connection(conn):
    register_functions(conn)
