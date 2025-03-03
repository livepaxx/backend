import sqlite3

# Створюємо або підключаємося до бази
conn = sqlite3.connect("clicker.db")
cursor = conn.cursor()

# Створюємо таблицю для збереження очок
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    username TEXT,
    score INTEGER DEFAULT 0
)
""")
conn.commit()

# Функція оновлення очок
def update_score(user_id, username, increment):
    cursor.execute("SELECT score FROM users WHERE user_id = ?", (user_id,))
    result = cursor.fetchone()

    if result:
        new_score = result[0] + increment
        cursor.execute("UPDATE users SET score = ? WHERE user_id = ?", (new_score, user_id))
    else:
        new_score = increment
        cursor.execute("INSERT INTO users (user_id, username, score) VALUES (?, ?, ?)", (user_id, username, new_score))

    conn.commit()
    return new_score

# Функція отримання очок
def get_score(user_id):
    cursor.execute("SELECT score FROM users WHERE user_id = ?", (user_id,))
    result = cursor.fetchone()
    return result[0] if result else 0

# Функція скидання очок
def reset_score(user_id):
    cursor.execute("UPDATE users SET score = 0 WHERE user_id = ?", (user_id,))
    conn.commit()
