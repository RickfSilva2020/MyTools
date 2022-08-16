from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
import random as rd


class Sorteio(BoxLayout):
    
        
    def sequenciacheckbox_click(self, seq, value, *args):
        
        self.seq = seq
        
        if value == True:
            
            seq == True
            self.ids.output_label.text = 'Sequência selecionada'
            
     
    def unicocheckbox_click(self, uni, value, *args):
        
        self.uni = uni
        
        if value == True:
            
            uni == True
            self.ids.output_label.text = 'Sorteio único selecionado' 
            
    def sorteio(self, *args):
        
        lista = []
        n = str(self.ids.element).upper().replace(' ', '_')



        lista = []
        n1 = n.split()

        for i in n1:
            lista.append(i)
        print(f'Os elemanentos digitados foram {lista}.')


        c = 0
        if self.uni == True:
            box = BoxLayout(orientation = 'vertical')
            botoes = BoxLayout(spacing = 10, padding= 10)

            res = rd.choice(lista)
            Popup(title= 'Processando!!', content = box, size_hint= (None, None), size= (200, 150) )
            sl(2)
            Popup(title= 'O SORTEADO FOI...', content = box, size_hint= (None, None), size= (200, 150) )
            sl(2)
            Popup(title= f'{res}', font_size= 40 , content = box, size_hint= (None, None), size= (200, 150))
            


        if self.seq == True:

            res = rd.sample(lista, len(lista))
            for e in res:
                self.ids.output_label.text = f'{e}'
                self.ids.output_label.text ='Clique em ok para o próximo'
                c += 1
                
                Popup(title= 'Processando!!', content = box, size_hint= (None, None), size= (200, 150) )
                sl(2)
                Popup(title= 'O SORTEADO FOI...', content = box, size_hint= (None, None), size= (200, 150) )
                
                sl(2)
                Popup(title= f'{c}º - {e}', font_size= 40 , content = box, size_hint= (None, None), size= (200, 150))
               
                

        else:
            Popup(title= 'Escolha o tipo de sorteio', font_size= 40 , content = box, size_hint= (None, None), size= (200, 150))
            



            
       
        
class Tela_sorteio(App):
    def build(self):
        return Sorteio()
    
Tela_sorteio().run()