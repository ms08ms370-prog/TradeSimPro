import os

APP_NAME = "TradeSim Pro"
APP_VERSION = "1.0.0"

# Initial Financial Capital setup
INITIAL_CAPITAL = 5000000.0  # ₹50,00,000.00
CURRENCY_SYMBOL = "₹"

# Paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "trading.db")

# Theme Settings
DEFAULT_THEME = "Dark"
PRIMARY_PALETTE = "Blue"
ACCENT_PALETTE = "Teal"
