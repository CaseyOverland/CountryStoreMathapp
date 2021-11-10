from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class FloatApp(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.label = Label(
            text="Please Enter NUMBERS\nIf PM shift, leave 'PM total' blank",
            size_hint=(0.3, 0.3),
            pos_hint={"x": 0.3, "y": 0.8}
        )
        self.regular = Label(
            text="Regular",
            size_hint=(0.2, 0.3),
            pos_hint={"x": 0, "y": 0.6}
        )
        self.regular_text_s = TextInput(
            size_hint=(0.17, 0.07),
            pos_hint={"x": 0.2, "y": 0.73}
        )
        self.regular_text_e = TextInput(
            size_hint=(0.15, 0.07),
            pos_hint={"x": 0.35, "y": 0.73}
        )
        self.premium = Label(
            text="Premium",
            size_hint=(0.2, 0.3),
            pos_hint={"x": 0, "y": 0.5}
        )
        self.premium_text_s = TextInput(
            size_hint=(0.151, 0.07),
            pos_hint={"x": 0.2, "y": 0.63}
        )
        self.premium_text_e = TextInput(
            size_hint=(0.15, 0.07),
            pos_hint={"x": 0.35, "y": 0.63}
        )
        self.diesel = Label(
            text="Diesel",
            size_hint=(0.2, 0.3),
            pos_hint={"x": 0, "y": 0.4}
        )
        self.diesel_text_s = TextInput(
            size_hint=(0.17, 0.07),
            pos_hint={"x": 0.2, "y": 0.53}
        )
        self.diesel_text_e = TextInput(
            size_hint=(0.15, 0.07),
            pos_hint={"x": 0.35, "y": 0.53}
        )
        self.col_fuel = Label(
            text="Col Fuel",
            size_hint=(0.2, 0.3),
            pos_hint={"x": 0, "y": 0.3}
        )
        self.col_fuel_text_s = TextInput(
            size_hint=(0.17, 0.07),
            pos_hint={"x": 0.2, "y": 0.43}
        )
        self.col_fuel_text_e = TextInput(
            size_hint=(0.15, 0.07),
            pos_hint={"x": 0.35, "y": 0.43}
        )
        self.start = Label(
            text="Start",
            size_hint=(0.2, 0.3),
            pos_hint={"x": 0.15, "y": 0.7}
        )
        self.end = Label(
            text="End",
            size_hint=(0.2, 0.3),
            pos_hint={"x": 0.3, "y": 0.7}
        )
        self.pumped_amount = Label(
            text="Pumped",
            size_hint=(0.2, 0.3),
            pos_hint={"x": 0.48, "y": 0.7}
        )
        self.sold_amount = Label(
            text="Sold",
            size_hint=(0.2, 0.3),
            pos_hint={"x": 0.7, "y": 0.7}
        )
        self.till_1 = Label(
            text="Till 1:",
            size_hint=(0.1, 0.15),
            pos_hint={"x": 0.71, "y": 0.740}
        )
        self.till_1_text = TextInput(
            size_hint=(0.15, 0.07),
            pos_hint={"x": 0.7, "y": 0.73}
        )
        self.till_2 = Label(
            text="Till 2:",
            size_hint=(0.1, 0.15),
            pos_hint={"x": 0.71, "y": 0.640}
        )
        self.till_2_text = TextInput(
            size_hint=(0.15, 0.07),
            pos_hint={"x": 0.7, "y": 0.63}
        )
        self.discount = Label(
            text="Discounts",
            size_hint=(0.1, 0.15),
            pos_hint={"x": 0.74, "y": 0.540}
        )
        self.discount_text = TextInput(
            size_hint=(0.15, 0.07),
            pos_hint={"x": 0.7, "y": 0.53}
        )
        self.totals = Label(
            text="Totals",
            size_hint=(0.2, 0.3),
            pos_hint={"x": 0.31, "y": 0.2}
        )
        self.balance = Label(
            text="Balance",
            size_hint=(0.215, 0.3),
            pos_hint={"x": 0.37, "y": 0.1}
        )
        self.PM_total = Label(
            text="PM Total",
            size_hint=(0.1, 0.15),
            pos_hint={"x": 0.74, "y": 0.44}
        )
        self.PM_total_text = TextInput(
            size_hint=(0.15, 0.07),
            pos_hint={"x": 0.7, "y": 0.43}
        )
        self.calculate_button = Button(
            text="Calculate Numbers",
            size_hint=(0.43, 0.1),
            pos_hint={"x": 0.5, "y": 0.1}
        )
        self.calculate_button.fbind("on_press", lambda x: self.calculate())

        self.add_widget(self.label)

        self.add_widget(self.regular)
        self.add_widget(self.regular_text_s)
        self.add_widget(self.regular_text_e)

        self.add_widget(self.premium)
        self.add_widget(self.premium_text_e)
        self.add_widget(self.premium_text_s)

        self.add_widget(self.diesel)
        self.add_widget(self.diesel_text_s)
        self.add_widget(self.diesel_text_e)

        self.add_widget(self.col_fuel)
        self.add_widget(self.col_fuel_text_s)
        self.add_widget(self.col_fuel_text_e)

        self.add_widget(self.start)
        self.add_widget(self.end)
        self.add_widget(self.pumped_amount)
        self.add_widget(self.sold_amount)
        self.add_widget(self.till_1)
        self.add_widget(self.till_1_text)
        self.add_widget(self.till_2)
        self.add_widget(self.till_2_text)
        self.add_widget(self.discount)
        self.add_widget(self.discount_text)
        self.add_widget(self.totals)
        self.add_widget(self.balance)
        self.add_widget(self.PM_total)
        self.add_widget(self.PM_total_text)
        self.add_widget(self.calculate_button)

    @staticmethod
    def cleaner():
        global regular_start, regular_end, premium_start, premium_end, diesel_start, diesel_end, col_fuel_start, col_fuel_end, till_1_total, till_2_total, PM_shift_total, discounts

        if regular_start == "":
            regular_start = 0
        if regular_end == "":
            regular_end = 0
        if premium_start == "":
            premium_start = 0
        if premium_end == "":
            premium_end = 0
        if diesel_start == "":
            diesel_start = 0
        if diesel_end == "":
            diesel_end = 0
        if col_fuel_start == "":
            col_fuel_start = 0
        if col_fuel_end == "":
            col_fuel_end = 0
        if till_1_total == "":
            till_1_total = 0
        if till_2_total == "":
            till_2_total = 0
        if PM_shift_total == "":
            PM_shift_total = 0
        if discounts == "":
            discounts = 0

    def calculate(self):
        global regular_start, regular_end, premium_start, premium_end, diesel_start, diesel_end, col_fuel_start, col_fuel_end, till_1_total, till_2_total, PM_shift_total, discounts

        regular_start = self.regular_text_s.text
        regular_end = self.regular_text_e.text

        premium_start = self.premium_text_s.text
        premium_end = self.premium_text_e.text

        diesel_start = self.diesel_text_s.text
        diesel_end = self.diesel_text_e.text

        col_fuel_start = self.col_fuel_text_s.text
        col_fuel_end = self.col_fuel_text_e.text

        till_1_total = self.till_1_text.text
        till_2_total = self.till_2_text.text
        PM_shift_total = self.PM_total_text.text
        discounts = self.discount_text.text

        self.cleaner()

        regular_pumped = round(float(regular_end) - float(regular_start), 2)
        premium_pumped = round(float(premium_end) - float(premium_start), 2)
        diesel_pumped = round(float(diesel_end) - float(diesel_start), 2)
        col_fuel_pumped = round(float(col_fuel_end) - float(col_fuel_start), 2)
        till_total = round(((float(till_1_total) + float(till_2_total)) - float(PM_shift_total)) - float(discounts), 2)
        pumped_total = round(regular_pumped + premium_pumped + diesel_pumped + col_fuel_pumped, 2)
        balance = round(pumped_total - till_total, 2)

        self.regular_p = Label(
            text=str(regular_pumped),
            size_hint=(0.215, 0.3),
            pos_hint={"x": 0.5, "y": 0.6}
        )
        self.premium_p = Label(
            text=str(premium_pumped),
            size_hint=(0.215, 0.3),
            pos_hint={"x": 0.5, "y": 0.5}
        )
        self.diesel_p = Label(
            text=str(diesel_pumped),
            size_hint=(0.215, 0.3),
            pos_hint={"x": 0.5, "y": 0.4}
        )
        self.col_fuel_p = Label(
            text=str(col_fuel_pumped),
            size_hint=(0.215, 0.3),
            pos_hint={"x": 0.5, "y": 0.3}
        )
        self.total_sold = Label(
            text=str(till_total),
            size_hint=(0.215, 0.3),
            pos_hint={"x": 0.65, "y": 0.2}
        )
        self.total_pumped = Label(
            text=str(pumped_total),
            size_hint=(0.215, 0.3),
            pos_hint={"x": 0.5, "y": 0.2}
        )
        self.balance_amount = Label(
            text=str(balance),
            size_hint=(0.215, 0.3),
            pos_hint={"x": 0.65, "y": 0.1}
        )

        self.add_widget(self.regular_p)
        self.add_widget(self.premium_p)
        self.add_widget(self.diesel_p)
        self.add_widget(self.col_fuel_p)
        self.add_widget(self.total_sold)
        self.add_widget(self.total_pumped)
        self.add_widget(self.balance_amount)


class MathApp(App):
    def build(self):
        return FloatApp()


MathApp().run()
