import sqlite3

def manage_roster_db():
    conn = sqlite3.connect('roster.db')
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Roster (
                        Name TEXT,
                        Species TEXT,
                        Age INTEGER)''')
    
    cursor.executemany('INSERT INTO Roster (Name, Species, Age) VALUES (?, ?, ?)', [
        ('Benjamin Sisko', 'Human', 40),
        ('Jadzia Dax', 'Trill', 300),
        ('Kira Nerys', 'Bajoran', 29)
    ])
    
    cursor.execute("UPDATE Roster SET Name = 'Ezri Dax' WHERE Name = 'Jadzia Dax'")
    
    cursor.execute("SELECT Name, Age FROM Roster WHERE Species = 'Bajoran'")
    print("Bajoran Characters:", cursor.fetchall())
    
    cursor.execute("DELETE FROM Roster WHERE Age > 100")
    
    try:
        cursor.execute("ALTER TABLE Roster ADD COLUMN Rank TEXT")
    except sqlite3.OperationalError:
        pass
    
    cursor.execute("UPDATE Roster SET Rank = 'Captain' WHERE Name = 'Benjamin Sisko'")
    cursor.execute("UPDATE Roster SET Rank = 'Lieutenant' WHERE Name = 'Ezri Dax'")
    cursor.execute("UPDATE Roster SET Rank = 'Major' WHERE Name = 'Kira Nerys'")
    
    cursor.execute("SELECT * FROM Roster ORDER BY Age DESC")
    print("Sorted Roster:", cursor.fetchall())
    
    conn.commit()
    conn.close()

def manage_library_db():
    conn = sqlite3.connect('library.db')
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Books (
                        Title TEXT,
                        Author TEXT,
                        Year_Published INTEGER,
                        Genre TEXT)''')
    
    cursor.executemany('INSERT INTO Books (Title, Author, Year_Published, Genre) VALUES (?, ?, ?, ?)', [
        ('To Kill a Mockingbird', 'Harper Lee', 1960, 'Fiction'),
        ('1984', 'George Orwell', 1949, 'Dystopian'),
        ('The Great Gatsby', 'F. Scott Fitzgerald', 1925, 'Classic')
    ])
    
    cursor.execute("UPDATE Books SET Year_Published = 1950 WHERE Title = '1984'")
    
    cursor.execute("SELECT Title, Author FROM Books WHERE Genre = 'Dystopian'")
    print("Dystopian Books:", cursor.fetchall())
    
    cursor.execute("DELETE FROM Books WHERE Year_Published < 1950")
    
    try:
        cursor.execute("ALTER TABLE Books ADD COLUMN Rating REAL")
    except sqlite3.OperationalError:
        pass
    
    cursor.execute("UPDATE Books SET Rating = 4.8 WHERE Title = 'To Kill a Mockingbird'")
    cursor.execute("UPDATE Books SET Rating = 4.7 WHERE Title = '1984'")
    cursor.execute("UPDATE Books SET Rating = 4.5 WHERE Title = 'The Great Gatsby'")
    
    cursor.execute("SELECT * FROM Books ORDER BY Year_Published ASC")
    print("Sorted Books:", cursor.fetchall())
    
    conn.commit()
    conn.close()

manage_roster_db()
manage_library_db()