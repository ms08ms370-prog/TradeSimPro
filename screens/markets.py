from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.label import MDLabel
from kivymd.uix.tab import MDTabsBase, MDTabs
from kivy.metrics import dp

class MarketTab(MDBoxLayout, MDTabsBase):
    pass

class MarketsScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = MDBoxLayout(orientation="vertical")
        
        toolbar = MDTopAppBar(title="Markets Hub", elevation=2)
        layout.add_widget(toolbar)

        tabs = MDTabs()
        categories = ["Stocks", "Indices", "Crypto", "Forex", "Commodities"]
        
        for cat in categories:
            tab = MarketTab(title=cat)
            content = MDLabel(
                text=f"{cat} Market Engine Initialized",
                halign="center",
                font_style="Body1"
            )
            tab.add_widget(content)
            tabs.add_widget(tab)

        layout.add_widget(tabs)
        self.add_widget(layout)
