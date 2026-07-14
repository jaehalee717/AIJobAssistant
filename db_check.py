from database.sqlite_manager import SQLiteManager

db = SQLiteManager()

db.cursor.execute("""
SELECT
    company,
    position,
    location,
    description,
    status
FROM jobs
LIMIT 5
""")

for row in db.cursor.fetchall():
    print(dict(row))

db.close()