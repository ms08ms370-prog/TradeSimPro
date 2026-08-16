from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.button import MDRaisedButton, MDRectangleFlatIconButton
from kivymd.uix.label import MDLabel
from kivymd.app import MDApp
from kivy.metrics import dp
from trading.portfolio import PortfolioManager

class ProfileScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = MDBoxLayout(orientation="vertical")
        
        toolbar = MDTopAppBar(title="Account Settings", elevation=2)
        layout.add_widget(toolbar)

        content = MDBoxLayout(
            orientation="vertical",
            padding=dp(20),
            spacing=dp(15)
        )

        user_label = MDLabel(
            text="User Profile: Account #1 (Trader)",
            font_style="H6",
            size_hint_y=None,
            height=dp(40)
        )
        content.add_widget(user_label)

        self.theme_btn = MDRectangleFlatIconButton(
            icon="theme-light-dark",
            text="Toggle Light/Dark Theme",
            size_hint_x=1,
            on_release=self.toggle_theme
        )
        content.add_widget(self.theme_btn)

        reset_btn = MDRaisedButton(
            text="Reset Virtual Capital (₹50,00,000)",
            md_bg_color=(0.9, 0.2, 0.2, 1),
            size_hint_x=1,
            on_release=self.reset_account
        )
        content.add_widget(reset_btn)

        content.add_widget(MDLabel())  # Spacer
        layout.add_widget(content)
        self.add_widget(layout)

    def toggle_theme(self, instance):
        app = MDApp.get_running_app()
        if app.theme_cls.theme_style == "Dark":
            app.theme_cls.theme_style = "Light"
        else:
            app.theme_cls.theme_style = "Dark"

    def reset_account(self, instance):
        PortfolioManager.reset_account()
        app = MDApp.get_running_app()
        home_screen = app.root.get_screen("home_screen")
        if home_screen:
            home_screen.refresh_dashboard()
