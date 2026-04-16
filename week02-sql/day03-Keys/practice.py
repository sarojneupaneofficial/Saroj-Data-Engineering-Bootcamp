import sqlite3

# Create / connect database
conn = sqlite3.connect("test_db.db")
cursor = conn.cursor()

# ---------------------------
# 1. CREATE TABLE (Primary Key, Unique Key example)
# ---------------------------
cursor.execute("""
CREATE TABLE IF NOT EXISTS dept (
    dept_id INTEGER PRIMARY KEY,
    dept_name TEXT UNIQUE
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS emp (
    id INTEGER PRIMARY KEY,
    name TEXT,
    salary INTEGER,
    dept_id INTEGER,
    FOREIGN KEY (dept_id) REFERENCES dept(dept_id)
)
""")

# ---------------------------
# 2. INSERT DATA
# ---------------------------
cursor.execute("INSERT INTO dept VALUES (1, 'IT')")
cursor.execute("INSERT INTO dept VALUES (2, 'HR')")

cursor.execute("INSERT INTO emp VALUES (1, 'Bipina', 2000, 1)")
cursor.execute("INSERT INTO emp VALUES (2, 'Shalini', 2500, 2)")
cursor.execute("INSERT INTO emp VALUES (3, 'Bipi', 2200, 1)")

# ---------------------------
# 3. SELECT DATA
# ---------------------------
cursor.execute("SELECT * FROM emp")
print("EMP TABLE:")
for row in cursor.fetchall():
    print(row)

# ---------------------------
# 4. DELETE specific row (DELETE vs DROP concept)
# ---------------------------
cursor.execute("DELETE FROM emp WHERE id = 2")

print("\nAfter deleting id=2:")
cursor.execute("SELECT * FROM emp")
for row in cursor.fetchall():
    print(row)

# ---------------------------
# 5. DELETE ALL ROWS
# ---------------------------
# cursor.execute("DELETE FROM emp")

# ---------------------------
# 6. DROP TABLE (UNCOMMENT TO TEST)
# ---------------------------
# cursor.execute("DROP TABLE emp")

# ---------------------------
# COMMIT CHANGES
# ---------------------------
conn.commit()
conn.close()
