from database.db import execute_query, fetch_one
from config.settings import INITIAL_CAPITAL

def init_db():
    queries = [
        """
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS accounts (
            account_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            starting_capital REAL NOT NULL,
            available_cash REAL NOT NULL,
            used_margin REAL DEFAULT 0.0,
            free_margin REAL NOT NULL,
            realized_pnl REAL DEFAULT 0.0,
            unrealized_pnl REAL DEFAULT 0.0,
            FOREIGN KEY(user_id) REFERENCES users(user_id)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS instruments (
            instrument_id INTEGER PRIMARY KEY AUTOINCREMENT,
            symbol TEXT UNIQUE NOT NULL,
            trading_symbol TEXT NOT NULL,
            company_name TEXT NOT NULL,
            exchange TEXT NOT NULL,
            segment TEXT NOT NULL,
            instrument_type TEXT NOT NULL,
            underlying TEXT,
            expiry TEXT,
            strike REAL DEFAULT 0.0,
            option_type TEXT,
            lot_size INTEGER DEFAULT 1,
            tick_size REAL DEFAULT 0.05,
            contract_multiplier REAL DEFAULT 1.0,
            status TEXT DEFAULT 'ACTIVE'
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS orders (
            order_id INTEGER PRIMARY KEY AUTOINCREMENT,
            symbol TEXT NOT NULL,
            exchange TEXT NOT NULL,
            order_type TEXT NOT NULL,
            transaction_type TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price REAL NOT NULL,
            trigger_price REAL DEFAULT 0.0,
            status TEXT NOT NULL,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS positions (
            position_id INTEGER PRIMARY KEY AUTOINCREMENT,
            symbol TEXT NOT NULL,
            exchange TEXT NOT NULL,
            segment TEXT NOT NULL,
            transaction_type TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            average_price REAL NOT NULL,
            current_price REAL NOT NULL,
            unrealized_pnl REAL DEFAULT 0.0,
            realized_pnl REAL DEFAULT 0.0,
            margin_used REAL DEFAULT 0.0
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS watchlists (
            watchlist_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS watchlist_items (
            item_id INTEGER PRIMARY KEY AUTOINCREMENT,
            watchlist_id INTEGER NOT NULL,
            symbol TEXT NOT NULL,
            FOREIGN KEY(watchlist_id) REFERENCES watchlists(watchlist_id)
        );
        """,
        """
        CREATE TABLE IF NOT EXISTS settings (
            key TEXT PRIMARY KEY,
            value TEXT NOT NULL
        );
        """
    ]
    
    for query in queries:
        execute_query(query)
        
    seed_initial_data()

def seed_initial_data():
    user = fetch_one("SELECT * FROM users WHERE username = ?", ("Trader",))
    if not user:
        cursor = execute_query("INSERT INTO users (username) VALUES (?)", ("Trader",))
        user_id = cursor.lastrowid
        execute_query(
            """
            INSERT INTO accounts (user_id, starting_capital, available_cash, used_margin, free_margin, realized_pnl, unrealized_pnl)
            VALUES (?, ?, ?, 0.0, ?, 0.0, 0.0)
            """,
            (user_id, INITIAL_CAPITAL, INITIAL_CAPITAL, INITIAL_CAPITAL)
        )
