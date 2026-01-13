import sqlite3
from infra.config import settings
conn=sqlite3.connect(database=settings.DATABASE,check_same_thread=False)