from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.label import Label
import random as rd
from time import sleep as sl


class Sorteio(BoxLayout):
    
    
    
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
            
        
            pop = Popup(title = 'Analizando resultado...', content = box, size_hint= (None, None),
                    size=(600, 360), background_color=(0.3, 0.5, 1, 0.5))
            pop2 = Popup(title = 'ESCOLHIDO', content = box1, size_hint= (None, None),
                    size=(640, 400), background_color=(0.4, 0.5 , 0.7 ,1))
            
                 
            ta = Button(text= 'VAI!!', on_release = pop2.open)
            exit = Button(text= 'Exit',on_press = pop.dismiss,  on_release = pop2.dismiss)
            texto = Label(text= 'Processando...')
            texto2 = Label(text= 'O SORTEADO FOI...')
            texto3 = Label(text = f'{res}',color =(1,0,0,1), font_size= 60)
            
            botao1.add_widget(Label(text = ''))
            botao1.add_widget(ta)
            botao1.add_widget(Label(text = ''))
            
        
            
            
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
                
                pop = Popup(title = 'Analizando sequência...', content = box, size_hint= (None, None),
                    size=(600, 360), background_color=(0.3, 0.5, 1, 0.5))
                
                pop1 = Popup(title = '', content = box1, size_hint= (None, None),
                    size=(600, 360), background_color=(0.3, 0.5, 1, 0.5))
                            
                ss = Button(text= 'Vai', on_release = pop.dismiss)
                
                box.add_widget(Label(text= f'{c}º - {e}'))
                box.add_widget(ss)
                
                box1.add_widget(Label(text= f'{res}'))
                box1.add_widget(Button(text='PRÓXIMO'))
                
                
                
                pop.open()
            
                c += 1
                 
            
        
        
class Tela_sorteio(App):
    def build(self):
        return Sorteio()
    
Tela_sorteio().run()