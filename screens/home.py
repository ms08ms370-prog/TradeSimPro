from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.scrollview import MDScrollView
from kivy.metrics import dp
from trading.portfolio import PortfolioManager
from config.settings import CURRENCY_SYMBOL

class MetricCard(MDCard):
    def __init__(self, title, value, val_color=None, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.padding = dp(12)
        self.spacing = dp(4)
        self.radius = [dp(8)]
        self.elevation = 1
        self.size_hint_y = None
        self.height = dp(80)

        title_label = MDLabel(
            text=title,
            font_style="Caption",
            theme_text_color="Hint"
        )
        
        self.value_label = MDLabel(
            text=value,
            font_style="Subtitle1",
            bold=True
        )
        if val_color:
            self.value_label.theme_text_color = "Custom"
            self.value_label.text_color = val_color

        self.add_widget(title_label)
        self.add_widget(self.value_label)

class HomeScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.layout = MDBoxLayout(orientation="vertical")
        
        self.toolbar = MDTopAppBar(
            title="Dashboard",
            elevation=2
        )
        self.layout.add_widget(self.toolbar)

        scroll = MDScrollView()
        self.content_layout = MDBoxLayout(
            orientation="vertical",
            spacing=dp(12),
            padding=dp(12),
            size_hint_y=None
        )
        self.content_layout.bind(minimum_height=self.content_layout.setter('height'))

        self.grid = MDGridLayout(
            cols=2,
            spacing=dp(10),
            size_hint_y=None
        )
        self.grid.bind(minimum_height=self.grid.setter('height'))

        self.content_layout.add_widget(self.grid)
        scroll.add_widget(self.content_layout)
        self.layout.add_widget(scroll)
        self.add_widget(self.layout)
        
    def on_enter(self):
        self.refresh_dashboard()

    def refresh_dashboard(self):
        self.grid.clear_widgets()
        summary = PortfolioManager.get_account_summary()

        metrics = [
            ("Starting Capital", f"{CURRENCY_SYMBOL}{summary['starting_capital']:,.2f}", None),
            ("Portfolio Value", f"{CURRENCY_SYMBOL}{summary['portfolio_value']:,.2f}", None),
            ("Available Cash", f"{CURRENCY_SYMBOL}{summary['available_cash']:,.2f}", None),
            ("Used Margin", f"{CURRENCY_SYMBOL}{summary['used_margin']:,.2f}", None),
            ("Free Margin", f"{CURRENCY_SYMBOL}{summary['free_margin']:,.2f}", None),
            ("Realized P&L", f"{CURRENCY_SYMBOL}{summary['realized_pnl']:,.2f}", self._get_pnl_color(summary['realized_pnl'])),
            ("Unrealized P&L", f"{CURRENCY_SYMBOL}{summary['unrealized_pnl']:,.2f}", self._get_pnl_color(summary['unrealized_pnl'])),
            ("Today's P&L", f"{CURRENCY_SYMBOL}{summary['today_pnl']:,.2f}", self._get_pnl_color(summary['today_pnl'])),
            ("Total P&L", f"{CURRENCY_SYMBOL}{summary['total_pnl']:,.2f}", self._get_pnl_color(summary['total_pnl'])),
            ("ROI", f"{summary['roi']:.2f}%", self._get_pnl_color(summary['roi'])),
            ("Drawdown", f"{summary['drawdown']:.2f}%", (1, 0.3, 0.3, 1) if summary['drawdown'] > 0 else None)
        ]

        for title, value, color in metrics:
            self.grid.add_widget(MetricCard(title, value, color))

    def _get_pnl_color(self, value):
        if value > 0:
            return (0.2, 0.8, 0.2, 1)
        elif value < 0:
            return (1, 0.3, 0.3, 1)
        return (0.7, 0.7, 0.7, 1)
