from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
import random as rd
from time import sleep as sl


class Sorteio(BoxLayout):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        pass
    
        
    def sequenciacheckbox_click(self, seq, value, *args):
        
        
        
        if value == True:
            
            self.ids.sequencia = True
            self.ids.sequencia = seq
            self.ids.output_label.text = 'Sequência selecionada'
            
     
    def unicocheckbox_click(self, uni, value, *args):
        
        
        
        if value == True:
            
            self.ids.unico = True
            self.ids.unico = uni
            self.ids.output_label.text = 'Sorteio único selecionado' 
            
    def sorteio(self, *args):
        
        lista = []
        n = str(self.ids.element.text).upper().replace(' ', '_')



        lista = []
        n1 = n.split()

        for i in n1:
            lista.append(i)
        
        self.ids.output_label.text = f'Os elemanentos digitados foram {lista}.'


        c = 0
        if self.ids.unico.active:
            
            res = rd.choice(lista)
            
            print(res)
          


        if self.ids.sequencia.active:

            res = rd.sample(lista, len(lista))
            for e in res:
                
                self.ids.output_label.text = f'{e} Clique em ok para o próximo'
                c += 1
                
               # Popup(title= 'Processando!!', size_hint= (None, None), size= (200, 150) )
                sl(2)
               # Popup(title= 'O SORTEADO FOI...', size_hint= (None, None), size= (200, 150) )
                
                sl(2)
               # Popup(title= f'{c}º - {e}', font_size= 40 , content = box, size_hint= (None, None), size= (200, 150))
               
                

        else:
            self.ids.output_label.text = 'Selecione o tipo de sorteio'
            



            
       
        
class Tela_sorteio(App):
    def build(self):
        return Sorteio()
    
Tela_sorteio().run()