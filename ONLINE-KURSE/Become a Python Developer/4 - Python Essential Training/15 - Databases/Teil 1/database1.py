# 1 - Python database API
print("# - 1")

#Pythons DB-API = Interface für DBs
import  sqlite3

print("connect")
db = sqlite3.connect("db-api.db")
cur = db.cursor()
print("create")
cur.execute("DROP TABLE IF EXISTS test")
cur.execute("""
    CREATE TABLE test (id INTEGER PRIMARY KEY, string TEXT, number INTEGER)
""")
print("insert row")
cur.execute("""
    INSERT INTO test (string, number) VALUES ("one", 1)
    """)
cur.execute("""
    INSERT INTO test (string, number) VALUES ("two", 2)
    """)

print("commit")
db.commit()
print("count")
cur.execute("SELECT COUNT(*) FROM test")
count = cur.fetchone()[0]
print("there are {} rows in the table".format(count))
print("read")
for row in cur.execute("select * from test"):
    print(row)
print("drop")
cur.execute("drop table test")
print("close")

#SqLite = ganze DB in einer Datei nähmlich "db-api.db"


