from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicWidgetsApp(App):
    """Kivy app to create label widgets from a list."""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = ["Perry Platypus", "John Doe", "Justin Bieber"]

    def build(self):
        """Build Kivy GUI"""
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file("dynamic_widgets.kv")
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Creat labels from names in names list."""
        for name in self.names:
            label = Label(text=name, color=(0.8, 0.41, 0.54, 1))
            self.root.ids.main.add_widget(label)


DynamicWidgetsApp().run()
