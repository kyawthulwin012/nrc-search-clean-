import pandas as pd
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout

def mm_to_en(text):
    mm = "၀၁၂၃၄၅၆၇၈၉"
    en = "0123456789"
    return str(text).translate(str.maketrans(mm, en))

class AppSearch(App):

    def build(self):
        self.df = pd.read_excel("people.xlsx")
        self.col = "နိုင်ငံသားစိစစ်ရေးကတ်ပြားအမှတ်"
        self.name = "အမည်"

        layout = BoxLayout(orientation="vertical", padding=10)

        self.input = TextInput(hint_text="NRC ရိုက်ထည့်ပါ", size_hint=(1, 0.2))
        layout.add_widget(self.input)

        btn = Button(text="Search", size_hint=(1, 0.2))
        btn.bind(on_press=self.search)
        layout.add_widget(btn)

        self.box = GridLayout(cols=1, size_hint_y=None)
        self.box.bind(minimum_height=self.box.setter('height'))

        scroll = ScrollView()
        scroll.add_widget(self.box)
        layout.add_widget(scroll)

        return layout

    def search(self, instance):
        key = mm_to_en(self.input.text.strip())

        self.box.clear_widgets()

        res = self.df[
            self.df[self.col].astype(str)
            .apply(mm_to_en)
            .str.contains(key, regex=False)
        ]

        if res.empty:
            self.box.add_widget(Label(text="မတွေ့ပါ"))
        else:
            for _, r in res.iterrows():
                self.box.add_widget(
                    Label(text=f"{r[self.name]} | {r[self.col]}", size_hint_y=None, height=40)
                )

if __name__ == "__main__":
    AppSearch().run()