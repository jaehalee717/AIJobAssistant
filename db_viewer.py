from database.sqlite_manager import SQLiteManager

db = SQLiteManager()

db.cursor.execute(
    """
    SELECT
        company,
        position,
        LENGTH(description) AS desc_len
    FROM jobs
    """
)

print("=" * 80)

for row in db.cursor.fetchall():
    print(dict(row))

print("=" * 80)

db.close()