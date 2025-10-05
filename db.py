import sqlite3
def create_table():
    conn = sqlite3.connect('user_data.db')
    cursor = conn.cursor()
    create_table_query = """
    CREATE TABLE IF NOT EXISTS users (
        username TEXT PRIMARY KEY,
        email_id TEXT  NOT NULL,
        public_key TEXT UNIQUE NOT NULL,
        balance REAL NOT NULL
    );
    """
    cursor.execute(create_table_query)
    conn.commit()
    conn.close()
    print("Database 'user_data.db' created successfully.")
def insert_record(user_data):
    try:
        conn = sqlite3.connect('user_data.db')
        cursor = conn.cursor()
        insert_query = """
        INSERT INTO users (username, email_id, public_key, balance) 
        VALUES (?, ?, ?, ?);
        """
        cursor.execute(insert_query, user_data)
        conn.commit()
        print(f"Successfully inserted user: {user_data[0]}")
        return True        
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return False
    finally:
        if conn:
            conn.close()
def fetch_user_from_pub_key(public_key):
    try:
        conn = sqlite3.connect('user_data.db')
        cursor = conn.cursor()
        query = "SELECT * FROM users WHERE public_key = ?;" 
        cursor.execute(query, (public_key,))
        user_data = cursor.fetchone()
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()
    return user_data
def update_balance(username, new_balance):
    try:
        conn = sqlite3.connect('user_data.db')
        cursor = conn.cursor()
        update_query = "UPDATE users SET balance = ? WHERE username = ?;"
        cursor.execute(update_query, (new_balance, username))
        conn.commit()
        print(f"Balance updated successfully for user: {username}")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    create_table()
    user_datas=[("ash", "boredman665@gmail.com", "02a3364170c39c9f78bba2a901b3b4e80c3dc07188a3f2c4b7641ab64862a8c008", 3.5)
                ,("ash2","21pc05@psgtech.ac.in"," 03a43fadd1040831d3d803932e4c76d497926c787dd66ff2df4dc563aab1ff99bc",2.9)]
    for user_data in user_datas:
        insert_record(user_data)