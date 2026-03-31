import sqlite3

# Initialize Database
conn = sqlite3.connect('specimens.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS measurements 
               (username TEXT, specimen_size REAL, actual_size REAL)''')
conn.commit()

def save_and_calculate():
    username = input("Enter your username: ")
    img_size = float(input("Enter microscope size: "))
    mag = float(input("Enter magnification: "))
    
    actual_size = img_size / mag
    
    # Save to DB
    cursor.execute("INSERT INTO measurements VALUES (?, ?, ?)", (username, img_size, actual_size))
    conn.commit()
    
    print(f"Stored! Actual size: {actual_size}")
    conn.close()

if __name__ == "__main__":
    save_and_calculate()