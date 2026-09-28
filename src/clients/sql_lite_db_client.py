import sqlite3
from langgraph.checkpoint.sqlite import SqliteSaver
from config.config import SQLITE_DATABASE_PATH


DATABASE_PATH = SQLITE_DATABASE_PATH

_conn = sqlite3.connect(
    DATABASE_PATH,
    check_same_thread=False
)

checkpointer = SqliteSaver(_conn)



