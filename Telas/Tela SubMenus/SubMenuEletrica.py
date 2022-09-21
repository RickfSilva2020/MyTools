from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout


class TelaMenuEletrica(BoxLayout):
    pass

class Subeletrica(App):
    def build(self):
        return TelaMenuEletrica()
    
    
Subeletrica().run()


