from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout


class Sorteio(BoxLayout):
    pass

class Tela_sorteio(App):
    def build(self):
        return Sorteio()
    
Tela_sorteio().run()