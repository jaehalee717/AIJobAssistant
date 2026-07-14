from database.sqlite_manager import SQLiteManager

db = SQLiteManager()

db.cursor.execute("PRAGMA table_info(jobs)")

print("=" * 80)
print("jobs table")
print("=" * 80)

for row in db.cursor.fetchall():
    print(dict(row))

db.close()