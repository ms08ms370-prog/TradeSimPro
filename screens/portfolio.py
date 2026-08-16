from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.tab import MDTabsBase, MDTabs
from kivymd.uix.label import MDLabel

class PortfolioTab(MDBoxLayout, MDTabsBase):
    pass

class PortfolioScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = MDBoxLayout(orientation="vertical")
        
        toolbar = MDTopAppBar(title="Positions & Holdings", elevation=2)
        layout.add_widget(toolbar)

        tabs = MDTabs()
        
        pos_tab = PortfolioTab(title="Positions")
        pos_tab.add_widget(MDLabel(text="No Open Positions", halign="center", theme_text_color="Hint"))
        tabs.add_widget(pos_tab)

        hold_tab = PortfolioTab(title="Holdings")
        hold_tab.add_widget(MDLabel(text="No Delivery Holdings", halign="center", theme_text_color="Hint"))
        tabs.add_widget(hold_tab)

        layout.add_widget(tabs)
        self.add_widget(layout)
