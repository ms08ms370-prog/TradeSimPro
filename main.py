from kivymd.app import MDApp
from kivymd.uix.bottomnavigation import MDBottomNavigation, MDBottomNavigationItem

from database.models import init_db
from config.settings import APP_NAME, DEFAULT_THEME, PRIMARY_PALETTE, ACCENT_PALETTE

from screens.home import HomeScreen
from screens.markets import MarketsScreen
from screens.watchlist import WatchlistScreen
from screens.orders import OrdersScreen
from screens.portfolio import PortfolioScreen
from screens.profile import ProfileScreen

class TradeSimApp(MDApp):
    def build(self):
        self.title = APP_NAME
        self.theme_cls.theme_style = DEFAULT_THEME
        self.theme_cls.primary_palette = PRIMARY_PALETTE
        self.theme_cls.accent_palette = ACCENT_PALETTE

        init_db()

        nav = MDBottomNavigation()

        items = [
            ("home_tab", "Home", "home", HomeScreen(name="home_screen")),
            ("markets_tab", "Markets", "chart-timeline-variant", MarketsScreen(name="markets_screen")),
            ("watchlist_tab", "Watchlist", "format-list-bulleted", WatchlistScreen(name="watchlist_screen")),
            ("orders_tab", "Orders", "book-open-outline", OrdersScreen(name="orders_screen")),
            ("portfolio_tab", "Portfolio", "briefcase-outline", PortfolioScreen(name="portfolio_screen")),
            ("profile_tab", "Profile", "account-circle-outline", ProfileScreen(name="profile_screen")),
        ]

        for tab_id, text, icon, screen_widget in items:
            nav_item = MDBottomNavigationItem(
                name=tab_id,
                text=text,
                icon=icon
            )
            nav_item.add_widget(screen_widget)
            nav.add_widget(nav_item)

        return nav

if __name__ == "__main__":
    TradeSimApp().run()
