import sqlite3

conn = sqlite3.connect("database4.db")
print("Database created")

conn.execute("CREATE TABLE movies (title TEXT, rating TEXT, run_time INTEGER)")
print("Table created")

conn.close()