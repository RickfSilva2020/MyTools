import random as rd
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window  # EVENTOS DE TECLADO
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.properties import ListProperty


class Gerenciador_de_Telas(ScreenManager):
    pass


class TelaPrincipal(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

    def confirmacao_de_saida(self, *args):

        box = BoxLayout(orientation='vertical')
        botoes = BoxLayout(padding=10, spacing=10)

        pop = Popup(title='Deseja mesmo sair?', content=box, size_hint=(None, None),
                    size=(600,300))

        sim = Button(text='Sim', on_release=App.get_running_app().stop)
        nao = Button(text='Não', on_release=pop.dismiss)

        botoes.add_widget(sim)
        botoes.add_widget(nao)

        atencao = Image(source='atencao.png')

        box.add_widget(atencao)
        box.add_widget(botoes)

        pop.open()


class EletricTools(Screen):
    pass


class MecanicTools(Screen):
    pass


class SeveralTools(Screen):
    pass

class SubMenuEletric(Screen):
    pass
class SubMenuMec(Screen):
    pass



class Sorteio(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

    # Eventos de teclado
    def on_pre_enter(self):
        Window.bind(on_keyboard=self.voltar)

    def voltar(self, window, key, *args):
        if key == 27:
            App.get_running_app().root.current = 'TelaPrincipal'
            return True

    def on_pre_leave(self, *args):
        Window.unbind(on_keyboard=self.voltar)

    def sorteio(self, *args):

        uni = self.ids.unico
        seq = self.ids.sequencia

        lista = []
        n = str(self.ids.element.text).upper().replace(' ', '_')
        n1 = n.split()

        for i in n1:
            lista.append(i)

        if uni.active:

            res = rd.choice(lista)

            box = BoxLayout(orientation='vertical')
            box1 = BoxLayout(orientation='vertical')
            botao1 = BoxLayout()

            pop = Popup(title='Analizando resultado...', content=box, size_hint=(None, None),
                        size=(600, 360), background_color=(0.3, 0.5, 1, 0.5))
            pop2 = Popup(title='ESCOLHIDO', content=box1, size_hint=(None, None),
                         size=(640, 400), background_color=(0.4, 0.5, 0.7, 1))

            ta = Button(text='VAI!!', on_release=pop2.open)
            exit = Button(text='Exit', on_press=pop.dismiss,
                          on_release=pop2.dismiss)
            texto = Label(text='Processando...')
            texto2 = Label(text='O SORTEADO FOI...')
            texto3 = Label(text=f'{res}', color=(1, 0, 0, 1), font_size=60)

            botao1.add_widget(Label(text=''))
            botao1.add_widget(ta)
            botao1.add_widget(Label(text=''))

            box.add_widget(texto)
            box.add_widget(texto2)
            box.add_widget(botao1)

            box1.add_widget(texto3)
            box1.add_widget(exit)

            pop.open()

        c = 1
        if seq.active:

            res = rd.sample(lista, len(lista))

            for e in res:

                box = BoxLayout(orientation='vertical')
                box1 = BoxLayout(orientation='vertical')
                botao1 = BoxLayout()

                pop = Popup(title='Analizando sequência...', content=box, size_hint=(None, None),
                            size=(600, 360), background_color=(0.3, 0.5, 1, 0.5))

                pop1 = Popup(title='', content=box1, size_hint=(None, None),
                             size=(600, 360), background_color=(0.3, 0.5, 1, 0.5))

                ss = Button(text='Vai', on_release=pop.dismiss)

                box.add_widget(Label(text=f'{c}º - {e}'))
                box.add_widget(ss)

                box1.add_widget(Label(text=f'{res}'))
                box1.add_widget(Button(text='PRÓXIMO'))

                pop.open()

                c += 1
                
class Cmotores(Screen):
    def Calc_motores(self,**kwargs):
        super().__init__(self, **kwargs)
        pass
        
    def escolhaPotencia(self):
        potencia = self.ids.pot.text
        print(potencia)
        
class ShadowLabel(Label):

    decal = ListProperty([0, 0])

    tint = ListProperty([1, 1, 1, 1])
    
    
class MyToolsApp(App):
    def build(self):
        return Gerenciador_de_Telas()


MyToolsApp().run()
