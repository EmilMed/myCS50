from cs50 import SQL

db = SQL("sqlite:///songs.db")

rows = db.execute("SELECT NAME FROM SONGS")

print(rows[0]["NAME"])