from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextField
from kivy.metrics import dp

class WatchlistScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = MDBoxLayout(orientation="vertical")
        
        toolbar = MDTopAppBar(title="Watchlists", elevation=2)
        layout.add_widget(toolbar)

        search_box = MDBoxLayout(padding=dp(10), size_hint_y=None, height=dp(60))
        search_field = MDTextField(
            hint_text="Search Symbol, Company Name...",
            mode="rectangle"
        )
        search_box.add_widget(search_field)
        layout.add_widget(search_box)

        empty_label = MDLabel(
            text="Watchlist is empty.\nSearch and add instruments to monitor.",
            halign="center",
            theme_text_color="Hint"
        )
        layout.add_widget(empty_label)
        self.add_widget(layout)
