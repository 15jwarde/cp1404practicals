from kivy.app import App
from kivy.lang import Builder
# from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class ConvertMilesToKilometresApp(App):
    """Kivy app to convert miles to kilometres."""
    def build(self):
        """Build Kivy app."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        """Calculate the conversion between miles to kilometres"""
        value = self.get_valid_miles()
        result = value * MILES_TO_KM
        self.root.ids.output_box.text = str(result)

    def handle_increment(self, change):
        """Increase or decrease the users input by 1 when user uses increment button in app."""
        value = self.get_valid_miles() + change
        self.root.ids.input_number.text = str(value)
        self.handle_calculate()

    def get_valid_miles(self):
        """Return valid input."""
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0


ConvertMilesToKilometresApp().run()
