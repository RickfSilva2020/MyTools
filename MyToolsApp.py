import random as rd
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout


class Gerenciador_de_Telas(ScreenManager):
    pass

class TelaPrincipal(Screen):
    pass

class EletricTools(Screen):
    pass

class MecanicTools(Screen):
    pass

class SeveralTools(Screen):
    pass

class Sorteio(Screen):
    pass



class MyToolsApp(App):
    def build(self):
        return Gerenciador_de_Telas()
    
MyToolsApp().run()
    

