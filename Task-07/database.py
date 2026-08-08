import sqlite3
import datetime

SHOP_ITEMS = [
    ("rum", "Barrel of Rum", 250, "Boosts pirate crew morale"),
    ("cutlass", "Pirate Cutlass", 750, "Steel sword for rookies"),
    ("den_den_mushi", "Den Den Mushi", 1500, "Transponder snail for calling"),
    ("vivre_card", "Vivre Card", 3000, "Paper that points to a friend"),
    ("log_pose", "Log Pose", 6000, "Compass for Grand Line islands")
]


def init_db():
    conn = sqlite3.connect("pirates.db")
    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS pirates (
        user_id INTEGER PRIMARY KEY,
        username TEXT,
        wallet INTEGER DEFAULT 1000,
        bank INTEGER DEFAULT 0,
        last_daily TEXT
    )""")

    c.execute("""CREATE TABLE IF NOT EXISTS shop (
        item_id TEXT PRIMARY KEY,
        name TEXT,
        cost INTEGER,
        effect TEXT
    )""")

    c.execute("""CREATE TABLE IF NOT EXISTS inventory (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        item_id TEXT,
        status TEXT DEFAULT 'active'
    )""")

    for item in SHOP_ITEMS:
        c.execute("INSERT OR IGNORE INTO shop VALUES (?, ?, ?, ?)", item)

    conn.commit()
    conn.close()


def get_pirate(user_id, username):
    conn = sqlite3.connect("pirates.db")
    c = conn.cursor()
    c.execute("SELECT * FROM pirates WHERE user_id = ?", (user_id,))
    row = c.fetchone()

    if row is None:
        c.execute("INSERT INTO pirates (user_id, username, wallet, bank) VALUES (?, ?, 1000, 0)", (user_id, username))
        conn.commit()
        c.execute("SELECT * FROM pirates WHERE user_id = ?", (user_id,))
        row = c.fetchone()

    conn.close()
    return {"user_id": row[0], "username": row[1], "wallet": row[2], "bank": row[3], "last_daily": row[4]}


def update_wallet(user_id, amount):
    conn = sqlite3.connect("pirates.db")
    c = conn.cursor()
    c.execute("UPDATE pirates SET wallet = wallet + ? WHERE user_id = ?", (amount, user_id))
    conn.commit()
    conn.close()


def trade_berries(sender_id, receiver_id, amount):
    if amount <= 0:
        return False, "Amount must be positive."
    if sender_id == receiver_id:
        return False, "You cannot trade with yourself."

    conn = sqlite3.connect("pirates.db")
    c = conn.cursor()
    c.execute("SELECT wallet FROM pirates WHERE user_id = ?", (sender_id,))
    row = c.fetchone()

    if not row or row[0] < amount:
        conn.close()
        return False, "Not enough berries."

    c.execute("UPDATE pirates SET wallet = wallet - ? WHERE user_id = ?", (amount, sender_id))
    c.execute("UPDATE pirates SET wallet = wallet + ? WHERE user_id = ?", (amount, receiver_id))
    conn.commit()
    conn.close()
    return True, "Trade complete."


def claim_daily_berries(user_id, reward):
    conn = sqlite3.connect("pirates.db")
    c = conn.cursor()
    c.execute("SELECT last_daily FROM pirates WHERE user_id = ?", (user_id,))
    row = c.fetchone()

    now = datetime.datetime.now()
    if row and row[0]:
        last = datetime.datetime.fromisoformat(row[0])
        if (now - last).total_seconds() < 86400:
            conn.close()
            return False, "You already claimed today. Come back tomorrow."

    c.execute("UPDATE pirates SET wallet = wallet + ?, last_daily = ? WHERE user_id = ?", (reward, now.isoformat(), user_id))
    conn.commit()
    conn.close()
    return True, f"Claimed {reward} berries!"


def get_top_pirates(limit=5):
    conn = sqlite3.connect("pirates.db")
    c = conn.cursor()
    c.execute("SELECT username, wallet + bank AS total FROM pirates ORDER BY total DESC LIMIT ?", (limit,))
    rows = c.fetchall()
    conn.close()
    result = []
    for row in rows:
        result.append({"username": row[0], "total": row[1]})
    return result


def get_shop_items():
    conn = sqlite3.connect("pirates.db")
    c = conn.cursor()
    c.execute("SELECT * FROM shop")
    rows = c.fetchall()
    conn.close()
    result = []
    for row in rows:
        result.append({"item_id": row[0], "name": row[1], "cost": row[2], "effect": row[3]})
    return result


def buy_shop_item(user_id, item_id):
    conn = sqlite3.connect("pirates.db")
    c = conn.cursor()
    c.execute("SELECT * FROM shop WHERE item_id = ?", (item_id.lower(),))
    item = c.fetchone()

    if not item:
        conn.close()
        return False, "Item does not exist."

    c.execute("SELECT wallet FROM pirates WHERE user_id = ?", (user_id,))
    user = c.fetchone()

    if not user or user[0] < item[2]:
        conn.close()
        return False, "Not enough berries."

    c.execute("UPDATE pirates SET wallet = wallet - ? WHERE user_id = ?", (item[2], user_id))
    c.execute("INSERT INTO inventory (user_id, item_id, status) VALUES (?, ?, 'active')", (user_id, item[0]))
    conn.commit()
    conn.close()
    return True, f"You bought {item[1]} for {item[2]} berries!"


def get_inventory(user_id):
    conn = sqlite3.connect("pirates.db")
    c = conn.cursor()
    c.execute("""SELECT shop.name, shop.effect, inventory.status
        FROM inventory
        JOIN shop ON inventory.item_id = shop.item_id
        WHERE inventory.user_id = ?""", (user_id,))
    rows = c.fetchall()
    conn.close()
    result = []
    for row in rows:
        result.append({"name": row[0], "effect": row[1], "status": row[2]})
    return result
