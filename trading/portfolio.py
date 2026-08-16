from database.db import fetch_one, execute_query
from config.settings import INITIAL_CAPITAL

class PortfolioManager:
    @staticmethod
    def get_account_summary():
        account = fetch_one("SELECT * FROM accounts LIMIT 1")
        if not account:
            return {
                "starting_capital": INITIAL_CAPITAL,
                "available_cash": INITIAL_CAPITAL,
                "used_margin": 0.0,
                "free_margin": INITIAL_CAPITAL,
                "portfolio_value": INITIAL_CAPITAL,
                "realized_pnl": 0.0,
                "unrealized_pnl": 0.0,
                "today_pnl": 0.0,
                "total_pnl": 0.0,
                "roi": 0.0,
                "drawdown": 0.0
            }

        starting_capital = account["starting_capital"]
        available_cash = account["available_cash"]
        used_margin = account["used_margin"]
        realized_pnl = account["realized_pnl"]
        unrealized_pnl = account["unrealized_pnl"]
        
        free_margin = available_cash - used_margin
        total_pnl = realized_pnl + unrealized_pnl
        portfolio_value = available_cash + used_margin + unrealized_pnl
        
        roi = ((portfolio_value - starting_capital) / starting_capital) * 100 if starting_capital > 0 else 0.0
        
        peak_val = max(starting_capital, portfolio_value)
        drawdown = ((peak_val - portfolio_value) / peak_val) * 100 if peak_val > 0 else 0.0

        return {
            "starting_capital": starting_capital,
            "available_cash": available_cash,
            "used_margin": used_margin,
            "free_margin": free_margin,
            "portfolio_value": portfolio_value,
            "realized_pnl": realized_pnl,
            "unrealized_pnl": unrealized_pnl,
            "today_pnl": total_pnl,
            "total_pnl": total_pnl,
            "roi": roi,
            "drawdown": drawdown
        }

    @staticmethod
    def reset_account(capital=INITIAL_CAPITAL):
        execute_query(
            """
            UPDATE accounts 
            SET starting_capital = ?, available_cash = ?, used_margin = 0.0, free_margin = ?, realized_pnl = 0.0, unrealized_pnl = 0.0
            WHERE account_id = 1
            """,
            (capital, capital, capital)
        )
        execute_query("DELETE FROM orders")
        execute_query("DELETE FROM positions")
