from kivymd.uix.screen import MDScreen
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.tab import MDTabsBase, MDTabs
from kivymd.uix.label import MDLabel

class OrderTab(MDBoxLayout, MDTabsBase):
    pass

class OrdersScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = MDBoxLayout(orientation="vertical")
        
        toolbar = MDTopAppBar(title="Order Book", elevation=2)
        layout.add_widget(toolbar)

        tabs = MDTabs()
        sections = ["Open", "Executed", "Cancelled"]
        
        for sec in sections:
            tab = OrderTab(title=sec)
            label = MDLabel(
                text=f"No {sec} Orders",
                halign="center",
                theme_text_color="Hint"
            )
            tab.add_widget(label)
            tabs.add_widget(tab)

        layout.add_widget(tabs)
        self.add_widget(layout)
